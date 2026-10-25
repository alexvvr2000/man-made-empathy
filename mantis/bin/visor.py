#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""visor.py - de una vision a su tesis, y solo con lo que esa vision sostiene.

Una vision es un candado, y su tesis sale de sus propios cortes. Dos visiones
distintas tienen que producir dos documentos distintos: si no, no son personales,
son la misma memoria con otro titulo.

Una vision vive en:
    Tesis/visiones/<nombre>/VISION.vd     lo que sostiene, de donde mira, y su borde
    Tesis/visiones/<nombre>/cortes.txt    una pieza por linea: su orden en la memoria
    Tesis/visiones/<nombre>/entregables/  aqui sale la tesis

Uso:
    python mantis/bin/visor.py --contar          que visiones hay y si pueden componer
    python mantis/bin/visor.py --vision <nombre> compone la tesis de esa vision
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
VISIONES = os.path.join(REPO, "Tesis", "visiones")
COMPONER = os.path.join(AQUI, "academico.py")
CANDADOS = os.path.join(REPO, "Tesis", "candados", "autor")


def leer_vision(carpeta):
    """La vision y sus campos: nombre, sostiene, mira, borde, blanco, cortes."""
    ruta = os.path.join(carpeta, "VISION.vd")
    if not os.path.isfile(ruta):
        return None
    texto = io.open(ruta, encoding="utf-8", errors="replace").read()
    campos = {}
    for m in re.finditer(r"^\*\*([A-Za-zÁÉÍÓÚáéíóúñÑ ]+)\.\*\*\s*(.+)$", texto, re.M):
        campos[m.group(1).strip().lower()] = m.group(2).strip()
    cortes = []
    ruta_cortes = os.path.join(carpeta, "cortes.txt")
    if os.path.isfile(ruta_cortes):
        for linea in io.open(ruta_cortes, encoding="utf-8"):
            linea = linea.strip()
            if linea and not linea.startswith("#"):
                cortes.append(linea)
    return {"campos": campos, "cortes": cortes, "ruta": ruta}


def candado_de(orden):
    """Busca el candado de esa pieza en las carpetas de la tesis."""
    for familia in sorted(os.listdir(CANDADOS)):
        sub = os.path.join(CANDADOS, familia)
        if not os.path.isdir(sub):
            continue
        for f in os.listdir(sub):
            if f.startswith("%03d " % int(orden)) or f.startswith("%04d " % int(orden)):
                return os.path.join(sub, f)
    return None


def componer(nombre):
    carpeta = os.path.join(VISIONES, nombre)
    if not os.path.isdir(carpeta):
        print("[SIN VISION] no existe {}".format(carpeta))
        return 2
    v = leer_vision(carpeta)
    if v is None:
        print("[SIN VISION] falta VISION.vd: una vision sin candado no compone.")
        return 2
    c = v["campos"]
    if not c.get("sostiene"):
        print("[SIN VISION] la vision no dice que sostiene, y sin eso no hay tesis.")
        return 2
    if not v["cortes"]:
        print("[SIN CORTES] la vision no declara ningun corte: no se compone una tesis vacia.")
        return 2

    piezas, faltan = [], []
    for orden in v["cortes"]:
        ruta = candado_de(orden)
        if ruta is None:
            faltan.append(orden)
            continue
        piezas.append((orden, ruta, io.open(ruta, encoding="utf-8").read()))

    if not piezas:
        print("[SIN CORTES VIVOS] ninguno de sus cortes existe en la tesis.")
        return 2

    # el manuscrito de la vision: portada, y cada corte como seccion
    lineas = [
        "**Titulo.** {}".format(c.get("nombre") or nombre),
        "**Subtitulo.** {}".format(c.get("sostiene", "")[:160]),
        "**Autor:** {}".format(c.get("dueño", "humano:autoridad").replace("humano:", "")),
        "**Adscripción:** {}".format(c.get("mira", "")),
        "**Fecha:** 2026-10-25",
        "**Estilo de cita:** APA, séptima edición.",
        "**Licencia:** CC-BY-4.0",
        "**Estado:** compuesto desde la memoria, on demand, para esta vision y no para otra.",
        "**Disponibilidad de datos:** Ver el repo; cada corte cita su archivo.",
        "",
        "**Resumen.** {}".format(
            "Tesis de la vision «{}»: sostiene que {}. Se compone de {} cortes de la memoria que esta "
            "vision se atreve a mirar, y no de los demás: lo que no está en su borde no aparece aquí.".format(
                nombre, c.get("sostiene", "").rstrip("."), len(piezas))),
        "**Palabras clave:** vision, candado, friccion, memoria, borde.",
        "",
    ]
    for orden, ruta, texto in piezas:
        titulo = re.search(r"^# (.+)$", texto, re.M)
        posicion = re.search(r"\*\*Posición\.\*\* (.+)", texto)
        porque = re.search(r"\*\*Por qué se sostiene\.\*\* (.+)", texto)
        prueba = re.search(r"\*\*Prueba\.\*\* (.+)", texto)
        falsif = re.search(r"\*\*Falsificador\.\*\* (.+)", texto)
        lineas.append("## {} {}".format(orden, titulo.group(1) if titulo else ""))
        lineas.append("")
        if posicion:
            lineas += ["**Posicion.** " + posicion.group(1).strip(), ""]
        if porque:
            lineas += ["**Por que se sostiene.** " + porque.group(1).strip(), ""]
        if prueba:
            lineas += ["**Prueba.** " + prueba.group(1).strip(), ""]
        if falsif:
            lineas += ["**Falsificador.** " + falsif.group(1).strip(), ""]
        lineas.append("Fuente: {}".format(os.path.relpath(ruta, REPO).replace("\\", "/")))
        lineas.append("")

    if faltan:
        lineas += ["## Lo que la vision no sostuvo", "",
                   "Cortes declarados que ya no existen en la tesis: {}.".format(", ".join(faltan)), ""]

    entregables = os.path.join(carpeta, "entregables")
    os.makedirs(entregables, exist_ok=True)
    base = re.sub(r"[^A-Za-z0-9 _-]", "", nombre).strip() or "vision"
    md = os.path.join(entregables, base + ".md")
    io.open(md, "w", encoding="utf-8", newline="").write("\n".join(lineas))

    print("[VISION] {}".format(nombre))
    print("  sostiene: {}".format(c.get("sostiene", "")[:90]))
    print("  cortes:   {} vivos, {} detenidos".format(len(piezas), len(faltan)))
    print("  manuscrito: {}".format(os.path.relpath(md, REPO).replace("\\", "/")))

    r = subprocess.run([sys.executable, COMPONER, "--fuente", md, "--salida", entregables,
                        "--clase", "springer"],
                       capture_output=True, text=True, cwd=REPO, timeout=900)
    print("  " + "\n  ".join((r.stdout or "").strip().split("\n")[-4:]))
    return r.returncode


def main():
    if not os.path.isdir(VISIONES):
        print("[SIN VISIONES] no existe {}".format(VISIONES))
        return 2
    if "--contar" in sys.argv:
        nombres = sorted(d for d in os.listdir(VISIONES) if os.path.isdir(os.path.join(VISIONES, d)))
        print("visiones: {}".format(len(nombres)))
        for n in nombres:
            v = leer_vision(os.path.join(VISIONES, n))
            if not v:
                print("  {}: SIN VISION.vd".format(n)); continue
            vivas = sum(1 for o in v["cortes"] if candado_de(o))
            print("  {}: {} cortes, {} vivos".format(n, len(v["cortes"]), vivas))
        return 0
    for i, a in enumerate(sys.argv):
        if a == "--vision" and i + 1 < len(sys.argv):
            return componer(sys.argv[i + 1])
    print("Uso: visor.py --contar | --vision <nombre>")
    return 2


if __name__ == "__main__":
    sys.exit(main())
