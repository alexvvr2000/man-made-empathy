#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso de tareas/: lee el disco, compara con el indice, y se rehace si cambio.

No decide que tarea crear: declara que entro, que salio, y que se movio.
La tarea que cubre una falta nueva la crea MUDAR, no esto.
"""
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
TAREAS = os.path.join(MANTIS, "tareas")
INDICE = os.path.join(TAREAS, "tareas.indice")


def leer_indice():
    if not os.path.isfile(INDICE):
        return {"fecha": None, "tareas": []}
    with open(INDICE, "r", encoding="utf-8") as fh:
        return json.load(fh)


def en_disco():
    fuera = []
    for n in sorted(os.listdir(TAREAS)):
        p = os.path.join(TAREAS, n)
        if not os.path.isdir(p):
            continue
        if any(f.endswith(".prs") for f in os.listdir(p)):
            fuera.append(n)
    return fuera


def escribir_indice(ahora, tareas):
    with open(INDICE, "w", encoding="utf-8") as fh:
        json.dump({"fecha": ahora, "tareas": tareas}, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def main():
    from datetime import datetime, timezone
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")

    antes = leer_indice()
    previas = set(antes.get("tareas", []))
    actuales = set(en_disco())

    entraron = sorted(actuales - previas)
    salieron = sorted(previas - actuales)

    print("[ok] tareas en disco: {}".format(len(actuales)))
    for t in sorted(actuales):
        print("  - " + t)

    if not antes.get("fecha"):
        print("")
        print("[nace] el indice no existia: se escribe con las {} tareas de hoy".format(len(actuales)))
    else:
        if entraron:
            print("")
            print("[entro] {}: {}".format(len(entraron), ", ".join(entraron)))
        if salieron:
            print("")
            print("[salio] {}: {}".format(len(salieron), ", ".join(salieron)))
        if not entraron and not salieron:
            print("")
            print("[igual] nada entro ni salio desde {}".format(antes["fecha"]))

    escribir_indice(ahora, sorted(actuales))
    print("")
    if entraron or salieron:
        print("pasa: el folder se rehizo, y lo declara")
    else:
        print("pasa: el folder no cambio, y lo declara")
    return 0


if __name__ == "__main__":
    sys.exit(main())
