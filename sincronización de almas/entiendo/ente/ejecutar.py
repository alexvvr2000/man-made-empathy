#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ejecutar — el ejecutor del ente: lee el corte de una tarea, y lo corre.


No es el estandar, y no sabe que hace ningun proceso. Hace cinco cosas:
leer el corte, buscar con que cumplirlo, correrlo, dejarlo escrito, y negarse.

A un paso se le pasan tres cosas, y ninguna es de este ejecutor:
    argv[1] el Entra: de la tarea     argv[2] el Sale: de la tarea
    argv[3] la carpeta del ente       (y la variable del archivo, en $ARCHIVO)

Donde busca con que, y en este orden:
  1. paso.<ext>   lo que trae la tarea: la implementacion de la tarea, en lo que sea.
                  .sh, .ps1, .py, .exe, cualquier cosa que el mundo sepa correr.
                  Se lleva con la tarea, y no es de nadie: es de quien escribio la tarea.
  2. bin/         lo del mundo: bin/<tarea>.sh | .ps1 | .py | .exe, segun el RUTA.pr.
                  Se queda aqui, y no viaja: el mismo corte se cumple distinto en cada mundo.
  3. nada         entonces dice [FALTA EN bin/] y NO corre. Nunca improvisa.

Y lo que no corre:
  - una tarea sin corte              -> [ACTIVIDAD - SIN CORTE]
  - una tarea cuyo corte no cambio  -> [IGUAL] no corrio, porque no habia nada nuevo que hacer
  - un corte que es una frase y no una prueba -> [SIN PRUEBA] no se puede verificar, y se dice

Uso:
    python ejecutar.py --listar              que tareas hay, y con que cuenta cada una
    python ejecutar.py --verificar           todos los folders tienen su corte
    python ejecutar.py --sin-tra <tarea>     corre y no deja rastro (para probar)
    python ejecutar.py <tarea>               corre una tarea, y deja su .tra

Sale 0 si pasa, 1 si falla, 2 si no puede, 3 si no corrio porque estaba igual.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

# el ejecutor vive EN la raiz del ente: el ente esta aqui, no arriba
AQUI = os.path.dirname(os.path.abspath(__file__))
ENTE = AQUI
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(ENTE, ".."))
TAREAS = os.path.join(ENTE, "tareas")
BIN = AQUI
RUTA_PR = os.path.join(ENTE, "RUTA.pr")
SUELTOS = ("tareas", "integridad")

CAMPOS = ("Entra:", "Falla si:", "Sale:", "Consume:")

# como se corre un paso en este mundo; el RUTA.pr puede decir otro orden
ORDEN = [".sh", ".ps1", ".py", ".exe", ".cmd", ".bat"]
if os.path.isfile(RUTA_PR):
    try:
        with open(RUTA_PR, "r", encoding="utf-8", errors="replace") as fh:
            _ruta = fh.read()
        m = re.search(r'"orden_paso:([^"]*)"', _ruta)
        if m:
            ORDEN = [x.strip() for x in m.group(1).split(",") if x.strip()]
    except Exception:
        pass


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def mensaje(nombre, resto):
    """El corte sin sus marcas: la frase que se compara, y que dice que se hace."""
    limpio = re.sub(r"`[^`]*`", "", nombre)
    limpio = re.sub(r"\*\*", "", limpio)
    limpio = re.sub(r"\[[^\]]*\]", "", limpio)
    limpio = re.sub(r"—+.*", "", limpio)
    limpio = re.sub(r"\s+", " ", limpio).strip().lower()
    return limpiar_variables(limpio + " | " + resto)


def limpiar_variables(texto):
    """Lo que cambia en cada corrida no es el corte: una fecha o un numero no lo cambia."""
    texto = re.sub(r"\d{4}-\d{2}-\d{2}(t[\d:+.\-z]*)?", "FECHA", texto)
    texto = re.sub(r"\b0x[0-9a-f]+\b", "HEX", texto)
    texto = re.sub(r"\b\d+\b", "N", texto)
    return texto


def cortes(texto):
    fuera = {}
    for c in CAMPOS:
        m = re.search(r"[-*]\s*\*\*" + re.escape(c) + r"\*\*\s*(.*)", texto)
        if m:
            fuera[c] = m.group(1).strip()
    return fuera


def firma_del_corte(c):
    cuerpo = "\n".join(c[k][:120] for k in CAMPOS if k in c)
    return hashlib.sha256(mensaje("", cuerpo).encode("utf-8")).hexdigest()[:16]


def procesos_de(carpeta):
    """El corte de una tarea vive en su .tra; el de un folder de proceso, en su .prs."""
    import glob
    ps = sorted(f for f in os.listdir(carpeta) if f.endswith(".prs"))
    if ps:
        return ps
    # el corte vive en el .tra de la tarea, y no en su rastro
    tras = sorted(x for x in glob.glob(os.path.join(carpeta, "*.tra"))
                  if os.path.basename(x) != "rastro.tra")
    return [os.path.basename(x) for x in tras]


def restos_de_correr(carpeta):
    """Un .corte, un rastro o una .tra vacia no son procesos: son lo que dejo correr."""
    malos = [f for f in os.listdir(carpeta) if f.endswith((".tra", ".md", ".indice"))]
    if not any(f.endswith(".prs") for f in os.listdir(carpeta)):
        malos = [f for f in malos if f != os.path.basename(os.path.abspath(carpeta)) + ".tra"]
    return malos


def es_tarea(carpeta):
    return not any(f.endswith(".prs") for f in os.listdir(carpeta))


def verificar(carpeta):
    if not os.path.isdir(carpeta):
        return False, "no existe"
    ps = procesos_de(carpeta)
    if not ps:
        return False, "no hay .prs"
    problemas = []
    for p in ps:
        c = cortes(leer(os.path.join(carpeta, p)))
        falta = [k for k in CAMPOS if k not in c]
        if falta:
            problemas.append("{}: le falta {}".format(p, ", ".join(falta)))
    if problemas:
        return False, "; ".join(problemas)
    return True, "{} proceso(s) con su corte".format(len(ps))


# ------------------------------------------------------------------ el corte
def fuentes(carpeta):
    """Los archivos cuyo contenido es el corte: si cambian, el corte cambio."""
    fuera = []
    for f in sorted(os.listdir(carpeta)):
        p = os.path.join(carpeta, f)
        if f == "rastro.tra":
            continue
        if os.path.isfile(p) and f.endswith((".prs", ".md", ".indice", ".tra", ".delete")):
            fuera.append(p)
    return fuera


def huella_entrada(carpeta):
    h = hashlib.sha256()
    for p in fuentes(carpeta):
        if p.endswith(".delete"):
            continue
        with open(p, "rb") as fh:
            h.update(fh.read())
        h.update(os.path.basename(p).encode("utf-8"))
    return h.hexdigest()[:16]


# ------------------------------------------------------------ lo que lo corre
def motor_propio(carpeta):
    """Una tarea puede traer su propio motor: un .py que no es un paso, y que corre la tarea."""
    for f in sorted(os.listdir(carpeta)):
        if f.endswith(".py") and not f.startswith("paso"):
            return os.path.join(carpeta, f)
    return None


def candidatos(carpeta, nombre):
    """Donde puede estar con que cumplir este corte, en este mundo, y en este orden."""
    motor = motor_propio(carpeta)
    if motor:
        return [motor]
    fuera = []
    for ext in ORDEN:
        fuera.append(os.path.join(carpeta, "paso" + ext))
    for ext in ORDEN:
        fuera.append(os.path.join(BIN, nombre + ext))
    for ext in ORDEN:
        fuera.append(os.path.join(BIN, nombre.replace("/", "_").replace(" ", "_") + ext))
    return [p for p in fuera if os.path.isfile(p)]


def comando(ruta, argv):
    ext = os.path.splitext(ruta)[1].lower()
    if ext == ".py":
        return [sys.executable, ruta] + argv
    if ext in (".ps1",):
        return ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ruta] + argv
    if ext == ".sh":
        # .sh se corre con sh; en Windows lo trae git, y si no esta, no se puede
        return ["sh", ruta] + argv
    if ext in (".cmd", ".bat"):
        return ["cmd", "/c", ruta] + argv
    return [ruta] + argv


ARCHIVO = "archivo de entrada: la ruta que vino en el pedido, o vacio"


def correr(ruta, argv, archivo=""):
    entorno = dict(os.environ)
    entorno["ARCHIVO"] = archivo or ""
    try:
        r = subprocess.run(comando(ruta, argv), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=1800, env=entorno)
        return ((r.stdout or "") + (r.stderr or "")).strip(), r.returncode, ""
    except FileNotFoundError:
        return "", 2, ("[NO SE PUEDE CORRER] este mundo no sabe correr " + ruta
                       + "\n                    y el paso declara que ese trabajo se puede hacer aqui")
    except subprocess.TimeoutExpired:
        return "", 2, "[NO TERMINO] paso de 30 minutos y se corto"
    except Exception as e:
        return "", 2, "[NO SE PUDO CORRER] " + str(e)


# --------------------------------------------------------------- lo que queda
def dejartra(carpeta, proceso, entro, salio, veredicto, extra=None):
    """El rastro de la corrida. Se llama rastro.tra y no <nombre>.tra.

    Y es a proposito: el <nombre>.tra es la TAREA: lleva su corte, y es lo que se corre.
    Si el ejecutor escribiera ahi, se comeria el corte, y la tarea no se podria
    volver a correr. El recibo es otro archivo, y el nombre no cambia.
    """
    nombre = os.path.basename(os.path.abspath(carpeta))
    p = os.path.join(carpeta, "rastro.tra")
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    cuerpo = (
        "# {n}.tra — lo que pasó\n\n"
        "**Nombre:** {n}\n"
        "**Expande:** {proc}\n"
        "**Se nombró:** {ahora}\n"
        "**Reemplaza:** NINGUNO\n"
        "**Miente si:** se dice que corrió y no hay recibo\n\n"
        "## Qué pasó\n\n"
        "**Qué pasó:** {e}\n"
        "**Contra:** {s}\n"
        "**Huella:** esta .tra\n"
        "**Distancia:** {v}\n"
    ).format(n=nombre, proc=proceso, ahora=ahora, e=entro, s=salio, v=veredicto)
    if extra:
        cuerpo += "\n" + extra + "\n"
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(cuerpo)
    return p


def memoria(carpeta, rastro):
    """Lo que paso, en la memoria del ente: congelado al correr, no al escribir.

    El nombre se congela aqui, no en el paso: si el paso cambia, el .tra cambia,
    y lo que se guarda es lo que LEYO la idea, no lo que dire despues.
    """
    ruta = os.path.join(ENTE, "memoria", "entrada.jsonl")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    ultimo = 0
    if os.path.isfile(ruta):
        with open(ruta, "r", encoding="utf-8", errors="replace") as fh:
            for l in fh:
                l = l.strip()
                if not l:
                    continue
                try:
                    ultimo = max(ultimo, int(json.loads(l).get("id") or 0))
                except Exception:
                    pass
    registro = dict(rastro)
    registro["id"] = ultimo + 1
    registro["fecha"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(ruta, "a", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(registro, ensure_ascii=False, sort_keys=True) + "\n")
    return registro


# ---------------------------------------------------------- donde esta la tarea
def carpeta_de(nombre):
    if nombre in SUELTOS:
        return os.path.join(ENTE, nombre)
    directa = os.path.join(TAREAS, nombre)
    if os.path.isdir(directa):
        return directa
    for raiz, dirs, files in os.walk(TAREAS):
        if nombre in dirs:
            return os.path.join(raiz, nombre)
    return directa


def indice():
    """Que tareas hay: toda carpeta que tenga un .tra con su nombre, y la busqueda."""
    if not os.path.isdir(TAREAS):
        return []
    halladas = []
    for raiz, dirs, files in os.walk(TAREAS):
        dirs.sort()
        if raiz == TAREAS:
            continue
        if any(x.endswith(".tra") for x in files):
            halladas.append(os.path.relpath(raiz, TAREAS).replace("\\", "/"))
    if any(f.endswith(".prs") for f in os.listdir(TAREAS)):
        halladas.insert(0, "tareas")
    return sorted(halladas)


def cuenta(carpeta):
    """Con que cuenta una tarea: lo suyo, o lo del mundo, o con nada."""
    nombre = os.path.basename(os.path.abspath(carpeta))
    cs = candidatos(carpeta, nombre)
    if not cs:
        return "[FALTA EN bin/]"
    propio = [c for c in cs if os.path.basename(c).startswith("paso")]
    if propio:
        return "paso" + os.path.splitext(propio[0])[1]
    if len(cs) == 1 and os.path.dirname(cs[0]) != BIN:
        return os.path.basename(cs[0]) + " (motor propio)"
    return "bin/" + os.path.basename(cs[0])


def main(argv):
    if len(argv) < 2:
        print("uso: ejecutar.py --listar | --verificar | [--sin-tra] <tarea>")
        return 1

    if argv[1] == "--verificar":
        malos = 0
        vistos = []
        for base in (TAREAS, ENTE):
            if not os.path.isdir(base):
                continue
            for n in sorted(os.listdir(base)):
                c = os.path.join(base, n)
                if not os.path.isdir(c):
                    continue
                if base == TAREAS and not any(f.endswith(".prs") for f in os.listdir(c)):
                    # un folder de proceso sin corte se declara; tareas/ es otra cosa
                    if n != "tareas":
                        ok, msg = verificar(c)
                        print(("[ok]    " if ok else "[falla] ") + n + ": " + msg)
                        malos += 0 if ok else 1
                        vistos.append(n)
                    continue
                if not procesos_de(c):
                    continue
                if base == ENTE and n not in SUELTOS:
                    continue
                vistos.append(n)
                ok, msg = verificar(c)
                print(("[ok]    " if ok else "[falla] ") + n + ": " + msg)
                malos += 0 if ok else 1
        print("")
        if malos:
            print("falla: {} folder(s) sin corte".format(malos))
            return 1
        print("pasa: {} folders con su corte".format(len(vistos)))
        return 0

    if argv[1] == "--listar":
        for n in indice():
            carpeta = carpeta_de(n)
            print("{:<28} {}".format(n, cuenta(carpeta)))
        return 0

    args = [a for a in argv[1:]]
    sin_tra = "--sin-tra" in args
    args = [a for a in args if a != "--sin-tra"]
    if not args:
        print("[FALTA EL NOMBRE] di que tarea")
        return 1

    nombre = args[0]
    carpeta = carpeta_de(nombre)
    ok, msg = verificar(carpeta)
    if not ok:
        print("[ACTIVIDAD - SIN CORTE] " + msg)
        return 2

    proceso = procesos_de(carpeta)[0]
    c = cortes(leer(os.path.join(carpeta, proceso)))
    print("[{}] {}".format(os.path.basename(carpeta), proceso))
    for k in CAMPOS:
        print("  {} {}".format(k, c[k]))

    # el corte, y si no cambio desde la ultima vez
    firma = firma_del_corte(c)
    antes = None
    previa = os.path.join(carpeta, ".corte")
    if os.path.isfile(previa):
        antes = leer(previa).strip()
    if antes == firma and not sin_tra:
        print("")
        print("[IGUAL] el corte no cambio desde la ultima corrida ({}): no se corre".format(firma))
        print("        si ya cambio algo que el corte no ve, se corre con --sin-tra")
        return 3
    if antes == firma and sin_tra:
        print("")
        print("[IGUAL] el corte no cambio: se corre igual porque se pidio --sin-tra")

    # lo que lo cumple
    cs = candidatos(carpeta, nombre)
    if not cs:
        print("")
        print("[FALTA EN bin/] esta tarea declara su corte, y este mundo no tiene con que cumplirlo.")
        print("                 se busca: paso.<ext> en la tarea, o {} en bin/.".format(nombre))
        print("                 no se improvisa.")
        if not sin_tra:
            dejartra(carpeta, proceso, c["Entra:"], "[FALTA EN bin/]", "codigo 2")
        return 2

    ruta = cs[0]
    if motor_propio(carpeta) == ruta:
        # el motor sabe que tarea es: se le pasa su nombre, y nada mas
        salida, codigo, aviso = correr(ruta, [os.path.basename(os.path.abspath(carpeta))])
    else:
        salida, codigo, aviso = correr(ruta, [c["Entra:"], c["Sale:"], carpeta])
    print("")
    if aviso:
        print(aviso)
    print(salida)

    if sin_tra:
        return codigo

    # el rastro: el .tra y la memoria
    tra = dejartra(carpeta, proceso, c["Entra:"], salida[:400], "codigo " + str(codigo))
    with open(previa, "w", encoding="utf-8", newline="") as fh:
        fh.write(firma)
    registro = memoria(carpeta, {
        "tarea": os.path.basename(os.path.abspath(carpeta)),
        "proceso": proceso,
        "firma": firma,
        "decidio": salida.splitlines()[0][:200] if salida else "",
        "salio": codigo,
        "con": os.path.relpath(ruta, ENTE).replace("\\", "/"),
        "sostuvo": (c["Sale:"] or "")[:200],
        "limite": (c["Entra:"] or "")[:200],
    })
    print("")
    print("deja: " + os.path.relpath(tra, ENTE) + "  (el rastro, no el corte)")
    print("memoria: entrada {} con huella {}".format(registro["id"], registro["firma"]))
    return codigo


if __name__ == "__main__":
    sys.exit(main(sys.argv))
