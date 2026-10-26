#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso del folder 'los candados': dice el estado de los candados.

No los abre: abrirlos es fricción, y la fricción la hace quien decide.
Esta vez declara qué hay, cuántos son, y cuáles no tienen llave escrita.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
CANDADOS = os.path.join(REPO, "Tesis", "candados", "autor")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def main():
    if not os.path.isdir(CANDADOS):
        print("[SIN CANDADOS] no esta " + CANDADOS)
        return 1

    carpetas = sorted(d for d in os.listdir(CANDADOS) if os.path.isdir(os.path.join(CANDADOS, d)))
    total = 0
    sin_llave = []
    sin_falsificador = []

    for cap in carpetas:
        ruta_cap = os.path.join(CANDADOS, cap)
        for f in sorted(os.listdir(ruta_cap)):
            if not f.endswith(".md"):
                continue
            total += 1
            t = leer(os.path.join(ruta_cap, f))
            if not re.search(r"LLAVE\.prs|llave|llave se hace", t, re.I):
                sin_llave.append(cap + "/" + f)
            if "Falsificador" not in t and "falsificador" not in t:
                sin_falsificador.append(cap + "/" + f)

    print("[ok] {} candados en {} carpetas".format(total, len(carpetas)))
    for cap in carpetas:
        n = len([f for f in os.listdir(os.path.join(CANDADOS, cap)) if f.endswith(".md")])
        print("  {:<32} {}".format(cap, n))

    if sin_llave:
        print("")
        print("[aviso] {} candado(s) no nombran su llave:".format(len(sin_llave)))
        for s in sin_llave[:10]:
            print("  - " + s)

    if sin_falsificador:
        print("")
        print("[falla] {} candado(s) sin falsificador:".format(len(sin_falsificador)))
        for s in sin_falsificador[:10]:
            print("  - " + s)
        return 1

    print("")
    print("pasa: todos los candados tienen falsificador")
    return 0


if __name__ == "__main__":
    sys.exit(main())
