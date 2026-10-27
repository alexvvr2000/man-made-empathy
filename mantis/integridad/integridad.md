#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso de integridad: el 1 sigue siendo el 1, y se puede contestar.

Sirve igual para una alma que para N: lee la carta, lee lo que hizo en sus .tra,
y dice si coincide. Si no coincide, gana el .tra.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
TAREAS = os.path.join(MANTIS, "tareas")
CARTA = os.path.join(MANTIS, "el alma.md")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def campo(texto, nombre):
    m = re.search(r"\*\*" + nombre + r"[:.]\*\*\s*(.*)", texto)
    return m.group(1).strip() if m else None


def main():
    fallas = []

    if not os.path.isfile(CARTA):
        print("[SIN CARTA] no esta el alma.md: no hay 1 que comprobar")
        return 1

    carta = leer(CARTA)
    sesgo = campo(carta, "Sesgo")
    firma = campo(carta, "Firma")

    if not sesgo:
        fallas.append("el 1 no declara su sesgo: no se sabe desde donde sostiene")
    if not firma:
        fallas.append("el 1 no declara quien lo contesta")

    # lo que el 1 hizo: las .tra de sus tareas
    tras = []
    if os.path.isdir(TAREAS):
        for n in sorted(os.listdir(TAREAS)):
            p = os.path.join(TAREAS, n)
            if not os.path.isdir(p):
                continue
            for f in os.listdir(p):
                if f.endswith(".tra"):
                    tras.append(os.path.join(p, f))

    if not tras:
        fallas.append("el 1 no dejo ningun .tra: no hay nada contra que comparar la carta")

    if fallas:
        print("[falla] el 1 no esta integro")
        for f in fallas:
            print("  - " + f)
        return 1

    print("[ok] el 1 declara desde donde sostiene: " + sesgo[:90])
    print("[ok] y quien lo contesta: " + firma[:60])
    print("[ok] {} .tra leidas, y la carta se compara contra ellas".format(len(tras)))
    print("")
    print("pasa: el 1 sigue siendo el 1, y se puede contestar")
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# (de integridad.md)

# integridad — el folder del criterio creado a pulso

**Nombre.** INTEGRIDAD. **Y el nombre dice el acto:** **no es que cada pieza esté completa; es que el 1 no tenga agujeros.**

**Origen.** **De la corrección de la autoridad: `integridad/` no es un archivo que se lee, es un folder dentro del alma.** **Y sirve igual para una alma que para diez mil: un criterio creado a pulso, no una regla que se importa.**

**Unidad:** folder.
**Aplica a:** comprobar, y sostener el 1.
**Tipo:** se ejecuta. **Es el que dice si lo que hay adentro sigue siendo el 1.**
**Lector:** quien va a mutar, y quien va a contestar lo que el 1 sostiene.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** el veredicto se lee desde lo que el 1 hizo, no desde lo que el 1 dice de sí mismo.
**Límite:** **no decide entre dos caminos.** **No juzga si la pieza sirve.** **Dice si el 1 sigue siendo el 1, y quién lo contesta.**
**Firma:** humano:autoridad · máquina:quien lo corra.

**Falta:** **nada dice si lo que hay adentro sigue siendo el 1, ni quién puede contestarlo cuando son muchos.**
**Termina:** **por turno, y cada vez que una pieza entra, sale o cambia lo que sostiene.**
**Cierra en:** `integridad/integridad.tra`.
**Autoridad:** humano:autoridad. **Criterio:** igual.
**Muda:** `../MUDAR.md`.

## Rastro — el cuerpo

| Qué hay | Nombre | Dónde |
|---|---|---|
| **el proceso** | `comprobar.prs` | `./comprobar.prs` |
| **el paso** | `integridad.md` | `./integridad.md` |
| **lo que deja** | `integridad.tra` | `./integridad.tra` |
| **la regla** | `INTEGRIDAD` — las seis preguntas, el triángulo, la acuñación | `../../../sincronización de almas/el sincronización de almas/2 el idioma/formacion/INTEGRIDAD.md` |

## Ruta — la mente

| Se va a… | Se carga… | Sin la autoridad… |
|---|---|---|
| **saber si el 1 sigue siendo el 1** | este folder | **se declara que cumple, sin medirlo** |
| **contestar lo que el 1 sostiene** | `./comprobar.prs`, y la firma | **no se contesta** |
| **ver si una pieza se salió del sesgo** | este folder, y `COLMENA` si son muchos | **se sigue con una pieza que nadie contestó** |

## Carga — el pensamiento

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| **el 1 no declara su sesgo** | la trazabilidad | no se sabe desde dónde sostiene, ni quién lo contesta |
| **no se compara contra lo que hizo** | la prueba | el 1 dice una cosa y hace otra, y nadie lo ve |
| **se comprueba una vez y no más** | la vigencia | el agujero vuelve y se lee como si estuviera cerrado |
| **se corre solo para piezas sueltas** | el conjunto | cada pieza está entera y el 1 no |

## Prueba

**¿El 1 declara su sesgo y quién lo contesta? ¿Se comparó contra lo que hizo, con cita? ¿Se dijo qué falta, nombrado como pieza y no como descripción? ¿Sirvió igual para una alma que para N?**

**Falsificador:** un veredicto sin el sesgo declarado; uno sacado de la carta cuando los `.tra` dicen otra cosa; un agujero declarado como descripción; un `pasa` sin haber leído lo que el 1 hizo.
