#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""privado.py — reduce la memoria a lo que se puede publicar.

Deja la forma y tira el cuerpo. Cada linea publicada es un resumen con su huella.
Si algo de lo que sale identifica a alguien, falla en vez de escribir.

Dos reglas que no se negocian:
  1. no sale ni un caracter de texto libre: solo numeros, fechas al dia y categorias cerradas;
  2. la huella se calcula sobre lo que se tiro, para que quien tenga el original
     pueda comprobar que la linea publicada le corresponde y que nada se invento.
"""
import hashlib
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
OBRA = os.path.join(MANTIS, "tareas", "la memoria", "privado")
FUENTE = os.path.join(REPO, ".memoria continua", "rastro", "texto")
CSV = os.environ.get("MANTIS_REQUESTS") or os.path.join(os.path.expanduser("~"), "Downloads",
                                                        "request-logs-2026-10-25.csv")
SALIDA = os.path.join(OBRA, "memoria publica.jsonl")
STATS = os.path.join(OBRA, "stats publicos.json")

# las categorias que se pueden decir en voz alta; lo que no esta aca, no sale
PERMITIDO = {
    "entrada": {
        "friccion": {"autoridad", "contradiccion", "mundo", "repeticion"},
        "estado": {"vivo", "suplantado"},
        "firma": {"humano:autoridad", "humano:autoridad y maquina:mantis",
                  "humano:autoridad y maquina:tesis.py"},
    },
}

# el vocabulario de la pieza: las nueve clases y las siete familias que existen
PERMITIDO["pieza"] = {
    "clase": {"principio", "jugo", "ciclo", "ciclo_rompe", "no_repetir", "cita", "poder",
              "candado_cero", "otra"},
    "familia": {"del caso", "el lenguaje", "el ente y el metodo", "el alma y el libre albedrio",
                "el nombre y la obra", "la maquina y su memoria", "el cero", "vacia", "otra"},
}

# lo que no puede salir en ninguna linea (red de seguridad, no la regla)
PROHIBIDO = [
    (r"[A-Za-z]:\\", "una ruta absoluta"),
    (r"C:\\Users", "una ruta de usuario"),
    (r"[\w.+-]+@[\w-]+\.[a-z]{2,}", "un correo"),
    (r"\b\d{2}:\d{2}\b", "una hora con minutos"),
    (r"@gmail|@hotmail|@outlook|@yahoo", "un dominio de correo"),
    (r"[^\x00-\x7f]", "un caracter fuera del ascii"),
]

# lo que se tira, declarado por tipo: es la lista que se hashea
TIRADO = {
    "entrada": ["sesgo", "limite", "firma", "contra", "sostuvo", "sostengo", "techo", "suplanta"],
    "pase": ["instancia", "sostuvo", "se_rompio", "retoma", "no_retoma", "abierto"],
    "pieza": ["nombre", "expansión", "porque", "referencia", "pregunta", "ficcion", "figura",
              "diferida", "reemplaza", "prueba", "falsificador"],
    "ruta": ["peticion", "decidido", "carga"],
    "descarte": ["que", "porque", "vista"],
    "corrida": ["piso", "rige", "sucede_a", "uuid"],
}


def numero(v):
    """no todos los registros viejos traen un entero: cuando no, se dice, no se inventa"""
    try:
        return int(v)
    except (TypeError, ValueError):
        return -1


def huella(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]


def categoria(d, campo, tipo="entrada"):
    """Una categoria se publica solo si esta en su vocabulario cerrado.

    Lo que no esta se degrada a 'otra': el nombre propio no se parte y no se adivina.
    """
    v = "" if d.get(campo) is None else str(d.get(campo)).strip()
    if campo in ("friccion", "estado", "categoria_firma", "firma", "clase", "familia"):
        pass
    if tipo == "entrada":
        clave = {"firma": "firma", "friccion": "friccion", "estado": "estado"}.get(campo, campo)
        validas = PERMITIDO["entrada"].get(clave, set())
        defecto = "otro" if campo == "estado" else ("vacio" if not v else "otra")
        if campo == "firma" and v.startswith("humano:autoridad") and v not in validas:
            # una firma con nombre propio se degrada a su categoria, no se parte
            return "humano:autoridad"
        return v if v in validas else defecto
    if tipo == "pieza":
        validas = PERMITIDO["pieza"].get(campo, set())
        if campo == "familia" and not v:
            return "vacia"
        return v if v in validas else "otra"
    return v


def campos_de(tipo, d):
    """La forma de cada tipo: solo numeros, fechas al dia y categorias cerradas."""
    base = {
        "tipo": tipo,
        "id": numero(d.get("id")),
        "fecha": str(d.get("fecha") or "")[:10],
    }
    if tipo == "entrada":
        base.update({
            "friccion": categoria(d, "friccion"),
            "estado": categoria(d, "estado"),
            "firma": categoria(d, "firma"),
            "sin_cambio": numero(d.get("sin_cambio")),
            "suplanta": 1 if str(d.get("suplanta") or "").strip() not in ("", "None") else 0,
            "largo_sostengo": len(str(d.get("sostengo") or "")),
            "largo_techo": len(str(d.get("techo") or "")),
            "largo_contra": len(str(d.get("contra") or "")),
        })
    elif tipo == "pase":
        base.update({
            "se_rompio": 1 if str(d.get("se_rompio") or "").strip() else 0,
            "no_retoma": 1 if str(d.get("no_retoma") or "").strip() else 0,
            "largo_sostuvo": len(str(d.get("sostuvo") or "")),
        })
    elif tipo == "pieza":
        base.update({
            "orden": numero(d.get("orden")),
            "clase": categoria(d, "clase", "pieza"),
            "familia": categoria(d, "familia", "pieza"),
            "diferida": 1 if str(d.get("diferida") or "").strip() else 0,
            "tiene_prueba": 1 if str(d.get("prueba") or "").strip() else 0,
            "tiene_falsificador": 1 if str(d.get("falsificador") or "").strip() else 0,
            "largo_expansion": len(str(d.get("expansión") or "")),
            "largo_porque": len(str(d.get("porque") or "")),
        })
    elif tipo == "ruta":
        base["fila"] = numero(d.get("fila"))
    elif tipo == "descarte":
        base["largo_que"] = len(str(d.get("que") or ""))
    elif tipo == "corrida":
        base["sucede_a"] = 1 if str(d.get("sucede_a") or "").strip() else 0

    # la huella se calcula sobre lo que se tiro: eso es lo que prueba que la linea
    # corresponde a un registro real y que no se invento ninguno
    tirado = "|".join(str(d.get(c) or "") for c in TIRADO.get(tipo, []))
    base["huella"] = huella(str(base.get("id")) + ":" + tirado)
    return base


def requests(ruta):
    """El CSV de requests: solo el conteo, el rango de fechas, los codigos y los tokens.

    Ni una celda de texto: se leen las columnas por nombre y se suman.
    """
    import csv
    if not os.path.isfile(ruta):
        return None, "no esta el CSV de requests en " + os.path.basename(ruta)
    total = ok = 0
    codigos = {}
    entrada_salida_cache = [0, 0, 0]
    fechas = []
    with io.open(ruta, encoding="utf-8", newline="") as fh:
        for fila in csv.DictReader(fh):
            bajo = {str(k).strip().lower(): v for k, v in fila.items() if k}
            total += 1
            codigo = str(bajo.get("status_code") or bajo.get("status") or "").strip()
            if codigo:
                codigos[codigo] = codigos.get(codigo, 0) + 1
                if codigo.isdigit() and codigo.startswith("2"):
                    ok += 1
            for i, nombre in enumerate(("input_tokens", "output_tokens", "cache_read_input_tokens")):
                try:
                    entrada_salida_cache[i] += int(float(bajo.get(nombre) or 0))
                except ValueError:
                    pass
            f = str(bajo.get("created_at") or bajo.get("timestamp") or bajo.get("date") or "")[:10]
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", f):
                fechas.append(f)
    return {
        "requests": total,
        "ok": ok,
        "por_codigo": dict(sorted(codigos.items())),
        "tokens_entrada": entrada_salida_cache[0],
        "tokens_salida": entrada_salida_cache[1],
        "tokens_cache_leidos": entrada_salida_cache[2],
        "desde": min(fechas) if fechas else "",
        "hasta": max(fechas) if fechas else "",
    }, ""


def main():
    if not os.path.isdir(FUENTE):
        print("[SIN MEMORIA] no esta " + FUENTE)
        return 1

    lineas = []
    conteo = {}
    for f in sorted(os.listdir(FUENTE)):
        if not f.endswith(".jsonl"):
            continue
        tipo = f[:-6]
        n = 0
        for linea in io.open(os.path.join(FUENTE, f), encoding="utf-8"):
            linea = linea.strip()
            if not linea:
                continue
            try:
                d = json.loads(linea)
            except Exception:
                continue
            lineas.append(campos_de(tipo, d))
            n += 1
        if n:
            conteo[tipo] = n
            print("[ok] {:<10} {} registros reducidos".format(tipo, n))

    if not lineas:
        print("[SIN DATOS] la memoria esta vacia: no se publica nada")
        return 1

    fallas = []
    for i, l in enumerate(lineas, 1):
        s = json.dumps(l, ensure_ascii=False, sort_keys=True)
        for pat, que in PROHIBIDO:
            if re.search(pat, s):
                fallas.append("linea {}: {} -> {}".format(i, que, s[:120]))
    # la regla de verdad: todo valor es un numero, un id, una fecha o una categoria cerrada
    permitidos = {"otra", "otro", "vacio", "vacia"}
    for grupo in PERMITIDO.values():
        for vals in grupo.values():
            permitidos |= set(vals)
    for i, l in enumerate(lineas, 1):
        for k, v in l.items():
            if isinstance(v, (int, float)):
                continue
            if not isinstance(v, str):
                fallas.append("linea {}: {} no es numero, fecha ni categoria".format(i, k))
                continue
            if k == "fecha":
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
                    fallas.append("linea {}: la fecha no esta al dia".format(i))
                continue
            if k == "huella":
                if not re.fullmatch(r"[0-9a-f]{16}", v):
                    fallas.append("linea {}: la huella no es una huella".format(i))
                continue
            if k == "tipo":
                if v not in TIRADO:
                    fallas.append("linea {}: tipo desconocido {}".format(i, v))
                continue
            if v not in permitidos:
                fallas.append("linea {}: {} dice '{}', que no es categoria cerrada".format(i, k, v))

    if fallas:
        print("[falla] el paquete lleva algo que identifica:")
        for f in fallas[:10]:
            print("  - " + f)
        print("no se escribe nada.")
        return 1

    lineas.sort(key=lambda l: (l.get("fecha") or "", l["tipo"], l.get("id") or 0))
    with io.open(SALIDA, "w", encoding="utf-8", newline="") as fh:
        for l in lineas:
            fh.write(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n")

    fechas = sorted({l["fecha"] for l in lineas if l.get("fecha")})
    req, aviso = requests(CSV)

    stats = {
        "registros": len(lineas),
        "por_tipo": conteo,
        "desde": fechas[0] if fechas else "",
        "hasta": fechas[-1] if fechas else "",
        "campos": sorted({k for l in lineas for k in l}),
        "que_no_sale": ["texto libre", "nombres", "rutas absolutas", "correos",
                        "horas con minutos", "el texto de cada registro"],
        "como_se_comprueba": ("cada huella = sha256(id + ':' + los campos tirados de ese tipo)[:16]; "
                              "quien tenga el registro original recalcula y compara"),
        "requests": req if req else aviso,
        "lo_que_no_prueba": ("la huella prueba que la linea corresponde a un registro real; "
                             "no prueba que el registro diga la verdad"),
    }
    with io.open(STATS, "w", encoding="utf-8", newline="") as fh:
        json.dump(stats, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print("")
    print("[ok] {} lineas en memoria publica.jsonl".format(len(lineas)))
    print("[ok] del {} al {}".format(stats["desde"], stats["hasta"]))
    print("[ok] campos: {}".format(", ".join(stats["campos"])))
    print("[ok] nada de lo que sale identifica a nadie")
    if req:
        print("[ok] requests: {} ({}, {} ok) del {} al {}".format(
            req["requests"], req["por_codigo"], req["ok"], req["desde"], req["hasta"]))
    else:
        print("[aviso] requests: " + aviso)
    print("")
    print("pasa: la memoria se puede publicar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
