#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""importar.py - el texto a la base, para que el .db se pueda rehacer.

Lee .memoria continua/rastro/texto/*.jsonl y reconstruye mantis.db.
Si la base existe, la reemplaza: el texto manda.

Uso:
    python mantis/procesos/importar.py            reconstruye la base
    python mantis/procesos/importar.py --probar   lo hace en temp y compara conteos

La prueba de verdad es esta: se borra la base, se importa, y el jugo vuelve.
"""
import json
import os
import sqlite3
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
RASTRO = os.path.join(REPO, ".memoria continua", "rastro")
TEXTO = os.path.join(RASTRO, "texto")
ESQUEMA = os.path.join(RASTRO, "esquema.sql")

TABLAS = ["pieza", "entrada", "pase", "candado", "corrida", "descarte", "ruta", "enlace"]


def reconstruir(destino):
    esq = open(ESQUEMA, "r", encoding="utf-8").read()
    con = sqlite3.connect(destino)
    con.executescript(esq)
    totales = {}
    for t in TABLAS:
        ruta = os.path.join(TEXTO, t + ".jsonl")
        if not os.path.isfile(ruta):
            totales[t] = 0
            continue
        cols = [r[1] for r in con.execute("PRAGMA table_info('{}')".format(t))]
        registros = []
        with open(ruta, "r", encoding="utf-8") as fh:
            for linea in fh:
                linea = linea.strip()
                if linea:
                    registros.append(json.loads(linea))
        insertados = 0
        for reg in registros:
            llaves = [c for c in cols if c in reg]
            valores = [reg[c] for c in llaves]
            con.execute(
                "INSERT INTO {} ({}) VALUES ({})".format(
                    t, ",".join(llaves), ",".join("?" * len(llaves))),
                valores,
            )
            insertados += 1
        con.commit()
        totales[t] = insertados
    con.close()
    return totales


def main():
    if not os.path.isfile(ESQUEMA):
        print("[SIN ESQUEMA] no esta {}".format(ESQUEMA))
        return 2
    if not os.path.isdir(TEXTO):
        print("[SIN TEXTO] no hay texto exportado: corre exportar.py primero.")
        return 2

    probar = "--probar" in sys.argv
    destino = os.path.join(tempfile.gettempdir(), "mantis-import-probar.db") if probar else os.path.join(RASTRO, "mantis.db")
    if probar and os.path.isfile(destino):
        os.remove(destino)

    totales = reconstruir(destino)
    print("base: {}".format(destino))
    for t in TABLAS:
        print("{:<10} {:>4}".format(t, totales[t]))
    print("total: {}".format(sum(totales.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
