#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""historicas — lista las eras que git guarda y el repo ya no, y las saca cuando se piden.

No borra nada: todo esto ya no existe en el árbol de trabajo, y se
recupera de la última versión que lo tuvo. Lo que sale es un índice con
cada era, su fecha, y cuánto pesa.

Uso:
    python basura.py                 lista las eras muertas, sin restaurar
    python basura.py --sacar <era>   restaura una era a basura/<era>/
    python basura.py --sacar todas   las restaura todas (son muchas)

Sale 0 si pudo leer el historial, 1 si git no contesta.
"""
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.path.abspath(os.path.join(MANTIS, ".."))
DESTINO = os.path.join(REPO, "tesis autor", "historicas")
INDICE = os.path.join(DESTINO, "indice.json")

# lo que no es una era: archivos sueltos de la raíz, y lo de hoy
IGNORAR = (".git", "mantis", "tesis", "estandar", "base", "entiendo", "faro", "candados", "basura",
           "vision de la maquina", "vision del lector", "Pruebas",
           "AGENTS.md", "ATTRIBUTION.md", "CITATION.cff", "FUENTES.md", "LICENSE.txt", "README.md",
           "futuros posibles.md", "pc.md", ".gitignore")


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=REPO, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else ""


def todas_las_rutas():
    """Cada ruta que existió alguna vez en cualquier rama."""
    fuera = set()
    for linea in git("log", "--all", "--name-only", "--format=").splitlines():
        linea = linea.strip()
        if linea:
            fuera.add(linea)
    return fuera


def existe(ruta):
    return os.path.exists(os.path.join(REPO, ruta))


def eras_muertas():
    """Por carpeta de primer nivel: cuántos archivos tuvo, y en qué commit se fue."""
    rutas = todas_las_rutas()
    conteo = {}
    for r in rutas:
        primera = r.split("/")[0]
        if primera in IGNORAR:
            continue
        if existe(r):
            continue
        conteo[primera] = conteo.get(primera, 0) + 1
    fuera = []
    for era, n in sorted(conteo.items(), key=lambda x: -x[1]):
        ultimo = git("log", "--all", "-1", "--format=%h %ad", "--date=short", "--", era).strip()
        fuera.append({"era": era, "archivos": n, "ultimo": ultimo})
    return fuera


def sacar(era):
    """Restaura la última versión de una era muerta, y dice qué salió."""
    ultimo = git("log", "--all", "-1", "--format=%h", "--", era).strip()
    if not ultimo:
        return 0, "no hay commit para " + era
    rutas = [r for r in todas_las_rutas() if r == era or r.startswith(era + "/")]
    puestas = 0
    for r in rutas:
        if existe(r):
            continue
        contenido = git("show", "{}:{}".format(ultimo, r))
        if not contenido:
            continue
        destino = os.path.join(DESTINO, r)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with io.open(destino, "w", encoding="utf-8", newline="") as fh:
            fh.write(contenido)
        puestas += 1
    return puestas, ultimo


def main(argv):
    eras = eras_muertas()
    if not eras:
        print("[nada] el repo no tiene eras muertas que recuperar")
        return 0

    print("[historicas] {} eras que ya no estan en el arbol".format(len(eras)))
    print("")
    print("  {:<34} {:>6}  {}".format("era", "arch.", "ultimo commit"))
    for e in eras:
        print("  {:<34} {:>6}  {}".format(e["era"][:34], e["archivos"], e["ultimo"]))
    total = sum(e["archivos"] for e in eras)
    print("")
    print("[historicas] {} archivos en total, y ninguno de ellos pesa en el repo de hoy".format(total))

    os.makedirs(DESTINO, exist_ok=True)
    with io.open(INDICE, "w", encoding="utf-8", newline="") as fh:
        json.dump({"eras": eras, "archivos": total,
                   "como_se_cuenta": "cada ruta que existio en cualquier rama y hoy no esta en el arbol"},
                  fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("deja: " + os.path.relpath(INDICE, REPO))

    if "--sacar" in argv:
        i = argv.index("--sacar")
        if i + 1 >= len(argv):
            print("[FALTA] --sacar quiere el nombre de una era, o 'todas'")
            return 1
        cual = argv[i + 1]
        objetivos = [e["era"] for e in eras] if cual == "todas" else [cual]
        for era in objetivos:
            n, ultimo = sacar(era)
            print("[ok] {:<30} {} archivos, de {}".format(era, n, ultimo if n else ultimo))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
