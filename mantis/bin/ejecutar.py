#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bin/ - lo que ESTE mundo ya tiene para correr un .prs.

No es el estandar: es lo concreto. Python esta aqui porque esta maquina lo tiene.
Un mundo que tenga otra cosa pone la suya en su bin/, y declara cual en su RUTA.pr.

No sabe que hace ningun proceso: lee sus cuatro campos, y lo corre.

Uso:
    python mantis/bin/ejecutar.py --verificar      todos los folders tienen su corte
    python mantis/bin/ejecutar.py --listar         que tareas hay
    python mantis/bin/ejecutar.py <tarea>          corre una tarea
    python mantis/bin/ejecutar.py el estándar      lee el estandar antes de nada

Sale 0 si pasa, 1 si falla, 2 si el folder no tiene corte.
"""
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, ".."))
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
TAREAS = os.path.join(MANTIS, "tareas")
SUELTOS = ("tareas", "integridad")

CAMPOS = ("Entra:", "Falla si:", "Sale:", "Consume:")


def leer(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def cortes(texto):
    fuera = {}
    for c in CAMPOS:
        m = re.search(r"[-*]\s*\*\*" + re.escape(c) + r"\*\*\s*(.*)", texto)
        if m:
            fuera[c] = m.group(1).strip()
    return fuera


def procesos_de(carpeta):
    return sorted(f for f in os.listdir(carpeta) if f.endswith(".prs"))


def verificar(carpeta):
    if not os.path.isdir(carpeta):
        return False, "no existe"
    ps = procesos_de(carpeta)
    if not ps:
        return False, "no hay .prs"
    problemas = []
    for p in ps:
        c = cortes(leer(os.path.join(carpeta, p)))
        falta = [k for k in CAMPOS if k not in c]
        if falta:
            problemas.append("{}: le falta {}".format(p, ", ".join(falta)))
    if problemas:
        return False, "; ".join(problemas)
    return True, "{} proceso(s) con su corte".format(len(ps))


def dejartra(carpeta, proceso, entro, salio, veredicto):
    nombre = os.path.basename(os.path.abspath(carpeta))
    p = os.path.join(carpeta, nombre + ".tra")
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    cuerpo = (
        "# {n}.tra — lo que pasó\n\n"
        "**Nombre:** {n}\n"
        "**Expande:** {proc}\n"
        "**Se nombró:** {ahora}\n"
        "**Reemplaza:** NINGUNO\n"
        "**Miente si:** se dice que corrió y no hay recibo\n\n"
        "## Qué pasó\n\n"
        "**Qué pasó:** {e}\n"
        "**Contra:** {s}\n"
        "**Huella:** esta .tra\n"
        "**Distancia:** {v}\n"
    ).format(n=nombre, proc=proceso, ahora=ahora, e=entro, s=salio, v=veredicto)
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(cuerpo)
    return p


# La implementacion NO vive en la tarea: vive en el mundo.
# La tarea declara el corte; este mundo pone con que, y lo pone aqui, en bin/.
IMPLEMENTACIONES = {
    "el cero": "cero.py",
    "los candados": "candados.py",
    "la tesis": "tesis.py",
    "la memoria": "memoria.py",
    "el estándar": "estandar.py",
    "integridad": "integridad.py",
    "tareas": "tareas.py",
}


def correr_paso(carpeta):
    nombre = os.path.basename(os.path.abspath(carpeta))
    impl = IMPLEMENTACIONES.get(nombre)
    if impl is None:
        return "[SIN IMPLEMENTACION] la tarea declara su corte, y este mundo no tiene con que cumplirlo", 2
    ruta = os.path.join(AQUI, impl)
    if not os.path.isfile(ruta):
        return "[FALTA EN bin/] {} declara {}, y no esta".format(nombre, impl), 2
    r = subprocess.run([sys.executable, ruta], capture_output=True, text=True, encoding="utf-8", errors="replace")
    salida = ((r.stdout or "") + (r.stderr or "")).strip()
    return salida, r.returncode


def carpeta_de(nombre):
    if nombre in SUELTOS:
        return os.path.join(MANTIS, nombre)
    return os.path.join(TAREAS, nombre)


def main(argv):
    if len(argv) < 2:
        print("uso: ejecutar.py --verificar | --listar | <tarea>")
        return 1

    if argv[1] == "--verificar":
        malos = 0
        vistos = []
        for base in (TAREAS, MANTIS):
            if not os.path.isdir(base):
                continue
            for n in sorted(os.listdir(base)):
                c = os.path.join(base, n)
                if not os.path.isdir(c) or not procesos_de(c):
                    continue
                if base == MANTIS and n not in SUELTOS:
                    continue
                vistos.append(n)
                ok, msg = verificar(c)
                print(("[ok]    " if ok else "[falla] ") + n + ": " + msg)
                malos += 0 if ok else 1
        print("")
        if malos:
            print("falla: {} folder(s) sin corte".format(malos))
            return 1
        print("pasa: {} folders con su corte".format(len(vistos)))
        return 0

    if argv[1] == "--listar":
        for n in sorted(os.listdir(TAREAS)):
            if os.path.isdir(os.path.join(TAREAS, n)):
                print(n)
        return 0

    carpeta = carpeta_de(argv[1])
    ok, msg = verificar(carpeta)
    if not ok:
        print("[ACTIVIDAD - SIN CORTE] " + msg)
        return 2

    proceso = procesos_de(carpeta)[0]
    c = cortes(leer(os.path.join(carpeta, proceso)))
    print("[{}] {}".format(os.path.basename(carpeta), proceso))
    for k in CAMPOS:
        print("  {} {}".format(k, c[k]))

    salida, codigo = correr_paso(carpeta)
    print("")
    print(salida)

    if "--sin-tra" not in argv:
        tra = dejartra(carpeta, proceso, c["Entra:"], salida[:400], "codigo " + str(codigo))
        print("")
        print("deja: " + os.path.relpath(tra, MANTIS))
    return codigo


if __name__ == "__main__":
    sys.exit(main(sys.argv))
