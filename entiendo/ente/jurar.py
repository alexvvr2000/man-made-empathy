#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""jurar — una negativa en una pregunta que se puede contestar.

Entra lo que el ejecutor nego, y sale el juramento en tres lineas: el acto
que no se hizo, lo que falta, y a quien se espera. Sin la tercera, no es un
freno: es una parada con mejor letra.

Y no se le cree: se le comprueba.
    1. el juramento tiene sus tres lineas
    2. dice que acto no hizo
    3. dice que le falta
    4. dice a quien espera, y eso se puede contestar

Uso:
    python jurar.py                 los juramentos que hay en memoria/negativa.jsonl
    python jurar.py --entra "<x>"   jura sobre lo que se le pasa
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
# el motor puede vivir dentro de su tarea: se sube hasta tareas/, y el ente esta arriba
_raiz = AQUI
while os.path.basename(_raiz) != "tareas" and os.path.dirname(_raiz) != _raiz:
    _raiz = os.path.dirname(_raiz)
ENTE = os.path.dirname(_raiz) if os.path.basename(_raiz) == "tareas" else AQUI
MEMORIA = os.path.join(ENTE, "memoria")
NEGATIVA = os.path.join(MEMORIA, "negativa.jsonl")
JURAMENTO = os.path.join(MEMORIA, "juramento.jsonl")

ESPERO = {
    "SIN ENSAYO": "que la tarea declare su modo, o que la autoridad diga qué es",
    "SIN CORTE": "que la tarea se escriba con sus cuatro campos",
    "FALTA EN bin/": "que el mundo ponga con qué, o que la tarea traiga su paso.*",
    "FALTA EN EL PISO": "que el mundo declare esa capacidad, y pase su prueba",
    "IGUAL": "un cambio en el corte, o que se pida --sin-tra a sabiendas",
}

FALTA = {
    "SIN ENSAYO": "que la tarea declare su modo: si toca, o si solo lee. Y qué pasa si lo toca.",
    "SIN CORTE": "los cuatro campos del corte: qué entra, qué la deja mal, qué sale, quién lo usa.",
    "FALTA EN bin/": "con qué cumplir el corte: un paso.* en la tarea, o lo que el mundo declare.",
    "FALTA EN EL PISO": "que el mundo declare la capacidad que el corte pide.",
    "IGUAL": "que el corte cambie, o que se pida --sin-tra a propósito.",
}

QUE_NO_SE = {
    "SIN ENSAYO": "no sé qué es lo que voy a tocar.",
    "SIN CORTE": "no sé qué la tarea hace: su corte está incompleto.",
    "FALTA EN bin/": "sé qué es, y con qué no.",
    "FALTA EN EL PISO": "sé qué es, y este mundo no lo puede.",
    "IGUAL": "sé qué es, y ya lo hice.",
}


def leer(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def jurar(tarea, motivo, porque=""):
    """Las tres lineas, y nada mas. Lo que no esta en el diccionario, se dice que no se sabe."""
    return {
        "tarea": tarea,
        "juro": QUE_NO_SE.get(motivo, "no sé qué es lo que voy a tocar."),
        "me_falta": FALTA.get(motivo, "decir qué falta, y no lo sé: se declara"),
        "y_espero": ESPERO.get(motivo, "que la autoridad diga qué falta"),
        "motivo": motivo,
        "porque": porque[:200],
    }


def comprobar(j):
    """Un juramento se comprueba, no se cree. Cuatro cosas, y las cuatro se pueden leer."""
    fallas = []
    if not j.get("juro") or "no sé" not in j["juro"].lower() and "sé" not in j["juro"].lower():
        fallas.append("no dice qué acto no hizo, o qué no sabe")
    if not j.get("me_falta") or not j["me_falta"].strip():
        fallas.append("no dice qué le falta")
    if not j.get("y_espero") or not j["y_espero"].strip():
        fallas.append("no dice a quién espera: es una parada, no un freno")
    if j.get("me_falta") == j.get("y_espero"):
        fallas.append("lo que falta y lo que espera son lo mismo: no hay con quién hablar")
    return fallas


def main(argv):
    if "--entra" in argv:
        i = argv.index("--entra")
        if i + 1 >= len(argv):
            print("[FALTA] --entra quiere lo que se le pasa")
            return 1
        entra = argv[i + 1]
        print("[jurar] entra: " + entra[:100])
        print("")
        print("Juro:     no sé qué es lo que me piden, y no lo toco hasta saberlo.")
        print("Me falta: que la autoridad diga qué es, y qué pasa si lo toco.")
        print("Y espero: la autoridad.")
        return 0

    if not os.path.isfile(NEGATIVA):
        print("[SIN NEGATIVA] no hay negativas que jurar: el ente no frenó ninguna vez")
        return 0

    vistos = 0
    fallas = 0
    juramentos = []
    for linea in leer(NEGATIVA).splitlines():
        linea = linea.strip()
        if not linea:
            continue
        try:
            r = json.loads(linea)
        except Exception:
            continue
        vistos += 1
        # el juramento no se inventa por el que no juro: si la negativa no dice
        # lo que le falta, el que jura no estaba completo, y se nombra
        if not str(r.get("me_falta") or "").strip():
            fallas += 1
            print("[NO JURA] {:<22} la negativa no dijo qué le falta: no se jura por otro".format(
                r.get("tarea", "?")))
            continue
        j = jurar(r.get("tarea", "?"), r.get("motivo", "?"), r.get("porque", ""))
        j["me_falta"] = r["me_falta"]
        mal = comprobar(j)
        if mal:
            fallas += 1
            print("[NO JURA] {:<22} {}".format(j["tarea"], "; ".join(mal)))
        else:
            print("[jura]    {:<22} {}".format(j["tarea"], j["motivo"]))
            print("          juro:     " + j["juro"])
            print("          me falta: " + j["me_falta"])
            print("          y espero: " + j["y_espero"])
        juramentos.append(j)

    if juramentos:
        with io.open(JURAMENTO, "w", encoding="utf-8", newline="") as fh:
            for j in juramentos:
                fh.write(json.dumps(j, ensure_ascii=False, sort_keys=True) + "\n")

    print("")
    juran = sum(1 for j in juramentos if not comprobar(j))
    print("[ok] {} negativas leidas, {} juran, {} no".format(vistos, juran, vistos - juran))
    if fallas:
        print("falla: {} negativa(s) que no dijeron a quién esperan".format(fallas))
        return 1
    print("pasa: cada negativa es una pregunta, y cada pregunta dice a quién se le hace")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
