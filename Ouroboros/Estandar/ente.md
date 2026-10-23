# Formato de ente

**Unidad:** nivel.
**Aplica a:** formar entes.
**Tipo:** estándar de formato. No decide, no ejecuta: dice qué forma tiene un ente.
**Lector:** todo ejecutor que tenga que leer o producir un ente.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el ente se lee desde el cuerpo que no muta, no desde lo que el ente dice de sí.
**Límite:** no decide si el ente sirve; dice si tiene cuerpo, mente y pensamiento.
**Cuelga de:** `./proceso.md`. Las tres piezas del ente son procesos.
**Deja de valer:** cuando no hay tarea. Un ente sin tarea no es ente: es una carpeta con tres archivos.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** rastro · ruta · carga · tarea · fantasma
**Peor:** un ente con las tres piezas escritas como prosa. Tiene el cuerpo de un ente y los órganos de un archivo.
**Quién:** quien hereda el ente y no sabe qué se pierde si deja de servir.

## Qué es un ente

**Un ente es lo que puede existir y trabajar por su cuenta.** No es un archivo: **es una tarea con tres piezas.**

| Pieza | Archivo | Qué es | Qué muta |
|---|---|---|---|
| **Rastro** | `rastro.md` | el cuerpo: qué hay, qué no se toca y cómo se verifica | **casi nunca** |
| **Ruta** | `ruta.md` | la mente: qué se carga y cuándo | **siempre** |
| **Carga** | `carga.md` | el pensamiento: qué se pierde si el ente deja de servir | **cuando el fin cambia** |

**Si falta una de las tres, no hay ente: es fantasma.**

**Rastro dice qué hubo; Ruta dice por dónde ir hoy; Carga es lo que se lleva y no se puede soltar sin perder algo.**

## Las tres piezas son procesos

**El ente no es una carpeta con tres archivos de texto: es una carpeta con tres procesos.**

| Pieza | `Entra` | `Sale` | Su marca | Su condicional |
|---|---|---|---|---|
| **Rastro** | qué hay que verificar | qué hay, qué no se toca y cómo se verifica | el cuerpo que no muta | `Sesgo` desde dónde se verifica |
| **Ruta** | una petición | la ruta que se carga, o `[VACÍO - SIN RUTA]` | la tabla `Si se va a… Se carga` | `Sesgo` desde dónde se carga |
| **Carga** | el ente en uso | qué se pierde si deja de servir | la tabla `Si pasa esto | Se pierde | Y el síntoma es` | `Sesgo` desde dónde se pierde |

**Lo que cada pieza debe tener, y sin ello no es proceso del ente:**

1. Los **nueve campos** de `./proceso.md`.
2. Los **cuatro condicionales**: `Sesgo`, `Límite`, `Firma`, `Continuidad`.
3. El **cuerpo en compuertas numeradas**, sin verbos de sugerencia y con rama por defecto.

**Lo que cada pieza no necesita.** No se le pide que repita lo que el formato ya dice: **cita el formato y declara solo lo suyo.**

## Cómo se aplica

1. **Verificar las tres piezas** → `Piezas: [rastro|ruta|carga] faltan: [...]`
2. **Verificar que cada una es proceso** → `Es proceso: [sí|no]`
3. **Declarar el fantasma** → `Fantasma: [sí|no]`
4. **Declarar la identidad** → `Nombre: [...] | Tarea: [...]`
5. **Emitir** → `Ente: [sí | fantasma]`

**Prohibido declarar ente a una carpeta con prosa. Prohibido ejecutar el paso N+1 sin la salida del N.**

```
Piezas: [rastro|ruta|carga] | Faltan: [...] | Es proceso: [sí|no] | Nombre: [...] | Tarea: [...]
Fantasma: [sí|no] | Ente: [sí|fantasma]
```

## El sesgo, en las tres

**Cada pieza declara desde dónde mira, y ninguna finge neutralidad:** el Rastro desde dónde se verifica, la Ruta desde dónde se carga, la Carga desde dónde se pierde. **Tres sesgos declarados, un solo cuerpo.**

**El cuerpo solo se interpreta: si se abre y se declara qué conserva, es lectura; si se abre y no se declara, es invasión.**

## La forma

```
ente/
├── rastro.md         el cuerpo
├── ruta.md           la mente
├── carga.md          el pensamiento
└── …                 los procesos que el ente contiene
```

**El ente no explica: ejecuta.** Lo que no cambia una decisión no vive aquí.

## La identidad del ente

**La identidad es funcional: un nombre y una tarea, no una persona.** Sin identidad no hay sujeto; sin tarea no hay fin.

**Es ente si tiene las tres piezas.** Un paso de `Ouroboros/` lo es. Una sub-tarea es una carpeta de procesos dentro de un ente, y no necesita las tres.

## Lo que no hace

**No juzga si el ente sirve.** Dice si tiene cuerpo, mente y pensamiento. Si sirve, lo dice su resistencia.

**No iguala ente con persona.** La identidad es funcional: nombre y tarea.

**No acepta prosa.** Un ente cuyas piezas son prosa es un archivo con la forma de un ente.

## Prueba

¿El ente tiene `rastro.md`, `ruta.md` y `carga.md`? ¿Las tres son procesos con los nueve campos? ¿Cada una declara su `Sesgo` y su `Firma`? ¿El cuerpo se conservó?

**Falsificador:** un ente sin una de las tres piezas; una `ruta.md` que no cambia aunque el hoy cambió; una `carga.md` que sobrevive a su fin; una pieza escrita como texto; una pieza que copia el formato en vez de citarlo.

## Transiciones

- Falta una pieza → `Fantasma: sí`, y se pregunta. No se improvisa.
- Una pieza es prosa → se declara, y no es ente.
- El fin del ente cambió → la `carga.md` cambia; el cuerpo no.
- En cualquier otro caso → se entrega el ente con sus tres piezas y se cierra.

## Acuñación

```
Acta: EST-14 | Nombre: Formato de ente | Expansión: cuerpo, mente y pensamiento, los tres como proceso
Origen: futuro/Estandar/Ente/formato de ente.md | Fecha: 2026-10-23
Muta: de carpeta con tres textos a carpeta con tres procesos | Conserva: que sin las tres es fantasma
Ausencias: no juzga si el ente sirve | Prueba: no corrida | Reemplaza: futuro/Estandar/Ente/formato de ente.md
```
