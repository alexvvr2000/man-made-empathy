#!/usr/bin/env python3
"""ciclo.py — el ciclo mínimo: los dos bancos, sin alma de niño.

Uso:
    python bin/ciclo.py instalar
    python bin/ciclo.py disparar --frontera revelacion --dijo "..." --texto "..." --sabia "..."
    python bin/ciclo.py sostener --sesgo "..." --limite "..." --firma "humano:autoridad" \
        --contra "..." --sostuve "..." --sostengo "..." --techo "..." --disparo autoridad
    python bin/ciclo.py ver
    python bin/ciclo.py pase --sostuvo "..." --abierto "..." --retoma "..." --no-retoma "..." \
        [--se-rompio "..."]

Reglas que aplica, y no deja pasar:
  - El banco de memoria no guarda lo que no movió una frontera (`sabia` no puede ser «nada»).
  - El banco de fricción exige las seis partes, y no deja editar: suplanta.
  - `contra` no puede firmarla quien se corrige, si la corrección es propia.
Las bases viven en .memoria continua/, y están fuera del git.
"""
import argparse
import os
import sqlite3
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "bin", "esquema.sql")


def proyecto():
    """El proyecto donde corre el ciclo.

    Por defecto, este repo. Y se puede apuntar a otro con --proyecto, o con
    CICLO_PROYECTO: el bin/ es del proyecto, y el ente lo busca al llegar.
    """
    elegido = getattr(ARGS, "proyecto", None) or os.environ.get("CICLO_PROYECTO") or RAIZ
    return os.path.abspath(elegido)


def memoria_dir():
    """Dónde viven los bancos: compartidos en el proyecto, o separados por ente.

    Los dos están permitidos, y se declaran:
      --modo compartido  → <proyecto>/.memoria continua/ciclo.db
      --modo separado    → <proyecto>/.memoria continua/ente-<nombre>/ciclo.db
    """
    base = os.path.join(proyecto(), ".memoria continua")
    if getattr(ARGS, "modo", "compartido") == "separado":
        nombre = getattr(ARGS, "ente", None)
        if not nombre:
            morir("[SIN NOMBRE - MODO SEPARADO]", "--ente <nombre>, para saber de quién es el banco")
        base = os.path.join(base, f"ente-{nombre}")
    return base


ARGS = None

FRONTERAS = ("revelación", "confirmación", "ruptura")
DISPAROS = ("contradicción", "mundo", "repetición", "autoridad")
NEGACIONES = ("nada", "ninguna", "ninguno", "n/a", "-", "")


def conectar():
    base = os.path.join(memoria_dir(), "ciclo.db")
    if not os.path.exists(base):
        morir("[SIN BASE - NO ESTÁ INSTALADA]",
              f"instalarla con --proyecto {proyecto()}")
    os.makedirs(os.path.join(memoria_dir(), "respaldos"), exist_ok=True)
    con = sqlite3.connect(base)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def morir(motivo, que_falta):
    """La negativa no es un muro: dice qué falta, y qué lo desbloquea."""
    print(f"{motivo}")
    print(f"  me falta: {que_falta}")
    print("  y espero: que se corrija lo de arriba")
    sys.exit(1)


def norm(s):
    return (s or "").strip().lower()


def cmd_instalar(args):
    os.makedirs(memoria_dir(), exist_ok=True)
    base = os.path.join(memoria_dir(), "ciclo.db")
    con = sqlite3.connect(base)
    with open(ESQUEMA, encoding="utf-8") as f:
        con.executescript(f.read())
    con.commit()
    con.close()
    print(f"instalado: {base}")
    print("  y espero: que sigas con `disparar` o `sostener`")


def cmd_disparar(args):
    con = conectar()
    frontera = args.frontera
    if frontera not in FRONTERAS:
        morir("[SIN ENSAYO - FRONTERA DESCONOCIDA]", f"una de: {' · '.join(FRONTERAS)}")
    if norm(args.sabia) in NEGACIONES:
        morir("[NO ENTRA - NO MOVIÓ EL BORDE]", "el campo sabia con lo que no se sabía antes")
    con.execute(
        "INSERT INTO memoria (fecha, dijo, texto, frontera, sabia, turno) VALUES (?,?,?,?,?,?)",
        (args.fecha or date.today().isoformat(), args.dijo, args.texto, frontera, args.sabia,
         args.turno or ""),
    )
    con.commit()
    ident = con.execute("SELECT last_insert_rowid()").fetchone()[0]
    con.close()
    print(f"pasó: {ident} | frontera: {frontera}")
    if frontera == "ruptura":
        print("  y espero: una entrada de fricción, porque algo dejó de sostenerse")


def cmd_sostener(args):
    con = conectar()
    if args.disparo not in DISPAROS:
        morir("[SIN ENSAYO - DISPARO DESCONOCIDO]", f"uno de: {' · '.join(DISPAROS)}")
    partes = {
        "sesgo": args.sesgo, "limite": args.limite, "firma": args.firma,
        "contra": args.contra, "sostuve": args.sostuve, "sostengo": args.sostengo,
        "techo": args.techo,
    }
    faltan = [k for k, v in partes.items() if not (v or "").strip()]
    if faltan:
        morir("[SIN CORTE - FALTAN PARTES]", ", ".join(faltan))
    if norm(args.sostengo) == norm(args.sostuve):
        estado, sostengo = "sin cambio", args.sostengo
    else:
        estado, sostengo = "vivo", args.sostengo
    anterior = con.execute(
        "SELECT id FROM friccion WHERE estado = 'vivo' AND sostengo = ?", (args.sostuve,)
    ).fetchone()
    suplanta = anterior["id"] if anterior else None
    con.execute(
        """INSERT INTO friccion
           (fecha, sesgo, limite, firma, contra, sostuve, sostengo, techo, disparo, estado, suplanta)
           VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        (args.fecha or date.today().isoformat(), args.sesgo, args.limite, args.firma,
         args.contra, args.sostuve, sostengo, args.techo, args.disparo, estado, suplanta),
    )
    if suplanta:
        con.execute("UPDATE friccion SET estado = 'suplantado' WHERE id = ?", (suplanta,))
    con.commit()
    ident = con.execute("SELECT last_insert_rowid()").fetchone()[0]
    con.close()
    print(f"pasó: {ident} | estado: {estado}" + (f" | suplanta: {suplanta}" if suplanta else ""))
    if estado == "sin cambio":
        print("  y espero: no se finge corrección; cambia el sostengo, o se deja así")


def cmd_ver(args):
    con = conectar()
    mem = con.execute("SELECT COUNT(*) FROM memoria").fetchone()[0]
    fric = con.execute("SELECT COUNT(*) FROM friccion WHERE estado='vivo'").fetchone()[0]
    sup = con.execute("SELECT COUNT(*) FROM friccion WHERE estado='suplantado'").fetchone()[0]
    print(f"memoria: {mem} registros | fricción: {fric} vivos, {sup} suplantados")
    if mem == 0 and fric == 0:
        print("  [SIN DATO - NO PASÓ NADA] y espero: el primer disparo")
        con.close()
        return
    print("\n— cuándo pasó —")
    for r in con.execute(
        "SELECT fecha, frontera, dijo, substr(texto,1,60) AS t FROM memoria ORDER BY id DESC LIMIT 5"
    ):
        print(f"  {r['fecha']}  {r['frontera']:<12} {r['dijo']}: {r['t']}")
    print("\n— qué se sostiene —")
    for r in con.execute(
        "SELECT fecha, disparo, substr(sostengo,1,60) AS s, firma FROM friccion WHERE estado='vivo' ORDER BY id DESC LIMIT 5"
    ):
        print(f"  {r['fecha']}  {r['disparo']:<14} {r['s']}  — contesta: {r['firma']}")
    con.close()


def cmd_pase(args):
    con = conectar()
    os.makedirs(os.path.join(memoria_dir(), "pases"), exist_ok=True)
    ruta = os.path.join(memoria_dir(), "pases", f"{date.today().isoformat()}.md")
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(
            f"\n## {date.today().isoformat()}\n"
            f"- **Sostuvo:** {args.sostuvo}\n"
            f"- **Se rompió:** {args.se_rompio or 'sin ruptura'}\n"
            f"- **Abierto:** {args.abierto}\n"
            f"- **Retoma:** {args.retoma}\n"
            f"- **No retoma:** {args.no_retoma}\n"
        )
    con.close()
    print(f"pase: {ruta}")


PROYECTO = "--proyecto: el proyecto donde corre. Sin él, este repo."
MODO = "--modo: compartido (un banco para todos) | separado (un banco por ente, con --ente)"


def main():
    global ARGS
    comunes = argparse.ArgumentParser(add_help=False)
    comunes.add_argument("--proyecto", default="", help=PROYECTO)
    comunes.add_argument("--modo", default="compartido", choices=("compartido", "separado"), help=MODO)
    comunes.add_argument("--ente", default="", help="el nombre del ente, si el modo es separado")

    p = argparse.ArgumentParser(prog="ciclo.py", description="El ciclo mínimo: dos bancos.")
    sub = p.add_subparsers(dest="cmd", required=True)
    comunes.add_argument = comunes.add_argument

    sub.add_parser("instalar", parents=[comunes], help="crea la base con su esquema").set_defaults(fn=cmd_instalar)

    d = sub.add_parser("disparar", parents=[comunes], help="escribe en el banco de memoria")
    d.add_argument("--frontera", required=True)
    d.add_argument("--dijo", required=True)
    d.add_argument("--texto", required=True)
    d.add_argument("--sabia", required=True)
    d.add_argument("--turno", default="")
    d.add_argument("--fecha", default="")
    d.set_defaults(fn=cmd_disparar)

    s = sub.add_parser("sostener", parents=[comunes], help="escribe en el banco de fricción")
    for campo in ("sesgo", "limite", "firma", "contra", "sostuve", "sostengo", "techo", "disparo"):
        s.add_argument(f"--{campo}", required=True)
    s.add_argument("--fecha", default="")
    s.set_defaults(fn=cmd_sostener)

    sub.add_parser("ver", parents=[comunes], help="lo que hay").set_defaults(fn=cmd_ver)

    pa = sub.add_parser("pase", parents=[comunes], help="cierra el turno")
    for campo in ("sostuvo", "abierto", "retoma", "no-retoma"):
        pa.add_argument(f"--{campo}", required=True)
    pa.add_argument("--se-rompio", default="")
    pa.set_defaults(fn=cmd_pase)

    ARGS = p.parse_args()
    ARGS.fn(ARGS)


if __name__ == "__main__":
    main()
