#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""firmar.py - la firma de friccion quitada, con hash.

Firma un contenido: calcula su sha256 y escribe la firma en texto plano,
junto al archivo o donde se le diga. No depende de git ni de nada mas.

Uso:
    python mantis/procesos/firmar.py archivo.md --quien "Alejandro" --quito "vertice pendejo de EXPRESION" --acepta "que lo producido no se probo contra lo pendejo"
    python mantis/procesos/firmar.py archivo.md --verificar

Sale 0 si la firma se escribio o si el hash coincide; 1 si no coincide.
"""
import hashlib
import os
import sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for bloque in iter(lambda: fh.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def leer_firma(ruta_firma):
    datos = {}
    if not os.path.isfile(ruta_firma):
        return datos
    with open(ruta_firma, "r", encoding="utf-8") as fh:
        for linea in fh:
            if ":" in linea:
                k, _, v = linea.partition(":")
                datos[k.strip().lower()] = v.strip()
    return datos


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    objetivo = sys.argv[1]
    if not os.path.isfile(objetivo):
        print("[SIN CONTENIDO] no existe {}".format(objetivo))
        return 2

    ruta_firma = objetivo + ".firma"
    digest = sha256(objetivo)

    if "--verificar" in sys.argv:
        datos = leer_firma(ruta_firma)
        if not datos:
            print("[SIN FIRMA] no hay firma junto a {}".format(os.path.basename(objetivo)))
            return 1
        if datos.get("hash") == digest:
            print("vale: el hash coincide con la firma de {}".format(datos.get("quien", "?")))
            return 0
        print("[NO VALE] el contenido cambio: la firma dice {} y el archivo da {}".format(
            datos.get("hash"), digest))
        return 1

    def arg(nombre, defecto=""):
        for i, a in enumerate(sys.argv):
            if a == nombre and i + 1 < len(sys.argv):
                return sys.argv[i + 1]
        return defecto

    quien = arg("--quien", "sin nombre")
    quito = arg("--quito", "sin declarar")
    acepta = arg("--acepta", "sin declarar")
    lugar = arg("--lugar", "junto al archivo")

    firma = [
        "FIRMA DE FRICCION QUITADA",
        "Quien:      {}".format(quien),
        "Quito:      {}".format(quito),
        "Cuando:     {}".format(datetime.now(timezone.utc).isoformat()),
        "Acepta:     {}".format(acepta),
        "Contenido:  {}".format(os.path.basename(objetivo)),
        "Hash:       {}".format(digest),
        "Lugar:      {}".format(lugar),
        "",
    ]
    with open(ruta_firma, "w", encoding="utf-8") as fh:
        fh.write("\n".join(firma))
    print(ruta_firma)
    print(digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())

