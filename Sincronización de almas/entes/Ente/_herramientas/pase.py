#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pase.py — leer y escribir el pase del dia, para no empezar ciego.

Y es generico: funciona en cualquier proyecto y en cualquier ente.
Encuentra su casa sola, subiendo hasta la carpeta que tiene el ente.

  python pase.py leer              lo que quedo abierto, y lo que se rompio
  python pase.py cerrar "..." ...  escribe el cierre del dia
  python pase.py abrir             la regla de apertura, y el pase

Regla: al abrir turno se LEE el pase. Antes no se contesta nada.
"""

import os
import sys
from datetime import datetime


def encontrar_casa():
    """Sube desde aqui hasta la carpeta que tiene el ente.

    Y no supone una ruta: la busca. Asi sirve copiado en cualquier lado.
    """
    actual = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        if os.path.isdir(os.path.join(actual, "memoria continua")):
            return actual
        padre = os.path.dirname(actual)
        if padre == actual:
            break
        actual = padre
    return None


def archivo_del_dia(casa):
    fecha = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(casa, "memoria continua", "pases", fecha + ".md")


def leer(casa):
    ruta = archivo_del_dia(casa)
    if not os.path.exists(ruta):
        print("[SIN PASE - NO SE QUE PASO AYER]")
        print("  no existe: %s" % ruta)
        print("  y no se supone: se pregunta, o se lee el ultimo que haya.")
        carpeta = os.path.dirname(ruta)
        if os.path.isdir(carpeta):
            otros = sorted(f for f in os.listdir(carpeta) if f.endswith(".md"))
            if otros:
                print("  el mas reciente: %s" % otros[-1])
        return 2
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read()
    print("=== PASE DE HOY: %s ===" % os.path.basename(ruta))
    print(texto.strip())
    print("=== FIN DEL PASE ===")
    abiertos = texto.count("Abierto:")
    roturas = texto.count("Se rompi")
    print("\n[RESUMEN] %d abiertos, %d roturas registradas" % (abiertos, roturas))
    return 0


def cerrar(casa, lineas):
    ruta = archivo_del_dia(casa)
    etiquetas = ["Sostuvo", "Se rompio", "Abierto", "Retoma", "No retoma"]
    lineas = list(lineas) + ["[SIN DECLARAR]"] * (len(etiquetas) - len(lineas))
    cuerpo = "\n## %s\n" % datetime.now().strftime("%Y-%m-%d")
    for etiqueta, valor in zip(etiquetas, lineas):
        cuerpo += "- **%s:** %s\n" % (etiqueta, valor)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(cuerpo)
    print("[PASE ESCRITO] %s" % ruta)
    return 0


def main():
    casa = encontrar_casa()
    if not casa:
        print("[SIN CASA - NO ENCONTRE memoria continua/ SUBIENDO DESDE %s]" % os.path.dirname(os.path.abspath(__file__)))
        print("  y no lo supongo: sin casa no hay pase que leer.")
        return 1
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    orden = sys.argv[1]
    if orden == "leer":
        return leer(casa)
    if orden == "abrir":
        print("AL ABRIR, ANTES DE CUALQUIER COSA:")
        print("  1. python _herramientas/pase.py leer")
        print("  2. y solo entonces, contestar.")
        return leer(casa)
    if orden == "cerrar":
        return cerrar(casa, sys.argv[2:])
    print("orden desconocida: %s" % orden)
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
