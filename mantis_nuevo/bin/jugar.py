#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""jugar.py - el jugo de la memoria en un solo archivo portable.

Lee la tabla pieza de la base y escribe UN archivo:
    mantis/vision del autor/contexto/pieza.jsonl
Una linea, una pieza. Sin carpetas por clase, sin 91 archivos.

Uso:
    python mantis/procesos/jugar.py            escribe el jsonl
    python mantis/procesos/jugar.py --contar   solo cuenta, no escribe
"""
import json
import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
DB = os.path.join(REPO, ".memoria continua", "rastro", "mantis.db")
DESTINO = os.path.join(REPO, "mantis", "vision del autor", "contexto")
SALIDA = os.path.join(DESTINO, "pieza.jsonl")


def estado_de(referencia, ficcion):
    sin_ref = not referencia or str(referencia).strip().lower().startswith("ninguna")
    sin_fic = not ficcion or str(ficcion).strip().lower().startswith("ninguna")
    if sin_ref:
        return "CRUDO"
    if sin_fic:
        return "PARCIAL"
    return "PROCESADA"


def main():
    if not os.path.isfile(DB):
        sys.stderr.write("[SIN MEMORIA] no esta la base: no se inventa un jugo vacio.\n")
        return 2

    con = sqlite3.connect(DB)
    filas = con.execute(
        'SELECT orden, clase, nombre, "expansión", porque, referencia, pregunta, ficcion '
        "FROM pieza WHERE estado='viva' ORDER BY orden"
    ).fetchall()
    con.close()

    if "--contar" in sys.argv:
        print("piezas vivas: {}".format(len(filas)))
        return 0

    os.makedirs(DESTINO, exist_ok=True)
    with open(SALIDA, "w", encoding="utf-8") as fh:
        for orden, clase, nombre, expansion, porque, referencia, pregunta, ficcion in filas:
            fh.write(json.dumps({
                "orden": orden,
                "clase": clase,
                "nombre": nombre,
                "expansión": expansion,
                "porque": porque,
                "referencia": referencia,
                "pregunta": pregunta,
                "ficcion": ficcion,
                "estado": estado_de(referencia, ficcion),
            }, ensure_ascii=False) + "\n")

    print("piezas: {}".format(len(filas)))
    print("archivo: {}".format(os.path.relpath(SALIDA, REPO).replace("\\", "/")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
