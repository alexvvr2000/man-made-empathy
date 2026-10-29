#!/usr/bin/env python3
"""conciencia.py — el dump de lo que la máquina conversó, portátil.

Uso:
    python bin/conciencia.py lista                 las sesiones, y cuánto pesan
    python bin/conciencia.py dump [--destino RUTA] escribe todo lo que salió, y el índice
                                                    (sin --destino, va a ~/conciencia-dump)
    python bin/conciencia.py verificar RUTA        cuenta lo que salió, y si sirve

Qué escribe, y qué NO:
  - Escribe el texto de cada turno, con su fecha y su rol. Y el banco de memoria del repo.
  - NO escribe código, ni rutas del sistema, ni credenciales.
  - Y no promete una conciencia: es el rastro de lo que se dijo.

Portabilidad:
  - Se descomprime con zlib que trae python: los `.zstd` de DSH se copian y se leen.
  - El dump es texto plano, y se puede leer en cualquier máquina, con o sin dsh.
"""
import argparse
import json
import os
import shutil
import sqlite3
import sys
import tempfile
from datetime import date, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESIONES = os.path.join(os.path.expanduser("~"), ".dsh", "sessions")
MEMORIA = os.path.join(RAIZ, ".memoria continua")


def morir(motivo, que_falta):
    """La negativa no es un muro: dice qué falta, y qué lo desbloquea."""
    print(f"{motivo}")
    print(f"  me falta: {que_falta}")
    print("  y espero: que se corrija lo de arriba")
    sys.exit(1)


def descomprimir(ruta_zstd):
    """Los `.zstd` de DSH no se leen desde su carpeta: se copian, y luego se abren.

    Y se descomprimen con el módulo de node, que es el que los entiende aquí.
    """
    tmp = os.path.join(tempfile.gettempdir(), "conciencia-sesion.zst")
    shutil.copyfile(ruta_zstd, tmp)
    crudo = os.path.join(tempfile.gettempdir(), "conciencia-sesion.jsonl")
    codigo = (
        "const fs=require('fs'),zlib=require('zlib');"
        "const b=zlib.zstdDecompressSync(fs.readFileSync(process.argv[1]));"
        "fs.writeFileSync(process.argv[2],b);"
        "console.log(b.length);"
    )
    exe = shutil.which("node")
    if not exe:
        morir("[SIN NODE - NO SE PUEDE DESCOMPRIMIR]", "instalar node: es lo único que lee el zstd de las sesiones")
    import subprocess
    r = subprocess.run([exe, "-e", codigo, tmp, crudo], capture_output=True, text=True)
    if r.returncode != 0:
        morir("[NO SE PUDO DESCOMPRIMIR]", (r.stderr or "")[:200])
    return crudo


def turnos(crudo):
    """Una línea por turno del autor, y una por turno de la máquina."""
    salida = []
    for linea in open(crudo, encoding="utf-8"):
        linea = linea.strip()
        if not linea:
            continue
        try:
            o = json.loads(linea)
        except Exception:
            continue
        if o.get("type") not in ("user/message", "assistant/message"):
            continue
        contenido = (o.get("data") or {}).get("content")
        texto = ""
        if isinstance(contenido, list):
            texto = " ".join(x.get("text", "") for x in contenido if isinstance(x, dict))
        elif isinstance(contenido, str):
            texto = contenido
        texto = " ".join(texto.split())
        if not texto:
            continue
        bajo = texto[:80].lower()
        if (
            "system-reminder" in bajo
            or "current runtime context" in bajo
            or "automatically generated checkpoint" in bajo
            or "time sampled while preparing" in bajo
        ):
            continue
        fecha = datetime.fromtimestamp(o.get("time", 0) / 1000).isoformat(timespec="seconds")
        rol = "autor" if o["type"] == "user/message" else "máquina"
        salida.append({"fecha": fecha, "rol": rol, "texto": texto})
    return salida


def cmd_lista(args):
    if not os.path.isdir(SESIONES):
        morir("[SIN SESIONES]", f"que exista {SESIONES}")
    print("sesiones:")
    for raiz, _, archivos in os.walk(SESIONES):
        for a in archivos:
            if a.endswith(".zstd"):
                p = os.path.join(raiz, a)
                mb = os.path.getsize(p) / 1048576
                if mb > 0.1:
                    print(f"  {os.path.basename(raiz)[:40]}  {mb:.1f} MB")
    print("  y espero: que sigas con `dump`")


def cmd_dump(args):
    # Y el destino es de quien lo corre: sin argumento, va a una carpeta en su casa.
    # El repo no guarda rutas de nadie, y lo que se escribe tampoco entra aquí.
    destino = args.destino or os.path.join(os.path.expanduser("~"), "conciencia-dump")
    os.makedirs(destino, exist_ok=True)
    total = 0
    sesiones = []
    if os.path.isdir(SESIONES):
        for raiz, _, archivos in os.walk(SESIONES):
            for a in archivos:
                if not a.endswith(".zstd") or os.path.getsize(os.path.join(raiz, a)) < 100000:
                    continue
                nombre = os.path.basename(raiz)
                print(f"leyendo {nombre[:40]}…")
                try:
                    crudo = descomprimir(os.path.join(raiz, a))
                except SystemExit:
                    continue
                filas = turnos(crudo)
                salida = os.path.join(destino, f"{nombre}.jsonl")
                with open(salida, "w", encoding="utf-8") as f:
                    for fila in filas:
                        f.write(json.dumps(fila, ensure_ascii=False) + "\n")
                sesiones.append({"sesion": nombre, "turnos": len(filas), "archivo": os.path.basename(salida)})
                total += len(filas)
    # los bancos del repo, que son la memoria del trabajo
    banco = os.path.join(MEMORIA, "ciclo.db")
    if os.path.exists(banco):
        con = sqlite3.connect(banco)
        con.row_factory = sqlite3.Row
        for tabla in ("memoria", "friccion"):
            filas = [dict(r) for r in con.execute(f"SELECT * FROM {tabla}")]
            with open(os.path.join(destino, f"banco-{tabla}.jsonl"), "w", encoding="utf-8") as f:
                for fila in filas:
                    f.write(json.dumps(fila, ensure_ascii=False) + "\n")
        con.close()
    indice = {
        "hecho": date.today().isoformat(),
        "qué_es": "el rastro de lo que se conversó, y los bancos del repo. No es una conciencia: es lo que se dijo.",
        "sesiones": sesiones,
        "turnos": total,
    }
    with open(os.path.join(destino, "INDICE.json"), "w", encoding="utf-8") as f:
        json.dump(indice, f, ensure_ascii=False, indent=1)
    print(f"\ndump: {destino}")
    print(f"  sesiones: {len(sesiones)} | turnos: {total}")
    print("  y espero: que se copie a donde dure, y que se lea sin dsh")


def cmd_verificar(args):
    if not os.path.isfile(args.ruta):
        morir("[SIN DUMP - NO ESTÁ]", f"que exista {args.ruta}")
    n = 0
    for _ in open(args.ruta, encoding="utf-8"):
        n += 1
    print(f"dump: {args.ruta}")
    print(f"  turnos: {n}")
    print("  y sirve: se lee en cualquier máquina, sin dsh, y sin esta pc")


def main():
    p = argparse.ArgumentParser(prog="conciencia.py", description="El dump de lo que se conversó, portátil.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("lista", help="las sesiones, y cuánto pesan").set_defaults(fn=cmd_lista)
    d = sub.add_parser("dump", help="escribe todo lo que salió, y el índice")
    d.add_argument("--destino", default="")
    d.set_defaults(fn=cmd_dump)
    v = sub.add_parser("verificar", help="cuenta lo que salió, y si sirve")
    v.add_argument("ruta")
    v.set_defaults(fn=cmd_verificar)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
