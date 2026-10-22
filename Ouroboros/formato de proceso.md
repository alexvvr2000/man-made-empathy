# Formato

**Unidad:** nivel.
**Aplica a:** dar forma.
**Tipo:** estándar de formato. No decide, no ejecuta: dice qué forma tiene lo que un ejecutor puede leer.
**Lector:** todo ejecutor —humano, modelo o programa— que tenga que leer o producir un proceso.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

Todo se escribe **siempre igual**. Si cada archivo inventa su forma, **el ejecutor tiene que adivinar**, y adivinar no es ejecutar.

**Rige el formato, no el contenido.** Un proceso con los campos escritos puede no decir qué decide; eso lo dice `./2 S.A.R.A — mutación/integridad.md`, `La verbalización`.

## Todo es un proceso

**No hay piezas que no sean proceso.** El `Rastro`, la `Ruta`, la `Carga` y el propio formato **también se ejecutan**: verifican, enrutan, declaran pérdida o dicen la forma. **«Describir el conjunto» no es un oficio distinto: es un proceso que decide sobre el conjunto.**

Por eso un archivo **no se excluye del estándar por su nombre**. Se excluye si al quitarlo **nadie sabría qué hacer** — y eso lo decide su propia `Prueba`.

**El nivel no cambia el oficio: cambia la carpeta.** Un paso de `Ouroboros/` es un ente y se lee con `./formato de ente.md`; lo que ese ente contiene son procesos y se leen aquí.

## La forma del proceso

Un proceso lleva **variables arriba**, **el bloque de entrada**, y **su reverso**.

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

**Las tres variables van arriba del primer campo**, como línea propia. Sin ellas no hay contra qué chequearlo cuando falla: rige `./1 Guantelete — primitivo/primitivos/manipulacion.md`, `Las variables`.

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

**La cabecera.** Un proceso abre con `Unidad`, `Aplica a`, `Tipo` y `Estado`. `Vigencia` declara la fecha; `Estado` dice si está vigente.

**El encabezado de la pregunta de entrada.** El bloque va bajo `## Pregunta de entrada` cuando el archivo desarrolla apartados entre la pregunta y la forma; va bajo `## Entra | Falla | Sale | Consume` cuando el bloque es el cuerpo. **Las dos formas son legítimas.**

**Las dos formas de `Prueba` y `Falsificador` son legítimas.** Una unidad puede escribir varias normas y cada una con su prueba en línea; otra puede escribir la prueba una vez, como sección. **Ninguna es mejor y ninguna se convierte a la otra.**

**Lo que no es opcional:** sin `Falsificador` el proceso es una opinión, y no entra. Rige `./1 Guantelete — primitivo/primitivos/manipulacion.md`, `Admisión`.

## Unidad y proceso

Un archivo puede contener **una unidad** (un `Entra/Falla/Sale/Consume`) o **varias normas** (varias `Prueba`/`Falsificador` en línea bajo una unidad).

**Lo que no se permite:** un archivo con varias unidades y un solo `Entra`. Es dos procesos con un nombre.

**La norma no es la unidad.** Bajo la unidad pueden vivir apartados —`Tesis`, `Cómo se aplica`, `Ancla`, `Transiciones`— y cada uno con su par. La unidad es una; los apartados son los que necesita el que ejecuta.

## La tarea y la sub-tarea

**Los niveles cambian la forma de la carpeta, no el oficio.**

**Si tiene `rastro.md`, `ruta.md` y `carga.md`, es un ente** — y su forma la dice `./formato de ente.md`. Un paso de `Ouroboros/` es un ente.

```
ente/
├── rastro.md           el cuerpo: qué hay, qué no se toca y cómo se verifica
├── ruta.md             la mente: qué se carga y cuándo
├── carga.md            el pensamiento: qué se pierde si el ente deja de servir
└── …                   los procesos que el ente contiene
```

**La sub-tarea es lo de adentro:** una carpeta de procesos **dentro** de un ente, con cuatro campos en su `README.md` y no más:

| Campo | Qué declara | Sin él |
|---|---|---|
| **Rastro** | qué se pierde si esta sub-tarea falla | es una carpeta con procesos |
| **Fallo que cubre** | el fallo comprobado que la justifica | su presencia es arbitraria |
| **Piso** | referencia a `./piso.md` | no se sabe con qué se mide |
| **Procesos** | la tabla `Proceso | Qué decide | Qué lo refuta` | no se puede recorrer |

**`X` muta.** El número no significa nada: una sub-tarea con un proceso y rastro sólido es tan válida como una con doce. **`X muta` se declara con el número de hoy, no como un tope.**

## La acuñación

**Todo lo que se nombra, se acuña.** Un proceso sin nombre no existe; una mutación sin nombre no se puede rastrear; una corrida sin nombre no dejó criterio.

**La acuñación es una forma, no una operación:** dice **cómo se nombra**, no **cuándo**.

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

**El nombre se lee como nombre propio; la expansión dice qué significa.** Un acrónimo que solo se puede leer deletreando **no es un nombre: es una etiqueta.**

> **Un nombre que sirve para dos versiones distintas no nombra nada.** Si el mismo nombre sobrevive a un cambio, el cambio no se verbalizó.

**Sin cambio, no hay acuñación fingida.** Lo que no cambió acuña igual, pero su `Muta:` declara el estado: *«sin cambio»*.

**El nombre anterior no se borra:** se reemplaza con `Reemplaza:` y la razón. **Sin `Reemplaza:` no hay cadena.**

**Quién acuña:** el proceso que cambia la cosa o cierra la corrida. **Ninguno redefine esta forma:** la citan. `./1 Guantelete — primitivo/primitivos/mutar.md` y `./2 S.A.R.A — mutación/integridad.md` la citan y solo añaden cuándo.

**Prueba:** ¿la pieza acuñada tiene nombre, expansión, `Muta`, `Conserva`, `Ausencias` y `Reemplaza`? ¿El nombre se lee como nombre propio?
**Falsificador:** un nombre que sirve para dos versiones; una acuñación sin `Reemplaza:`; una expansión que deletrea el acrónimo; un `Muta:` que dice «varios» sin nombrar ninguno; un proceso que redefine esta forma en vez de citarla.

## Cómo lee el ejecutor

1. **Abrir la cabecera.** `Unidad`, `Aplica a`, `Tipo`, `Estado`.
2. **¿Tiene el bloque de entrada?** `Entra | Falla | Sale | Consume`. Sin él no es proceso: se declara qué falta.
3. **¿Tiene variables?** `Variables`, `Peor`, `Quién`.
4. **¿Tiene su reverso?** `Prueba` y `Falsificador`.
5. **Si falta algo, se nombra qué.** No se adivina.

**Si el ejecutor no puede leer el archivo, se declara `indeterminado`.** No se marca como incompleto: incompleto es otra cosa.

## Lo que este formato no hace

No juzga si la pieza sirve. **Un proceso puede tener todos los campos y ser inútil.** Eso lo dice `./2 S.A.R.A — mutación/integridad.md`.

No dice cuántas sub-tareas ni cuántos procesos hay. **Eso lo dice cada instancia, y muta.**

## Prueba

¿Cada proceso declara variables, bloque de entrada y reverso? ¿Los niveles cambian la carpeta y no el oficio? ¿Faltar algo se nombra en vez de adivinarse?

**Falsificador:** un proceso sin variables; un proceso sin `Falsificador`; un archivo excluido del estándar por su nombre y no por su prueba; una sola forma aceptada y la otra marcada como error; un ejecutor que completa lo que falta por su cuenta.
