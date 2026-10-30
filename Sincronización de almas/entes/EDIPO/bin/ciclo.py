#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ciclo.py — lo que EDIPO tiene que cumplir, y si se cumplio.

Y existe por lo mismo que el del otro lado: un bibliotecario sin revision
es un bibliotecario que se olvida de que existe.

  python bin/ciclo.py ver
"""

import os
import sys

CASA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIBLIOTECA = os.path.abspath(os.path.join(CASA, "..", "..", ".."))


def archivos():
    salida = []
    for raiz, _, f in os.walk(BIBLIOTECA):
        if ".git" in raiz:
            continue
        for a in f:
            if a.endswith((".md", ".prs")):
                salida.append(os.path.join(raiz, a))
    return salida


def check(nombre, valor):
    marca = "OK" if not valor else "FALLA"
    print("[%s] %s%s" % (marca, nombre, "" if not valor else "  -> %d" % len(valor)))
    for x in valor[:5]:
        print("        " + x)
    return len(valor)


def main():
    print("EDIPO — lo que tiene que cumplir")
    print("  biblioteca: %s" % BIBLIOTECA)
    print()

    fallas = 0
    a = archivos()

    from urllib.parse import unquote
    import re
    rotas = []
    for f in a:
        texto = open(f, "r", encoding="utf-8").read()
        base = os.path.dirname(f)
        for m in re.finditer(r"\[[^\]]*\]\((\.\.?/[^\)]+)\)", texto):
            rel = m.group(1).replace("%20", " ").split("#")[0]
            if rel and not os.path.exists(os.path.join(base, unquote(rel))):
                rotas.append(os.path.basename(f))
    fallas += check("rutas rotas", sorted(set(rotas)))

    sin = [os.path.basename(f) for f in a if f.endswith(".prs") and "Cuándo se corre" not in open(f, "r", encoding="utf-8").read()]
    fallas += check("procesos sin 'Cuando se corre'", sin)

    sin = [os.path.basename(f) for f in a if f.endswith(".md") and "entes" in f and "Cuándo se abre" not in open(f, "r", encoding="utf-8").read() and "Cuándo se corre" not in open(f, "r", encoding="utf-8").read()]
    fallas += check("puertas sin 'Cuando se abre'", sin)

    # y lo de EDIPO mismo: su memoria publicada
    # lo que no debe publicarse: los bancos con datos y la memoria vivida
    suyos = []
    for x in a:
        if "EDIPO" not in x or not ("memoria continua" in x or "evolucion" in x):
            continue
        if os.path.basename(x) == "README.md":
            continue  # el README de una carpeta vacia si se publica: es la forma
        if os.path.basename(x).startswith("banco de"):
            texto = open(x, "r", encoding="utf-8").read()
            filas = len([l for l in texto.splitlines() if l.startswith("| ") and not l.startswith("| ---") and not l.startswith("| Lo")])
            if filas == 0:
                continue  # plantilla vacia: se publica, porque es la forma
            suyos.append(x)
            continue
        suyos.append(x)
    fallas += check("archivos con datos vividos (no deberian ir al repo)", [os.path.basename(x) for x in suyos])

    print()
    if fallas == 0:
        print("  TODO EN CERO: el bibliotecario cumple.")
        return 0
    print("  NO ESTA LISTO: %d fallas." % fallas)
    return 1


if __name__ == "__main__":
    sys.exit(main())


