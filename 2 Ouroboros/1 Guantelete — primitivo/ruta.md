# Guantelete — derrotero del paso 1

**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Carta:** [`./rastro.md`](./rastro.md). Sin carta no se lee.
**Deterrente:** [`./carga.md`](./carga.md). Sin él, no se sabe qué se pierde si el paso deja de servir.
**Piso:** `../../1 Tesis/piso.md`.
**Abstracción:** `../` — el guantelete es el paso 1 de `2 Ouroboros/`.

## Entra | Falla | Sale | Consume

**Variables:** petición · gema · puerta · carga abierta · quién la levanta
**Peor:** se cargan dos gemas y el rastro de por qué se hizo algo se pierde entre las dos.
**Quién:** quien enruta, y quien audita después qué se cargó.

- **Entra:** una petición de trabajo sobre el paso 1.
- **Falla si:** no hay fila para lo pedido; se cargan dos gemas y no se declara por qué.
- **Sale:** la gema que se carga y la puerta que se cierra, o [VACÍO - SIN GEMA].
- **Consume:** quien ejecuta la gema cargada.

**Prueba:** ¿cada fila tiene su gema y su consecuencia? ¿el vacío se declara?

**Falsificador:** una petición sin fila que se ejecuta igual; dos gemas cargadas sin declararlo; un vacío implícito.
## La tabla: si se va a...

| Si se va a... | Se carga | Si no... |
|---|---|---|
| crear, calibrar, reemplazar o retirar un proceso | `./primitivos/manipulacion.md` | no se toca un proceso |
| ejecutar un proceso sobre una entrada | `./primitivos/aplicar.md` | no se ejecuta |
| cambiar un proceso y dejar rastro | `./primitivos/mutacion.md` | no se muta |
| retirar un proceso cuyo fin dejó de existir | `./primitivos/retiro.md` | se queda ocupando el lugar |
| deducir un proceso de lo observable | `./primitivos/ingenieria-inversa.md` | no se deduce |
| escribir o emitir cualquier archivo | `./primitivos/claridad.md` | no se emite |
| decidir algo que afecta a otro | `./mutaciones/friccion.md` | no se decide: se ejecuta |
| mirar algo que no cabe en lo sabido | `./mutaciones/sesgo-declarado.md` | no se ve desde dónde se mira |

**Una fila, una gema.** Si se cargan dos, se declara por qué: **dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

## Las puertas que no se abren solas

| Puerta | Cuándo se cierra | Quién la levanta |
|---|---|---|
| **sostener** | si no se nombran las variables antes de crear | la autoridad |
| **aplicar** | si la entrada no le corresponde al proceso | quien aplica |
| **mutar** | si no se declara qué conserva y qué reemplaza | quien muta |
| **retirar** | si no se declara el fin que queda descubierto | quien retira |
| **deducir** | si el deducido no reproduce nada observable | quien deduce |
| **decir** | si la forma no llega al lector | quien emite |
| **friccionar** | si la decisión se ejecuta sin pasar por quien la toma | quien decide |
| **sesgar** | si se descarta sin nombrar la regla que rompe | quien mira |

**Cerrar una puerta no es bloquear: es no dejar pasar algo que iba a fallar después, más lejos y más caro.**

## Vacío

**Lo que no entra en una fila se declara `[VACÍO - SIN GEMA]` y se pregunta; no se improvisa.**

## Transiciones

- No hay fila para lo que se va a hacer → `[VACÍO - SIN GEMA]`.
- Una sub-tarea no puede declarar su deterrente → se declara fantasma y se retira.
- Una gema no tiene puerta → rige `./mutaciones/sesgo-declarado.md`, y se nombra la regla que rompe.
- El paso 1 se cierra → `../2 S.A.R.A`.
- En cualquier otro caso → se enruta, se ejecuta y se cierra.

## Lectura

**Sin derrotero no se carga una gema; con él, se carga la que coincide y ni una más.**
