# IMA.md — qué pedido va a qué herramienta

**El guantelete no tiene una herramienta: tiene siete, y un índice.** **Sin el índice, cada uno elige cómo se aplica, y dos llegan a sitios distintos.**

---

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
| **tocar algo que otro sostiene** | `GUANTELETE.vd`, y `herramientas/FRICCION.prs` antes | **no se toca** |

**Una fila, un destino.** **Si se cargan dos, se declara por qué.**

## Las puertas que no se abren solas

| Puerta | Se cierra si | La levanta |
|---|---|---|
| **sostener** | la pieza no declara posición, límite, firma y reapertura | quien produce la pieza |
| **friccionar** | la decisión se ejecuta sin pasar por quien la toma | quien decide |
| **componer** | el proceso nuevo no declara sus cuatro campos | quien compone |
| **aplicar** | la entrada no le corresponde al proceso | quien aplica |
| **mutar** | no se declara qué conserva | quien muta |
| **retirar** | no se escribió el `Vacío:` antes | quien retira |
| **deducir** | el deducido no reproduce nada observable | quien deduce |

**Cerrar una puerta no es bloquear: es no dejar pasar algo que iba a fallar después, más lejos y más caro.**

## Lo que no entra en una fila

**Se declara `[VACÍO - SIN HERRAMIENTA]`, y se pregunta.** **No se improvisa.**

## Prueba

**¿Cada pedido que llegó tiene fila, o quedó como `[VACÍO - SIN HERRAMIENTA]`? ¿Se declara cuándo se gasta la forma de enrutar? ¿La carta queda fuera de lo que se intercambia?**

**Falsificador:** un pedido sin fila que se corrió igual; una herramienta nueva sin fila; una carta reescrita para que quepa el índice.
