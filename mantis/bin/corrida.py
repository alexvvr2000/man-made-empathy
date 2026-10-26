#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""corrida.py - la corrida del piso. Se corre ANTES de tocar el repo.
Requisitos que puede comprobar sola:
  1. Los estandares existen donde se citan.
  4. Nada sucio dentro del repo: binarios, caches, __pycache__, salidas de prueba.
Los otros tres (clase, reverso y rastro) se comprueban por artefacto al escribir.
Sale 0 si pasa, 1 si falla. Con --despues declara que corre tarde y no cuenta.
"""
import os, sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
BASE_ALMAS = os.path.join(REPO, "sincronizacion de almas", "faro 1.0", "lenguajes")
GRUPOS = ("formacion", "friccion", "relacion", "salida")


def estandar(nombre):
    for g in GRUPOS:
        p = os.path.join(BASE_ALMAS, g, nombre)
        if os.path.isfile(p):
            return p
    p = os.path.join(BASE_ALMAS, nombre)
    return p if os.path.isfile(p) else None
SUCIO_EXT = (".exe", ".dll", ".pdb", ".zip", ".pyc", ".aux", ".log")
SUCIO_DIRS = ("__pycache__", ".pytest_cache", "node_modules", "piso de prueba")


def rel(p):
    return os.path.relpath(p, REPO).replace("\\", "/")


def r1():
    faltan = [n for n in ("FORMATO.md", "LENGUAJE.md", "CLARIDAD.md", "JONN.md", "CONTEXTO.md", "ALAS.md")
              if estandar(n) is None]
    if faltan:
        return False, "faltan: " + ", ".join(faltan)
    return True, "los estandares estan donde se citan"


def r4():
    sucios = []
    for raiz, dirs, files in os.walk(REPO):
        partes = raiz.split(os.sep)
        if ".git" in partes or ".memoria continua" in partes:
            continue
        for d in list(dirs):
            if d in SUCIO_DIRS:
                sucios.append(rel(os.path.join(raiz, d)) + "/")
        for f in files:
            bajo = f.lower()
            if bajo.startswith("prueba.") or bajo.endswith(SUCIO_EXT) or bajo.endswith((".ps1", ".bat", ".vbs", ".sh")):
                sucios.append(rel(os.path.join(raiz, f)))
    if sucios:
        return False, "; ".join(sucios[:8])
    return True, "limpio"


def main():
    ok1, d1 = r1()
    ok4, d4 = r4()
    v = "pasa" if (ok1 and ok4) else "falla"
    if "--despues" in sys.argv:
        v = "tarde: no cuenta como piso"
    print("Piso: " + datetime.now(timezone.utc).isoformat())
    print("1. Estandares que existen: " + ("si" if ok1 else "no") + " -> " + d1)
    print("4. Limpieza del arbol: " + ("si" if ok4 else "no") + " -> " + d4)
    print("2, 3 y 5: por artefacto, al escribir; 5 al cerrar el turno")
    print("Veredicto: " + v)
    return 0 if v == "pasa" else 1


if __name__ == "__main__":
    sys.exit(main())







