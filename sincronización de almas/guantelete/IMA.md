# IMA.md — qué pedido va a qué herramienta

**Nombre.** RUTA — **R**econocimiento, **U**bicación, **T**razo, **A**cción. La expansión dice el acto: enrutar el pedido a la herramienta que le toca, y marcarse gastado cuando la forma deja de servir.

**Unidad:** índice.
**Aplica a:** enrutar.
**Tipo:** se intercambia. No es estándar: es el índice que se gasta.
**Lector:** quien abre `./GUANTELETE.md` y no sabe qué herramienta cargar.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** el pedido se lee desde lo que pide, no desde el nombre de la herramienta.
**Límite:** no decide qué se hace con el pedido. **Dice qué herramienta corre, y nada más.**
**Firma:** humano:autoridad · máquina:quien enrute.

**Variables:** pedido · herramienta · respuesta · gastadura
**Peor:** se enruta a la herramienta que ya no sirve, y la salida parece correcta porque nadie declara desde dónde se tomó.
**Quién:** quien cargue la salida de una herramienta gastada.

## El estándar de esta RUTA es que no hay estándar

> No hay una forma fija de enrutar. Hay un índice: cada pedido se enruta a la herramienta que le toca, y cuando la forma se gasta, se intercambia.

**Y lo que NO se intercambia es la carta.** La carta dice qué es el ente; la RUTA se cambia de forma.

## Las filas, y cada una se lee antes de enrutar

| Se va a… | Se enruta a… | Sin la autoridad… |
|---|---|---|
| **sostener una pieza, y saber quién puede contestarla** | `herramientas/SOSTENER.prs` | **no entra: hay opinión, no pieza** |
| **decidir algo que afecta a otro** | `herramientas/FRICCION.prs` | **no se decide: se ejecuta** |
| **producir lo que todavía no existe** | `herramientas/COMPONER.prs` | **no se produce: se improvisa** |
| **ejecutar un proceso que ya existe** | `herramientas/APLICAR.prs` | **no se ejecuta** |
| **cambiar un proceso sin perder lo que servía** | `herramientas/MUTAR.prs` | **no se muta** |
| **quitar un proceso cuyo fin dejó de existir** | `herramientas/RETIRAR.prs` | **se queda ocupando el lugar** |
| **deducir un proceso de lo observable** | `herramientas/INVERTIR.prs` | **no se deduce** |
| **tocar algo que otro sostiene** | **`../guantelete/GUANTELETE.md`, y `herramientas/FRICCION.prs` antes** | **no se toca** |
| **escribir y emitir lo que sale** | `../../el sincronización de almas/2 el idioma/formacion/CLARIDAD.md` | **no se emite** |
| **decir qué se usó, y qué no había** | `../../el sincronización de almas/2 el idioma/friccion/PISO.md` | **se inventa la capacidad** |

Una fila, un destino. **Si se cargan dos, se declara por qué: dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

## Las puertas que no se abren solas

| Puerta | Cuándo se cierra | Quién la levanta |
|---|---|---|
| **sostener** | si la pieza no declara posición, límite, firma y reapertura | quien produce la pieza |
| **friccionar** | si la decisión se ejecuta sin pasar por quien la toma | quien decide |
| **componer** | si el proceso nuevo no declara sus cuatro campos | quien compone |
| **aplicar** | si la entrada no le corresponde al proceso | quien aplica |
| **mutar** | si no se declara qué conserva | quien muta |
| **retirar** | si no se escribió el `Vacío:` antes | quien retira |
| **deducir** | si el deducido no reproduce nada observable | quien deduce |

**Cerrar una puerta no es bloquear: es no dejar pasar algo que iba a fallar después, más lejos y más caro.**

## Vacío

**Lo que no entra en una fila se declara `[VACÍO - SIN HERRAMIENTA]`, y se pregunta; no se improvisa.**

## La gastadura, y es lo que lo vuelve índice

```
RUTA:        [qué forma de enrutar se usa]
Gastado si:  [qué muestra que la forma ya no sirve]
Se cambia:   [por qué forma]
La carta no: [qué sigue diciendo, pase lo que pase]
```

**Un índice que nunca se gasta es un estándar disfrazado; y un estándar del índice es justamente lo que no hay.**

## Lo que este índice no hace

**No guarda el rastro del pedido.** **El rastro queda en la `.tra` de la tarea.**
**No decide si la herramienta sirve.** **Eso lo dice su propio `Falsificador`, cuando se corre.**

## Prueba

**¿Cada pedido que llegó tiene fila, o quedó como `[VACÍO - SIN HERRAMIENTA]`? ¿La forma de enrutar está declarada? ¿Se declara cuándo se gasta? ¿La carta queda fuera de lo que se intercambia?**

**Falsificador:** un pedido sin fila que se corrió igual; una RUTA presentada como estándar; una forma que se gasta y no se intercambia; una carta que se reescribe para que quepa el índice.

## Transiciones

- El pedido coincide con una fila → **se carga esa herramienta, y ni una más.**
- No hay fila para el pedido → **`[VACÍO - SIN HERRAMIENTA]`, y se pregunta.**
- La forma se gasta → **se cambia la RUTA, y la carta no se toca.**
- En cualquier otro caso → **se enruta, se ejecuta, y se cierra.**
