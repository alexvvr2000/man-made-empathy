#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pruebas — mide si las siete pruebas del autor están en condiciones de correr.

No las corre: no puede, porque cada una pide a personas y a corridas reales.
Lo que mide es lo que sí se puede medir de un documento que se aplica:
que entre, que falle por algo, que salga con algo, que diga a quién consume,
y que tenga su falsificador escrito.

Y lo que NO tiene, lo dice en voz alta: una prueba sin falsificador es una
opinión con formato de prueba.

Uso:
    python pruebas.py            mide las siete
    python pruebas.py --json     sale en json
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.path.abspath(os.path.join(MANTIS, ".."))
PRUEBAS = os.path.join(REPO, "Pruebas")
SALIDA = os.path.join(MANTIS, "tareas", "la memoria", "pruebas", "pruebas.json")

# lo que toda prueba que se aplica tiene que declarar, y no es negociable
CAMPOS = {
    "entra": ("**Entra:**", "- **Entra:**"),
    "falla": ("**Falla si:**", "- **Falla si:**", "**Falla:**", "- **Falla:**"),
    "sale": ("**Sale:**", "- **Sale:**"),
    "consume": ("**Consume:**", "- **Consume:**"),
    "falsificador": ("**Falsificador:**", "## Falsificador", "**Falsificador.**"),
}


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def medir(nombre, texto):
    """Una prueba está en condiciones si declara lo cinco, y se dice cuál le falta."""
    tiene = {}
    for campo, marcas in CAMPOS.items():
        tiene[campo] = any(m in texto for m in marcas)
    # y si declara lo que NO prueba, que es la señal de que piensa su límite
    tiene["limite"] = bool(re.search(r"^## Lo que (esta|este)[^#]*no (hace|mide|prueba|juzga)", texto, re.M))
    # y cómo se aplica: si no hay pasos, no se puede aplicar
    tiene["como"] = bool(re.search(r"^## C[oó]mo se aplica", texto, re.M))
    return {
        "prueba": nombre,
        "bytes": len(texto.encode("utf-8")),
        **tiene,
        "faltan": [k for k, v in tiene.items() if not v],
    }


def main(argv):
    if not os.path.isdir(PRUEBAS):
        print("[SIN PRUEBAS] no esta " + PRUEBAS)
        return 1
    archivos = sorted(f for f in os.listdir(PRUEBAS)
                      if f.endswith(".md") and f.lower() != "readme.md")
    if not archivos:
        print("[SIN PRUEBAS] la carpeta esta pero no hay ninguna")
        return 1

    medidas = [medir(f[:-3], leer(os.path.join(PRUEBAS, f))) for f in archivos]

    if "--json" in argv:
        print(json.dumps(medidas, ensure_ascii=False, indent=2))
        return 0

    print("[pruebas] {} en la carpeta".format(len(medidas)))
    print("")
    print("  {:<44} {:>6}  {}".format("prueba", "bytes", "declara"))
    faltan_total = []
    for m in medidas:
        estado = "las cinco, y su limite" if not m["faltan"] else "le falta: " + ", ".join(m["faltan"])
        print("  {:<44} {:>6}  {}".format(m["prueba"][:44], m["bytes"], estado))
        faltan_total.extend((m["prueba"], f) for f in m["faltan"])

    print("")
    if faltan_total:
        print("[falta] {} campo(s) vacios en {} prueba(s)".format(len(faltan_total), len({a for a, _ in faltan_total})))
        for p, c in faltan_total[:12]:
            print("  - {}: {}".format(p, c))
        print("")
        print("una prueba sin falsificador es una opinion con formato de prueba: se nombra, y no se corre")

    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    with io.open(SALIDA, "w", encoding="utf-8", newline="") as fh:
        json.dump({"medidas": medidas, "archivos": len(archivos),
                   "como_se_mide": "cinco campos declarados por prueba, mas su limite y su como se aplica"},
                  fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print("")
    print("pasa: las {} pruebas se midieron, y ninguna se dio por buena sin mirarla".format(len(medidas)))
    print("deja: " + os.path.relpath(SALIDA, MANTIS))
    print("")
    print("lo que este proceso NO hace: no las corre. cada una pide personas y corridas reales,")
    print("y eso no se simula. mide si estan en condiciones de correrse, que es otra cosa.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
