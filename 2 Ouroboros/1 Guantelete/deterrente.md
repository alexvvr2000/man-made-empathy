# Deterrente de Guantelete

**Unidad:** tarea.
**Aplica a:** enrutar.
**Tipo:** deterrente de la tarea. No produce, no ejecuta, no chequea: **enruta las gemas y cierra la puerta de cada una.**
**Lector:** quien va a usar el guantelete, y quien lo va a mutar.
**Estado:** vigente.

**Variables:** gema · uso solo · uso compuesto · quién decide · dimensión
**Peor:** una gema se usa sola y funciona, y el sistema cree que tiene un primitivo cuando tiene un juguete. Nadie lo nota porque el juguete produce una salida, y una salida que funciona no se pregunta de dónde viene.
**Quién:** quien carga con el poder que no alcanza, y quien muta después sin saber sobre qué está parado.

## Qué es

**El guantelete es una tarea.** Tiene gemas, y cada gema resuelve una cosa. Este archivo no explica qué son: **decide cuál se carga en cada momento.**

A diferencia de un derrotero —que enruta tareas a un agente— **este enruta gemas dentro de una sola tarea.** Es la puerta de la etapa 1, y ninguna se abre sola.

**El flujo es el mismo que el del paso 2 y el del paso 3:** lo que no está en una fila de abajo se declara `[VACÍO - SIN GEMA]` y se pregunta; no se improvisa.

## La estructura

```
1 Guantelete/                ← la tarea. Este archivo.
├── README.md                  el Acta: qué es y qué no es
├── deterrente.md              este archivo: enruta gemas
├── primitivos/                sub-tarea · 6 gemas
└── mutaciones/                sub-tarea · 2 gemas
```

**Un nivel, un deterrente.** La tarea enruta; cada sub-tarea declara el suyo en su `README`; cada gema declara su `Falsificador`. **No se hereda hacia abajo ni se suma hacia arriba.**

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

**Una fila, una gema.** Si una tarea carga dos, se declara por qué: **dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

**Chequear que el nivel se sostiene no es una gema de esta etapa.** Rige `../2 S.A.R.A/integridad.md`.

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
