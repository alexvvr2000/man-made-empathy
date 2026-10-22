# Deterrente de Guantelete

**Unidad:** tarea.
**Aplica a:** enrutar.
**Tipo:** deterrente de la tarea. No produce, no ejecuta, no chequea: **enruta las gemas y cierra la puerta de cada una.**
**Lector:** quien va a usar el guantelete, y quien lo va a mutar.
**Estado:** vigente.

**Variables:** gema · uso solo · uso compuesto · quién decide · dimensión
**Peor:** una gema se usa sola y funciona, y el sistema cree que tiene un primitivo cuando tiene un juguete. Nadie lo nota porque el juguete produce una salida, y una salida que funciona no se pregunta de dónde viene.
**Quién:** quien carga con el poder que no alcanza, y quien muta después sin saber sobre qué está parado.

## Entra | Falla | Sale | Consume

**Variables:** gema · uso solo · uso compuesto · quién decide · dimensión
**Peor:** una gema se usa sola y funciona: el sistema cree que tiene un primitivo cuando tiene un juguete.
**Quién:** quien carga con el poder que no alcanza.

- **Entra:** el guantelete en uso.
- **Falla si:** no dice qué se pierde cuando el guantelete se vuelve catálogo.
- **Sale:** la tabla Si pasa esto | Se pierde | Y el síntoma es, y el límite del guantelete.
- **Consume:** quien decide si el paso 1 se sostiene.

**Prueba:** ¿la pérdida se puede señalar? ¿el síntoma se ve cuando pasa?

**Falsificador:** un deterrente sin tabla; una pérdida que nadie puede señalar.

## Qué es

**El guantelete es una tarea.** Tiene gemas, y cada gema resuelve una cosa. Este archivo no explica qué son: **decide cuál se carga en cada momento.**

A diferencia de un derrotero —que enruta tareas a un agente— **este enruta gemas dentro de una sola tarea.** Es la puerta de la etapa 1, y ninguna se abre sola.

**El flujo es el mismo que el del paso 2 y el del paso 3:** lo que no está en una fila de abajo se declara `[VACÍO - SIN GEMA]` y se pregunta; no se improvisa.

## Qué se pierde si se viola

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| una gema se usa sola y funciona | el punto donde se para | el sistema cree que tiene un primitivo cuando tiene un juguete |
| entra una pieza que se deriva de otra | la irreducibilidad | el sinfín vuelve disfrazado de pieza nueva |
| una pieza entra sin cerrar un implícito | la justificación | el guantelete se vuelve un catálogo: crece y no compone |
| una gema llega al paso 2 sin pasar por `mutar` | la puerta | la abstracción se construye sobre algo que no se declaró |
| el guantelete se mide por cuántas gemas tiene | el criterio | se defiende por tamaño lo que debía defenderse por composición |
| se retira una gema sin declarar el fin que cubría | el rastro | el hueco existe y nadie sabe que estaba |

**Chequear que el nivel se sostiene no es una gema de esta etapa.** Rige `../2 S.A.R.A — mutación/integridad.md`.

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

## Lo que el guantelete no es

**No es un estándar.** Es una tarea. El estándar es `../../1 Tesis/`, y el guantelete lo cumple.

**No es un catálogo.** Las gemas no se listan: **se componen.** La salida de una es la entrada de otra sin traducción.

**No es una jerarquía.** Las gemas no mandan unas sobre otras; cada una se rompe de una manera distinta.

## Prueba

¿Cada sub-tarea tiene su deterrente? ¿Cada gema tiene su fila en la tabla? ¿Cada puerta declara cuándo se cierra y quién la levanta? ¿Una mutación puede llegar al paso 2 sin haber pasado por `mutar`?

**Falsificador:** una sub-tarea sin deterrente; una gema sin fila; una puerta que se abre sola; dos gemas cargadas en la misma tarea sin declararlo; una mutación que llega a `integridad` después de haber mutado.

## Transiciones

- No hay fila para lo que se va a hacer → se declara `[VACÍO - SIN GEMA]` y se pregunta; no se improvisa.
- Una sub-tarea no puede declarar su deterrente → se declara fantasma y se retira.
- Una gema no tiene puerta → rige `./mutaciones/sesgo-declarado.md`, y se nombra la regla que rompe.
- En cualquier otro caso → se enruta, se ejecuta y se cierra.
