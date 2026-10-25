#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""componer.py - de una tesis dicha, a un .tex y un .pdf.

Lee una tesis --un archivo de texto, o un candado, o un tema con sus fuentes--
y escribe el documento con la forma de su tipo. Despues compila.

Uso:
    python mantis/bin/componer.py --tipo teoria --fuente <archivo> --salida <carpeta>
    python mantis/bin/componer.py --tipo coro   --fuente <archivo> --salida <carpeta>
    python mantis/bin/componer.py --tipo mesa   --fuente <archivo> --salida <carpeta>

Los tres tipos no comparten formato, y no deben: una le habla a un revisor de
filosofia, otra a un revisor de academia, y otra a quien va a usarlo.

Si no hay compilador, deja el .tex y lo dice: no finge un PDF.
Si a la fuente le falta lo que el tipo exige, devuelve el marcador vacio.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))

PORTADAS = {
    "teoria": "Tesis teorica",
    "coro": "Tesis de academia",
    "mesa": "Tesis practica",
}

# lo que cada tipo exige en el texto de la fuente, y su nombre legible
EXIGE = {
    "teoria": [("aunque", "el aunque: lo que ya se dice"),
               ("sostiene", "el sostiene: la posicion"),
               ("porque", "el porque: la razon")],
    "coro": [("problema", "el problema"),
             ("metodo", "el metodo"),
             ("resultado", "el resultado"),
             ("referencia", "las referencias")],
    "mesa": [("problema", "el problema"),
             ("procedimiento", "el procedimiento"),
             ("numero", "los numeros"),
             ("queda", "lo que queda")],
}

# el marcador vacio de cada tipo: si el campo falta en la fuente, se deja dicho
# y no se rellena. Una seccion que parece contenido y esta hueca es el error.
VACIO = "[SIN ESTE CAMPO EN LA FUENTE]"

# lo que no se puede sostener con una palabra que aparezca de paso: los
# campos se buscan como encabezado (**Campo.**) o como fila de tabla que empieza
# con el nombre. Buscar la palabra en cualquier parte daba por buena una tesis
# que solo la mencionaba.
PREFIJO_TABLA = {'numero': ('numero', 'numeros', 'número', 'números', 'numeros medidos')}


def esc(s):
    if s is None:
        return ""
    s = str(s)
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
                 ("$", r"\$"), ("#", r"\#"), ("_", r"\_"),
                 ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciicircum{}")):
        s = s.replace(a, b)
    return s


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


def leer_fuente(ruta):
    with open(ruta, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def sin_tildes(s):
    """Baja a minusculas y quita tildes: la fuente puede escribir Metodo o Método."""
    tabla = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ", "aeiouunAEIOUUN")
    return s.translate(tabla).lower().strip()


def bloques(texto):
    """Saca los **Campo.** de la fuente: sirve para el candado y para la ficha.

    Tres formas de escribir el mismo campo, y las tres valen: el encabezado con
    punto (**Problema.** la pregunta), la entrada de lista con dos puntos
    (**Problema:** la pregunta), y la fila de tabla (| **Problema** | la pregunta |).
    Lo que sigue al campo se lee atravesando el cierre en negrita.
    """
    salida = {}
    # encabezado: **Campo.** contenido
    for m in re.finditer(r"\*\*([^*\n]{2,30}?)\.\*\*\s*(?:\*\*)?\s*([^\n]+)", texto):
        salida.setdefault(sin_tildes(m.group(1)), m.group(2).strip())
    # lista: **Campo:** contenido, con el cierre en negrita atravesado
    for m in re.finditer(r"^[\s\-*+>]*\*\*([^*\n]{2,30})[:.]?\*\*:?\s*([^\n]+)", texto, re.M):
        salida.setdefault(sin_tildes(m.group(1).rstrip(":.")), m.group(2).strip())
    # tabla: | **Campo** | contenido |
    for m in re.finditer(r"^\s*\|\s*\**([^*|\n]{2,30}?)\**\s*\|\s*([^|\n]+?)\s*\|", texto, re.M):
        salida.setdefault(sin_tildes(m.group(1)), m.group(2).strip())
    return salida


def esta_declarado(clave, texto, campos):
    """Dice si la fuente trae el campo, no si menciona la palabra.

    Vale el campo como encabezado (**Problema.** ...), como entrada de lista
    (**Problema:** ...), como fila que empieza con su nombre (| **Problema** | ...)
    y como marca en linea (**aunque** X, **sostiene** Y, **porque** Z), que es la
    forma en que se dicen las tres piezas de una tesis teorica.
    No vale que la palabra aparezca suelta: eso daba por buena una tesis que
    solo la nombraba.
    """
    if sin_tildes(clave) in campos:
        return True
    for pref in PREFIJO_TABLA.get(clave, (clave,)):
        p = sin_tildes(pref)
        if re.search(r"\*\*" + re.escape(p) + r"\*\*\s*[:\u2014]?", sin_tildes(texto)):
            return True
    for linea in texto.splitlines():
        resto = linea.strip().lstrip("-*+> ").strip()
        celdas = []
        if resto.startswith("|"):
            celdas = [c.strip().strip("*").strip() for c in resto.strip("|").split("|")]
        else:
            m = re.match(r"\*\*([^*]+?)\.?\*\*", resto)
            if m:
                celdas = [m.group(1).strip()]
        if not celdas:
            continue
        primera = sin_tildes(celdas[0])
        for pref in PREFIJO_TABLA.get(clave, (clave,)):
            p = sin_tildes(pref)
            if (primera == p or primera.startswith(p + " ")
                    or primera.startswith(p + ":") or primera.startswith(p + ".")):
                return True
    return False


def main():
    tipo = None
    fuente = None
    salida = None
    for i, a in enumerate(sys.argv):
        if a == "--tipo" and i + 1 < len(sys.argv):
            tipo = sys.argv[i + 1].lower()
        if a == "--fuente" and i + 1 < len(sys.argv):
            fuente = sys.argv[i + 1]
        if a == "--salida" and i + 1 < len(sys.argv):
            salida = sys.argv[i + 1]

    if not tipo or tipo not in PORTADAS:
        print("Falta el tipo. Uso: --tipo teoria|coro|mesa")
        return 2
    if not fuente or not os.path.isfile(fuente):
        print("[SIN FUENTE] no existe el archivo de la tesis.")
        return 2

    texto = leer_fuente(fuente)
    campos = bloques(texto)

    faltan = [legible for clave, legible in EXIGE[tipo] if not esta_declarado(clave, texto, campos)]
    if faltan:
        print("[SIN TESIS - ES UN TEMA] a la fuente de tipo {} le falta: {}".format(tipo, ", ".join(faltan)))
        print("No se compone: un documento que finge tener lo que no tiene se lee y se cae solo.")
        return 1

    titulo = campos.get("nombre") or campos.get("posicion") or os.path.splitext(os.path.basename(fuente))[0]

    doc = []
    doc.append(r"\documentclass[12pt,letterpaper]{article}")
    doc.append(r"\usepackage[T1]{fontenc}")
    doc.append(r"\usepackage[utf8]{inputenc}")
    doc.append(r"\usepackage{lmodern}")
    doc.append(r"\usepackage{geometry}")
    doc.append(r"\geometry{margin=2.5cm}")
    doc.append(r"\title{" + esc(titulo) + r"}")
    doc.append(r"\author{Man-Made Empathy}")
    doc.append(r"\date{" + datetime.now(timezone.utc).strftime("%Y-%m-%d") + "}")
    doc.append(r"\begin{document}")
    doc.append(r"\maketitle")
    doc.append(r"\begin{center}")
    doc.append(r"\textbf{" + esc(PORTADAS[tipo]) + r"}")
    doc.append(r"\end{center}")
    doc.append(r"\vspace{0.5cm}")

    if tipo == "teoria":
        doc.append(r"\section{El problema conceptual}")
        doc.append(esc(campos.get("posicion", "")) + r"\par")
        doc.append(r"\section{El argumento}")
        doc.append(esc(campos.get("porque", "")) + r"\par")
        doc.append(r"\section{Lo que no afirma}")
        doc.append(esc(campos.get("límite", campos.get("limite", "Lo que la fuente no declara."))) + r"\par")
    elif tipo == "coro":
        for seccion, clave in (("Introduccion", "problema"),
                               ("Metodos", "metodo"),
                               ("Resultados", "resultado"),
                               ("Discusion", "queda")):
            doc.append(r"\section{" + seccion + "}")
            doc.append(esc(campos.get(clave) or VACIO) + r"\par")
    else:
        for seccion, clave in (("Problema", "problema"),
                               ("Procedimiento", "procedimiento"),
                               ("Numeros", "numero"),
                               ("Lo que queda", "queda")):
            doc.append(r"\section{" + seccion + "}")
            doc.append(esc(campos.get(clave) or VACIO) + r"\par")

    doc.append(r"\section*{Atribucion}")
    doc.append(esc("Origen: ver ATTRIBUTION.md y FUENTES.md en la raiz. "
                   "La obra ajena se cita y no se reproduce."))
    doc.append(r"\end{document}")

    destino = salida or os.path.dirname(os.path.abspath(fuente))
    os.makedirs(destino, exist_ok=True)
    base = os.path.splitext(os.path.basename(fuente))[0]
    base = re.sub(r"[^A-Za-z0-9 _-]", "", base)[:60].strip() or "tesis"
    tex = os.path.join(destino, base + ".tex")
    with open(tex, "w", encoding="utf-8") as fh:
        fh.write("\n".join(doc) + "\n")
    print("tex: {}".format(tex))

    tectonic = buscar_tectonic()
    if not tectonic:
        print("[SIN COMPILADOR] se dejo el .tex. No se finge un PDF.")
        return 2

    outdir = os.path.join(tempfile.gettempdir(), "mantis-componer")
    os.makedirs(outdir, exist_ok=True)
    env = dict(os.environ)
    env["TECTONIC_CACHE_DIR"] = os.path.join(tempfile.gettempdir(), "tectonic-cache-mantis")
    r = subprocess.run([tectonic, "-X", "compile", tex, "--outdir", outdir],
                       capture_output=True, text=True, timeout=600, env=env)
    ok = r.returncode == 0
    pdf = os.path.join(outdir, base + ".pdf")
    if os.path.isfile(pdf):
        shutil.copyfile(pdf, os.path.join(destino, base + ".pdf"))
    pes = os.path.getsize(os.path.join(destino, base + ".pdf")) if os.path.isfile(os.path.join(destino, base + ".pdf")) else 0
    print("compilo: {}".format("si" if ok else "no"))
    print("pdf: {} ({} bytes)".format(os.path.join(destino, base + ".pdf"), pes))
    if not ok:
        print((r.stdout or "")[-800:])
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
