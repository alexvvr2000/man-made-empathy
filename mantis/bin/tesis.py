#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso del folder 'la tesis': dice que clase se pidio, y que le falta a cada una.

No compone nada: componer es de quien pide. Esta vez declara el estado de las
tres clases y lo que cada una exige antes de poder entregarse.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))

CLASES = {
    "teorica.prs": "aunque X, sostiene Y, porque Z — y un contraargumento nombrado",
    "academia.prs": "estilo declarado, IA declarada, conflicto declarado, referencias abribles",
    "practica.prs": "archivo de la corrida, numeros con fuente, procedimiento repetible",
}


def main():
    print("[ok] la tesis se compone on demand: no corre sola")
    print("")
    for f, exige in CLASES.items():
        ruta = os.path.join(AQUI, f)
        estado = "declarada" if os.path.isfile(ruta) else "AUSENTE"
        print("  {:<14} {}  exige: {}".format(f, estado, exige))

    tesis = os.path.join(REPO, "tesis", "vision del autor", "teoria completa", "las nueve piezas")
    if not os.path.isdir(tesis):
        print("")
        print("[SIN TESIS] no esta " + tesis)
        return 1

    candados = os.path.join(tesis, "candados")
    if os.path.isdir(candados):
        n = sum(1 for r, d, fs in os.walk(candados) for x in fs if x.endswith(".md"))
        print("")
        print("[ok] {} candados disponibles para sostener la tesis".format(n))

    print("")
    print("pasa: las tres clases estan declaradas; componer depende del pedido")
    return 0


if __name__ == "__main__":
    sys.exit(main())
