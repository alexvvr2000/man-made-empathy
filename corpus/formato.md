# Formato

**Unidad:** nivel.
**Aplica a:** dar forma.
**Tipo:** estándar de formato. No decide, no ejecuta: dice qué forma tiene lo que un ejecutor puede leer: la tarea, la sub-tarea y el proceso.
**Lector:** todo ejecutor —humano, modelo o programa— que tenga que leer o producir un proceso.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

Una tarea, una sub-tarea y un proceso se escriben **siempre igual**. Si cada archivo inventa su forma, **el ejecutor tiene que adivinar**, y adivinar no es ejecutar.

Este archivo dice **la forma de los tres niveles y qué formas son legítimas.** No dice qué hay: eso lo dice cada instancia.

**Las tres formas están abajo, en el orden en que se leen:** la tarea, la sub-tarea y el proceso.

## La tarea

Una tarea tiene **un deterrente principal y N sub-tareas.** Nada más.

```
tarea/
├── deterrente.md       qué se pierde si la tarea deja de cumplir su Acta
├── README.md           el Acta: qué es, de dónde nace, qué conserva
├── piso.md             → referencia a corpus/piso.md
└── sub-tarea × N       cada una con su deterrente y sus procesos
```

| Pieza | Qué declara | Sin ella |
|---|---|---|
| **deterrente** | qué se pierde si la tarea deja de cumplir su `Acta` | la tarea se mantiene porque está: es un fantasma |
| **Acta** | nace de dónde, conserva qué, ausencias qué | no se puede reconstruir por qué existe |
| **piso** | qué estándar cumple, y dónde corre | no se puede comparar con otra instancia |

**El deterrente de la tarea no refuta procesos: refuta que el nivel se sostenga.**

## La sub-tarea

Una sub-tarea es **una carpeta con su deterrente y X procesos.** Nada más.

```
sub-tarea/
├── README.md           deterrente · fallo que cubre · piso · tabla de procesos
└── proceso × X         cada uno con su forma completa
```

El `README` de una sub-tarea tiene **cuatro cosas y no más**:

| Campo | Qué declara | Sin él |
|---|---|---|
| **Deterrente** | qué se pierde si esta sub-tarea falla | no puede justificarse: es una carpeta con procesos |
| **Fallo que cubre** | el fallo comprobado que la justifica | su presencia es arbitraria |
| **Piso** | referencia a `corpus/piso.md` | no se sabe con qué se mide |
| **Procesos** | la tabla: cada uno con **qué decide** y **qué lo refuta** | no se puede recorrer |

**`X` muta.** Una sub-tarea puede tener un proceso o veinte. **El número no significa nada:** una sub-tarea con un proceso y deterrente sólido es tan válida como una con doce.

**X muta** se declara con el número de hoy y la fecha, no como un tope.

## Qué es un proceso, y qué no

Un proceso es un archivo que **declara cómo se hace algo**: qué entra, qué falla, qué sale y quién lo consume.

**No son procesos, aunque vivan junto a ellos:**

| No es proceso | Qué es | Por qué se excluye |
|---|---|---|
| `README.md` | la puerta de una sub-tarea o de una carpeta | describe el conjunto, no ejecuta uno |
| un **índice** | la lista de lo que hay | es una vista, no una unidad |
| la ficha de un **estándar** | la forma de algo | dice cómo debe ser, no cómo se hace |

**La prueba:** ¿el archivo se puede ejecutar? Si no se puede, no es proceso.

## La forma del proceso

Un proceso lleva **Variables** arriba y **seis campos** obligatorios.

| Campo | Qué dice | Forma literal |
|---|---|---|
| `Entra` | qué recibe | `**Entra:**` o `- **Entra:**` |
| `Falla` | el caso concreto que lo incumple | `**Falla:**` o `- **Falla si:**` |
| `Sale` | qué emite, con su forma exacta | `**Sale:**` o `- **Sale:**` |
| `Consume` | quién decide con la salida | `**Consume:**` o `- **Consume:**` |
| `Prueba` | cómo se comprueba que cumplió | `**Prueba:**` **o** `## Prueba` como sección |
| `Falsificador` | qué lo refuta | `**Falsificador:**` **o** `## Falsificador` como sección |

**Arriba del primer campo, todo proceso declara sus variables.** Sin ellas no hay contra qué chequearlo cuando falla.

```
**Variables:** variable1 · variable2 · variable3
**Peor:** qué pasa si se mueve la que más pesa
**Quién:** quien puede decir que se movió mal, o ninguno
```

**Las dos formas de `Prueba` y `Falsificador` son legítimas.** Una unidad puede escribir varias normas y cada una con su prueba en línea; otra puede escribir la prueba una vez, como sección. **Ninguna es mejor y ninguna se convierte a la otra.**

## Unidad y proceso

Un archivo puede contener **una unidad** (un `Entra/Falla/Sale/Consume`) o **varias normas** (varias `Prueba`/`Falsificador` en línea bajo una unidad).

**Lo que no se permite:** un archivo con varias unidades y un solo `Entra`. Es dos procesos con un nombre.

## Cómo lee el ejecutor

1. **¿Es una tarea?** Tiene `deterrente.md` y sub-tareas. Se lee como tarea.
2. **¿Es una sub-tarea?** Es una carpeta con `README` y procesos dentro. Se lee como sub-tarea, y su `README` tiene los cuatro campos.
3. **¿Es un proceso?** No es `README`, ni índice, ni deterrente, ni formato. Se lee como proceso, y lleva `Variables`, `Peor`, `Quién` y los seis campos.
4. **Si falta algo, se nombra qué.** No se adivina.

**Si el ejecutor no puede leer el archivo, se declara `indeterminado`.** No se marca como incompleto: incompleto es otra cosa.

## Lo que este formato no hace

No juzga si la pieza sirve. **Un proceso puede tener los seis campos y ser inútil; una sub-tarea puede tener deterrente y no cubrir nada.** Eso lo dice `../Ouroboros/integridad.md`.

No dice cuántas sub-tareas ni cuántos procesos hay. **Eso lo dice cada instancia, y muta.**

## Prueba

¿Cada nivel se distingue del siguiente? ¿La tarea declara su deterrente y su piso? ¿La sub-tarea declara deterrente, fallo, piso y procesos? ¿El proceso declara variables y los seis campos? ¿Faltar algo se nombra en vez de adivinarse?

**Falsificador:** una tarea sin deterrente; una sub-tarea sin fallo que cubra; un proceso sin variables; un `README` contado como proceso; una sola forma aceptada y la otra marcada como error; un ejecutor que completa lo que falta por su cuenta.
