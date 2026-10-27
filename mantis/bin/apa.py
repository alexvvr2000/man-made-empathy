#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apa — pasa las 63 obras de FUENTES.md a una lista de referencias en APA 7.

Lo que hace: toma el campo de autoría, que ya esta escrito a mano, y lo
parte en los pedazos que APA 7 pide. No inventa autores, ni anos, ni
productoras: lo que no se puede partir se queda como esta, y se marca.

El molde lo da el tipo de obra, y son los de Purdue OWL
(owl.purdue.edu, Reference List: Audiovisual Media):

    Film        Director, D. D. (Director). (Ano). Titulo [Film]. Productora.
    TV series   Productor, P. P. (Productor ejecutivo). (Anos). Titulo [TV series]. Productora.
    Episode     Guionista, G. (Guionista), & Director, D. D. (Director). (Fecha).
                Titulo (Temporada, Episodio) [TV series episode]. En Serie. Productora.
    Comic/libro Autor, A. A. (Ano). Titulo. Editorial.
    Videojuego  Compania. (Ano). Titulo [Video game]. Compania.

Y la regla que no cambia: se cita para analizar. Titulo, autoria, ano, y
nada que se reproduzca.

Uso:
    python apa.py            ensena como quedaria, sin escribir
    python apa.py --escribir reescribe FUENTES.md con la lista en APA 7
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
ORIGEN = os.path.join(REPO, "FUENTES.md")

# el tipo de obra, por como esta escrito su nombre o su autoria
FICHA = [
    (r"\bFilm\b|\bpel[ií]cula\b", "film"),
    (r"serie|TV series|temporada", "serie"),
    (r"episodio|Episode", "episodio"),
    (r"Video game|videojuego|Games|Squaresoft|Game Freak", "juego"),
    (r"Comics|Marvel|DC|Shueisha|Kodansha|Shogakukan|Square Enix|Dupuis", "comic"),
]


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def limpia(s):
    return re.sub(r"\*{1,3}", "", s).strip()


def anio_de(autoria):
    """El primer ano de cuatro cifras que aparezca en la autoria."""
    m = re.search(r"\b(1[89]\d{2}|20\d{2})\b", autoria)
    return m.group(1) if m else ""


def anios_de(autoria):
    """Los anos, y el rango si son dos con guion: 2005-2008."""
    m = re.search(r"\b((?:1[89]\d{2}|20\d{2}))\s*[-–]\s*((?:1[89]\d{2}|20\d{2}))", autoria)
    if m:
        return m.group(1) + "-" + m.group(2)
    return anio_de(autoria)


def tipo_de(obra, autoria, donde):
    texto = " ".join((obra, autoria, donde)).lower()
    if re.search(r"video game|videojuego|squaresoft|rockstar|toby fox", texto):
        return "juego"
    if re.search(r"episodio|episode|temporada \d", texto):
        return "episodio"
    if re.search(r"\bserie\b|tv series|temporada", texto):
        return "serie"
    if re.search(r"pel[ií]cula|director|directora|\bfilm\b", texto):
        return "film"
    return "comic"


def autores_apa(texto):
    """'Stan Lee, Larry Lieber y Jack Kirby' -> 'Lee, S., Lieber, L., & Kirby, J.'"""
    s = limpia(texto)
    # lo que sigue al primer ';' es editorial, no autor
    partes = [x.strip() for x in re.split(r";", s) if x.strip()]
    if not partes:
        return "", s
    nombres = [x.strip() for x in re.split(r",|\by\b|\band\b|&", partes[0]) if x.strip()]
    fuera = []
    for n in nombres:
        pal = n.split()
        if len(pal) < 2:
            continue
        apellido = " ".join(pal[:-1])
        inicial = pal[-1][0].upper()
        fuera.append("{}, {}.".format(apellido, inicial))
    if not fuera:
        return "", s
    if len(fuera) == 1:
        return fuera[0], s
    if len(fuera) == 2:
        return fuera[0] + ", & " + fuera[1], s
    return ", ".join(fuera[:-1]) + ", & " + fuera[-1], s


def referencia(obra, autoria, donde):
    """La entrada en APA 7, con el molde que le toca."""
    titulo = limpia(obra)
    # si la obra trae personaje, se queda aparte
    personaje = ""
    if "—" in titulo:
        titulo, personaje = [x.strip() for x in titulo.split("—", 1)]

    tipo = tipo_de(obra, autoria, donde)
    autores, resto = autores_apa(autoria)
    ano = anios_de(autoria)
    if not ano:
        ano = "s.f."

    # la editorial: lo que sigue al primer ';', o lo que queda
    editorial = ""
    partes = [x.strip() for x in autoria.split(";") if x.strip()]
    if len(partes) > 1:
        editorial = limpia(partes[1].split(",")[0])

    if tipo == "juego":
        quien = limpia(partes[0]) if partes else titulo
        return "{}. ({}, {}). *{}* [Video game]. {}.".format(
            quien, "recurso" if not ano else "recurso", ano, titulo, editorial or quien)
    if tipo == "film":
        if autores:
            return "{} (Director). ({}, {}). *{}* [Film]. {}.".format(
                autores, "recurso", ano, titulo, editorial)
        return "*{}* [Film]. ({}, {}). {}.".format(titulo, "recurso", ano, editorial)
    if tipo == "serie":
        if autores:
            return "{} (Productor ejecutivo). ({}, {}). *{}* [TV series]. {}.".format(
                autores, "recurso", ano, titulo, editorial)
        return "*{}* [TV series]. ({}, {}). {}.".format(titulo, "recurso", ano, editorial)
    if tipo == "episodio":
        return "*{}* [Episode]. ({}, {}). {}.".format(titulo, "recurso", ano, editorial)
    # comic, libro, y lo demás
    if autores:
        return "{}. ({}). *{}*.{}.".format(autores, ano, titulo,
                                           (" " + editorial) if editorial else "")
    return "*{}*. {}. ({}).".format(titulo, editorial, ano)


def filas_de_fuentes(texto):
    lineas = texto.split("\n")
    if "## 2. Las obras que se citan" not in lineas:
        return []
    i = lineas.index("## 2. Las obras que se citan")
    j = len(lineas)
    for k in range(i + 1, len(lineas)):
        if lineas[k].startswith("## "):
            j = k
            break
    fuera = []
    for l in lineas[i + 1:j]:
        if l.startswith("|") and not l.startswith("|---"):
            c = [x.strip() for x in l.strip("|").split("|")]
            if len(c) == 4 and c[0] != "Obra":
                fuera.append(c)
    return fuera


def main(argv):
    if not os.path.isfile(ORIGEN):
        print("[SIN FUENTES] no esta " + ORIGEN)
        return 1
    texto = leer(ORIGEN)
    filas = filas_de_fuentes(texto)
    if not filas:
        print("[SIN FILAS] no encontre la tabla de obras")
        return 1

    refs = []
    for f in filas:
        r = referencia(f[0], f[1], f[2])
        refs.append((limpia(f[0]), r, f[2], f[3]))

    # APA pide orden alfabetico
    refs.sort(key=lambda x: x[0].lower())

    print("[apa] {} obras".format(len(refs)))
    print("")
    for titulo, r, donde, toma in refs[:10]:
        print("  " + r)
    print("")
    print("  ... y {} mas".format(max(0, len(refs) - 10)))

    if "--escribir" not in argv:
        print("")
        print("para reescribir FUENTES.md:  python mantis/bin/apa.py --escribir")
        return 0

    # se reescribe la seccion 2, y se conserva el resto
    lineas = texto.split("\n")
    i = lineas.index("## 2. Las obras que se citan")
    j = len(lineas)
    for k in range(i + 1, len(lineas)):
        if lineas[k].startswith("## "):
            j = k
            break

    bloque = ["## 2. Las obras que se citan", ""]
    bloque.append("**Formato: APA 7, lista de referencias.** **Se cita para analizar: título, autoría y año.**")
    bloque.append("**No se reproduce nada: ni imágenes, ni escenas, ni logos.**")
    bloque.append("")
    bloque.append("**Y cómo se usó cada una, y qué provocó, vive en [`./contexto/`](./contexto/): ese archivo es del autor, y no lleva formato.**")
    bloque.append("")
    bloque.append("| Obra | Referencia (APA 7) | Dónde se cita | Qué se toma de ella |")
    bloque.append("|---|---|---|---|")
    for titulo, r, donde, toma in refs:
        bloque.append("| **{}** | {} | {} | {} |".format(titulo, r.replace("|", "/"), donde, toma))

    nuevo = lineas[:i] + bloque + lineas[j:]
    with io.open(ORIGEN, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(nuevo))
    print("")
    print("[apa] FUENTES.md reescrito, en el orden alfabetico de APA 7")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
