# VISION DEL AUTOR

**Dos tesis, y nada más.**

| | Qué es | Estado |
|---|---|---|
| **`tesis teorica/`** | **nueve carpetas, cada una con su `.tex` y su `.pdf`** | **terminadas y compiladas** |
| **`tesis practica/`** | **`EL SESGO DECLARADO.md`, el registro de 26 días** | **abierta: la etiqueta está montada, el adhesivo no** |

**Y las dos están hechas de candados.** **Cada tesis es lo que 93 reglas sostienen, y cada regla dice qué la tumba.**

## La forma

```
vision del autor/
├── tesis teorica/
│   ├── convivir/            convivir.tex + convivir.pdf
│   ├── la colmena/          la-colmena.tex + la-colmena.pdf
│   └── ... nueve en total
└── tesis practica/
    └── EL SESGO DECLARADO.md
```

**Cada carpeta de `tesis teorica/` tiene sus dos archivos y nada más.** **El `.tex` para quien lo quiera tocar, y el `.pdf` para quien lo quiera leer.**

## Cómo se rehace

```powershell
python mantis/bin/teoricas.py            las nueve
python mantis/bin/teoricas.py convivir   una
```

**El script lee los ocho campos de cada tesis, los vuelve las ocho secciones de un paper, y compila.** **Nada se escribe nuevo: se mueve lo que ya está escrito al formato de la academia.**

**Y por eso el formato no es el trabajo.** **El trabajo es la tesis. El formato lo hace un comando.**
