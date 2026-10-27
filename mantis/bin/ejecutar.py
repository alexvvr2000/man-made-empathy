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
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
# la raiz del ente es la carpeta del ejecutor. ENTE_PRUEBA permite correrlo contra un banco.
MANTIS = os.environ.get("ENTE_PRUEBA") or AQUI
REPO = os.environ.get("MANTIS_REPO") or os.path.abspath(os.path.join(MANTIS, ".."))
TAREAS = os.path.join(MANTIS, "tareas")
SUELTOS = ("tareas", "integridad")

CAMPOS = ("Entra:", "Falla si:", "Sale:", "Consume:")


def imports_hash(texto):
    import hashlib
    return {"hash": hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]}


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
    """El corte de una tarea vive en su .tra; el de un folder de proceso, en su .prs."""
    import glob
    ps = sorted(f for f in os.listdir(carpeta) if f.endswith(".prs"))
    if ps:
        return ps
    tras = sorted(x for x in glob.glob(os.path.join(carpeta, "*.tra"))
                  if os.path.basename(x) != "rastro.tra")
    return [os.path.basename(x) for x in tras]


def verificar(carpeta):
    if not os.path.isdir(carpeta):
        return False, "no existe"
    ps = procesos_de(carpeta)
    if not ps:
        return False, "no hay .prs"
    if ps[0].endswith(".tra") and not cortes(leer(os.path.join(carpeta, ps[0]))):
        return False, "el .tra existe y no declara el corte"
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
    p = os.path.join(carpeta, "rastro.tra")
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
    "privado": "privado.py",
    "stats": "stats.py",
    "basura": "basura.py",
}


def modo_de(c):
    """El modo lo declara la tarea en su Entra:. Si no lo dice, no lo tiene."""
    entra = (c.get("Entra:") or "").lower()
    if "solo-lectura" in entra:
        return "solo-lectura"
    if any(x in entra for x in ("escrib", "borra", "crea", "mueve", "toca")):
        return "escritura"
    return "ninguno"


def candidato(carpeta, nombre):
    """Donde esta con que: paso.* en la tarea, o el paso declarado del mundo."""
    import glob
    propio = sorted(glob.glob(os.path.join(carpeta, "paso.*")))
    if propio:
        return propio[0]
    impl = IMPLEMENTACIONES.get(nombre)
    if impl:
        ruta = os.path.join(AQUI, impl)
        return ruta if os.path.isfile(ruta) else None
    return None


def correr_paso(carpeta):
    nombre = os.path.basename(os.path.abspath(carpeta))
    ruta = candidato(carpeta, nombre)
    if ruta is None:
        return ("[FALTA EN bin/] esta tarea declara su corte, y este mundo no tiene con que cumplirlo.\n"
                "                 se busca: paso.* en la tarea, o el paso que el mundo declare."), 2
    ext = os.path.splitext(ruta)[1].lower()
    if ext == ".py":
        argv = [sys.executable, ruta]
    elif ext == ".ps1":
        argv = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ruta]
    else:
        argv = [ruta]
    r = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace")
    salida = ((r.stdout or "") + (r.stderr or "")).strip()
    return salida, r.returncode


FALTA_LO_QUE = {
    "SIN ENSAYO": "que la tarea declare su modo: si toca, o si solo lee. Y qué pasa si lo toca.",
    "SIN CORTE": "los cuatro campos del corte: qué entra, qué la deja mal, qué sale, quién lo usa.",
    "FALTA EN bin/": "con qué cumplir el corte: un paso.* en la tarea, o lo que el mundo declare.",
}


ESPERO_QUIEN = {
    "SIN ENSAYO": "que la tarea lo declare, o que la autoridad diga qué es",
    "SIN CORTE": "que la tarea se escriba con sus cuatro campos",
    "FALTA EN bin/": "que el mundo ponga con qué, o que la tarea traiga su paso.*",
}


def preguntar(motivo, que_no_se):
    """Las tres lineas de JURAR. No es parar: es frenar."""
    return ("[{m}] {q}\n"
            "             me falta: {f}\n"
            "             y espero: {e}").format(
                m=motivo, q=que_no_se, f=FALTA_LO_QUE.get(motivo, "decir qué falta"),
                e=ESPERO_QUIEN.get(motivo, "que alguien diga qué falta"))


def negarse(carpeta, motivo, porque):
    """La negativa se firma con hash: una negativa sin firma no se puede contestar."""
    import uuid
    texto = "{}|{}|{}".format(os.path.basename(carpeta), motivo, datetime.now(timezone.utc).isoformat())
    ruta = os.path.join(MANTIS, "memoria", "negativa.jsonl")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    registro = imports_hash(texto)
    registro.update({"tarea": os.path.basename(carpeta), "motivo": motivo, "porque": porque[:200],
                     "me_falta": FALTA_LO_QUE.get(motivo, "decir qué falta para poder"),
                     "firma": "ejecutor", "fecha": datetime.now(timezone.utc).isoformat(timespec="seconds")})
    with open(ruta, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(registro, ensure_ascii=False, sort_keys=True) + "\n")
    return registro


def carpeta_de(nombre):
    if nombre in SUELTOS:
        return os.path.join(MANTIS, nombre)
    # una tarea puede vivir dentro de otra: la memoria tiene sus privadas
    directa = os.path.join(TAREAS, nombre)
    if os.path.isdir(directa):
        return directa
    for raiz, dirs, files in os.walk(TAREAS):
        if nombre in dirs:
            return os.path.join(raiz, nombre)
    return directa


def indice():
    """Las tareas que hay: las de arriba y las que viven dentro de otra."""
    if not os.path.isdir(TAREAS):
        return []
    halladas = []
    for nombre in sorted(os.listdir(TAREAS)):
        if not os.path.isdir(os.path.join(TAREAS, nombre)):
            continue
        halladas.append(nombre)
        for dentro in sorted(os.listdir(os.path.join(TAREAS, nombre))):
            if os.path.isdir(os.path.join(TAREAS, nombre, dentro)):
                halladas.append(nombre + "/" + dentro)
    return halladas


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
        for n in indice():
            print(n)
        return 0

    # --sin-tra es un interruptor, y el nombre de la tarea es otra cosa
    resto = [a for a in argv[1:] if not a.startswith("--")]
    if not resto:
        print("[FALTA EL NOMBRE] di que tarea")
        return 1
    sin_tra = "--sin-tra" in argv

    carpeta = carpeta_de(resto[0])
    ok, msg = verificar(carpeta)
    if not ok:
        print(preguntar("SIN CORTE", "no sé qué la tarea hace: su corte está incompleto. " + msg))
        if os.path.isdir(carpeta):
            r = negarse(carpeta, "SIN CORTE", msg)
            print("[NEGARSE] firmada: {}, hash {}".format(r["firma"], r["hash"]))
        return 2

    proceso = procesos_de(carpeta)[0]
    c = cortes(leer(os.path.join(carpeta, proceso)))
    print("[{}] {}".format(os.path.basename(carpeta), proceso))
    for k in CAMPOS:
        print("  {} {}".format(k, c[k]))

    # ENSAYAR: el verbo tercero. El nino mira antes de agarrar.
    modo = modo_de(c)
    print("")
    if modo == "ninguno":
        print(preguntar("SIN ENSAYO", "no sé qué es lo que voy a tocar."))
        r = negarse(carpeta, "SIN ENSAYO", "la tarea no declara su modo")
        print("[NEGARSE] firmada: {}, hash {}".format(r["firma"], r["hash"]))
        print("[NEGARSE] y no corrio: el silencio no es permiso")
        return 4
    print("[ENSAYAR] modo: {} | pasa".format(modo))

    salida, codigo = correr_paso(carpeta)
    print("")
    print(salida)
    if codigo == 2 and salida.startswith("[FALTA EN bin/"):
        r = negarse(carpeta, "FALTA EN bin/", salida[:200])
        print("[NEGARSE] firmada: {}, hash {}".format(r["firma"], r["hash"]))

    if not sin_tra:
        import hashlib
        firma = hashlib.sha256("\n".join(c[k][:120] for k in CAMPOS).encode("utf-8")).hexdigest()[:16]
        with open(os.path.join(carpeta, ".corte"), "w", encoding="utf-8") as fh:
            fh.write(firma)
        tra = dejartra(carpeta, proceso, c["Entra:"], salida[:400], "codigo " + str(codigo))
        print("")
        print("deja: " + os.path.relpath(tra, MANTIS))
    return codigo


if __name__ == "__main__":
    sys.exit(main(sys.argv))
