#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""exportar.py - la base a texto, para que el jugo no viva en un binario.

Escribe un .jsonl por tabla en .memoria continua/rastro/texto/.
Una linea, un registro, con sus llaves en el orden de la tabla.

Uso:
    python mantis/procesos/exportar.py          exporta everything
    python mantis/procesos/exportar.py --pieza  solo la tabla pieza

No depende de ninguna ruta de esta maquina: descubre el repo desde el archivo.
Si no hay base, lo dice y para: no exporta una vacia.
"""
import json
import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
DB = os.path.join(REPO, ".memoria continua", "rastro", "mantis.db")
DESTINO = os.path.join(REPO, ".memoria continua", "rastro", "texto")

TABLAS = ["pieza", "entrada", "pase", "candado", "corrida", "descarte", "ruta", "enlace"]


def columnas(con, tabla):
    return [r[1] for r in con.execute("PRAGMA table_info('{}')".format(tabla))]


def exportar(con, tabla):
    cols = columnas(con, tabla)
    if not cols:
        return None, 0
    ruta = os.path.join(DESTINO, tabla + ".jsonl")
    filas = con.execute("SELECT * FROM {}".format(tabla)).fetchall()
    with open(ruta, "w", encoding="utf-8") as fh:
        for fila in filas:
            registro = dict(zip(cols, fila))
            fh.write(json.dumps(registro, ensure_ascii=False) + "\n")
    return ruta, len(filas)


def main():
    if not os.path.isfile(DB):
        print("[SIN MEMORIA] no esta la base en {}".format(DB))
        print("No se exporta una vacia: un texto vacio se lee como que no habia nada.")
        return 2

    solo = None
    for i, a in enumerate(sys.argv):
        if a.startswith("--") and a[2:] in TABLAS:
            solo = a[2:]

    os.makedirs(DESTINO, exist_ok=True)
    con = sqlite3.connect(DB)
    total = 0
    for t in TABLAS:
        if solo and t != solo:
            continue
        ruta, n = exportar(con, t)
        if ruta is None:
            print("{}: no existe".format(t))
            continue
        total += n
        print("{:<10} {:>4} registros -> {}".format(t, n, os.path.relpath(ruta, REPO).replace("\\", "/")))
    con.close()
    print("total: {} registros".format(total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
