#!/usr/bin/env python3
"""historia.py — trae una era del historial de git, una cuando se pide.

Uso:
    python bin/historia.py buscar "texto"          qué commits tocan ese texto
    python bin/historia.py era <commit>            qué había en ese commit
    python bin/historia.py traer <commit> <ruta>   escribe un archivo a %TEMP%
    python bin/historia.py listar                  las eras, con su fecha y su tema

Reglas, y no deja pasar:
  - No se escribe nada en el repo. Todo va a %TEMP%/historia/.
  - Se trae UNA era cuando alguien la pide, y no todas.
  - Lo que se trae se declara: qué commit, qué ruta, y qué día.
"""
import argparse
import os
import subprocess
import sys
import tempfile
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(tempfile.gettempdir(), "historia")


def git(*args):
    """Corre git desde la raíz del repo, y devuelve el texto."""
    try:
        r = subprocess.run(
            ["git", *args],
            cwd=RAIZ,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        morir("[SIN GIT - NO HAY HISTORIAL]", "instalar git, o abrir el repo donde sí lo haya")
    # Y cuando git falla, no siempre es un error de git:
    # -S con un texto que no está devuelve 0 líneas y código distinto de 0.
    if r.returncode != 0 and not r.stdout.strip():
        if "signal pipe" in (r.stderr or "") or "unable to read" in (r.stderr or ""):
            return ""
        morir("[SIN DATO - GIT NO DEVOLVIÓ NADA]", (r.stderr or "").strip()[:200])
    return r.stdout


def morir(motivo, que_falta):
    """La negativa no es un muro: dice qué falta, y qué lo desbloquea."""
    print(f"{motivo}")
    print(f"  me falta: {que_falta}")
    print("  y espero: que se corrija lo de arriba")
    sys.exit(1)


def cmd_listar(args):
    """Las eras, con su fecha y su tema, y sin el contenido."""
    salida = git(
        "log", "--all", "--date=short",
        "--pretty=format:%h\t%ad\t%s",
    )
    lineas = [l for l in salida.splitlines() if l.strip()]
    print(f"eras: {len(lineas)}")
    print("  y espero: que se pida una, y no todas")
    for l in lineas[: args.limite]:
        print(l)


def cmd_buscar(args):
    """Qué commits tocan ese texto, sin traer el contenido."""
    salida = git("log", "--all", "--date=short", "--pretty=format:%h\t%ad\t%s", "-S", args.texto)
    lineas = [l for l in salida.splitlines() if l.strip()]
    if not lineas:
        print("[SIN HUELLA - ESE TEXTO NO ESTÁ EN NINGUNA ERA]")
        print(f"  me falta: otra palabra; se buscó «{args.texto}»")
        return
    print(f"era que tocan «{args.texto}»: {len(lineas)}")
    for l in lineas[:20]:
        print(l)


def cmd_era(args):
    """Qué había en ese commit: su tema, su fecha, y sus carpetas."""
    tema = git("log", "-1", "--date=short", "--pretty=format:%ad %s", args.commit).strip()
    print(f"era: {args.commit} — {tema}")
    print("\n— sus carpetas —")
    salida = git("ls-tree", "-r", "--name-only", args.commit)
    carpetas = sorted({l.split("/")[0] for l in salida.splitlines() if "/" in l})
    for c in carpetas:
        print(f"  {c}/")
    print(f"\narchivos: {len([l for l in salida.splitlines() if l.strip()])}")
    print("  y espero: que se traiga uno, con `traer`")


def cmd_traer(args):
    """Escribe un archivo de esa era en %TEMP%, y declara de dónde salió."""
    contenido = git("show", f"{args.commit}:{args.ruta}")
    if not contenido.strip():
        morir("[SIN DATO - EL ARCHIVO ESTÁ VACÍO O NO EXISTE]", f"otra ruta en {args.commit}")
    os.makedirs(DESTINO, exist_ok=True)
    nombre = args.ruta.replace("/", "__").replace("\\", "__")
    ruta = os.path.join(DESTINO, f"{args.commit}__{nombre}")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"traído: {ruta}")
    print(f"  de: {args.commit}:{args.ruta}")
    print(f"  el: {date.today().isoformat()}")
    print("  y espero: que se lea, y que se declare si se sostiene o no")
    print("  regla: el repo no se toca; lo que se queda, se declara primero")


def main():
    p = argparse.ArgumentParser(prog="historia.py", description="Trae una era del historial, una cuando se pide.")
    sub = p.add_subparsers(dest="cmd", required=True)

    li = sub.add_parser("listar", help="las eras, con su fecha y su tema")
    li.add_argument("--limite", type=int, default=40)
    li.set_defaults(fn=cmd_listar)

    b = sub.add_parser("buscar", help="qué commits tocan ese texto")
    b.add_argument("texto")
    b.set_defaults(fn=cmd_buscar)

    e = sub.add_parser("era", help="qué había en ese commit")
    e.add_argument("commit")
    e.set_defaults(fn=cmd_era)

    t = sub.add_parser("traer", help="escribe un archivo de esa era fuera del repo")
    t.add_argument("commit")
    t.add_argument("ruta")
    t.set_defaults(fn=cmd_traer)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
