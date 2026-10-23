# VIDERE — derrotero del paso 2

**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Carta:** [`./rastro.md`](./rastro.md). Sin carta no se lee.
**Deterrente:** [`./carga.md`](./carga.md). Sin él, no se sabe qué se pierde si VIDERE deja de testificar.
**Piso:** `MEGA/mme/Ouroboros/piso.md` — la forma de una unidad.
**Forma de cambio:** `MEGA/mme/Ouroboros/mutacion.md`.

**Sesgo:** la ruta se lee desde lo que el repo cambió, no desde lo que se pide.
**Límite:** no elige qué se hace con lo que vio; solo decide qué se carga para verlo.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `MEGA/mme/Ouroboros/formato de proceso.md`

## Entra | Falla | Sale | Consume

**Variables:** petición · cambio · rastro · pase · quién lee
**Peor:** se carga el proceso que no cubre el cambio que se está mirando, y el pase dice que todo está bien.
**Quién:** quien enruta, y quien va a leer el pase sin poder preguntar.

- **Entra:** una petición sobre lo que cambió, y el repo.
- **Falla si:** no hay fila para lo pedido; se cargan dos procesos y no se declara por qué.
- **Sale:** el proceso que se carga, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿cada fila tiene su proceso y su consecuencia? ¿el vacío se declara?

**Falsificador:** una petición sin fila que se ejecuta igual; dos procesos cargados sin declararlo.

## La tabla: si se va a...

| Si se va a... | Se carga | Si no... |
|---|---|---|
| dejar el pase del turno | `MEGA/mme/Ouroboros/procesos/memoria continua.md`, `El pase de turno` | el turno cierra sin qué reconstruir |
| saber si el repo está entero | `mantis/piso/piso.ps1` | no hay veredicto |
| rastrear de dónde salió una idea | `./VIDERE/` y `Tesis/referencias/index.md` | la referencia se pierde |
| chequear y reescribir una tarea | `MEGA/mme/Ouroboros/procesos/integridad.md` | no hay veredicto |
| dejar que una decisión se repita sin volver a preguntar | `MEGA/mme/Ouroboros/2 S.A.R.A — mutación/decisión.md` | se pregunta lo mismo cada vez |
| aprender de lo ejecutado y corregir la tarea intuida | `MEGA/mme/Ouroboros/2 S.A.R.A — mutación/aprendizaje/aprender.md` | el sistema repite el mismo error |
| proponer lo que nadie pidió, sin ejecutarlo | `MEGA/mme/Ouroboros/2 S.A.R.A — mutación/aprendizaje/iniciar.md` | el sistema solo reacciona |
| dar voz a quien no tiene poder sobre el resultado | `MEGA/mme/Ouroboros/2 S.A.R.A — mutación/autoridad-humanidad/dar-voz.md` | el efecto cae sobre quien no decide |
| identificar quién decide y quién responde | `MEGA/mme/Ouroboros/2 S.A.R.A — mutación/autoridad-equipo/identificar-partes.md` | ninguna autoridad se sabe suya |

**Una fila, un proceso.** Si se cargan dos, se declara por qué: **dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

## Vacío

**Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.**

## Prueba

¿Cada fila tiene su proceso? ¿El vacío se declara? ¿Un testigo se cargó para decidir?

**Falsificador:** una petición sin fila que se ejecuta igual; un proceso cargado para decidir en vez de para testificar.

## Lectura

**Sin derrotero no se carga un proceso; con él, se carga el que coincide y ni uno más.**
