# BIN — el código que hace correr el ciclo

**Hecho:** 2026-10-29. **Clase:** taller. **Estado:** el ciclo mínimo corre.
**Dueño:** quien lo corra.

**Sesgo:** se lee desde el que ya copió un ente y quiere verlo disparar.
**Límite:** **no es el producto.** **El producto dice qué hacer en [`../Sincronización de almas/entes/`](../Sincronización%20de%20almas/entes/); esto lo hace correr.**
**Firma:** humano:autoridad · máquina:aquí.

**Y lo que este código escribe no vive en el repo:** **las bases y los dumps van a una carpeta de la máquina, y cada quien elige cuál.** **El repo no guarda rutas de nadie.**

---

## Qué hay

| Archivo | Qué hace |
|---|---|
| **`ciclo.py`** | **el ciclo mínimo: disparar en memoria, sostener en fricción, ver, y cerrar el pase** |
| **`esquema.sql`** | **las dos tablas: `memoria` y `friccion`, y nada más** |
| **`historia.py`** | **trae una era del historial de git, cuando se pide** |
| **`historia.md`** | **la regla del historial: una era cuando se pide, y no todas** |
| **`conciencia.py`** | **el dump de lo que se conversó, en texto plano, para no amarrarse a una herramienta ni a una máquina** |
| **`conciencia.md`** | **qué es ese dump, y qué no es: no es una conciencia** |

---

## Cómo se usa

```plaintext
python bin/ciclo.py instalar
python bin/ciclo.py disparar  --frontera revelación --dijo "quién" --texto "qué pasó" --sabia "qué no se sabía"
python bin/ciclo.py sostener  --sesgo "…" --limite "…" --firma "humano:autoridad" \
                              --contra "…" --sostuve "…" --sostengo "…" --techo "…" --disparo autoridad
python bin/ciclo.py ver
python bin/ciclo.py pase --sostuvo "…" --abierto "…" --retoma "…" --no-retoma "…"

python bin/historia.py listar
python bin/historia.py buscar "un texto"
python bin/historia.py traer <commit> "<ruta>"

python bin/conciencia.py dump --destino "<tu carpeta>"
```

**Y la base del ciclo vive fuera del git, en la máquina de quien trabaja.** **No se copia: se rehace desde el esquema.**

---

## Las reglas que aplica el ciclo, y no deja pasar

**1. Sin frontera no hay memoria.** **`--sabia "nada"` se niega: no movió el borde.**

**2. Sin las seis partes no hay fricción**, y **el disparo tiene que ser de los cuatro.**

**3. La anterior no se edita: se suplanta.** **Y queda visible.**

**4. `sostengo` igual a `sostuve` se declara `sin cambio`, y no se finge corrección.**

**Y cada negativa dice qué falta, y qué la desbloquea.**

---

## Lo que falta, y se declara

- **El alma de niño no está en este ciclo.** **Es el ciclo mínimo: los dos bancos, y nada más.**
- **Esto es el `bin/` del proyecto, y crece con quien lo usa.** **No viaja con el ente.**
- **El `pase` escribe fuera de la biblioteca, y no a la base.** **Se unificará cuando el ciclo crezca.**

---

## Prueba

**¿Se niega un disparo que no mueve frontera? ¿Se niega una fricción sin sus seis partes? ¿La anterior queda suplantada y visible? ¿Ninguna base, dump o archivo se guarda dentro del repo?**

**Falsificador:** un disparo con `sabia: nada` que entró; una fricción sin partes que entró; una entrada editada; una base o un dump dentro del repo; una ruta de una máquina escrita en un archivo del repo.
