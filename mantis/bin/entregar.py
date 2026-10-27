#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""entregar — convierte un candado en un paper de LaTeX, listo para mandar.

No pide aprender LaTeX, ni instalar nada. Un candado ya trae sus siete
campos, y esos siete ya son las siete secciones de un paper:

    Posición              -> Resumen y la tesis
    Por qué se sostiene   -> Introducción y argumento
    De dónde viene        -> Trabajo previo y contexto
    Qué pregunta deja     -> Lo que queda abierto
    Ficción               -> El caso
    Prueba                -> Método
    Falsificador          -> Límites, y qué lo tumba

Y el sesgo declarado se pone en la primera página, porque eso es lo que
este repo agrega.

Uso:
    python entregar.py                       lista los candados que se pueden entregar
    python entregar.py "<el candado>"        escribe vision del autor/<el candado>/

Sale 0 si escribió, 1 si el candado no está, 2 si le falta un campo.
"""
import io
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.path.abspath(os.path.join(MANTIS, ".."))
CANDADOS = os.path.join(REPO, "candados")
ENTREGAS = os.path.join(REPO, "tesis", "vision del autor", "teoria completa", "las nueve piezas")

CAMPOS = [
    ("Posición", "resumen"),
    ("Por qué se sostiene", "argumento"),
    ("De dónde viene", "contexto"),
    ("Qué pregunta deja", "abierto"),
    ("Ficción", "caso"),
    ("Prueba", "metodo"),
    ("Falsificador", "limites"),
]


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def campos_de(texto):
    """Los siete campos, tal como están escritos en el candado."""
    fuera = {}
    for nombre, _ in CAMPOS:
        m = re.search(r"\*\*" + re.escape(nombre) + r"\.\*\*\s*(.+?)(?=\n\*\*|\n\n\*\*|\Z)", texto, re.S)
        fuera[nombre] = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    return fuera


def limpia(s):
    """De markdown a LaTeX: lo justo y nada más."""
    s = s.replace("\\", "\\textbackslash{}")
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = s.replace("“", "``").replace("”", "''")
    s = s.replace("¿", "\\textquestiondown{}").replace("¡", "\\textexclamdown{}")
    s = s.replace("=", "$=$").replace(" gate ", " $>$ ")
    s = re.sub(r"(?<!\\)%", r"\\%", s)
    s = re.sub(r"(?<!\\)&", r"\\&", s)
    s = re.sub(r"(?<!\\)_", r"\\_", s)
    s = re.sub(r"(?<!\\)#", r"\\#", s)
    s = re.sub(r"(?<!\\)\^", r"\\^{}", s)
    # palabras sueltas que LaTeX se come
    return s


def id_de(nombre):
    """Un nombre de archivo que no rompa nada."""
    s = unicodedata.normalize("NFD", nombre.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    return re.sub(r"\s+", "-", s.strip())[:60]


def paper(nombre, c, archivo):
    falta = [n for n, _ in CAMPOS if not c.get(n)]
    if falta:
        return None, falta

    titulo = nombre
    autor = "Alejandro Valenzuela Rivera"
    cuerpo = []
    cuerpo.append(r"\documentclass[11pt,a4paper]{article}")
    cuerpo.append(r"\usepackage[utf8]{inputenc}")
    cuerpo.append(r"\usepackage[T1]{fontenc}")
    cuerpo.append(r"\usepackage[spanish]{babel}")
    cuerpo.append(r"\usepackage{hyperref}")
    cuerpo.append(r"\usepackage{geometry}")
    cuerpo.append(r"\geometry{margin=2.5cm}")
    cuerpo.append(r"\usepackage{parskip}")
    cuerpo.append("")
    cuerpo.append(r"\title{" + limpia(titulo) + "}")
    cuerpo.append(r"\author{" + autor + r"\\\small Universidad Autónoma de Nuevo León}")
    cuerpo.append(r"\date{\today}")
    cuerpo.append(r"\begin{document}")
    cuerpo.append(r"\maketitle")
    cuerpo.append("")
    cuerpo.append(r"\begin{quote}")
    cuerpo.append(r"\textbf{Sesgo declarado.} " + limpia(
        "Este trabajo se sostiene desde el sesgo declarado de su autor, y no finge neutralidad. "
        "Lo que afirma se puede tumbar, y ese es el punto: el falsificador está escrito, "
        "no escondido."))
    cuerpo.append(r"\end{quote}")
    cuerpo.append("")
    cuerpo.append(r"\section*{Resumen}")
    cuerpo.append(limpia(c["Posición"]))
    cuerpo.append("")
    cuerpo.append(r"\section{Por qué se sostiene}")
    cuerpo.append(limpia(c["Por qué se sostiene"]))
    cuerpo.append("")
    cuerpo.append(r"\section{De dónde viene}")
    cuerpo.append(limpia(c["De dónde viene"]))
    cuerpo.append("")
    cuerpo.append(r"\section{El caso}")
    cuerpo.append(limpia(c["Ficción"]))
    cuerpo.append("")
    cuerpo.append(r"\section{Método}")
    cuerpo.append(limpia(c["Prueba"]))
    cuerpo.append("")
    cuerpo.append(r"\section{Límites, y qué lo tumba}")
    cuerpo.append(limpia(c["Falsificador"]))
    cuerpo.append("")
    cuerpo.append(r"\section{Lo que queda abierto}")
    cuerpo.append(limpia(c["Qué pregunta deja"]))
    cuerpo.append("")
    cuerpo.append(r"\section*{Cómo se leyó esta tesis}")
    cuerpo.append(limpia(
        "Esto se escribió en el repositorio man-made-empathy, del que este candado es una pieza: "
        + archivo + ". La máquina que lo compuso lo hizo desde este mismo archivo, y no agregó nada que no estuviera escrito. "
        "Si algo de esto es falso, se dice en el mismo sitio, y se corrige con fecha."))
    cuerpo.append("")
    cuerpo.append(r"\end{document}")
    return "\n".join(cuerpo) + "\n", []


def lista():
    fuera = []
    for base, dirs, files in os.walk(CANDADOS):
        for f in sorted(files):
            if not f.endswith(".md") or f.lower() == "readme.md":
                continue
            fuera.append(os.path.join(base, f))
    return fuera


def compilar(tex):
    """Compila el .tex si este mundo tiene con qué. Si no, lo dice."""
    import shutil, subprocess
    # y si el mundo no lo tiene en el PATH, se busca donde se instalo
    candidatos = [shutil.which(c) for c in ("tectonic", "pdflatex", "xelatex")]
    candidatos.append(os.path.join(os.path.expanduser("~"), "AppData", "Local", "Programs",
                                   "tectonic", "tectonic.exe"))
    for exe in [c for c in candidatos if c and os.path.isfile(c)]:
        cmd = "tectonic" if "tectonic" in os.path.basename(exe).lower() else "pdflatex"
        try:
            if cmd == "tectonic":
                subprocess.run([exe, "-X", "compile", tex, "--outdir", os.path.dirname(tex)],
                               capture_output=True, timeout=600)
            else:
                subprocess.run([exe, "-interaction=nonstopmode", "-output-directory", os.path.dirname(tex), tex],
                               capture_output=True, timeout=600)
        except Exception:
            return None
        pdf = os.path.splitext(tex)[0] + ".pdf"
        return pdf if os.path.isfile(pdf) else None
    return None


def main(argv):
    todos = lista()
    if not todos:
        print("[SIN CANDADOS] no hay candados en " + CANDADOS)
        return 1

    if len(argv) < 2:
        print("[entregar] {} candados".format(len(todos)))
        completos = 0
        for p in todos:
            c = campos_de(leer(p))
            falta = [n for n, _ in CAMPOS if not c.get(n)]
            if not falta:
                completos += 1
        print("[entregar] {} tienen sus siete campos, y se pueden entregar".format(completos))
        print("[entregar] los demás se listan con lo que les falta:")
        for p in todos:
            c = campos_de(leer(p))
            falta = [n for n, _ in CAMPOS if not c.get(n)]
            if falta:
                print("  {:<58} le falta: {}".format(os.path.basename(p)[:58], ", ".join(falta)))
        return 0

    cual = " ".join(argv[1:])
    p = None
    for x in todos:
        if cual.lower() in os.path.basename(x).lower():
            p = x
            break
    if p is None:
        print("[SIN CANDADO] no está: " + cual)
        return 1
    c = campos_de(leer(p))
    nombre = os.path.basename(p)[:-3]
    tex, falta = paper(nombre, c, os.path.relpath(p, REPO).replace("\\", "/"))
    if tex is None:
        print("[SIN ENTREGA] le falta: " + ", ".join(falta))
        return 2
    carpeta = os.path.join(ENTREGAS, nombre)
    os.makedirs(carpeta, exist_ok=True)
    destino = os.path.join(carpeta, id_de(nombre) + ".tex")
    with io.open(destino, "w", encoding="utf-8", newline="") as fh:
        fh.write(tex)
    print("[entregar] " + nombre)
    print("deja: " + os.path.relpath(destino, REPO))
    print("")
    pdf = compilar(destino)
    if pdf:
        print("y el PDF: " + os.path.relpath(pdf, REPO))
    else:
        print("y el PDF: no hay con qué compilar en este mundo (falta tectonic o pdflatex)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
