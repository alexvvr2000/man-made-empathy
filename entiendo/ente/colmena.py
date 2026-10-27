#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""colmena — corre a cada alma una vez, y mide si sigue dentro del sesgo del 1.

El 1 no es un resumen: es un sesgo, cuatro campos que cada alma tiene que
poder leer. La colmena no pregunta que sostiene cada alma: corre el sesgo,
y cada alma responde dentro | se salió | contradice.

Uso:
    python colmena.py                      lista las colmenas declaradas
    python colmena.py <nombre>             corre una, y deja su fila
"""
import io
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTE = AQUI
BIN = AQUI
# el motor puede vivir dentro de su tarea: se busca la raiz subiendo hasta tareas/
_raiz = AQUI
while os.path.basename(_raiz) != "tareas" and os.path.dirname(_raiz) != _raiz:
    _raiz = os.path.dirname(_raiz)
if os.path.basename(_raiz) == "tareas":
    ENTE = os.path.dirname(_raiz)
    BIN = ENTE
TAREAS = os.path.join(ENTE, "tareas")
ESTADOS = {"dentro", "se salió", "se salio", "contradice"}
ORDEN = [".ps1", ".sh", ".py", ".exe", ".cmd", ".bat"]


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def campo(texto, nombre):
    m = re.search(r"^\s*-?\s*\*\*" + nombre + r":\*\*\s*(.+)$", texto, re.M)
    return m.group(1).strip() if m else None


def colmenas():
    fuera = []
    if not os.path.isdir(TAREAS):
        return fuera
    for raiz, dirs, files in os.walk(TAREAS):
        for f in files:
            if f.endswith(".colmena"):
                fuera.append(os.path.join(raiz, f))
    return sorted(fuera)


def leer_colmena(ruta):
    t = leer(ruta)
    uno = campo(t, "El 1")
    sesgo = campo(t, "Sesgo")
    firma = campo(t, "Firma")
    almas = []
    dentro = False
    for linea in t.splitlines():
        s = linea.strip()
        if s.lower().startswith("almas:"):
            dentro = True
            continue
        if dentro and s.startswith("-"):
            nombre = s[1:].strip().split("|")[0].strip().strip("`")
            if nombre:
                almas.append(nombre)
        elif dentro and s and not s.startswith("-"):
            if not s.startswith("#"):
                dentro = False
    return uno, sesgo, firma, almas


def donde_esta(nombre):
    """Un alma se busca por su nombre en tareas/, o como paso del mundo."""
    for raiz, dirs, files in os.walk(TAREAS):
        if os.path.basename(raiz) == nombre:
            return raiz
    return None


def lo_que_lo_corre(carpeta, nombre):
    if carpeta:
        for ext in ORDEN:
            p = os.path.join(carpeta, "paso" + ext)
            if os.path.isfile(p):
                return p
    for ext in ORDEN:
        p = os.path.join(BIN, nombre.replace(" ", "_") + ext)
        if os.path.isfile(p):
            return p
    return None


def comando(ruta):
    ext = os.path.splitext(ruta)[1].lower()
    if ext == ".py":
        return [sys.executable, ruta]
    if ext == ".ps1":
        return ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ruta]
    return [ruta]


def correr(ruta, alguien, sesgo):
    try:
        r = subprocess.run(comando(ruta) + [alguien, sesgo or ""], capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=600)
        return ((r.stdout or "") + (r.stderr or "")).strip(), r.returncode
    except FileNotFoundError:
        return "", 2
    except Exception as e:
        return str(e), 2


def estado_de(salida, codigo):
    """El estado lo devuelve el alma, y no se adivina."""
    for linea in (salida or "").splitlines():
        s = linea.strip().lower()
        for e in ("se salió", "se salio", "contradice", "dentro"):
            if s.startswith(e):
                return ("se salió" if e == "se salio" else e), linea.strip()
    if codigo != 0:
        return "se salió", (salida or "").splitlines()[0] if salida else "codigo " + str(codigo)
    return "dentro", "no dijo otra cosa, y salio sin error"


def main(argv):
    lista = colmenas()
    if len(argv) < 2:
        if not lista:
            print("[SIN COLMENA] no hay ningun .colmena declarado")
            return 1
        for p in lista:
            uno, sesgo, firma, almas = leer_colmena(p)
            print("{:<24} 1: {} | almas: {}".format(os.path.basename(p)[:-8], uno, len(almas)))
        return 0

    nombre = argv[1]
    ruta = None
    for p in lista:
        if os.path.basename(p)[:-8] == nombre:
            ruta = p
    if ruta is None:
        print("[SIN COLMENA] no esta declarada: " + nombre)
        return 1

    uno, sesgo, firma, almas = leer_colmena(ruta)
    if not sesgo:
        print("[SIN SESGO] el 1 no declara desde donde sostiene: no hay colmena, hay muchos")
        return 1
    if not almas:
        print("[SIN ALMAS] la colmena no declara a nadie: no hay a quien correr")
        return 1
    if not firma:
        print("[SIN FIRMA] el sesgo del 1 no dice quien lo contesta")
        return 1

    print("[colmena] {} | 1: {}".format(nombre, uno))
    print("  Sesgo:  " + sesgo[:120])
    print("  Firma:  " + firma[:80])
    print("  Almas:  " + ", ".join(almas))
    print("")

    filas = []
    salieron = []
    contradicen = []
    for alma in almas:
        carpeta = donde_esta(alma)
        paso = lo_que_lo_corre(carpeta, alma)
        if paso is None:
            print("[SIN PASO] {:<20} se declara y este mundo no la sabe correr: no se cuenta".format(alma))
            salieron.append(alma)
            filas.append("Se salió:    {} | Por qué: no se pudo correr aquí | El 1 lo sabe: sí".format(alma))
            continue
        salida, codigo = correr(paso, alma, sesgo)
        estado, porque = estado_de(salida, codigo)
        print("[{:<10}] {:<20} {}".format(estado, alma, porque[:80]))
        if estado == "contradice":
            contradicen.append(alma)
            filas.append("Contradice:  {} | {} | El 1: [se muda | se retira el alma]".format(alma, porque))
        elif estado == "se salió":
            salieron.append(alma)
            filas.append("Se salió:    {} | Por qué: {} | El 1 lo sabe: sí".format(alma, porque))
        else:
            filas.append("Dentro:      {} | Lee: el sesgo del 1 | Sigue: sí".format(alma))

    if contradicen:
        veredicto = "se muda | se retira el alma: " + ", ".join(contradicen)
    elif salieron:
        veredicto = "aguantó, y se salieron {}".format(", ".join(salieron))
    else:
        veredicto = "aguantó: todas dentro"

    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    cuantas = len(almas) - len(salieron) - len(contradicen)
    cuerpo = (
        "# {} — lo que pasó\n\n"
        "**Nombre:** {}\n"
        "**Expande:** COLMENA.prs\n"
        "**Se nombró:** {}\n"
        "**Reemplaza:** NINGUNO\n"
        "**Miente si:** se dice que la colmena corrió y alguna alma no tiene su fila\n\n"
        "## Qué pasó\n\n"
        "**Qué pasó:** se corrieron {} almas del 1, y cada una dijo dónde está\n"
        "**Contra:** {}\n"
        "**Huella:** esta .tra\n"
        "**Distancia:** {}\n\n"
        "## Las filas\n\n"
        "{}\n"
    ).format(nombre, nombre, ahora, len(almas), veredicto, ahora[:10],
             "\n".join(filas))
    destino = os.path.join(os.path.dirname(ruta), nombre + ".tra")
    with io.open(destino, "w", encoding="utf-8", newline="") as fh:
        fh.write(cuerpo)

    print("")
    print("[fila] {}".format(veredicto))
    print("deja: " + os.path.relpath(destino, ENTE))
    return 0 if not contradicen else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
