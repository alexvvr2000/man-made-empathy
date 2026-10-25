#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pedir.py - la única entrada de MANTIS. Todo es on demand.

No corre nada en segundo plano y no escribe nada que no se le pida.
Si no se sabe dónde está el repo, lo descubre desde su propia ruta.
Si no hay memoria, lo dice y para: no crea una vacía.

Uso:
    python mantis/bin/pedir.py piso                 la corrida y la dirección
    python mantis/bin/pedir.py contexto             lo suelto (el jugo), desde la base, y se firma
    python mantis/bin/pedir.py pieza <orden>        una pieza, con sus enlaces
    python mantis/bin/pedir.py deuda                qué sigue en rojo
    python mantis/bin/pedir.py llave               (abre un candado: LLAVE.prs)
    python mantis/bin/pedir.py teoria              (tesis teórica: TEORIA.prs)
    python mantis/bin/pedir.py coro                (tesis de academia: CORO.prs)
    python mantis/bin/pedir.py mesa                (tesis práctica: MESA.prs)
    python mantis/bin/pedir.py privado <fuente>    (PRIVADO.prs)
    python mantis/bin/pedir.py stats <fuente>      (STATS.prs)

Los seis últimos declaran su proceso y no lo inventan: el proceso es el que dice
cómo se hace. Este archivo solo lleva al proceso, y para si no está.
"""
import os
import sqlite3
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.path.abspath(os.path.join(MANTIS, ".."))
DB = os.path.join(REPO, ".memoria continua", "rastro", "mantis.db")
PROCESOS = os.path.join(MANTIS, "procesos")


def hay_base():
    if not os.path.isfile(DB):
        print("[SIN MEMORIA] no esta la base en {}".format(DB))
        print("No se crea una vacia: una memoria vacia dice cero piezas y parece que uno miro.")
        return False
    return True


def correr(script, args=None):
    r = subprocess.run([sys.executable, os.path.join(AQUI, script)] + (args or []),
                       capture_output=True, text=True, cwd=REPO)
    return r.returncode, ((r.stdout or "") + (r.stderr or "")).rstrip()


def espera_proceso(nombre, extra=""):
    ruta = os.path.join(PROCESOS, nombre + ".prs")
    comp = os.path.join(AQUI, "componer.py")
    if not os.path.isfile(ruta):
        print("[VACIO - SIN PROCESO] falta procesos/{}.prs".format(nombre))
        print("No se improvisa: el proceso es el que dice como se hace.")
        return 1
    print("[PROCESO] procesos/{}.prs{}".format(nombre, extra))
    if nombre in ("TEORIA", "CORO", "MESA") and os.path.isfile(comp):
        print("[COMPONER] mantis/bin/componer.py --tipo {} --fuente <archivo>".format(nombre.lower()))
    print("Se abre el proceso y se sigue paso a paso. Este pedido no lo sustituye.")
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    que = sys.argv[1].lower()

    if que == "piso":
        for s in ("corrida.py", "direccion.py"):
            print("=== {} ===".format(s))
            code, salida = correr(s)
            print(salida)
        return 0

    if not hay_base():
        return 2

    if que == "contexto":
        print("[APAGADO] el jugo ya no es el camino del candado: lo que se sostiene de pie se escribe como candado.")
        print("Lo que ya estaba sigue en la base y en el texto, y se convierte cuando la autoridad lo pida.")
        return 0

    if que == "contexto-viejo":
        code, salida = correr("jugar.py")
        print(salida)
        if code == 0:
            destino = os.path.join(MANTIS, "..", "mantis", "vision del autor", "contexto", "pieza.jsonl")
            code2, salida2 = correr("firmar.py", [destino, "--quien", "mantis",
                                                  "--quito", "nada",
                                                  "--acepta", "que el contexto se pidio y se firmo"])
            print(salida2)
        return code

    if que == "pieza":
        if len(sys.argv) < 3:
            print("Falta el orden. Uso: pedir.py pieza <orden>")
            return 2
        con = sqlite3.connect(DB)
        filas = con.execute(
            'SELECT orden, clase, nombre, "expansión", porque, referencia, pregunta, ficcion, estado '
            "FROM pieza UNION ALL SELECT NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL "
            "WHERE 0").fetchall() if False else con.execute(
            'SELECT orden, clase, nombre, "expansión", porque, referencia, pregunta, ficcion, estado '
            "FROM pieza WHERE orden = ?", (sys.argv[2],)).fetchall()
        con.close()
        if not filas:
            print("[VACIO - SIN PIEZA] no hay pieza con orden {}".format(sys.argv[2]))
            return 2
        for f in filas:
            print("orden:     {}".format(f[0]))
            print("clase:     {}".format(f[1]))
            print("nombre:    {}".format(f[2]))
            print("expande:   {}".format(f[3]))
            print("porque:    {}".format(f[4]))
            print("de donde:  {}".format(f[5]))
            print("pregunta:  {}".format(f[6]))
            print("ficcion:   {}".format(f[7]))
            print("estado:    {}".format(f[8]))
        return 0

    if que == "deuda":
        con = sqlite3.connect(DB)
        crudas = con.execute(
            "SELECT COUNT(*) FROM pieza WHERE estado='viva' AND (referencia IS NULL OR referencia='' OR referencia LIKE 'ninguna%')"
        ).fetchone()[0]
        vacias = con.execute("SELECT COUNT(*) FROM enlace").fetchone()[0]
        con.close()
        print("piezas crudas (sin fuente): {}".format(crudas))
        print("relaciones declaradas:      {}".format(vacias))
        print("y lo que no se puede contar desde la base: las citas muertas del repo.")
        print("Se corre con: pedir.py piso")
        return 0

    for nombre, clave in (("llave", "LLAVE"), ("teoria", "TEORIA"), ("coro", "CORO"),
                          ("mesa", "MESA"), ("privado", "PRIVADO"), ("stats", "STATS")):
        if que == nombre:
            return espera_proceso(clave, " ".join(sys.argv[2:]))

    print("[VACIO - SIN PEDIDO] no hay proceso para '{}'".format(que))
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())

