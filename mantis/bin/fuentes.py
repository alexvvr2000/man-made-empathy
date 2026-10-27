#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fuentes — parte FUENTES.md en una carpeta por obra, y lo deja mutable.

FUENTES.md es una tabla: una fila por obra. Y esa tabla es lo que no se
deja tocar: agregar un ejemplo de una obra obliga a buscar su fila y
reescribirla, y ahi se pierden cosas.

Lo que la vuelve mutable es partirla: una carpeta `contexto/`, un archivo
por obra, y adentro sus puntos, cada uno con su momento y lo que se tomo
de el. Agregar un punto es una linea nueva, no una fila reescrita.

Lo que este script NO hace: borrar FUENTES.md, ni inventar filas, ni
corregir texto. La tabla se conserva entera en `fuentes/_la tabla.md`
durante la transicion, y lo que sale es una copia fiel.

Uso:
    python fuentes.py              dice que saldria, sin escribir
    python fuentes.py --partir     escribe fuentes/ con una carpeta por obra
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
ORIGEN = os.path.join(REPO, "FUENTES.md")
DESTINO = os.path.join(REPO, "fuentes")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def slug(s):
    s = s.lower()
    s = re.sub(r"[áàäâ]", "a", s)
    s = re.sub(r"[éèëê]", "e", s)
    s = re.sub(r"[íìïî]", "i", s)
    s = re.sub(r"[óòöô]", "o", s)
    s = re.sub(r"[úùüû]", "u", s)
    s = re.sub(r"[ñ]", "n", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:60]


def limpia(s):
    """El texto de un campo, sin el markdown de los asteriscos."""
    s = s.strip()
    s = re.sub(r"\*{1,3}", "", s)
    return s.strip()


def obra_de(primera):
    """De '***Obra*** — **Personaje**' saca la obra, y el personaje si lo hay."""
    m = re.match(r"\s*\*{2,3}(.+?)\*{2,3}\s*(?:—\s*\*{2}(.+?)\*{2})?", primera)
    if m:
        return m.group(1).strip(), (m.group(2) or "").strip()
    return limpia(primera), ""


def seccion(lineas, titulo):
    if titulo not in lineas:
        return []
    i = lineas.index(titulo)
    j = len(lineas)
    for k in range(i + 1, len(lineas)):
        if lineas[k].startswith("## "):
            j = k
            break
    return lineas[i + 1:j]


def filas_de(bloque):
    fuera = []
    for l in bloque:
        if l.startswith("|") and not l.startswith("|---"):
            cols = [c.strip() for c in l.strip("|").split("|")]
            if len(cols) == 4 and cols[0] != "Obra":
                fuera.append(cols)
    return fuera


def main(argv):
    if not os.path.isfile(ORIGEN):
        print("[SIN FUENTES] no esta " + ORIGEN)
        return 1

    t = leer(ORIGEN)
    lineas = t.split("\n")
    obras = filas_de(seccion(lineas, "## 2. Las obras que se citan"))

    agrupadas = {}
    for f in obras:
        obra, personaje = obra_de(f[0])
        agrupadas.setdefault(obra, []).append({"personaje": personaje, "cols": f})

    print("[fuentes] {} filas en FUENTES.md".format(len(obras)))
    print("[fuentes] {} obras distintas".format(len(agrupadas)))
    print("")
    for o, fs in sorted(agrupadas.items(), key=lambda x: -len(x[1]))[:12]:
        print("  {:<40} {} punto(s)".format(o[:40], len(fs)))

    multi = {o: fs for o, fs in agrupadas.items() if len(fs) > 1}
    if multi:
        print("")
        print("[fuentes] {} obra(s) con mas de un punto, y esas son las que se pierden hoy:".format(len(multi)))
        for o, fs in multi.items():
            print("  " + o + ": " + ", ".join(p["personaje"] or "(sin personaje)" for p in fs))

    if "--partir" not in argv:
        print("")
        print("para escribir las carpetas:  python mantis/bin/fuentes.py --partir")
        return 0

    os.makedirs(DESTINO, exist_ok=True)
    # la tabla original se conserva entera mientras dura la transicion
    with open(os.path.join(DESTINO, "_la tabla.md"), "w", encoding="utf-8", newline="") as fh:
        fh.write(t)

    escritas = 0
    for o, fs in agrupadas.items():
        carpeta = os.path.join(DESTINO, slug(o))
        os.makedirs(carpeta, exist_ok=True)
        l = ["# " + o, ""]
        l.append("**Lo que se guarda aquí es lo que esta obra provoca, y no lo que la obra es.**")
        l.append("")
        l.append("Cada punto dice **dónde pasa** y **qué se toma de él**. Si mañana entra otro punto,")
        l.append("se agrega una línea. No se reescribe la obra: se le suma.")
        l.append("")
        for p in fs:
            cols = p["cols"]
            l.append("## " + (p["personaje"] if p["personaje"] else limpia(cols[0])))
            l.append("")
            l.append("- **Autoría:** " + cols[1])
            l.append("- **Dónde se cita:** " + cols[2])
            l.append("- **Qué se toma:** " + cols[3])
            l.append("")
        with open(os.path.join(carpeta, slug(o) + ".md"), "w", encoding="utf-8", newline="") as fh:
            fh.write("\n".join(l) + "\n")
        escritas += 1

    print("")
    print("[fuentes] {} carpetas escritas en fuentes/".format(escritas))
    print("[fuentes] y la tabla original, entera, en fuentes/_la tabla.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
