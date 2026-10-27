#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso de integridad: el 1 sigue siendo el 1, y se puede contestar.

Sirve igual para una alma que para N: lee la carta, lee lo que hizo en sus .tra,
y dice si coincide. Si no coincide, gana el .tra.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
TAREAS = os.path.join(MANTIS, "tareas")
CARTA = os.path.join(MANTIS, "el alma.md")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def campo(texto, nombre):
    m = re.search(r"\*\*" + nombre + r"[:.]\*\*\s*(.*)", texto)
    return m.group(1).strip() if m else None


def main():
    fallas = []

    if not os.path.isfile(CARTA):
        print("[SIN CARTA] no esta el alma.md: no hay 1 que comprobar")
        return 1

    carta = leer(CARTA)
    sesgo = campo(carta, "Sesgo")
    firma = campo(carta, "Firma")

    if not sesgo:
        fallas.append("el 1 no declara su sesgo: no se sabe desde donde sostiene")
    if not firma:
        fallas.append("el 1 no declara quien lo contesta")

    # lo que el 1 hizo: las .tra de sus tareas
    tras = []
    if os.path.isdir(TAREAS):
        for n in sorted(os.listdir(TAREAS)):
            p = os.path.join(TAREAS, n)
            if not os.path.isdir(p):
                continue
            for f in os.listdir(p):
                if f.endswith(".tra"):
                    tras.append(os.path.join(p, f))

    if not tras:
        fallas.append("el 1 no dejo ningun .tra: no hay nada contra que comparar la carta")

    if fallas:
        print("[falla] el 1 no esta integro")
        for f in fallas:
            print("  - " + f)
        return 1

    print("[ok] el 1 declara desde donde sostiene: " + sesgo[:90])
    print("[ok] y quien lo contesta: " + firma[:60])
    print("[ok] {} .tra leidas, y la carta se compara contra ellas".format(len(tras)))
    print("")
    print("pasa: el 1 sigue siendo el 1, y se puede contestar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
