#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso del folder 'los candados': dice el estado, y los parte a entregable.

No los abre: abrirlos es friccion, y la friccion la hace quien decide.
Esta vez declara que hay, cuantos son, cuales no tienen falsificador, y
—si se le pide— parte cada uno a lo que se puede mandar.

Un candado ya trae los siete campos que un paper teorico pide, y no hay
que inventar nada: se mueve lo que esta escrito.

    Posicion            -> el resumen, y la tesis
    Por que se sostiene -> la proposicion, y el argumento
    De donde viene      -> el contexto, y con quien conversa
    Ficcion             -> el caso
    Prueba              -> el metodo conceptual
    Falsificador        -> el limite, y lo que genuinamente lo tumba
    Que pregunta deja   -> lo que queda abierto

Y como el formato ya no es el trabajo, salen los dos que la gente usa: un
.md (que es lo que se abre y se lee) y un .tex (para el destino que pida
LaTeX).

Uso:
    python candados.py                     mide, sin escribir
    python candados.py --entregar          escribe los 92
    python candados.py --entregar 078      escribe uno
"""
import io
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
ORIGEN = os.path.join(REPO, "candados")
DESTINO = os.path.join(REPO, "tesis", "vision del autor", "teoricas")

CAMPOS = ["Posición", "Por qué se sostiene", "De dónde viene",
          "Ficción", "Prueba", "Falsificador", "Qué pregunta deja"]


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def campos(texto):
    fuera = {}
    for nombre in CAMPOS:
        m = re.search(r"\*\*" + re.escape(nombre) + r"\.\*\*\s*(.+?)(?=\n\*\*|\n## |\Z)", texto, re.S)
        fuera[nombre] = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    return fuera


def carpeta_de(titulo):
    """El nombre de carpeta: lo que Windows no acepta, se quita. El titulo se queda entero."""
    s = re.sub(r'[<>:"/\\|?*]', "", titulo)
    return re.sub(r"\s+", " ", s).strip()[:90]


def titulo_de(texto, archivo):
    m = re.search(r"^#\s+(.+)$", texto, re.M)
    if m:
        return m.group(1).strip()
    return os.path.splitext(os.path.basename(archivo))[0]


def slug(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:70]


def esc(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"(?<!\\)%", r"\\%", s)
    s = re.sub(r"(?<!\\)&", r"\\&", s)
    s = re.sub(r"(?<!\\)_", r"\\_", s)
    s = re.sub(r"(?<!\\)#", r"\\#", s)
    return s


def a_markdown(titulo, c, ruta):
    l = ["# " + titulo, ""]
    l.append("**Sesgo declarado.** Este trabajo se sostiene desde el sesgo declarado de su autor, "
             "y no finge neutralidad. Lo que afirma se puede tumbar, y ese es el punto: "
             "el falsificador está escrito, no escondido.")
    l.append("")
    for sec, campo in (("Resumen", "Posición"),
                       ("1. La proposición", "Por qué se sostiene"),
                       ("2. De dónde viene, y con quién conversa", "De dónde viene"),
                       ("3. El caso", "Ficción"),
                       ("4. Método conceptual", "Prueba"),
                       ("5. Límites, y qué la tumba", "Falsificador"),
                       ("6. Lo que queda abierto", "Qué pregunta deja")):
        l.append("## " + sec)
        l.append(c[campo])
        l.append("")
    l.append("---")
    l.append("")
    l.append("*Este candado está completo en `" + ruta + "`. La máquina que lo compuso no agregó "
             "nada que no estuviera escrito.*")
    return "\n".join(l) + "\n"


def a_latex(titulo, c, ruta):
    l = [r"\documentclass[11pt,a4paper]{article}",
         r"\usepackage[utf8]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage[spanish]{babel}",
         r"\usepackage{hyperref}",
         r"\usepackage{geometry}",
         r"\geometry{margin=2.5cm}",
         r"\usepackage{parskip}",
         "",
         r"\title{" + esc(titulo) + "}",
         r"\author{Alejandro Valenzuela Rivera\\\small Universidad Autónoma de Nuevo León}",
         r"\date{\today}",
         r"\begin{document}",
         r"\maketitle",
         "",
         r"\begin{quote}"]
    l.append(r"\textbf{Sesgo declarado.} " + esc(
        "Este trabajo se sostiene desde el sesgo declarado de su autor, y no finge neutralidad. "
        "Lo que afirma se puede tumbar, y ese es el punto: el falsificador está escrito, no escondido."))
    l.append(r"\end{quote}")
    l.append("")
    for sec, campo in ((r"\section*{Resumen}", "Posición"),
                       (r"\section{La proposición}", "Por qué se sostiene"),
                       (r"\section{De dónde viene, y con quién conversa}", "De dónde viene"),
                       (r"\section{El caso}", "Ficción"),
                       (r"\section{Método conceptual}", "Prueba"),
                       (r"\section{Límites, y qué la tumba}", "Falsificador"),
                       (r"\section{Lo que queda abierto}", "Qué pregunta deja")):
        l.append(sec)
        l.append(esc(c[campo]))
        l.append("")
    l.append(r"\section*{Nota de procedencia}")
    l.append(esc("Este candado está completo en " + ruta + ". La máquina que lo compuso no agregó "
                 "nada que no estuviera escrito."))
    l.append(r"\end{document}")
    return "\n".join(l) + "\n"


def todos_los_candados():
    fuera = []
    if not os.path.isdir(ORIGEN):
        return fuera
    for cap in sorted(d for d in os.listdir(ORIGEN) if os.path.isdir(os.path.join(ORIGEN, d))):
        ruta_cap = os.path.join(ORIGEN, cap)
        for f in sorted(os.listdir(ruta_cap)):
            if f.endswith(".md") and f.lower() != "readme.md":
                fuera.append(os.path.join(ruta_cap, f))
    return fuera


def main(argv):
    if not os.path.isdir(ORIGEN):
        print("[SIN CANDADOS] no esta " + ORIGEN)
        return 1

    todos = todos_los_candados()
    sin_falsificador = []
    sin_campos = []
    for p in todos:
        t = leer(p)
        if "Falsificador" not in t and "falsificador" not in t:
            sin_falsificador.append(os.path.basename(p))
        c = campos(t)
        falta = [k for k in CAMPOS if not c[k]]
        if falta:
            sin_campos.append((os.path.basename(p), falta))

    carpetas = sorted(d for d in os.listdir(ORIGEN) if os.path.isdir(os.path.join(ORIGEN, d)))
    print("[ok] {} candados en {} carpetas".format(len(todos), len(carpetas)))
    for cap in carpetas:
        n = len([f for f in os.listdir(os.path.join(ORIGEN, cap)) if f.endswith(".md") and f.lower() != "readme.md"])
        print("  {:<32} {}".format(cap, n))
    print("")
    print("[ok] {} con sus siete campos, y por lo tanto entregables".format(len(todos) - len(sin_campos)))

    if sin_falsificador:
        print("")
        print("[falla] {} candado(s) sin falsificador:".format(len(sin_falsificador)))
        for s in sin_falsificador[:10]:
            print("  - " + s)
        return 1

    if sin_campos:
        print("")
        print("[aviso] {} candado(s) sin sus siete campos, y no se entregan:".format(len(sin_campos)))
        for n, f in sin_campos:
            print("  {:<56} le falta: {}".format(n[:56], ", ".join(f)))

    if "--entregar" in argv:
        i = argv.index("--entregar")
        filtro = argv[i + 1].lower() if i + 1 < len(argv) else None
        hechos = 0
        for p in todos:
            t = leer(p)
            c = campos(t)
            if [k for k in CAMPOS if not c[k]]:
                continue
            titulo = titulo_de(t, p)
            if filtro and filtro not in titulo.lower() and filtro not in os.path.basename(p).lower():
                continue
            carpeta = os.path.join(DESTINO, carpeta_de(titulo))
            os.makedirs(carpeta, exist_ok=True)
            base = slug(titulo)
            ruta = os.path.relpath(p, REPO).replace("\\", "/")
            with open(os.path.join(carpeta, base + ".md"), "w", encoding="utf-8", newline="") as fh:
                fh.write(a_markdown(titulo, c, ruta))
            with open(os.path.join(carpeta, base + ".tex"), "w", encoding="utf-8", newline="") as fh:
                fh.write(a_latex(titulo, c, ruta))
            hechos += 1
        print("")
        print("[ok] {} escritos en {}, con su .md y su .tex".format(
            hechos, os.path.relpath(DESTINO, REPO)))
    else:
        print("")
        print("para escribirlos:  python mantis/bin/candados.py --entregar")
        print("")

    print("pasa: todos los candados tienen falsificador")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
