# INVENTARIO — lo que hay en el repositorio, pieza por pieza, y con fecha

**Hecho:** 2026-10-29. **Clase:** inventario firmado, y no un resumen. **Estado:** vigente, y se actualiza antes de cada publicación.
**Lector:** el abogado, y quien tenga que verificar sin abrir el repositorio entero.
**Dueño:** humano:autoridad.

**Sesgo:** se lee desde el que tiene que comprobar, y no desde el que escribió.
**Límite:** **no dice si algo es legal.** **Dice qué hay, cuánto, y dónde.**
**Firma:** humano:autoridad.

---

## Lo que se puede comprobar, con su comando

**Y cada línea de esta tabla se puede volver a contar.** **Si un número no cuadra, este documento está mal, y se corrige antes de publicar.**

| Lo que | Cuánto | Dónde | Cómo se comprueba |
|---|---|---|---|
| **archivos en el repositorio** | **121** | **la raíz, y sus carpetas** | **contar los archivos, sin el `.git`** |
| **fichas de obras** | **34** | **`Sincronización de almas/ejemplos/ficcion/`** | **contar los `.md`** |
| **direcciones** | **11** | **`direcciones/`** | **contar los `.md`** |
| **pruebas escritas** | **7** | **`Pruebas/`** | **contar los `.md`** |
| **piezas de ideas** | **14** | **`Sincronización de almas/ideas/`** | **contar los archivos** |
| **piezas en `bin/`** | **7** | **`bin/`** | **contar los archivos** |
| **imágenes, clips, o audio** | **0** | **—** | **buscar `*.jpg`, `*.png`, `*.mp4`, `*.webp`** |
| **commits en el historial** | **592** | **el historial de git** | **`git rev-list --count HEAD`** |
| **primer commit** | **`505c659`, del 2026-10-01** | **el historial de git** | **`git log --reverse`** |

---

## Lo que NO hay, y se declara

**Y esto es tan importante como lo que sí hay.**

| Lo que no hay | Por qué importa |
|---|---|
| **ninguna imagen, clip, ni audio** | **el copyright de obras no aplica: no se reproduce nada** |
| **ningún texto largo de otra obra** | **se recortó el 2026-10-29: la ficha más larga cita 30 palabras, y no 100** |
| **ninguna fuente académica** | **no hay paper detrás, y no se cita como si lo hubiera** |
| **ningún dato de salud, finanzas, ni menores** | **se escaneó** |
| **ningún nombre de obra usado como nombre propio** | **los que se usaron, están en `contexto.md` con su reemplazo** |
| **ningún correo de un tercero** | **el correo del autor sí está, en `CITATION.cff`, y es suyo** |

---

## El punto que se midió y se recortó

**El 2026-10-29 había una ficha que citaba ~100 palabras seguidas de un monólogo: `all-star-superman.md`.** **Se recortó a 30 palabras, en tres frases, y el resto remite a la obra.**

**Y las otras 33 fichas citan una frase corta cada una.**

| Lo que | Antes | Hoy |
|---|---|---|
| **texto literal de una obra** | **6 párrafos, ~100 palabras** | **3 frases, 30 palabras** |
| **la obra** | ***All-Star Superman*, 2011, Warner** | **igual, y se remite a ella** |
| **la fuente** | **Wikiquote, 2026-08-10** | **igual** |

**Y lo que queda por dictaminar:** **si 30 palabras en tres frases se sostienen como cita, o hay que quitar también el nombre de la obra.**

---



## Y el estado de verificación, que no es lo mismo que el inventario

**Las 34 fichas están verificadas con una sola mirada, y ninguna con dos.** **La tabla completa está en [`../Sincronización de almas/ejemplos/ESTADO.md`](./Sincronización%20de%20almas/ejemplos/ESTADO.md).**

| Estado | Cuántas |
|---|---|
| **`verificado`** | **28** |
| **`parcial`** | **4** |
| **`declarado`** | **2** |

**Y ninguna tiene segunda mirada independiente.** **Eso está declarado, y es lo que hay.**

---

## Lo que este inventario no hace

**No sustituye a un dictamen.** **Cuenta lo que hay, y nombra dónde mirar.**

**No promete que esté completo.** **Promete que lo que dice se puede volver a contar, y que lo que falta se dice.**

**Y si un número cambia, este documento se actualiza antes de publicar.** **Un inventario viejo es peor que ninguno.**

---

## Prueba

**¿Cada número se puede volver a contar con un comando? ¿Lo que no hay está dicho? ¿El punto que hay que mirar está medido? ¿Se distingue el inventario del dictamen?**

**Falsificador:** un número que no cuadra con lo que hay; un «no hay imágenes» sin haber buscado; un inventario que se presenta como dictamen; un inventario que no se actualiza.
