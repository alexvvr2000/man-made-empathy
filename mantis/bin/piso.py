#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""piso — mide un mundo: qué declara, y qué puede de verdad.

No le cree a la prosa. Lee el RUTA.pr, y prueba cada capacidad declarada
con algo que se pueda hacer aquí y ahora. Lo que no pasa la prueba no es
una capacidad: se declara no_puede.

Uso:
    python piso.py                 mide el mundo de este ente
    python piso.py --ruta <b>      mide el mundo declarado en otro RUTA.pr

Sale 0 si todas las capacidades declaradas pasaron su prueba, 1 si alguna fallo.
"""
import io
import os
import re
import subprocess
import sys
import tempfile
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTE = os.path.abspath(os.path.join(AQUI, ".."))
CAPACIDADES = ("leer", "escribir", "ejecutar", "medir", "fuera", "entre_turnos")


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def declaradas(texto):
    """La linea `capacidades:` del piso. Lo que no este ahi, no existe."""
    for linea in texto.splitlines():
        limpia = linea.strip().strip("*").strip()
        if limpia.startswith('"'):
            limpia = limpia.strip('"')
            if limpia.endswith("\\n"):
                limpia = limpia[:-2]
        if limpia.lower().startswith("capacidades:"):
            resto = limpia.split(":", 1)[1]
            fuera = []
            for parte in re.split(r"[·,|;]", resto):
                nombre = parte.strip().strip("`").strip().lower()
                if nombre and nombre in CAPACIDADES:
                    fuera.append(nombre)
            return fuera


def lo_que_no_puede(texto):
    """El campo no_puede: lo que el mundo dice que no tiene. Se lee, y se le cree."""
    for linea in texto.splitlines():
        limpia = linea.strip().strip("*").strip()
        if limpia.startswith('"'):
            limpia = limpia.strip('"')
            if limpia.endswith("\\n"):
                limpia = limpia[:-2]
        if limpia.lower().startswith("no_puede:"):
            resto = limpia.split(":", 1)[1].strip()
            if resto.startswith("["):
                return []           # el formulario sin llenar no dice nada
            fuera = []
            for parte in re.split(r"[·,|;]", resto):
                nombre = parte.strip().strip("`").strip().lower()
                if nombre:
                    fuera.append(nombre)
            return fuera
    return []


def es_formulario(texto):
    """Un piso con corchetes sin llenar no es un piso: es un formulario."""
    for linea in texto.splitlines():
        limpia = linea.strip().strip("*").strip()
        if limpia.lower().startswith(("capacidades:", "mundo:")):
            if "[" in limpia:
                return True
    return False
    return []


# ------------------------------------------------------------------ pruebas
def prueba_leer(ruta_pr):
    try:
        texto = leer(ruta_pr)
    except OSError as e:
        return False, "no se pudo leer el RUTA.pr: " + str(e)
    if "mundo:" not in texto:
        return False, "leido, pero no dice de que mundo es"
    return True, "leyo el RUTA.pr ({} bytes)".format(len(texto))


def prueba_escribir(carpeta):
    marca = "prueba de escritura del piso {}".format(time.time())
    destino = os.path.join(carpeta, ".piso.prueba")
    try:
        with io.open(destino, "w", encoding="utf-8", newline="") as fh:
            fh.write(marca)
        if leer(destino) != marca:
            return False, "escribio, y al releer no era lo mismo"
        return True, "escribio y releeyo igual"
    except OSError as e:
        return False, "no pudo escribir: " + str(e)
    finally:
        try:
            os.remove(destino)
        except OSError:
            pass


def prueba_ejecutar(carpeta):
    """Se corre un paso que se sabe que existe, y que tiene que devolver ok."""
    paso = os.path.join(tempfile.gettempdir(), "piso_prueba.py")
    with io.open(paso, "w", encoding="utf-8", newline="") as fh:
        fh.write("import sys\nprint('ok')\nsys.exit(0)\n")
    try:
        r = subprocess.run([sys.executable, paso], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=60)
        if r.returncode != 0:
            return False, "corrio, y salio con codigo " + str(r.returncode)
        if "ok" not in (r.stdout or ""):
            return False, "corrio, y no devolvio lo que se le pidio"
        return True, "corrio un paso, y devolvio ok"
    except FileNotFoundError:
        return False, "no hay con que correr un paso"
    except Exception as e:
        return False, "no pudo correr: " + str(e)
    finally:
        try:
            os.remove(paso)
        except OSError:
            pass


def prueba_medir(carpeta):
    """Medir es contar. Si no se puede contar el tiempo, no se puede medir nada."""
    inicio = time.time()
    antes = len(os.listdir(carpeta))
    despues = len(os.listdir(carpeta))
    transcurrido = time.time() - inicio
    if transcurrido < 0:
        return False, "el reloj va al reves"
    if antes != despues:
        return False, "contó dos veces cosas distintas sin que cambiara nada"
    return True, "contó {} cosas, en {:.3f} s".format(antes, transcurrido)


def prueba_fuera(carpeta):
    """No se prueba sin red: se declara que no hay, y no se promete nada."""
    return False, "no se prueba sin salir del mundo: si se declara, se declara con testigo"


def prueba_entre_turnos(carpeta):
    """Un proceso que sobrevive al que lo lanza. Aqui no hay: si no se declara, no se promete."""
    return False, "no hay proceso que sobreviva al que lo lanza"


PRUEBAS = {
    "leer": lambda ruta_pr, carpeta: prueba_leer(ruta_pr),
    "escribir": lambda ruta_pr, carpeta: prueba_escribir(carpeta),
    "ejecutar": lambda ruta_pr, carpeta: prueba_ejecutar(carpeta),
    "medir": lambda ruta_pr, carpeta: prueba_medir(carpeta),
    "fuera": lambda ruta_pr, carpeta: prueba_fuera(carpeta),
    "entre_turnos": lambda ruta_pr, carpeta: prueba_entre_turnos(carpeta),
}


def main(argv):
    ruta_pr = os.path.join(ENTE, "RUTA.pr")
    if "--ruta" in argv:
        i = argv.index("--ruta")
        if i + 1 >= len(argv):
            print("[FALTA] --ruta quiere un RUTA.pr")
            return 1
        ruta_pr = argv[i + 1]

    if not os.path.isfile(ruta_pr):
        print("[SIN PISO] no esta {}: este mundo no declara lo que puede".format(
            os.path.relpath(ruta_pr, ENTE) if ruta_pr.startswith(ENTE) else ruta_pr))
        return 1

    texto = leer(ruta_pr)
    if es_formulario(texto):
        print("[SIN ALLENAR] el piso es un formulario: sus corchetes no dicen nada")
        print("             se llena capacidades: y no_puede:, y se vuelve a medir")
        return 2
    declaradas_aqui = declaradas(texto)
    negadas = lo_que_no_puede(texto)
    if not declaradas_aqui:
        print("[SIN CAPACIDADES] el piso no declara ninguna: un mundo sin piso no existe")
        return 1

    print("[piso] {}".format(os.path.relpath(ruta_pr, ENTE) if ruta_pr.startswith(ENTE) else ruta_pr))
    print("[piso] declara: " + " · ".join(declaradas_aqui))
    print("")

    fallaron = 0
    for cap in CAPACIDADES:
        if cap not in declaradas_aqui:
            print("[no]      {:<14} no se declara: no existe para el ente".format(cap))
            continue
        ok, msg = PRUEBAS[cap](ruta_pr, ENTE)
        print(("[prueba]  " if ok else "[FALLA]   ") + "{:<14} {}".format(cap, msg))
        fallaron += 0 if ok else 1

    # que declara y no prueba
    declaradas_y_malas = [c for c in declaradas_aqui
                          if not PRUEBAS[c](ruta_pr, ENTE)[0]
                          and c not in negadas]
    if negadas:
        print("")
        print("[declara] no puede, y lo dice: " + ", ".join(negadas))
    print("")
    if declaradas_y_malas:
        print("[MIENTE]  declara y no puede: " + ", ".join(declaradas_y_malas))
        print("          se corrige el piso, y se declara no_puede")
        return 1
    if fallaron:
        print("falla: {} capacidad(es) declaradas que no pasaron su prueba".format(fallaron))
        return 1

    print("pasa: el mundo declara lo que puede, y lo puede")
    print("")
    print("lo que no declara, no existe: si un corte lo necesita, se declara [FALTA EN EL PISO]")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
