# Formato de proceso

**Unidad:** nivel.
**Aplica a:** dar forma a un proceso.
**Tipo:** estándar de formato. No decide, no ejecuta: dice qué forma tiene lo que un ejecutor puede leer.
**Lector:** todo ejecutor —humano, modelo o programa— que tenga que leer o producir un proceso.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

Un proceso se escribe siempre igual. Si cada archivo inventa su forma, **el ejecutor tiene que adivinar**, y adivinar no es ejecutar.

Este archivo dice **qué campos lleva un proceso y qué formas son legítimas.** No dice qué procesos hay: eso lo dice cada instancia.

## Qué es un proceso, y qué no

Un proceso es un archivo que **declara cómo se hace algo**: qué entra, qué falla, qué sale y quién lo consume.

**No son procesos, aunque vivan junto a ellos:**

| No es proceso | Qué es | Por qué se excluye |
|---|---|---|
| `README.md` | la puerta de una sub-tarea o de una carpeta | describe el conjunto, no ejecuta uno |
| un **índice** | la lista de lo que hay | es una vista, no una unidad |
| la ficha de un **estándar** | la forma de algo | dice cómo debe ser, no cómo se hace |

**La prueba:** ¿el archivo se puede ejecutar? Si no se puede, no es proceso.

## Los campos

Seis obligatorios, uno por unidad.

| Campo | Qué dice | Forma literal |
|---|---|---|
| `Entra` | qué recibe | `**Entra:**` o `- **Entra:**` |
| `Falla` | el caso concreto que lo incumple | `**Falla:**` o `- **Falla si:**` |
| `Sale` | qué emite, con su forma exacta | `**Sale:**` o `- **Sale:**` |
| `Consume` | quién decide con la salida | `**Consume:**` o `- **Consume:**` |
| `Prueba` | cómo se comprueba que cumplió | `**Prueba:**` **o** `## Prueba` como sección |
| `Falsificador` | qué lo refuta | `**Falsificador:**` **o** `## Falsificador` como sección |

**Las dos formas de `Prueba` y `Falsificador` son legítimas.** Una unidad puede escribir varias normas y cada una con su prueba en línea; otra puede escribir la prueba una vez, como sección. **Ninguna es mejor y ninguna se convierte a la otra.**

## Unidad y proceso

Un archivo puede contener **una unidad** (un `Entra/Falla/Sale/Consume`) o **varias normas** (varias `Prueba`/`Falsificador` en línea bajo una unidad).

**Lo que no se permite:** un archivo con varias unidades y un solo `Entra`. Es dos procesos con un nombre.

## Cómo lee el ejecutor

1. **¿Es un proceso?** Si es `README`, índice o ficha de estándar, se excluye.
2. **¿Tiene los seis campos?** En cualquiera de las formas de arriba.
3. **Si falta uno, se nombra cuál.** No se adivina.

**Si el ejecutor no puede leer el archivo, se declara `indeterminado`.** No se marca como incompleto: incompleto es otra cosa.

## Lo que este formato no hace

No juzga si el proceso sirve. **Un proceso puede tener los seis campos y ser inútil.** Eso lo dice `../../Ouroboros/Proceso de integridad de procesos.md`.

No obliga a los archivos ya escritos a cambiar de forma. **El repo ya sigue este formato**; la instancia lo declara en `../../S.A.R.A/piso/README.md`.

## Prueba

¿Un archivo que no es proceso queda excluido? ¿Las dos formas de `Prueba` se aceptan? ¿Faltar un campo se nombra en vez de adivinarse?

**Falsificador:** un README contado como proceso; una sola forma aceptada y la otra marcada como error; un archivo sin campo marcado como completo; un ejecutor que completa lo que falta por su cuenta.
