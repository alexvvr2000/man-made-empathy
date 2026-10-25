#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""candados.py - un archivo por candado, desde la memoria.

Cada pieza que el autor sostuvo y que puede ser atacada por separado se vuelve
un candado: un archivo corto, con la voz del autor, su porqué, de dónde viene,
y una sección que dice qué lo abre.

Uso:
    python mantis/bin/candados.py            escribe todos los candados explicitos
    python mantis/bin/candados.py --contar   solo cuenta
"""
import os
import re
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
DB = os.path.join(REPO, ".memoria continua", "rastro", "mantis.db")
DESTINO = os.path.join(REPO, "Tesis", "candados", "autor")
CERO = "000 la tesis.md"


def plano(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"[\\/:*?\"<>|]", "-", s)
    return s[:80].rstrip(" .")


def main():
    if not os.path.isfile(DB):
        sys.stderr.write("[SIN MEMORIA] no esta la base.\n")
        return 2
    con = sqlite3.connect(DB)
    filas = con.execute(
        'SELECT orden, nombre, "expansión", porque, referencia, pregunta, ficcion '
        "FROM pieza WHERE estado='viva' AND clase='principio' ORDER BY orden, id"
    ).fetchall()
    con.close()

    if "--contar" in sys.argv:
        print("candados explicitos: {}".format(len(filas)))
        return 0

    os.makedirs(DESTINO, exist_ok=True)
    escritos = 0
    for orden, nombre, expansion, porque, referencia, pregunta, ficcion in filas:
        archivo = os.path.join(DESTINO, "{:03d} {}.md".format(int(orden), plano(nombre)))
        # El candado cero es la cabeza de la tesis y lo que conecta el repo:
        # este script no lo pisa. Se escribe, se dice, y se salta.
        if os.path.basename(archivo) == CERO:
            print("[NO SE PISA] {}: es el candado cero y lo escribe la autoridad.".format(CERO))
            continue
        # El campo que dice "ninguna" no se escribe: un apartado vacio no es contenido.
        def campo(etiqueta, valor):
            valor = (valor or "").strip()
            if not valor or valor.lower().rstrip(".") == "ninguna":
                return None
            valor = valor[0].upper() + valor[1:]
            if not valor.endswith((".", "!", "?")):
                valor += "."
            return "**{}.** {}".format(etiqueta, valor)

        texto = ["# {}".format(nombre), ""]
        for etiqueta, valor in (("Posición", expansion), ("Por qué se sostiene", porque),
                                ("De dónde viene", referencia), ("Qué pregunta deja", pregunta),
                                ("Ficción", ficcion)):
            linea = campo(etiqueta, valor)
            if linea:
                texto += [linea, ""]
        texto += [
            "**Se abre con fricción, y no se reescribe: `../../../mantis/procesos/LLAVE.prs`.**",
            "",
            "---",
            "",
            "Del historial de sesgos del autor.",
            "",
        ]
        with open(archivo, "w", encoding="utf-8") as fh:
            fh.write("\n".join(texto))
        escritos += 1

    print("candados escritos: {}".format(escritos))
    print("en: {}".format(os.path.relpath(DESTINO, REPO).replace("\\", "/")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
