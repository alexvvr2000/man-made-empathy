#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""teoricas — las nueve tesis de la vision del autor, cada una con sus dos archivos.

Entra una tesis, y sale lo que se entrega:

    vision del autor/tesis teorica/<el nombre>/<el nombre>.tex
    vision del autor/tesis teorica/<el nombre>/<el nombre>.pdf

La tesis trae ocho campos, y esos ocho son las ocho secciones de un paper.
No hay que escribir nada nuevo: se mueve lo que ya esta escrito al formato
de la academia, y se compila.

Uso:
    python teoricas.py            escribe las nueve
    python teoricas.py "convivir" escribe una
"""
import io
import os
import re
import shutil
import subprocess
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.path.abspath(os.path.join(MANTIS, ".."))
ORIGEN = os.path.join(REPO, "tesis autor", "fuente", "man made empathy")
DESTINO = os.path.join(REPO, "tesis autor", "teoricas")

CAMPOS = [
    ("Posición", "La tesis"),
    ("Por qué se sostiene", "Por qué se sostiene"),
    ("De dónde viene", "De dónde viene"),
    ("Qué pregunta deja", "Lo que queda abierto"),
    ("Ficción", "El caso"),
    ("Prueba", "Método"),
    ("Falsificador", "Límites, y qué la tumba"),
    ("Estado", "Estado de la tesis"),
]


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def campos(texto):
    fuera = {}
    for nombre, _ in CAMPOS:
        m = re.search(r"\*\*" + re.escape(nombre) + r"[.:]?\*\*\s*(.+?)(?=\n\*\*|\n## |\Z)", texto, re.S)
        fuera[nombre] = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    return fuera


def tex(s):
    s = s.replace("\\", "\\textbackslash{}")
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"\*(.+?)\*", r"\\emph{\1}", s)
    s = s.replace("“", "``").replace("”", "''")
    s = s.replace("¿", "\\textquestiondown{}").replace("¡", "\\textexclamdown{}")
    s = re.sub(r"(?<!\\)%", r"\\%", s)
    s = re.sub(r"(?<!\\)&", r"\\&", s)
    s = re.sub(r"(?<!\\)_", r"\\_", s)
    s = re.sub(r"(?<!\\)#", r"\\#", s)
    s = re.sub(r"(?<!\\)\^", r"\\^{}", s)
    return s


def slug(n):
    s = unicodedata.normalize("NFD", n.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def construir(nombre, markdown):
    c = campos(markdown)
    falta = [n for n, _ in CAMPOS if not c.get(n) and n != "Estado"]
    if falta:
        return None, falta

    titulo = nombre if nombre != "man made empathy" else "Man made empathy"
    l = []
    l.append(r"\documentclass[11pt,a4paper]{article}")
    l.append(r"\usepackage[utf8]{inputenc}")
    l.append(r"\usepackage[T1]{fontenc}")
    l.append(r"\usepackage[spanish]{babel}")
    l.append(r"\usepackage{hyperref}")
    l.append(r"\usepackage{geometry}")
    l.append(r"\geometry{margin=2.5cm}")
    l.append(r"\usepackage{parskip}")
    l.append("")
    l.append(r"\title{" + tex(titulo.capitalize()) + "}")
    l.append(r"\author{Alejandro Valenzuela Rivera\\\small Universidad Autónoma de Nuevo León}")
    l.append(r"\date{\today}")
    l.append(r"\begin{document}")
    l.append(r"\maketitle")
    l.append("")
    l.append(r"\begin{quote}")
    l.append(r"\textbf{Sesgo declarado.} " + tex(
        "Este trabajo se sostiene desde el sesgo declarado de su autor, y no finge neutralidad. "
        "Lo que afirma se puede tumbar, y ese es el punto: el falsificador está escrito, no escondido."))
    l.append(r"\end{quote}")
    l.append("")
    for campo, seccion in CAMPOS:
        if not c.get(campo):
            continue
        l.append(r"\section{" + tex(seccion) + "}")
        l.append(tex(c[campo]))
        l.append("")
    l.append(r"\section*{Cómo se leyó esta tesis}")
    l.append(tex(
        "Esto se escribió en el repositorio man-made-empathy, y la tesis está completa en "
        "vision del autor/tesis/man made empathy/" + nombre + "/. La máquina que la compuso no agregó "
        "nada que no estuviera escrito: si algo de esto es falso, se dice en el mismo sitio, y se corrige con fecha."))
    l.append(r"\end{document}")
    return "\n".join(l) + "\n", []


def compilar(carpeta, texfile):
    candidatos = [shutil.which(c) for c in ("tectonic", "pdflatex", "xelatex")]
    candidatos.append(os.path.join(os.path.expanduser("~"), "AppData", "Local", "Programs",
                                   "tectonic", "tectonic.exe"))
    for exe in [c for c in candidatos if c and os.path.isfile(c)]:
        if "tectonic" in os.path.basename(exe).lower():
            subprocess.run([exe, "-X", "compile", texfile, "--outdir", carpeta],
                           capture_output=True, timeout=900)
        else:
            subprocess.run([exe, "-interaction=nonstopmode", "-output-directory", carpeta, texfile],
                           capture_output=True, timeout=900)
        pdf = os.path.splitext(texfile)[0] + ".pdf"
        if os.path.isfile(pdf):
            return pdf
    return None


def main(argv):
    if not os.path.isdir(ORIGEN):
        print("[SIN ORIGEN] no esta " + ORIGEN)
        return 1
    nombres = []
    for d in sorted(os.listdir(ORIGEN)):
        if os.path.isdir(os.path.join(ORIGEN, d)):
            nombres.append((d, os.path.join(ORIGEN, d, "el cero.md")))
    nombres.insert(0, ("man made empathy", os.path.join(ORIGEN, "man made empathy.md")))
    if len(argv) > 1:
        nombres = [n for n in nombres if argv[1].lower() in n[0].lower()]

    hechos = 0
    faltan = []
    for nombre, archivo in nombres:
        if not os.path.isfile(archivo):
            faltan.append((nombre, ["archivo"]))
            continue
        cuerpo, falta = construir(nombre, leer(archivo))
        if cuerpo is None:
            faltan.append((nombre, falta))
            continue
        carpeta = os.path.join(DESTINO, nombre)
        os.makedirs(carpeta, exist_ok=True)
        t = os.path.join(carpeta, slug(nombre) + ".tex")
        with io.open(t, "w", encoding="utf-8", newline="") as fh:
            fh.write(cuerpo)
        pdf = compilar(carpeta, t)
        hechos += 1
        print("[ok] {:<26} {}".format(nombre[:26], "tex y pdf" if pdf else "solo tex: no hay con que compilar"))

    print("")
    print("[teoricas] {} escritas en vision del autor/tesis teorica/".format(hechos))
    if faltan:
        print("[falta] y no se entregaron:")
        for n, f in faltan:
            print("  {:<26} le falta: {}".format(n[:26], ", ".join(f)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
