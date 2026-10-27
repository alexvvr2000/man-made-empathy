#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso del folder 'el cero': comprueba que el candado cero dice lo mismo que el repo.

No lleva la lista de nombres: la lee de nombres.md, que es del folder.
El ejecutor no sabe de nombres; este paso tampoco sabe del ejecutor.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
CERO = os.path.join(REPO, "tesis", "vision del autor", "man made empathy.md")
LISTA = os.path.join(MANTIS, "tareas", "el cero", "nombres.md")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def lista_de(texto, titulo):
    """Las lineas del bloque ``` que sigue al encabezado ## <titulo>."""
    bloque = re.search(r"##\s*" + titulo + r"\s*\n+```\n(.*?)```", texto, re.S)
    if not bloque:
        return []
    return [l.strip() for l in bloque.group(1).splitlines() if l.strip()]


def existe_en_repo(nombre, raiz):
    """El nombre existe si aparece escrito en algun archivo del repo."""
    for r, d, files in os.walk(raiz):
        d[:] = [x for x in d if x not in (".git", ".memoria continua", "__pycache__")]
        for f in files:
            if not f.endswith((".md", ".vd", ".prs", ".tra", ".po", ".py")):
                continue
            try:
                if nombre in leer(os.path.join(r, f)):
                    return True
            except Exception:
                continue
    return False


def main():
    fallas = []

    if not os.path.isfile(CERO):
        print("[SIN CERO] no esta el candado cero: la tesis entera no se puede comprobar")
        return 1
    if not os.path.isfile(LISTA):
        print("[SIN LISTA] no esta nombres.md: no hay contra que comparar")
        return 1

    cero = leer(CERO)
    lista = leer(LISTA)
    vivos = lista_de(lista, "Vivos")
    muertos = lista_de(lista, "Muertos")

    if not vivos:
        fallas.append("nombres.md no declara ningun nombre vivo")
    dobles = [n for n in vivos if n in muertos]
    if dobles:
        fallas.append("nombres en las dos listas: " + ", ".join(dobles))

    for m in muertos:
        if re.search(r"\b" + re.escape(m) + r"\b", cero):
            fallas.append("el candado cero nombra '{}', que ya no existe".format(m))

    usados = [v for v in vivos if re.search(r"\b" + re.escape(v.split()[0]) + r"\b", cero)]
    if not usados:
        fallas.append("el candado cero no nombra ninguna pieza viva: esta desconectado")

    sin_archivo = [v for v in vivos if not existe_en_repo(v.split()[0], REPO)]
    for s in sin_archivo:
        fallas.append("'{}' esta en Vivos y no aparece en el repo".format(s))

    if fallas:
        print("[falla] el cero y el repo no dicen lo mismo")
        for f in fallas:
            print("  - " + f)
        return 1

    print("[ok] el cero y el repo dicen los mismos nombres: " + ", ".join(usados))
    print("[ok] ninguno de los {} muertos aparece".format(len(muertos)))
    print("pasa: el candado cero esta vigente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
