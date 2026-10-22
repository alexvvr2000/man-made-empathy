# Deterrente de Ouroboros

**Unidad:** tarea.
**Aplica a:** enrutar.
**Tipo:** deterrente de la tarea. No produce, no ejecuta, no chequea: **enruta subprocesos y cierra la puerta de cada nivel.**
**Lector:** quien va a usar Ouroboros, y quien lo va a mutar.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** sub-tarea · subproceso · ruta · condición · quién la levanta
**Peor:** se ejecuta un subproceso de la sub-tarea equivocada y el resultado parece correcto. Nadie lo nota porque la puerta estaba abierta y nadie preguntó qué se había abierto.
**Quién:** quien carga un subproceso, y quien audita después qué se cargó.

## Qué es

**Ouroboros es una tarea.** Tiene sub-tareas, y cada sub-tarea tiene subprocesos. Este archivo no explica qué son: **decide cuál se carga en cada momento.**

A diferencia de un derrotero —que enruta tareas a un agente— **este enruta subprocesos dentro de una sola tarea.** Es la puerta de cada nivel, y ninguna se abre sola.

## La estructura

```
Ouroboros                       ← la tarea
├── README.md                     el Acta
├── deterrente.md                 este archivo: enruta subprocesos
├── piso.md                       → ../corpus/piso.md

├── primitivos/                   sub-tarea · 5 subprocesos
└── mutaciones/                   sub-tarea · 2 subprocesos
```

**Un nivel, un deterrente.** La tarea enruta; cada sub-tarea declara el suyo en su `README`; cada subproceso declara su `Falsificador`. **No se hereda hacia abajo ni se suma hacia arriba.**

## La tabla: si se va a...

| Si se va a... | Se carga | Si no... |
|---|---|---|
| crear, calibrar, reemplazar o retirar un proceso | `./primitivos/manipulacion.md` | no se toca un proceso |
| ejecutar un proceso sobre una entrada | `./primitivos/aplicar.md` | no se ejecuta |
| cambiar un proceso y dejar rastro | `./primitivos/mutacion.md` | no se muta |
| escribir o emitir cualquier archivo | `./primitivos/claridad.md` | no se emite |
| deducir un proceso de lo observable | `./primitivos/ingenieria-inversa.md` | no se deduce |
| decidir algo que afecta a otro | `./mutaciones/friccion.md` | no se decide: se ejecuta |
| mirar algo que no cabe en lo sabido | `./mutaciones/sesgo-declarado.md` | no se ve desde dónde se mira |
| retirar un proceso cuyo fin dejó de existir | `./primitivos/retiro.md` | se queda ocupando el lugar |
| chequear que el nivel se sostiene | `./integridad.md` | no hay veredicto |

**Una fila, un subproceso.** Si una tarea carga dos, se declara por qué: **dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

## Las puertas que no se abren solas

| Puerta | Cuándo se cierra | Quién la levanta |
|---|---|---|
| **manipulación** | si no se nombran las variables antes de crear | la autoridad |
| **aplicar** | si la entrada no le corresponde al proceso | quien aplica |
| **mutación** | si no se declara qué conserva y qué reemplaza | quien muta |
| **claridad** | si la forma no llega al lector | quien emite |
| **ingeniería inversa** | si el deducido no reproduce nada observable | quien deduce |
| **fricción** | si la decisión se ejecuta sin pasar por quien la toma | quien decide |
| **sesgo declarado** | si se descarta sin nombrar la regla que rompe | quien mira |
| **integridad** | si se muta sin haber chequeado | quien muta |

**Cerrar una puerta no es bloquear: es no dejar pasar algo que iba a fallar después, más lejos y más caro.**

## Lo que Ouroboros no es

**No es un estándar.** Es una tarea. El estándar es `../corpus/`, y Ouroboros lo cumple.

**No es un catálogo.** Los subprocesos no se listan: **se componen.** La salida de uno es la entrada de otro sin traducción.

**No es una jerarquía.** Los cinco primitivos no manda uno sobre otro; cada uno se rompe de una manera distinta.

## Prueba

¿Cada sub-tarea tiene su deterrente? ¿Cada subproceso tiene su fila en la tabla? ¿Cada puerta declara cuándo se cierra y quién la levanta? ¿Una tarea puede llegar a `integridad` sin pasar por `manipulación`?

**Falsificador:** una sub-tarea sin deterrente; un subproceso sin fila; una puerta que se abre sola; dos subprocesos cargados en la misma tarea sin declararlo; una mutación que llega a `integridad` después de haber mutado.

## Transiciones

- No hay fila para lo que se va a hacer → se declara `[VACÍO - SIN SUBPROCESO]` y se pregunta; no se improvisa.
- Una sub-tarea no puede declarar su deterrente → se declara fantasma y se retira.
- Un subproceso no tiene puerta → `./mutaciones/sesgo-declarado.md`, y se nombra la regla que rompe.
- En cualquier otro caso → se enruta, se ejecuta y se cierra.
