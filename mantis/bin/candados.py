#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""candados.py - una pieza de la memoria, a un candado en su carpeta.

El archivo manda. Lo que ya esta escrito no se toca: este script mete lo que no
existe, y nada mas. Volver a escribir un candado que ya vive es lo que lo dejo
viejo dos veces, y por eso esta prohibido aqui.

Una pieza entra solo si esta completa: posicion, por que se sostiene, de donde
viene, que pregunta deja, y una familia. Si le falta algo, se queda diferida y
se escribe en la base que le falta, en vez de un archivo a medio hacer.

Uso:
    python mantis/bin/candados.py --contar    cuantas estarian listas, y cuantas no
    python mantis/bin/candados.py --probar    dice que haria, sin escribir nada
    python mantis/bin/candados.py             escribe los que faltan, y solo esos
"""
import os
import re
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
DB = os.path.join(REPO, ".memoria continua", "rastro", "mantis.db")

# La carpeta es la familia de la pieza. El nombre de la familia es corto en la
# base ("el lenguaje") y con numero en el disco ("04 el lenguaje").
DESTINO = os.path.join(REPO, "Tesis", "candados", "autor")
CARPETAS = {
    "el cero": "000 el cero",
    "el ente y el metodo": "01 el ente y el metodo",
    "el alma y el libre albedrio": "02 el alma y el libre albedrio",
    "el nombre y la obra": "03 el nombre y la obra",
    "el lenguaje": "04 el lenguaje",
    "la maquina y su memoria": "05 la maquina y su memoria",
    "del caso": "06 del caso",
}
CERO = "candado_cero"
CAMPOS = ("Posición", "Por qué se sostiene", "De dónde viene", "Qué pregunta deja", "Ficción")


def plano(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"[\\/:*?\"<>|]", "-", s)
    return s[:80].rstrip(" .")


def campo(etiqueta, valor):
    """Una linea de campo, o nada si el valor dice ninguna.

    Un apartado que dice "ninguna" es un apartado vacio, y lo vacio no se escribe.
    """
    valor = (valor or "").strip()
    if not valor or valor.lower().rstrip(".") == "ninguna":
        return None
    valor = valor[0].upper() + valor[1:]
    if not valor.endswith((".", "!", "?")):
        valor += "."
    if etiqueta == "Qué pregunta deja" and "?" not in valor:
        valor = valor[:-1] + "?" if valor.endswith(".") else valor + "?"
    if etiqueta == "Qué pregunta deja" and "¿" not in valor:
        valor = "¿" + valor
    return "**{}.** {}".format(etiqueta, valor)


def texto_de(fila):
    """El candado entero, con la forma unica: titulo y los campos que existen."""
    orden, nombre, expansion, porque, referencia, pregunta, ficcion, figura = fila
    lineas = ["# {}".format(nombre), ""]
    for etiqueta, valor in (("Posición", expansion), ("Por qué se sostiene", porque),
                            ("De dónde viene", referencia), ("Qué pregunta deja", pregunta),
                            ("Ficción", ficcion), ("Figura", figura)):
        linea = campo(etiqueta, valor)
        if linea:
            lineas += [linea, ""]
    lineas += [
        "**Se abre con fricción, y no se reescribe: `../../../mantis/procesos/LLAVE.prs`.**",
        "",
        "---",
        "",
        "Del historial de sesgos del autor.",
        "",
    ]
    return "\n".join(lineas)


def ya_vive(nombre_archivo):
    """Dice en que carpeta esta el archivo, si esta en alguna."""
    for familia in CARPETAS.values():
        ruta = os.path.join(DESTINO, familia, nombre_archivo)
        if os.path.isfile(ruta):
            return familia
    return None


def main():
    if not os.path.isfile(DB):
        sys.stderr.write("[SIN MEMORIA] no esta la base.\n")
        return 2

    con = sqlite3.connect(DB)
    filas = con.execute(
        'SELECT id, orden, clase, nombre, "expansión", porque, referencia, pregunta, '
        "ficcion, figura, diferida, familia FROM pieza WHERE estado='viva' ORDER BY orden, id"
    ).fetchall()
    con.close()

    listas, detenidas, vivas = [], [], []
    for (pid, orden, clase, nombre, expansion, porque, referencia, pregunta,
         ficcion, figura, diferida, familia) in filas:
        if clase == CERO:
            continue
        archivo = "{:03d} {}.md".format(int(orden), plano(nombre))
        if familia and ya_vive(archivo):
            vivas.append(nombre)
            continue
        faltan = []
        for etiqueta, valor in (("Posición", expansion), ("Por qué se sostiene", porque),
                                ("De dónde viene", referencia), ("Qué pregunta deja", pregunta)):
            if not (valor or "").strip() or (valor or "").strip().lower().rstrip(".") == "ninguna":
                faltan.append(etiqueta)
        if not (familia or "").strip() or familia not in CARPETAS:
            faltan.append("la familia")
        if (diferida or "").strip():
            detenidas.append((nombre, diferida.strip()))
            continue
        if faltan:
            detenidas.append((nombre, "le falta: " + ", ".join(faltan)))
            continue
        listas.append(((orden, nombre, expansion, porque, referencia, pregunta, ficcion, figura), familia, archivo))

    if "--contar" in sys.argv:
        print("ya viven, y no se tocan: {}".format(len(vivas)))
        print("listas para escribir:     {}".format(len(listas)))
        print("detenidas:                {}".format(len(detenidas)))
        for nombre, razon in detenidas[:5]:
            print("   - {}: {}".format(nombre[:60], razon[:70]))
        return 0

    probar = "--probar" in sys.argv
    escritos = 0
    mudas = []
    for datos, familia, archivo in listas:
        carpeta = os.path.join(DESTINO, CARPETAS[familia])
        destino = os.path.join(carpeta, archivo)
        if ya_vive(archivo):
            mudas.append(archivo)
            continue
        if probar:
            print("[PROBAR] {} -> {}/".format(archivo, CARPETAS[familia]))
            escritos += 1
            continue
        os.makedirs(carpeta, exist_ok=True)
        if os.path.isfile(destino):
            print("[NO SE PISA] {}: ya existe, y el archivo manda.".format(archivo))
            continue
        with open(destino, "w", encoding="utf-8", newline="") as fh:
            fh.write(texto_de(datos))
        escritos += 1

    print("candados escritos: {}".format(escritos))
    print("detenidos:         {}".format(len(detenidas)))
    if mudas:
        print("y {} que ya viven en otra carpeta: mover es una mutación aparte.".format(len(mudas)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
