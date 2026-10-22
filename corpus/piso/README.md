# Piso

**Unidad:** nivel.
**Aplica a:** converger.
**Tipo:** estándar de ejecución. No decide, no enruta: hace que lo mismo se ejecute igual.
**Lector:** quien corre algo y necesita que otro llegue al mismo sitio.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

El piso es **la herramienta que hace que distintos ejecutores hagan lo mismo de maneras distintas y lleguen al mismo sitio.**

Un modelo cambia entre corridas, entre versiones y entre proveedores. **El piso no.** Por eso el piso no es una ayuda para el que ejecuta: es **lo que hace comparable lo que produce.**

Es el `Piso` de `ATLAS` aplicado a la ejecución: allí es lo que hay disponible para comunicar; aquí es **lo que hay disponible para no depender del ejecutor.**

## Qué vuelve piso a una herramienta

Cuatro condiciones. Sin las cuatro, es un script: sirve, pero no es piso.

| Condición | Qué significa | Si falta |
|---|---|---|
| **corre igual en cualquier ejecutor** | no depende de un modelo, una versión ni un proveedor | es una herramienta de una era |
| **su salida ya es un veredicto** | no emite materia prima: emite `pasa / falla / indeterminado` y por qué | el que lee interpreta, y ahí se pierde la comparación |
| **se puede correr sola** | no necesita las otras para dar un resultado | es parte de una tubería, no una unidad |
| **es desechable** | se tira cuando deja de servir, sin tocar lo que chequeaba | se vuelve un sistema que hay que mantener |

## Se nombra por lo que decide

Una herramienta del piso se llama por **lo que decide**, no por cómo está hecha.

| Se nombra por lo que decide | Se nombra por cómo está hecha |
|---|---|
| `integridad` | `chequeo.ps1` |
| `inventario` | `scan.py` |
| `pares` | `compare_v2.sh` |
| sobrevive a reescribirse en otro lenguaje | muere con el lenguaje y con la era |

**La prueba:** si la reescribes en otro lenguaje y sigue siendo la misma pieza, estaba bien nombrada.

## El piso no decide. El criterio decide.

> **El piso es lo que hace que distintos ejecutores hagan lo mismo. El criterio es lo que decide qué hacer con eso. Un piso sin criterio es un pendrive; un criterio sin piso es una opinión.**

Por eso **el piso no lleva modelo.** Si un `if` resuelve, un modelo introduce ruido, cuesta por corrida y no se puede re-correr igual mañana. Un modelo que decide en el piso no es piso: es criterio disfrazado de herramienta.

**Regla:** si el veredicto de la unidad cambia entre dos corridas del mismo repo, no es piso: es criterio.

## Por qué la industria no lo tiene

Cada herramienta de la industria habla el idioma de **su** modelo. Las que comparan se hacen para un proveedor. Las que auditan dependen del registro de una plataforma.

**Un piso que solo corre en un modelo no es piso: es una dependencia.** Y es la razón por la que dos equipos con el mismo proceso llegan a resultados que no se pueden comparar: **no comparten piso.**

## El tren

Las unidades no son un programa: son un **tren**. Cada una consume la salida de la anterior, y **ninguna resuelve el problema entero.**

```
inventario  →  pares  →  integridad  →  veredicto
```

**La regla de cada unidad:** si no puede decidir, escribe `indeterminado` **y por qué**. No adivina, y no se calla lo que no pudo ver.

| Unidad | Qué decide | Qué no puede ver |
|---|---|---|
| `inventario` | qué procesos hay, cuáles están completos, qué campo falta | si lo que falta importa |
| `pares` | qué hermanos se pueden comparar | cuáles se contradicen |
| `integridad` | contradicción, disfrazada, huérfano | si un implícito conceptual está cerrado |
| `veredicto` | `pasa / falla` y qué quedó `indeterminado` | lo que ninguna unidad pudo mirar |

**Un tren no es una tubería:** una tubería se rompe entera si una pieza falla. Las unidades del tren **se pueden correr sueltas**, y la salida de cada una se lee sola.

## Cómo entra una herramienta al piso

1. **Nombrarla por lo que decide.**
2. **Cumplir las cuatro condiciones.** Si falla una, no entra: se declara qué falta.
3. **Emitir veredicto, no datos.** Con `pasa / falla / indeterminado` y el por qué.
4. **Declarar su reverso:** cómo se sabe que está mal. Sin eso es un `if` que nadie audita.

**Falsificador:** una herramienta del piso que necesita un modelo para dar veredicto; una que emite datos y no conclusión; una que solo corre junto a las otras; una que se nombra por su lenguaje.

## Prueba

¿Corre igual en dos ejecutores distintos? ¿Su salida se lee sola? ¿Se puede correr suelta? ¿Se tira sin daño?

**Falsificador:** el mismo proceso en dos ejecutores y dos resultados sin explicación; una herramienta que necesita que alguien interprete su salida; una herramienta que arrastra a las demás; una que nadie puede reescribir sin perderla.
