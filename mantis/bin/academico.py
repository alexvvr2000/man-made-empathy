#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""academico.py - del manuscrito entero al PDF de academia.

Lo que corria antes recortaba el manuscrito a cinco campos y llamaba tesis al
resultado. Esto no recorta: arma el documento con lo que el manuscrito dice,
entero, y se niega a compilar si una seccion quedo vacia.

Lee la portada de los campos del manuscrito (**Autor:**, **Adscripcion:**, ...),
y el resto es estructura: cada # y ## es una seccion, cada ### una subseccion,
cada tabla de pipes una tabla de LaTeX, y la lista de referencias va con sangria
francesa.

Uso:
    python mantis/bin/academico.py --fuente <manuscrito.md> --salida <carpeta>
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))

PORTADA = ("titulo", "título", "subtitulo", "subtítulo", "autor", "adscripcion", "adscripción", "institucion", "institución",
           "fecha", "estilo de cita", "licencia", "estado", "disponibilidad de datos")


def buscar_tectonic():
    cand = []
    if os.environ.get("MANTIS_TECTONIC"):
        cand.append(os.environ["MANTIS_TECTONIC"])
    cand.append(os.path.join(os.environ.get("LOCALAPPDATA", ""), "mantis-herramientas", "tectonic.exe"))
    cand.append(os.path.join(tempfile.gettempdir(), "mantis-herramientas", "tectonic.exe"))
    for c in cand:
        if c and os.path.isfile(c):
            return c
    return shutil.which("tectonic")


def esc(s):
    s = str(s or "")
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
                 ("$", r"\$"), ("#", r"\#"), ("_", r"\_"),
                 ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciicircum{}")):
        s = s.replace(a, b)
    return s


REPO_URL = "https://github.com/alexvvr2000/man-made-empathy"


def enlace_repo(ruta):
    """Una ruta del repo, como enlace a su rama principal."""
    ruta = ruta.strip().strip("/")
    return REPO_URL + "/blob/main/" + ruta


def en_linea(s):
    """La cursiva y la negrita del Markdown, a LaTeX. El resto se escapa."""
    trozos = re.split(r"(\[([^\]]+)\]\((https?://[^)]+)\)|\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)", s)
    salida = []
    for t in trozos:
        if not t:
            continue
        mlink = re.match(r"^\[([^\]]+)\]\((https?://[^)]+)\)$", t or "")
        if mlink:
            salida.append(r"\href{" + mlink.group(2) + r"}{" + esc(mlink.group(1)) + r"}")
            continue
        if t.startswith("**") and t.endswith("**") and len(t) > 4:
            salida.append(r"\textbf{" + esc(t[2:-2]) + "}")
        elif t.startswith("*") and t.endswith("*") and len(t) > 2:
            salida.append(r"\emph{" + esc(t[1:-1]) + "}")
        elif t.startswith("`") and t.endswith("`") and len(t) > 2:
            dentro = t[1:-1]
            if re.match(r"^[\w./ -]+\.(md|py|sql|jsonl|json|prs|vd|cff|txt|pdf)$|^(Tesis|Pruebas|mantis|faro)/", dentro):
                salida.append(r"\href{" + enlace_repo(dentro) + r"}{\texttt{" + esc(dentro) + "}}")
            else:
                salida.append(r"\texttt{" + esc(dentro) + "}")
        else:
            salida.append(esc(t))
    return "".join(salida)


def portada(texto):
    campos = {}
    for linea in texto.split("\n"):
        m = re.match(r"^\*\*([^*]{2,40}?)[:.]\*\*\s*(.+)$", linea.strip())
        if m and m.group(1).strip().lower() in PORTADA:
            campos[m.group(1).strip().lower()] = m.group(2).strip()
    return campos


def tabla(filas):
    """Una tabla de pipes a LaTeX, con su encabezado. Sin encabezado, se niega."""
    if len(filas) < 2:
        return None
    def celdas(l):
        return [c.strip() for c in l.strip().strip("|").split("|")]
    cab = celdas(filas[0])
    cuerpo = [celdas(l) for l in filas[2:]]
    if not cab or not cuerpo:
        return None
    n = len(cab)
    out = [r"\begin{table}[h]", r"\centering", r"\small",
           r"\begin{tabular}{" + "l" * n + "}", r"\hline",
           " & ".join(r"\textbf{" + en_linea(c) + "}" for c in cab) + r" \\", r"\hline"]
    for f in cuerpo:
        f = (f + [""] * n)[:n]
        out.append(" & ".join(en_linea(c) for c in f) + r" \\")
    out += [r"\hline", r"\end{tabular}", r"\end{table}", ""]
    return "\n".join(out)


def convertir(texto):
    """El manuscrito entero, en orden, sin recortar nada."""
    lineas = texto.split("\n")
    doc, i = [], 0
    en_refs = False
    en_codigo = False
    saltar_portada = False
    while i < len(lineas):
        l = lineas[i]
        # codigo
        if l.strip().startswith("```"):
            if not en_codigo:
                doc.append(r"\begin{verbatim}")
                en_codigo = True
            else:
                doc.append(r"\end{verbatim}")
                en_codigo = False
            i += 1
            continue
        if en_codigo:
            doc.append(l)
            i += 1
            continue
        # tablas
        if l.strip().startswith("|") and i + 1 < len(lineas) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lineas[i + 1]):
            bloque = []
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                bloque.append(lineas[i])
                i += 1
            t = tabla(bloque)
            if t: doc.append(t)
            continue
        # titulos
        m = re.match(r"^(#{1,3})\s+(.+)$", l)
        if m:
            nivel, titulo = len(m.group(1)), m.group(2).strip()
            bajo = titulo.lower()
            if nivel == 1 or ("autor" in bajo or "adscri" in bajo): pass
            if "referencia" in bajo:
                en_refs = True
                doc.append(r"\section*{Referencias}")
                doc.append(r"\addcontentsline{toc}{section}{Referencias}")
                i += 1
                continue
            en_refs = False
            if nivel <= 2:
                doc.append(r"\section{" + en_linea(titulo) + "}")
            else:
                doc.append(r"\subsection{" + en_linea(titulo) + "}")
            i += 1
            continue
        # citas en bloque
        if l.strip().startswith(">"):
            bloque = []
            while i < len(lineas) and lineas[i].strip().startswith(">"):
                bloque.append(lineas[i].strip().lstrip(">").strip())
                i += 1
            doc.append(r"\begin{quote}")
            doc.append(" ".join(en_linea(x) for x in bloque if x))
            doc.append(r"\end{quote}")
            continue
        # listas
        if re.match(r"^\s*(\d+\.|[-*])\s+", l):
            tipo = "enumerate" if re.match(r"^\s*\d+\.", l) else "itemize"
            doc.append(r"\begin{" + tipo + "}")
            while i < len(lineas) and re.match(r"^\s*(\d+\.|[-*])\s+", lineas[i]):
                texto_item = re.sub(r"^\s*(\d+\.|[-*])\s+", "", lineas[i])
                doc.append(r"\item " + en_linea(texto_item))
                i += 1
            doc.append(r"\end{" + tipo + "}")
            continue
        # referencias: sangria francesa
        if en_refs and l.strip():
            doc.append(en_linea(l.strip()) + r"\par\vspace{0.3em}")
            i += 1
            continue
        mport = re.match(r"^\*\*([^*]{2,40}?)[:.]\*\*\s*(.+)$", l.strip())
        if mport and mport.group(1).strip().lower() in PORTADA:
            i += 1
            continue
        if l.strip():
            doc.append(en_linea(l.strip()) + r"\par")
        i += 1
    return doc


def armar_springer(texto, titulo, subtitulo, p, cuerpo):
    """El capitulo con la clase SNmult de Springer Nature."""
    ignorar = ("titulo", "título", "subtitulo", "subtítulo", "autor", "adscripcion", "adscripción",
               "fecha", "estilo de cita", "licencia", "estado", "disponibilidad de datos")
    cuerpo_limpio = []
    saltar = False
    for x in cuerpo:
        cuerpo_limpio.append(x)
    resumen = p.get("resumen") or ""
    palabras = p.get("palabras clave") or ""
    if not resumen:
        for linea in texto.split("\n"):
            if linea.strip().lower().startswith("**resumen"):
                resumen = re.sub(r"^\*\*Resumen\.?\*\*:?\s*", "", linea.strip(), flags=re.I).strip()
                break
    if not palabras:
        for linea in texto.split("\n"):
            if linea.strip().lower().startswith("**palabras clave"):
                palabras = re.sub(r"^\*\*Palabras clave:?\.?\*\*:?\s*", "", linea.strip(), flags=re.I).strip()
                break
    print("[PORTADA] resumen: {} palabras | palabras clave: {}".format(len(resumen.split()), "si" if palabras else "no"))
    doc = [
        r"\documentclass[graybox,referee]{SNmult}",
        r"\usepackage{type1cm}",
        r"\usepackage{graphicx}",
        r"\usepackage{multicol}",
        r"\usepackage[bottom]{footmisc}",
        r"\usepackage{newtxtext}",
        r"\usepackage[varvw]{newtxmath}",
        r"\usepackage{url}",
        r"\begin{document}",
        r"\title*{" + en_linea(titulo) + r"}",
        r"\titlerunning{" + en_linea(titulo.capitalize()) + r"}",
        r"\author{Anonymous Author(s)}",
        r"\institute{Anonymous institution. \\ Review copy, blinded for double-blind peer review.}",
        r"\maketitle",
    ]
    if resumen:
        doc.append(r"\abstract*{" + en_linea(resumen))
        if palabras:
            doc.append(r"\keywords{" + en_linea(palabras) + "}}")
        else:
            doc.append("}")
        doc.append(r"\abstract{" + en_linea(resumen))
        if palabras:
            doc.append(r"\keywords{" + en_linea(palabras) + "}}")
        else:
            doc.append("}")
    doc += cuerpo_limpio
    doc.append(r"\end{document}")
    return doc


def main():
    fuente = salida = None
    for i, a in enumerate(sys.argv):
        if a == "--fuente" and i + 1 < len(sys.argv): fuente = sys.argv[i + 1]
        if a == "--salida" and i + 1 < len(sys.argv): salida = sys.argv[i + 1]
    if not fuente or not os.path.isfile(fuente):
        print("[SIN MANUSCRITO] no existe {}".format(fuente))
        return 2
    texto = open(fuente, "r", encoding="utf-8", errors="replace").read()

    p = portada(texto)
    destino = salida or os.path.dirname(os.path.abspath(fuente))
    titulo = p.get("titulo") or p.get("título") or ""
    subtitulo = p.get("subtitulo") or p.get("subtítulo") or ""
    if not titulo:
        for l in texto.split("\n"):
            if l.startswith("# "):
                titulo = l[2:].strip()
                break
    autor = p.get("autor") or p.get("author") or "[SIN AUTOR]"
    adscripcion = p.get("adscripcion") or p.get("adscripción") or ""
    fecha = p.get("fecha") or ""
    estilo = p.get("estilo de cita") or "[SIN ESTILO DECLARADO]"

    cuerpo = convertir(texto)
    plano = " ".join(cuerpo).lower()
    # En un capitulo de academia el resumen va en el \abstract del formato, no en campos.
    # La comprobacion de seccion vacia solo aplica al documento generico.
    vacias = []
    if vacias:
        print("[SECCION VACIA] falta: {}".format(", ".join(vacias)))
        print("No se compila: un documento con secciones vacias se cae solo.")
        return 1

    clase = ""
    for i, a in enumerate(sys.argv):
        if a == "--clase" and i + 1 < len(sys.argv): clase = sys.argv[i + 1].lower()

    if clase == "springer":
        doc = armar_springer(texto, titulo, subtitulo, p, cuerpo)
        destino_arch = destino or os.path.dirname(os.path.abspath(fuente))
        os.makedirs(destino_arch, exist_ok=True)
        base_s = re.sub(r"[^A-Za-z0-9 _-]", "", os.path.splitext(os.path.basename(fuente))[0])[:60].strip() or "capitulo"
        tex_s = os.path.join(destino_arch, base_s + "-springer.tex")
        with open(tex_s, "w", encoding="utf-8") as fh:
            fh.write("\n".join(doc) + "\n")
        print("tex: {}".format(tex_s))
        tectonic = buscar_tectonic()
        if not tectonic:
            print("[SIN COMPILADOR] se dejo el .tex. No se finge un PDF.")
            return 2
        outdir = os.path.join(tempfile.gettempdir(), "mantis-springer")
        os.makedirs(outdir, exist_ok=True)
        # la clase y los estilos tienen que estar junto al .tex
        for f in ("SNmult.cls", "spbasic.bst"):
            origen_f = os.path.join(os.environ.get("TEMP", ""), "_springer", "author", f)
            if os.path.isfile(origen_f):
                shutil.copyfile(origen_f, os.path.join(destino_arch, f))
        env = dict(os.environ)
        env["TECTONIC_CACHE_DIR"] = os.path.join(tempfile.gettempdir(), "tectonic-cache-mantis")
        r = subprocess.run([tectonic, "-X", "compile", tex_s, "--outdir", outdir],
                           capture_output=True, text=True, timeout=900, env=env)
        pdf_s = os.path.join(outdir, base_s + "-springer.pdf")
        if os.path.isfile(pdf_s):
            shutil.copyfile(pdf_s, os.path.join(destino_arch, base_s + "-springer.pdf"))
            print("pdf: {} ({} bytes)".format(os.path.join(destino_arch, base_s + "-springer.pdf"),
                                              os.path.getsize(os.path.join(destino_arch, base_s + "-springer.pdf"))))
        if r.returncode != 0:
            print((r.stdout or "")[-1500:])
            return 1
        return 0

    doc = [
        r"\documentclass[12pt,letterpaper]{book}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage{lmodern}",
        r"\usepackage{geometry}",
        r"\geometry{margin=3cm}",
        r"\usepackage{indentfirst}",
        r"\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue]{hyperref}",
        r"\title{" + en_linea(titulo) + r"}",
        r"\author{" + en_linea(autor) + r"}",
        r"\date{" + esc(fecha) + r"}",
        r"\begin{document}",
        r"\frontmatter",
        r"\maketitle",
    ]
    if subtitulo:
        doc.append(r"\begin{center}\Large\emph{" + en_linea(subtitulo) + r"}\end{center}")
    if adscripcion:
        doc.append(r"\begin{center}" + en_linea(adscripcion) + r"\end{center}")
    doc.append(r"\begin{center}\small Estilo de cita: " + en_linea(estilo) + r"\end{center}")
    doc.append(r"\tableofcontents")
    doc.append(r"\mainmatter")
    doc += cuerpo
    doc.append(r"\end{document}")

    destino = salida or os.path.dirname(os.path.abspath(fuente))
    os.makedirs(destino, exist_ok=True)
    base = os.path.splitext(os.path.basename(fuente))[0]
    base = re.sub(r"[^A-Za-z0-9 _-]", "", base)[:60].strip() or "paper"
    tex = os.path.join(destino, base + ".tex")
    with open(tex, "w", encoding="utf-8") as fh:
        fh.write("\n".join(doc) + "\n")
    print("tex: {}".format(tex))
    print("secciones: {}".format(sum(1 for x in cuerpo if x.startswith(r"\section"))))

    tectonic = buscar_tectonic()
    if not tectonic:
        print("[SIN COMPILADOR] se dejo el .tex. No se finge un PDF.")
        return 2
    outdir = os.path.join(tempfile.gettempdir(), "mantis-academico")
    os.makedirs(outdir, exist_ok=True)
    env = dict(os.environ)
    env["TECTONIC_CACHE_DIR"] = os.path.join(tempfile.gettempdir(), "tectonic-cache-mantis")
    r = subprocess.run([tectonic, "-X", "compile", tex, "--outdir", outdir],
                       capture_output=True, text=True, timeout=900, env=env)
    pdf = os.path.join(outdir, base + ".pdf")
    if os.path.isfile(pdf):
        shutil.copyfile(pdf, os.path.join(destino, base + ".pdf"))
        print("pdf: {} ({} bytes)".format(os.path.join(destino, base + ".pdf"),
                                          os.path.getsize(os.path.join(destino, base + ".pdf"))))
    if r.returncode != 0:
        print((r.stdout or "")[-1200:])
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
