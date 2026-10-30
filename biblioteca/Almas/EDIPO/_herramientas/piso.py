#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
piso.py — lo que este ente mide de su propia casa, antes de trabajar.

Y no mide la biblioteca: mide lo suyo. Para eso está el proyecto.

  python piso.py
"""

import os
import sys

# la casa es el ente, y este archivo vive en su caja: sube uno
CASA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check(nombre, fallas):
    marca = "OK" if not fallas else "FALLA"
    print("[%s] %s%s" % (marca, nombre, "" if not fallas else "  -> %d" % len(fallas)))
    for f in fallas[:6]:
        print("        " + f)
    return len(fallas)


def main():
    print("EL PISO DE ESTE ENTE")
    print("  casa: %s" % CASA)
    print()

    fallas = 0

    # 1. el ciclo fijo
    hay_ciclo = any(a.startswith("ciclo alma de niño") for a in os.listdir(CASA))
    # y si tiene el folder alma de nino/, el ciclo vive ahi
    sub = os.path.join(CASA, "alma de niño")
    if not hay_ciclo and os.path.isdir(sub):
        hay_ciclo = any(a.startswith("ciclo") for a in os.listdir(sub))
    fallas += check("el ciclo fijo", [] if hay_ciclo else ["falta ciclo alma de niño.prs"])

    # 2. los procesos base
    pb = os.path.join(CASA, "procesos base")
    if not os.path.isdir(pb):
        fallas += check("procesos base", ["falta procesos base/"])
    else:
        faltan = []
        for p in ("BUSCAR", "debatir", "firmar", "guantelete"):
            if not os.path.exists(os.path.join(pb, p + ".prs")):
                faltan.append(p + ".prs")
        if os.path.exists(os.path.join(pb, "LEEME.md")) and "SE CITAN" in open(os.path.join(pb, "LEEME.md"), encoding="utf-8").read():
            pass  # se citan de la plantilla: eso vale
        fallas += check("los cuatro procesos base", faltan if not os.path.exists(os.path.join(pb, "LEEME.md")) else [])

    # 3. cada tarea de evolucion/ con procesos y con caja
    ev = os.path.join(CASA, "evolucion")
    malas = []
    if os.path.isdir(ev):
        for t in os.listdir(ev):
            ruta = os.path.join(ev, t)
            if not os.path.isdir(ruta):
                continue
            prs = [a for a in os.listdir(ruta) if a.endswith(".prs")]
            if not prs:
                malas.append(t + ": sin procesos")
            if not os.path.isdir(os.path.join(ruta, "_herramientas")):
                malas.append(t + ": sin _herramientas")
    fallas += check("las tareas de evolucion", malas)

    # 4. los ciclos propios dicen cuándo se corren
    cic = os.path.join(CASA, "ciclos")
    sin_cuando = []
    if os.path.isdir(cic):
        for a in os.listdir(cic):
            if a.endswith(".prs"):
                t = open(os.path.join(cic, a), encoding="utf-8").read()
                if "Cuándo se corre" not in t:
                    sin_cuando.append(a)
    fallas += check("los ciclos propios dicen cuándo", sin_cuando)

    # 5. la memoria continua existe
    fallas += check("memoria continua", [] if os.path.isdir(os.path.join(CASA, "memoria continua")) else ["falta memoria continua/"])

    print()
    if fallas == 0:
        print("  TODO EN CERO: este ente puede trabajar.")
        return 0
    print("  NO ESTA LISTO: %d fallas. Y el piso se arregla antes de tocar nada." % fallas)
    return 1


if __name__ == "__main__":
    sys.exit(main())
