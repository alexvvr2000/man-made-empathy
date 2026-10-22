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

**Rige el formato, no el contenido.** Un proceso con los campos escritos puede no decir qué decide; eso lo dice `../2 Ouroboros/2 S.A.R.A — mutación/integridad.md`, `La verbalización`.

## La tarea

Una tarea tiene **un deterrente principal y N sub-tareas.** Nada más.

```
tarea/
├── deterrente.md       qué se pierde si la tarea deja de cumplir su Acta
├── README.md           el Acta: qué es, de dónde nace, qué conserva
├── piso.md             → referencia a ./piso.md
└── sub-tarea × N       cada una con su deterrente y sus procesos
```

| Pieza | Qué declara | Sin ella |
|---|---|---|
| **deterrente** | qué se pierde si la tarea deja de cumplir su `Acta` | la tarea se mantiene porque está: es un fantasma |
| **Acta** | nace de dónde, conserva qué, ausencias qué | no se puede reconstruir por qué existe |
| **piso** | qué estándar cumple, y dónde corre | no se puede comparar con otra instancia |

**El deterrente de la tarea no refuta procesos: refuta que el nivel se sostenga.** Lleva su propia cabecera —qué enruta— y su tabla `Si pasa esto | Se pierde | Y el síntoma es`.

## La sub-tarea

Una sub-tarea es **una carpeta con su deterrente y X procesos.** Nada más.

```
sub-tarea/
├── README.md           deterrente · fallo que cubre · piso · tabla de procesos
└── proceso × X         cada uno con su forma completa
```

El `README.md` de una sub-tarea tiene **cuatro cosas y no más**:

| Campo | Qué declara | Sin él |
|---|---|---|
| **Deterrente** | qué se pierde si esta sub-tarea falla | no puede justificarse: es una carpeta con procesos |
| **Fallo que cubre** | el fallo comprobado que la justifica | su presencia es arbitraria |
| **Piso** | referencia a `./piso.md` | no se sabe con qué se mide |
| **Procesos** | la tabla `Proceso | Qué decide | Qué lo refuta` | no se puede recorrer |

**`X` muta.** Una sub-tarea puede tener un proceso o veinte. **El número no significa nada:** una sub-tarea con un proceso y deterrente sólido es tan válida como una con doce.

**`X muta` se declara con el número de hoy y la fecha, no como un tope.**

## Qué es un proceso, y qué no

Un proceso es un archivo que **declara cómo se hace algo**: qué entra, qué falla, qué sale y quién lo consume.

**No son procesos, aunque vivan junto a ellos:**

| No es proceso | Qué es | Por qué se excluye |
|---|---|---|
| `README.md` | la puerta de una sub-tarea o de una carpeta | describe el conjunto, no ejecuta uno |
| un **índice** | la lista de lo que hay | es una vista, no una unidad |
| la ficha de un **estándar** | la forma de algo | dice cómo debe ser, no cómo se hace |
| un **deterrente** | qué se pierde si un nivel se viola | refuta el nivel, no ejecuta |

**La prueba:** ¿el archivo se puede ejecutar? Si no se puede, no es proceso.

## La forma del proceso

Un proceso lleva **variables arriba** y **el bloque de entrada**. Los dos se leen igual en cualquier archivo, y de aquí los lee el inventario.

| Campo | Qué dice | Forma literal |
|---|---|---|
| `Variables` | qué mueve el proceso, antes de escribir | `**Variables:** nombre1 · nombre2 · nombre3` |
| `Peor` | qué pasa si se mueve la que más pesa | `**Peor:** qué pasa` |
| `Quién` | quien puede decir que se movió mal, o `ninguno` | `**Quién:** tipo:nombre` |
| `Entra` | qué recibe | `- **Entra:** ...` |
| `Falla` | el caso concreto que lo incumple | `- **Falla si:** ...` |
| `Sale` | qué emite, con su forma exacta | `- **Sale:** ...` |
| `Consume` | quién decide con la salida | `- **Consume:** ...` |
| `Prueba` | cómo se comprueba que cumplió | `**Prueba:** ...` o `## Prueba` |
| `Falsificador` | qué lo refuta | `**Falsificador:** ...` o `## Falsificador` |

**Las tres variables van arriba del primer campo**, como línea propia. Sin ellas no hay contra qué chequearlo cuando falla: rige `../2 Ouroboros/1 Guantelete — primitivo/primitivos/manipulacion.md`, `Las variables`.

```
**Variables:** variable1 · variable2 · variable3
**Peor:** qué pasa si se mueve la que más pesa
**Quién:** quien puede decir que se movió mal, o `ninguno`

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** qué recibe.
- **Falla si:** el caso concreto.
- **Sale:** qué emite.
- **Consume:** quién decide con la salida.
```

**La cabecera.** Un proceso abre con `Unidad`, `Aplica a`, `Tipo` y `Estado`. `Vigencia` es el campo del proceso que declara su fecha; `Estado` dice si está vigente. Ninguno de los dos se omite.

**El encabezado de la pregunta de entrada.** El bloque va bajo `## Pregunta de entrada` cuando el archivo desarrolla apartados entre la pregunta y la forma; va bajo `## Entra | Falla | Sale | Consume` cuando el bloque es el cuerpo. Las dos formas son legítimas.

**Las dos formas de `Prueba` y `Falsificador` son legítimas.** Una unidad puede escribir varias normas y cada una con su prueba en línea; otra puede escribir la prueba una vez, como sección. **Ninguna es mejor y ninguna se convierte a la otra.**

**Lo que no es opcional:** sin `Falsificador` el proceso es una opinión, y no entra. Rige `../2 Ouroboros/1 Guantelete — primitivo/primitivos/manipulacion.md`, `Admisión`.

## Unidad y proceso

Un archivo puede contener **una unidad** (un `Entra/Falla/Sale/Consume`) o **varias normas** (varias `Prueba`/`Falsificador` en línea bajo una unidad).

**Lo que no se permite:** un archivo con varias unidades y un solo `Entra`. Es dos procesos con un nombre.

**La norma no es la unidad.** Bajo la unidad pueden vivir apartados —`Tesis`, `Cómo se aplica`, `Ancla`, `Transiciones`— y cada uno con su par. La unidad es una; los apartados son los que necesita el que ejecuta, no los que pide la simetría.

## La acuñación

**Todo lo que se nombra, se acuña.** Un proceso sin nombre no existe; una mutación sin nombre no se puede rastrear; una corrida sin nombre no dejó criterio.

**La acuñación es una forma, no una operación:** dice **cómo se nombra**, no **cuándo**. Cada proceso que acuña declara su momento y cita esta sección.

```
Acta: [id] | Nombre: [nombre] | Expansión: [significado] | Origen: [fuente] | Fecha: [ISO]
Encargo: [qué se encarga] | Fin: [estado observable]
Muta: [qué cambia] | Conserva: [qué no] | Ausencias: [qué no tiene] | Prueba: [corrida|no corrida|pendiente]
Autoridad: [tipo:nombre] | Cierra en: [tipo:nombre] | Reemplaza: [nombre anterior o NINGUNA]
```

| Campo | Qué declara | Sin él |
|---|---|---|
| **Nombre** | se lee como nombre propio | es una etiqueta, no un nombre |
| **Expansión** | qué significa | el acrónimo solo se puede deletrear |
| **Muta** | qué cambió | no se distingue de un invento |
| **Conserva** | qué no cambió | no se sabe qué se perdió |
| **Ausencias** | qué no tiene | se finge completo |
| **Reemplaza** | el nombre anterior | no hay cadena |

**El nombre se lee como nombre propio; la expansión dice qué significa.** Un acrónimo que solo se puede leer deletreando no es un nombre: es una etiqueta.

**La regla que lo vuelve criterio:**

> **Un nombre que sirve para dos versiones distintas no nombra nada.** Si el mismo nombre sobrevive a un cambio, el cambio no se verbalizó.

**Sin cambio, no hay acuñación fingida.** Lo que no cambió acuña igual, pero su `Muta:` declara el estado: *«sin cambio»*. Lo que no se permite es acuñar como si hubiera pasado algo.

**El nombre anterior no se borra:** se reemplaza con `Reemplaza:` y la razón. **Sin `Reemplaza:` no hay cadena**, y un nombre nuevo sin cadena no se distingue de un invento.

**Quién acuña:** el proceso que cambia la cosa o cierra la corrida. **Ninguno redefine esta forma:** la citan. `../2 Ouroboros/1 Guantelete — primitivo/primitivos/mutar.md` y `../2 Ouroboros/2 S.A.R.A — mutación/integridad.md` la citan y solo añaden cuándo.

**Prueba:** ¿la pieza acuñada tiene nombre, expansión, `Muta`, `Conserva`, `Ausencias` y `Reemplaza`? ¿El nombre se lee como nombre propio?
**Falsificador:** un nombre que sirve para dos versiones; una acuñación sin `Reemplaza:`; una expansión que deletrea el acrónimo; un `Muta:` que dice «varios» sin nombrar ninguno; un proceso que redefine esta forma en vez de citarla.

## Cómo lee el ejecutor

1. **¿Es una tarea?** Tiene `carga.md` y sub-tareas. Se lee como tarea.
2. **¿Es una sub-tarea?** Es una carpeta con `README.md` y procesos dentro. Se lee como sub-tarea, y su `README.md` tiene los cuatro campos.
3. **¿Es un proceso?** No es `README.md`, ni índice, ni deterrente, ni formato. Se lee como proceso, y lleva `Variables`, `Peor`, `Quién`, el bloque de entrada y su `Acta`.
4. **Si falta algo, se nombra qué.** No se adivina.

**Si el ejecutor no puede leer el archivo, se declara `indeterminado`.** No se marca como incompleto: incompleto es otra cosa.

## Lo que este formato no hace

No juzga si la pieza sirve. **Un proceso puede tener todos los campos y ser inútil; una sub-tarea puede tener deterrente y no cubrir nada.** Eso lo dice `../2 Ouroboros/2 S.A.R.A — mutación/integridad.md`.

No dice cuántas sub-tareas ni cuántos procesos hay. **Eso lo dice cada instancia, y muta.**

## Prueba

¿Cada nivel se distingue del siguiente? ¿La tarea declara su deterrente y su piso? ¿La sub-tarea declara deterrente, fallo, piso y procesos? ¿El proceso declara variables y el bloque de entrada? ¿Faltar algo se nombra en vez de adivinarse?

**Falsificador:** una tarea sin deterrente; una sub-tarea sin fallo que cubra; un proceso sin variables; un `README.md` contado como proceso; un proceso sin `Falsificador`; una sola forma aceptada y la otra marcada como error; un ejecutor que completa lo que falta por su cuenta.
