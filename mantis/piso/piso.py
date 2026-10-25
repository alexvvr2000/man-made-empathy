#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""piso.py - el punto de entrada del repo, para cualquiera.

Uso:
    python mantis/piso/piso.py            corre la corrida y la direccion
    python mantis/piso/piso.py --todo     corre todo lo que se puede correr
    python mantis/piso/piso.py --vision "vision del autor"
                                          compone la tesis de una vision

No sabe donde esta el repo: lo descubre desde su propia ruta. Si el repo se
clona en otra maquina, esto sigue funcionando. Y si no encuentra la base, lo
dice y para: no crea una vacia ni sigue como si nada.
"""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))

BASE = os.path.join(REPO, ".memoria continua", "rastro", "mantis.db")
ESQUEMA = os.path.join(REPO, ".memoria continua", "rastro", "esquema.sql")


def correr(script, args=None):
    cmd = [sys.executable, script] + (args or [])
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    print("repo: {}".format(REPO))

    if not os.path.isdir(".git"):
        pass
    if not os.path.isfile(BASE):
        print("[SIN MEMORIA] no esta la base en {}".format(BASE))
        print("No se crea una vacia: una memoria vacia dice cero piezas y parece que uno miro.")
        return 2
    if not os.path.isfile(ESQUEMA):
        print("[SIN ESQUEMA] no esta el esquema: el clon no puede reproducir la memoria.")
        return 2

    vision = None
    for i, a in enumerate(sys.argv):
        if a == "--vision" and i + 1 < len(sys.argv):
            vision = sys.argv[i + 1]

    if vision:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        tes = os.path.join(os.path.dirname(AQUI), "procesos", "tesis.py")
        if not os.path.isfile(tes):
            print("[SIN MECANISMO] no esta tesis.py junto al repo.")
            return 2
        code, salida = correr(tes, ["--vision", vision])
        print(salida)
        return code

    scripts = [
        os.path.join(AQUI, "corrida.py"),
        os.path.join(AQUI, "direccion.py"),
    ]
    resultados = []
    for s in scripts:
        if not os.path.isfile(s):
            print("[FALTA] {}".format(os.path.basename(s)))
            resultados.append(2)
            continue
        print("")
        print("=== {} ===".format(os.path.basename(s)))
        code, salida = correr(s)
        print(salida.rstrip())
        resultados.append(code)

    print("")
    print("--- resumen ---")
    for s, c in zip(scripts, resultados):
        print("{:<16} {}".format(os.path.basename(s), {0: "pasa", 1: "falla", 2: "indeterminado"}.get(c, c)))
    return max(resultados) if resultados else 0


if __name__ == "__main__":
    sys.exit(main())


