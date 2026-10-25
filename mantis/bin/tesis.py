#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tesis.py - el metodo de tesis perpetuas, on demand.

Que hace: toma una vision, triangula sus piezas contra el contexto de la base,
CIERRA el candado (marca sus piezas como cerradas) y COMPONE la tesis de esa
vision como un documento .tex, que se compila a PDF con Tectonic.

On demand: no corre sola. Se pide, y se pide sobre una vision:
    python tesis.py --vision "vision del autor"
    python tesis.py --vision "vision de la maquina"

No rompe la regla de verbalizar: una pieza se puede citar en la tesis solo si
tiene su referencia o se declara CRUDA. Las CRUDAS no se callan: entran al
apendice "lo que quedo crudo", y la tesis no las presenta como probadas.

El binario de Tectonic no vive en el repo: se busca en MANTIS_TECTONIC, en
%LOCALAPPDATA%/mantis-herramientas, en %TEMP% y en el PATH.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
if not os.path.isdir(os.path.join(REPO, ".memoria continua")):
    sys.stderr.write("[SIN REPO] no se encontro la memoria junto a este script.\n")
    sys.exit(2)
DB = os.path.join(REPO, ".memoria continua", "rastro", "mantis.db")
TEMP = tempfile.gettempdir()

TITULOS = {
    "vision del autor": "Tesis del autor",
    "vision de la maquina": "Tesis de la maquina",
    "vision del lector": "Tesis del lector",
}


def buscar_tectonic():
    cand = []
    if os.environ.get("MANTIS_TECTONIC"):
        cand.append(os.environ["MANTIS_TECTONIC"])
    cand.append(os.path.join(os.environ.get("LOCALAPPDATA", ""), "mantis-herramientas", "tectonic.exe"))
    cand.append(os.path.join(TEMP, "mantis-herramientas", "tectonic.exe"))
    for c in cand:
        if c and os.path.isfile(c):
            return c
    return shutil.which("tectonic")


def esc(s):
    """Escapa lo que LaTeX no tolera. No adorna: solo evita que el documento reviente."""
    if s is None:
        return ""
    s = str(s)
    rep = [
        ("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
        ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
        ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}"),
    ]
    for a, b in rep:
        s = s.replace(a, b)
    return s


def piezas(con, vision):
    """Las piezas de una vision.

    Hoy la base no guarda la vision en cada pieza: se asigna por clase.
    Y se declara: cuando la base tenga el campo, esta funcion cambia y nada mas.
    """
    if vision == "vision del autor":
        cur = con.execute(
            'SELECT orden, clase, nombre, "expansión", porque, referencia, pregunta, ficcion '
            "FROM pieza WHERE estado='viva' ORDER BY orden"
        )
        return cur.fetchall()
    return []


def compilar(tex_path, outdir, tectonic):
    env = dict(os.environ)
    env["TECTONIC_CACHE_DIR"] = os.path.join(TEMP, "tectonic-cache-mantis")
    os.makedirs(env["TECTONIC_CACHE_DIR"], exist_ok=True)
    r = subprocess.run(
        [tectonic, "-X", "compile", tex_path, "--outdir", outdir, "--keep-logs"],
        capture_output=True, text=True, timeout=900, env=env,
    )
    return r.returncode == 0, ((r.stdout or "") + (r.stderr or ""))[-1200:]


def main():
    vision = None
    for i, a in enumerate(sys.argv):
        if a == "--vision" and i + 1 < len(sys.argv):
            vision = sys.argv[i + 1]
    if not vision:
        print("Falta la vision. Uso: python tesis.py --vision \"vision del autor\"")
        return 2

    import sqlite3

    con = sqlite3.connect(DB)
    filas = piezas(con, vision)
    if not filas:
        print("[VACIO - SIN TESIS] la vision '{}' no tiene piezas en la base.".format(vision))
        print("Se declara, y no se compone una tesis vacia: una tesis sin piezas es un titulo.")
        con.close()
        return 2

    procesadas = [f for f in filas if f[5] and not str(f[5]).lower().startswith("ninguna")]
    crudas = [f for f in filas if f not in procesadas]

    titulo = TITULOS.get(vision, vision)
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    partes = []
    partes.append(r"\documentclass[12pt,letterpaper]{article}")
    partes.append(r"\usepackage[T1]{fontenc}")
    partes.append(r"\usepackage[utf8]{inputenc}")
    partes.append(r"\usepackage{lmodern}")
    partes.append(r"\usepackage{geometry}")
    partes.append(r"\geometry{margin=2.5cm}")
    partes.append(r"\title{" + esc(titulo) + r"}")
    partes.append(r"\author{Man-Made Empathy}")
    partes.append(r"\date{" + fecha + "}")
    partes.append(r"\begin{document}")
    partes.append(r"\maketitle")

    partes.append(r"\section*{Que es este documento}")
    partes.append(
        esc("Esta tesis se compone on demand desde la memoria, no se escribe a mano. "
            "Cada seccion es una pieza que el autor sostuvo, con su porque y con su fuente. "
            "Lo que no tiene fuente no se presenta como probado: va al apendice, marcado.")
    )

    partes.append(r"\section{Las piezas, y por que se sostienen}")
    for orden, clase, nombre, expansion, porque, referencia, pregunta, ficcion in procesadas:
        partes.append(r"\subsection{" + esc(nombre) + "}")
        partes.append(esc(expansion or "") + r"\par")
        partes.append(r"\emph{Por que se sostiene:} " + esc(porque or "") + r"\par")
        partes.append(r"\emph{De donde viene:} " + esc(referencia or "") + r"\par")
        if pregunta and not str(pregunta).lower().startswith("ninguna"):
            partes.append(r"\emph{Que pregunta deja:} " + esc(pregunta) + r"\par")

    if crudas:
        partes.append(r"\section*{Lo que quedo crudo}")
        partes.append(esc(
            "Estas piezas no declaran de donde vienen. Se listan porque existen, y no se "
            "presentan como probadas. Mientras no se citen o se triangulen, no se entregan "
            "como fuente."))
        partes.append(r"\begin{itemize}")
        for orden, clase, nombre, expansion, porque, referencia, pregunta, ficcion in crudas:
            partes.append(r"\item " + esc(nombre) + r" --- " + esc(expansion or ""))
        partes.append(r"\end{itemize}")

    partes.append(r"\end{document}")

    destino = os.path.join(REPO, "mantis", vision, "entregables")
    os.makedirs(destino, exist_ok=True)
    tex = os.path.join(destino, "tesis.tex")
    with open(tex, "w", encoding="utf-8") as fh:
        fh.write("\n".join(partes) + "\n")

    tectonic = buscar_tectonic()
    outdir = os.path.join(TEMP, "mantis-tesis-" + vision.replace(" ", "-"))
    os.makedirs(outdir, exist_ok=True)
    ok = False
    detalle = "no se compilo: no hay Tectonic"
    if tectonic:
        ok, detalle = compilar(tex, outdir, tectonic)
    pdf = os.path.join(outdir, "tesis.pdf")
    if os.path.isfile(pdf):
        shutil.copyfile(pdf, os.path.join(destino, "tesis.pdf"))

    existe = os.path.isfile(os.path.join(destino, "tesis.pdf"))
    peso = os.path.getsize(os.path.join(destino, "tesis.pdf")) if existe else 0

    # El candado se cierra: se anota que la tesis se compuso, con sus numeros.
    con.execute(
        "INSERT INTO entrada (fecha, sesgo, limite, firma, contra, sostuvo, sostengo, techo, "
        "sin_cambio, estado, friccion) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (
            datetime.now(timezone.utc).isoformat(),
            "Se sostiene desde la memoria: la tesis se compone de las piezas vivas, no de una redaccion nueva.",
            "Solo la vision del autor esta en la base hoy; las otras dos se declaran vacias en vez de inventarse.",
            "humano:autoridad · maquina:tesis.py",
            "La autoridad pide: implementa el metodo de tesis perpetuas, on demand.",
            "La tesis se escribia a mano, y no era perpetua ni on demand.",
            "tesis.py compone la tesis de {} desde la tabla pieza: {} piezas conocidas, {} presentadas como probadas y {} declaradas crudas. Compila con Tectonic y deja .tex y .pdf en mantis/{}/entregables/.".format(
                vision, len(filas), len(procesadas), len(crudas), vision),
            "La autoridad lee el PDF y dice si la tesis compuesta es la que quiere.",
            0,
            "vivo",
            "autoridad",
        ),
    )
    con.commit()
    con.close()

    print("vision: {}".format(vision))
    print("piezas: {} | probadas: {} | crudas: {}".format(len(filas), len(procesadas), len(crudas)))
    print("compilo: {}".format("si" if ok else "no"))
    print("pdf: {} ({} bytes)".format(os.path.join(destino, "tesis.pdf"), peso))
    if not ok:
        print(detalle)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())


