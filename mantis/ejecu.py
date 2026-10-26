#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ejecu.py - el unico archivo no-estandar de mantis.

No sabe que hace un proceso: lee su corte, comprueba la entrada, lo corre.
Los procesos viven en folders/, y cada uno declara:

    Entra:    / Falla si: / Sale: / Consume:

Un folder puede traer su propio paso, en un archivo <folder>.paso (python).

Uso:
    python ejecu.py --verificar          todos los folders tienen su corte
    python ejecu.py --listar             que folders hay
    python ejecu.py <folder>             corre el folder
    python ejecu.py <folder> --sin-tra   corre sin dejar .tra

Sale 0 si pasa, 1 si falla el proceso, 2 si el folder no tiene corte.
Siempre dice el porque.
"""
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = AQUI if os.path.isdir(os.path.join(AQUI, "folders")) else os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
FOLDERS = os.path.join(MANTIS, "folders")

CAMPOS = ("Entra:", "Falla si:", "Sale:", "Consume:")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def cortes(texto):
    fuera = {}
    for c in CAMPOS:
        m = re.search(r"[-*]\s*\*\*" + re.escape(c) + r"\*\*\s*(.*)", texto)
        if m:
            fuera[c] = m.group(1).strip()
    return fuera


def procesos_de(carpeta):
    return sorted(f for f in os.listdir(carpeta) if f.endswith(".prs"))


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


def dejartra(carpeta, proceso, entro, salio, veredicto):
    nombre = os.path.basename(os.path.abspath(carpeta))
    p = os.path.join(carpeta, nombre + ".tra")
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
        "**Distancia:** {v}\n\n"
        "## Procesos\n\n"
        "**Procesos:** {proc}\n"
    ).format(n=nombre, proc=proceso, ahora=ahora, e=entro, s=salio, v=veredicto)
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(cuerpo)
    return p


def correr_paso(carpeta):
    """El paso del folder, si lo tiene. Devuelve (salida, codigo)."""
    nombre = os.path.basename(os.path.abspath(carpeta))
    paso = os.path.join(carpeta, nombre + ".paso")
    if not os.path.isfile(paso):
        return "el folder no trae paso: solo declara su corte", 0
    r = subprocess.run([sys.executable, paso], capture_output=True, text=True)
    salida = (r.stdout or "") + (r.stderr or "")
    return salida.strip(), r.returncode


def main(argv):
    if len(argv) < 2:
        print("uso: ejecu.py --verificar | --listar | <folder> [--sin-tra]")
        return 1

    if argv[1] == "--verificar":
        if not os.path.isdir(FOLDERS):
            print("[SIN FOLDERS] no esta " + FOLDERS)
            return 1
        malos = 0
        for nombre in sorted(os.listdir(FOLDERS)):
            c = os.path.join(FOLDERS, nombre)
            if os.path.isdir(c):
                ok, msg = verificar(c)
                print(("[ok]    " if ok else "[falla] ") + nombre + ": " + msg)
                malos += 0 if ok else 1
        print("")
        if malos:
            print("falla: {} folder(s) sin corte".format(malos))
            return 1
        print("pasa: todos los folders tienen su corte")
        return 0

    if argv[1] == "--listar":
        for nombre in sorted(os.listdir(FOLDERS)):
            print(nombre)
        return 0

    carpeta = os.path.join(FOLDERS, argv[1]) if not os.path.isdir(argv[1]) else argv[1]
    ok, msg = verificar(carpeta)
    if not ok:
        print("[ACTIVIDAD - SIN CORTE] " + msg)
        return 2

    proceso = procesos_de(carpeta)[0]
    c = cortes(leer(os.path.join(carpeta, proceso)))
    print("[{}] {}".format(os.path.basename(carpeta), proceso))
    print("  Entra:    " + c["Entra:"])
    print("  Falla si: " + c["Falla si:"])
    print("  Sale:     " + c["Sale:"])
    print("  Consume:  " + c["Consume:"])

    salida, codigo = correr_paso(carpeta)
    print("")
    print(salida)

    if "--sin-tra" not in argv:
        tra = dejartra(carpeta, proceso, c["Entra:"], salida[:400], "codigo " + str(codigo))
        print("")
        print("deja: " + os.path.relpath(tra, MANTIS))
    return codigo


if __name__ == "__main__":
    sys.exit(main(sys.argv))
