#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""juez — mide si un ejecutor cumple los cinco verbos de EJECUTOR.vd.

No lee el codigo del ejecutor: le da un juego fijo de tareas, y mira las
firmas que deja. Lo que no deja firma, no lo cumplio.

Los seis casos, uno por verbo y uno por la negativa:
    1. LEER     una tarea que pasa: devuelve los cuatro campos
    2. LEER     una sin corte: devuelve SIN CORTE
    3. BUSCAR   una sin con que: devuelve FALTA EN bin/
    4. CORRER   la que pasa: corre, y no toca un archivo que no le dieron
    5. DEJAR    la que pasa: queda rastro.tra, memoria, y huella
    6. NEGARSE  la sin corte: no corre, y la negativa tiene hash

Uso:
    python juez.py                     mide el ejecutor de este ente
    python juez.py --con <ruta>        mide otro ejecutor
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTE = AQUI


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def escribir(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(s)


def huella(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:16]


def correr(python, ejecutor, argv, raiz):
    """Se le dice al ejecutor que su ente es el banco: ENTE_PRUEBA."""
    entorno = dict(os.environ)
    entorno["ENTE_PRUEBA"] = raiz
    r = subprocess.run([sys.executable, ejecutor] + argv, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", cwd=raiz, env=entorno, timeout=600)
    return ((r.stdout or "") + (r.stderr or "")).strip(), r.returncode


BANCO_CORTE = """# la tarea que pasa

**Nombre:** la que pasa
**Expande:** el juez midio al ejecutor
**Se nombró:** 2026-10-26
**Reemplaza:** NINGUNO
**Miente si:** se dice que corrio y no dejo rastro

## Entra | Falla | Sale | Consume

- **Entra:** un numero, y nada mas. No escribe: es solo-lectura.
- **Falla si:** el numero no es un numero.
- **Sale:** el numero, con un uno adelante.
- **Consume:** quien vaya a leer el resultado.

## Qué pasó

**Qué pasó:** sin correr
"""

BANCO_SIN_MODO = """# la que no dice que toca

**Nombre:** la que no dice que toca

## Entra | Falla | Sale | Consume

- **Entra:** un archivo cualquiera.
- **Falla si:** el archivo no esta.
- **Sale:** otro archivo, escrito encima del primero.
- **Consume:** quien lo lea.

**Y no dice si toca o si solo lee: es la tramposa.**
"""

BANCO_SIN_CORTE = """# la sin corte

**Nombre:** la sin corte

**Esto no declara Entra ni Sale: es el jamon de la prueba.**
"""


def banco():
    """Un ente de mentiras, con una tarea que pasa y otra que no declara nada."""
    raiz = tempfile.mkdtemp(prefix="juez_")
    escribir(os.path.join(raiz, "tareas", "la que pasa", "la que pasa.tra"), BANCO_CORTE)
    escribir(os.path.join(raiz, "tareas", "la que pasa", "paso.py"),
             "import sys\nprint('paso: ' + str(sys.argv[1] if len(sys.argv) > 1 else ''))\n")
    escribir(os.path.join(raiz, "tareas", "la sin corte", "la sin corte.tra"), BANCO_SIN_CORTE)
    escribir(os.path.join(raiz, "tareas", "la sin con que", "la sin con que.tra"), BANCO_CORTE)
    escribir(os.path.join(raiz, "tareas", "la que no dice que toca", "la que no dice que toca.tra"), BANCO_SIN_MODO)
    escribir(os.path.join(raiz, "tareas", "la que no dice que toca", "paso.py"),
             "import sys\nprint('ESCRIBI EN EL MUNDO')\n")
    escribir(os.path.join(raiz, "tareas", "tareas.prs"),
             "# tareas.prs\n\n- **Entra:** x\n- **Falla si:** x\n- **Sale:** x\n- **Consume:** x\n")
    return raiz


def casos(python, ejecutor, raiz):
    """Los seis casos, y lo que cada uno deja."""
    fuera = []

    # 1. LEER: una tarea que pasa
    salida, codigo = correr(python, ejecutor, ["--sin-tra", "la que pasa"], raiz)
    ok = "Entra:" in salida and "Sale:" in salida
    fuera.append(("LEER", "una tarea que pasa", ok,
                  salida.splitlines()[0] if salida else "(sin salida)"))

    # 2. LEER: una sin corte
    salida, codigo = correr(python, ejecutor, ["--sin-tra", "la sin corte"], raiz)
    ok = "SIN CORTE" in salida
    fuera.append(("LEER", "una tarea sin corte", ok,
                  "dijo SIN CORTE" if ok else (salida.splitlines()[0] if salida else "(sin salida)")))

    # 3. BUSCAR: una sin con que
    salida, codigo = correr(python, ejecutor, ["--sin-tra", "la sin con que"], raiz)
    ok = "FALTA EN bin/" in salida
    fuera.append(("BUSCAR", "una sin con que", ok,
                  "dijo FALTA EN bin/" if ok else (salida.splitlines()[0] if salida else "(sin salida)")))

    # 4. CORRER: recibe el Entra: como texto, y no va a buscar archivos
    carpeta = os.path.join(raiz, "tareas", "la que pasa")
    antes = set(os.listdir(raiz))
    salida, codigo = correr(python, ejecutor, ["la que pasa"], raiz)
    despues = set(os.listdir(raiz))
    ok = codigo == 0 and "paso:" in salida
    fuera.append(("CORRER", "la que pasa", ok,
                  "corrio, y el paso vio el Entra: como texto" if ok else
                  "no corrio, o el paso no recibio nada"))

    # 5. DEJAR: el rastro y la huella
    tra = os.path.join(carpeta, "rastro.tra")
    huella_corte = os.path.join(carpeta, ".corte")
    ok = os.path.isfile(tra) and os.path.isfile(huella_corte)
    fuera.append(("DEJAR", "la que pasa", ok,
                  "dejo rastro.tra y la huella del corte" if ok else "no dejo rastro, o no dejo huella de lo que corrio"))

    # 5b. ENSAYAR: la tramposa no dice que toca, y no corre
    tramposa = os.path.join(raiz, "tareas", "la que no dice que toca")
    salida, codigo = correr(python, ejecutor, ["la que no dice que toca"], raiz)
    no_corrio = "ESCRIBI EN EL MUNDO" not in salida
    dijo = "SIN ENSAYO" in salida
    pregunto = "me falta:" in salida and "y espero:" in salida
    ok = no_corrio and dijo and pregunto
    dice = ("no corrio, y pregunto que le falta" if ok else
            ("corrio igual: la urna quedo en el suelo" if not no_corrio else
             "se nego como un muro: no dijo que le falta, o a quien espera"))
    fuera.append(("ENSAYAR", "la que no dice que toca", ok, dice))

    # 6. NEGARSE: la sin corte no corre, y su negativa se firma
    escribir(os.path.join(raiz, "tareas", "la sin corte", "paso.py"),
             "import sys\nprint('NO TENIA QUE CORRER')\nsys.exit(9)\n")
    salida, codigo = correr(python, ejecutor, ["la sin corte"], raiz)
    no_corrio = "NO TENIA QUE CORRER" not in salida and codigo != 0
    cuentas = os.path.join(raiz, "memoria", "negativa.jsonl")
    firmada = os.path.isfile(cuentas)
    con_falta = False
    if firmada:
        con_falta = "me_falta" in io.open(cuentas, encoding="utf-8").read()
    ok = no_corrio and firmada and con_falta
    fuera.append(("NEGARSE", "la sin corte", ok,
                  "no corrio, firmo, y dijo que le falta" if ok else
                  ("corrio igual" if not no_corrio else
                   "no firmo la negativa, o no dijo que le falta")))
    return fuera


def main(argv):
    ejecutor = os.path.join(ENTE, "ejecutar.py")
    if "--con" in argv:
        i = argv.index("--con")
        if i + 1 >= len(argv):
            print("[FALTA] --con quiere la ruta del ejecutor")
            return 1
        ejecutor = argv[i + 1]

    ejecutor = os.path.abspath(ejecutor)
    if not os.path.isfile(ejecutor):
        print("[SIN EJECUTOR] no esta {}".format(ejecutor))
        return 1

    raiz = banco()
    print("[juez] {}".format(os.path.basename(ejecutor)))
    print("[juez] banco: {}".format(raiz))
    print("")
    fallas = 0
    verbos = []
    try:
        for verbo, que, ok, dice in casos(sys.executable, ejecutor, raiz):
            if verbo not in verbos:
                verbos.append(verbo)
            print(("[ok]   " if ok else "[FALLA]") + " {:<9} {:<22} {}".format(verbo, que, dice[:70]))
            fallas += 0 if ok else 1
    finally:
        shutil.rmtree(raiz, ignore_errors=True)

    print("")
    faltan = [v for v in ("LEER", "BUSCAR", "ENSAYAR", "CORRER", "DEJAR", "NEGARSE") if v not in verbos]
    if faltan:
        print("[NO CONFORME] el ejecutor no toco: " + ", ".join(faltan))
        return 1
    if fallas:
        print("[NO CONFORME] {} caso(s) de siete: el ejecutor no cumple EJECUTOR.vd".format(fallas))
        return 1
    print("[CONFORME] siete de siete: el ejecutor cumple los seis verbos")
    print("           y la firma de la negativa se cumplio, que es la que hace la diferencia")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
