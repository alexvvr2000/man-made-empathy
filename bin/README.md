# BIN — el código que hace correr el ciclo

**Hecho:** 2026-10-28. **Clase:** taller. **Estado:** el ciclo mínimo corre.

**Sesgo:** se lee desde el que ya copió un ente y quiere verlo disparar.
**Límite:** **no es el producto.** **El producto dice qué hacer en [`../Sincronización de almas/entes/`](../Sincronización%20de%20almas/entes/); esto lo hace correr.**
**Firma:** humano:autoridad · máquina:aquí.

---

## Qué hay

| Archivo | Qué hace |
|---|---|
| **`ciclo.py`** | **el ciclo mínimo: disparar en memoria, sostener en fricción, ver, y cerrar el pase** |
| **`esquema.sql`** | **las dos tablas: `memoria` y `friccion`, y nada más** |

**Y la base vive en `.memoria continua/ciclo.db`, fuera del git.** **No se copia: se rehace desde el esquema.**

---

## Cómo se usa

```plaintext
python bin/ciclo.py instalar
python bin/ciclo.py disparar  --frontera revelación --dijo "quién" --texto "qué pasó" --sabia "qué no se sabía"
python bin/ciclo.py sostener  --sesgo "…" --limite "…" --firma "humano:autoridad" \
                              --contra "…" --sostuve "…" --sostengo "…" --techo "…" --disparo autoridad
python bin/ciclo.py ver
python bin/ciclo.py pase --sostuvo "…" --abierto "…" --retoma "…" --no-retoma "…"
```

---

## Las reglas que aplica, y no deja pasar

**1. Sin frontera no hay memoria.** **`--sabia "nada"` se niega: no movió el borde.**

**2. Sin las seis partes no hay fricción**, y **el disparo tiene que ser de los cuatro.**

**3. La anterior no se edita: se suplanta.** **Y queda visible.**

**4. `sostengo` igual a `sostuve` se declara `sin cambio`, y no se finge corrección.**

**Y cada negativa dice qué falta, y qué la desbloquea:** **`[NO ENTRA - NO MOVIÓ EL BORDE]`, `[SIN CORTE - FALTAN PARTES]`, `[SIN BASE - NO ESTÁ INSTALADA]`.**

---

## Lo que falta, y se declara

- **El alma de niño no está en este ciclo.** **Es el ciclo mínimo: los dos bancos, y nada más.**
- **No hay `bin/` por ente.** **Esto es el `bin/` del proyecto, y crece con el tiempo.**
- **El `pase` escribe a `.memoria continua/pases/`, y no a la base.** **Se unificará cuando el ciclo crezca.**

---

## Prueba

**¿Se niega un disparo que no mueve frontera? ¿Se niega una fricción sin sus seis partes? ¿La anterior queda suplantada y visible? ¿La base vive fuera del git y se puede rehacer?**

**Falsificador:** un disparo con `sabia: nada` que entró; una fricción sin partes que entró; una entrada editada; una base dentro del git.
