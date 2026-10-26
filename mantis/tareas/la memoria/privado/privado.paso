#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El paso de la tarea privado: reduce la memoria y la deja publicable."""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANTIS = os.path.abspath(os.path.join(AQUI, "..", ".."))
BIN = os.path.join(MANTIS, "bin", "privado.py")
r = subprocess.run([sys.executable, BIN], capture_output=True, text=True, encoding="utf-8", errors="replace")
print(((r.stdout or "") + (r.stderr or "")).strip())
sys.exit(r.returncode)
