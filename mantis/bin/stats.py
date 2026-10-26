#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""stats — cuenta la sesión desde el registro del mundo, y la publica.

No le cree a nadie: lee el registro crudo de DeepSeek Harness, que es un
.jsonl comprimido con zstd y una línea por evento, y cuenta lo que hay.
Lo que no está en el registro, no se escribe.

Uso:
    python stats.py                 cuenta la sesión más grande de este repo
    python stats.py --entrada <x>   cuenta otro registro
    python stats.py --json          sale en json, para que lo lea un paper

Sale 0 si la cuenta cuadra, 1 si el registro no se puede leer.
"""
import io
import json
import os
import sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
SESIONES = os.path.join(os.path.expanduser("~"), ".dsh", "sessions")
OBRA = os.path.join(MANTIS, "tareas", "la memoria", "stats")
SALIDA = os.path.join(OBRA, "stats de la sesion.json")
NOMBRE = {"inputTokens": "entrada", "outputTokens": "salida",
          "cacheReadTokens": "cache_leido", "cacheWriteTokens": "cache_escrito"}


def leer_registro(ruta):
    """Abre el session.v4.jsonl.zstd y devuelve sus eventos."""
    try:
        import zstandard
    except ImportError:
        return None, "[SIN ZSTD] falta el modulo zstandard: pip install zstandard"
    if not os.path.isfile(ruta):
        return None, "[SIN REGISTRO] no esta " + ruta
    d = zstandard.ZstdDecompressor()
    with io.open(ruta, "rb") as fh:
        datos = d.stream_reader(fh).read()
    eventos = []
    for linea in datos.decode("utf-8", "replace").split("\n"):
        linea = linea.strip()
        if not linea:
            continue
        try:
            eventos.append(json.loads(linea))
        except Exception:
            continue
    return eventos, ""


def sesiones_de(raiz):
    """Los registros de este repo: uno por sesión, del más grande al más chico."""
    fuera = []
    if not os.path.isdir(raiz):
        return fuera
    for base, dirs, files in os.walk(raiz):
        for f in files:
            if f.endswith(".jsonl.zstd"):
                p = os.path.join(base, f)
                fuera.append((os.path.getsize(p), p))
    return sorted(fuera, reverse=True)


def contar(eventos):
    """Cuenta lo que hay, y nada más. Cada número tiene su porqué."""
    tipos = {}
    tokens = {"inputTokens": 0, "outputTokens": 0, "cacheReadTokens": 0, "cacheWriteTokens": 0}
    con_usage = 0
    proveedor = ""
    modelo = ""
    ventana = None
    primero = None
    ultimo = None
    for o in eventos:
        t = o.get("type")
        tipos[t] = tipos.get(t, 0) + 1
        ms = o.get("time")
        if isinstance(ms, (int, float)):
            if primero is None or ms < primero:
                primero = ms
            if ultimo is None or ms > ultimo:
                ultimo = ms
        dat = o.get("data") or {}
        u = dat.get("usage")
        if not isinstance(u, dict) and isinstance(dat.get("message"), dict):
            u = dat["message"].get("usage")
        if isinstance(u, dict) and "inputTokens" in u:
            con_usage += 1
            for k in tokens:
                v = u.get(k)
                if isinstance(v, (int, float)):
                    tokens[k] += int(v)
        if t == "request/context":
            proveedor = dat.get("provider") or proveedor
            modelo = dat.get("model") or modelo
            ventana = dat.get("contextWindow") or ventana
        if t == "request/header" and not proveedor:
            cfg = (dat.get("header") or {}).get("config") or {}
            proveedor = cfg.get("provider") or proveedor
            modelo = cfg.get("model") or modelo
    total = sum(tokens.values())
    return {
        "eventos": len(eventos),
        "turnos": tipos.get("turn/start", 0),
        "pasos": tipos.get("step/start", 0),
        "mensajes_de_asistente": tipos.get("assistant/message", 0),
        "herramientas_llamadas": tipos.get("tool/call", 0),
        "herramientas_con_resultado": tipos.get("tool/result", 0),
        "reintentos_de_llm": tipos.get("llm/retry", 0),
        "compactaciones": tipos.get("compaction/start", 0),
        "mensajes_de_usuario": tipos.get("user/message", 0),
        "registros_con_tokens": con_usage,
        "tokens": tokens,
        "tokens_total": total,
        "proveedor": proveedor,
        "modelo": modelo,
        "ventana_de_contexto": ventana,
        "desde": datetime.fromtimestamp(primero / 1000, timezone.utc).isoformat(timespec="seconds") if primero else "",
        "hasta": datetime.fromtimestamp(ultimo / 1000, timezone.utc).isoformat(timespec="seconds") if ultimo else "",
        "tipos_de_evento": dict(sorted(tipos.items(), key=lambda x: -x[1])),
    }


def main(argv):
    ruta = None
    if "--entrada" in argv:
        i = argv.index("--entrada")
        if i + 1 >= len(argv):
            print("[FALTA] --entrada quiere un registro")
            return 1
        ruta = argv[i + 1]
    else:
        propias = sesiones_de(SESIONES)
        if not propias:
            print("[SIN REGISTRO] no hay sesiones de este mundo en " + SESIONES)
            return 1
        ruta = propias[0][1]

    eventos, aviso = leer_registro(ruta)
    if eventos is None:
        print(aviso)
        return 1

    c = contar(eventos)
    c["registro"] = os.path.basename(os.path.dirname(ruta)) + "/" + os.path.basename(ruta)
    c["bytes_comprimidos"] = os.path.getsize(ruta)
    c["como_se_cuenta"] = ("cada número sale de los eventos del registro; los tokens, de los bloques "
                           "usage de cada assistant/message; lo que no está en el registro, no se escribe")

    if "--json" in argv:
        print(json.dumps(c, ensure_ascii=False, indent=2))
        return 0

    print("[registro] {}".format(c["registro"]))
    print("[registro] {} comprimidos, {} eventos".format(c["bytes_comprimidos"], c["eventos"]))
    print("[registro] del {} al {}".format(c["desde"][:10], c["hasta"][:10]))
    print("")
    print("  proveedor        {}".format(c["proveedor"] or "(no declarado)"))
    print("  modelo           {}".format(c["modelo"] or "(no declarado)"))
    print("  ventana          {}".format(c["ventana_de_contexto"] or "(no declarada)"))
    print("")
    print("  turnos           {:>14,}".format(c["turnos"]))
    print("  pasos            {:>14,}".format(c["pasos"]))
    print("  mensajes         {:>14,}".format(c["mensajes_de_asistente"]))
    print("  herramientas     {:>14,}".format(c["herramientas_llamadas"]))
    print("  reintentos       {:>14,}".format(c["reintentos_de_llm"]))
    print("  compactaciones   {:>14,}".format(c["compactaciones"]))
    print("")
    for k in ("inputTokens", "outputTokens", "cacheReadTokens", "cacheWriteTokens"):
        print("  tokens {:<14} {:>14,}".format(NOMBRE[k], c["tokens"][k]))
    print("  {:<21} {:>14,}".format("TOTAL", c["tokens_total"]))
    print("")
    if c["tokens_total"]:
        cache = c["tokens"]["cacheReadTokens"]
        print("  el caché trabajó {:.1f} veces lo que la entrada".format(
            cache / c["tokens"]["inputTokens"] if c["tokens"]["inputTokens"] else 0))
    print("")
    print("pasa: la sesión se cuenta desde su registro, y no desde la memoria de nadie")

    os.makedirs(OBRA, exist_ok=True)
    with io.open(SALIDA, "w", encoding="utf-8", newline="") as fh:
        json.dump(c, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("deja: " + os.path.relpath(SALIDA, MANTIS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
