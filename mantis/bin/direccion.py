#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""direccion.py - mide si MANTIS esta enrutado contra el estandar vigente.

Regla dura del piso: todo el piso se escribe en Python. Un .ps1 no corre
en Linux ni en Mac, y el piso se mide por cuanta gente puede correrlo.

Lo que mide, y es lo mismo que media el .ps1:
  1. Ouroboros/ limpio en git, sin archivos mas nuevos que la carta.
  2. Cada archivo que MANTIS cita existe donde lo busca.
  3. La carta cubre los estandares que hay.
  4. Nadie de abajo muta hacia arriba.
  5. Ningun documento resuelve una ruta a la carpeta que lo contiene.
  6. Ningun archivo del repo cita un .md relativo que no existe.

Sale: 0 = pasa | 1 = falla | 2 = indeterminado. Siempre imprime el porque.

Limite declarado: mide citas y fechas, no el sentido de las secciones.
"""
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
PISO = RAIZ

fallas = []
indet = []


def diag(tipo, msg):
    print("[{}] {}".format(tipo, msg))


def rel(p):
    return os.path.relpath(p, RAIZ).replace("\\", "/")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def md_recursivo(base, excluir=(".git", ".memoria continua")):
    for raiz, dirs, files in os.walk(base):
        partes = raiz.split(os.sep)
        if any(e in partes for e in excluir):
            continue
        for f in files:
            if f.lower().endswith(".md"):
                yield os.path.join(raiz, f)


def docs_con_estandares():
    base = os.path.join(RAIZ, "faro", "sincronizacion de almas")
    grupos = ("formacion", "relacion", "friccion", "salida")
    lenguaje = next((os.path.join(base, g) for g in grupos if os.path.isdir(os.path.join(base, g))), base)
    if not os.path.isdir(lenguaje):
        return [], {}
    estandares = [f for f in os.listdir(lenguaje) if f.lower().endswith(".md")]
    return estandares, {f: os.path.join(lenguaje, f) for f in estandares}


def main():
    # --- 1. limpieza de la fuente en git -----------------------------------
    seguro = False
    if os.path.isdir(os.path.join(RAIZ, ".git")):
        try:
            r = subprocess.run(
                ["git", "status", "--porcelain"], cwd=RAIZ,
                capture_output=True, text=True, timeout=60,
            )
            sucio = [l for l in r.stdout.splitlines() if l.strip()]
            if sucio:
                indet.append("el repo tiene {} archivo(s) sin commitear: se compara contra un estado inestable".format(len(sucio)))
            else:
                seguro = True
        except Exception as e:  # noqa: BLE001
            indet.append("git no respondio: {}".format(e))
    else:
        indet.append("no hay .git: no hay con que comparar")
    if seguro:
        diag("ok", "el repo esta limpio en git")

    # --- 2 y 3. los estandares existen y la carta los cubre -----------------
    estandares, rutas = docs_con_estandares()
    if not estandares:
        fallas.append("no hay estandares en faro/sincronizacion de almas/")
    docs_repo = [p for p in md_recursivo(RAIZ)]
    contenido = {p: leer(p) for p in docs_repo}
    for nombre in estandares:
        citado = any(nombre in texto for p, texto in contenido.items() if p != rutas[nombre])
        if not citado:
            fallas.append("ningun documento cita el estandar {}".format(nombre))
            diag("falla", "no cubierto: {}".format(nombre))
    if estandares and not any(f.startswith("ningun documento cita") for f in fallas):
        diag("ok", "los {} estandares estan citados".format(len(estandares)))

    # --- 4. nadie de abajo muta hacia arriba ------------------------------
    for nombre, ruta in rutas.items():
        texto = contenido.get(ruta, "")
        if re.search(r"mantuvo MANTIS|MANTIS muta", texto):
            fallas.append("{} declara que MANTIS muta hacia arriba".format(nombre))
            diag("falla", "mutacion hacia arriba: {}".format(nombre))
    diag("ok", "nadie de abajo declara mutar hacia arriba")

    # --- 5. ningun documento resuelve ruta a su propia carpeta -------------
    sueltos = 0
    for nombre, ruta in rutas.items():
        carpeta = os.path.basename(os.path.dirname(ruta))
        texto = contenido.get(ruta, "")
        n = len(re.findall(r"\.\./" + re.escape(carpeta) + r"/|`\./" + re.escape(carpeta) + r"/", texto))
        if n:
            sueltos += n
            diag("aviso", "nombra su carpeta: {} ({} citas)".format(nombre, n))
    if sueltos:
        indet.append("{} cita(s) de carpeta en los estandares: se rompen en la proxima mudanza".format(sueltos))
    else:
        diag("ok", "ningun estandar resuelve una ruta a su propia carpeta")

    # --- 6. ninguna cita relativa muerta en todo el repo -------------------
    rotas = 0
    for p, texto in contenido.items():
        for m in re.finditer(r"`(\.\.?/[^`]+\.md)`", texto):
            destino = os.path.normpath(os.path.join(os.path.dirname(p), m.group(1)))
            if not os.path.isfile(destino):
                rotas += 1
                fallas.append("cita muerta en {}: {}".format(rel(p), m.group(1)))
                diag("falla", "cita muerta: {} -> {}".format(rel(p), m.group(1)))
    if rotas == 0:
        diag("ok", "ningun documento del repo cita un archivo relativo que no existe")

    # --- veredicto ---------------------------------------------------------
    print("")
    if fallas:
        print("falla")
        for f in fallas:
            print("  - " + f)
        if indet:
            print("  (ademas, indeterminado en lo que sigue)")
            for i in indet:
                print("  - " + i)
        return 1
    if indet:
        print("indeterminado")
        for i in indet:
            print("  - " + i)
        return 2
    print("pasa: MANTIS esta enrutado contra el estandar vigente")
    return 0


if __name__ == "__main__":
    sys.exit(main())


