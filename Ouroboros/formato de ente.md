# Formato de ente

**Unidad:** nivel.
**Aplica a:** formar entes.
**Tipo:** estándar de formato. No decide, no ejecuta: dice qué forma tiene un ente.
**Lector:** todo ejecutor que tenga que leer o producir un ente.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es un ente

**Un ente es lo que puede existir y trabajar por su cuenta.** No es un archivo: **es una tarea con tres piezas.**

**Todo ente tiene tres piezas, y las tres son obligatorias:**

| Pieza | Archivo | Qué es | Qué muta |
|---|---|---|---|
| **Rastro** | `rastro.md` | el cuerpo: qué hay, qué no se toca y cómo se verifica | **casi nunca**: el cuerpo no cambia sin cambiar de especie |
| **Ruta** | `ruta.md` | la mente: qué se carga y cuándo | **siempre**: si el hoy cambia y la ruta no, enruta lo de ayer |
| **Carga** | `carga.md` | el pensamiento: qué se pierde si el ente deja de servir | **cuando el fin cambia**; si el fin deja de existir, no se muta: se retira |

**Si falta una de las tres, no hay ente: es fantasma.** Rige `./procesos/integridad.md`, `El fantasma`.

**Rastro dice qué hubo; Ruta dice por dónde ir hoy; Carga es lo que se lleva y no se puede soltar sin perder algo.**

**Las tres piezas son procesos, no textos.** Se escriben con el formato de `./formato de proceso.md`: nueve campos, cuatro condicionales y cuerpo en forma. Un ente cuyas piezas son prosa tiene el cuerpo de un ente y los órganos de un archivo.

## La forma

```
ente/
├── rastro.md         el cuerpo
├── ruta.md           la mente
├── carga.md          el pensamiento
└── …                 los procesos que el ente contiene
```

**El ente no explica: ejecuta.** Lo que no cambia una decisión no vive aquí.

## Qué declara cada pieza

Las tres son **procesos** y se escriben con la forma de `./formato de proceso.md`. Cada una declara, además, lo suyo:

| Pieza | `Entra` | `Sale` | Su marca |
|---|---|---|---|
| **Rastro** | qué hay que verificar | el veredicto de qué hay, qué no se toca y cómo se verifica | el cuerpo que no muta |
| **Ruta** | una petición | la ruta que se carga, o `[VACÍO - SIN RUTA]` | la tabla `Si se va a… Se carga` |
| **Carga** | el ente en uso | qué se pierde si el ente deja de servir | la tabla `Si pasa esto | Se pierde | Y el síntoma es` |

## El sesgo, en las tres

**Cada pieza declara desde dónde mira, y ninguna finge neutralidad:** el Rastro desde dónde se verifica, la Ruta desde dónde se carga, la Carga desde dónde se pierde. **Tres sesgos declarados, un solo cuerpo.**

**Quien abre el ente ve lo mismo y difiere en todo menos en el cuerpo.** El cuerpo solo se interpreta: **si se abre y se declara qué conserva, es lectura; si se abre y no se declara, es invasión.**

## Las tres piezas son procesos

**El ente no es una carpeta con tres archivos de texto: es una carpeta con tres procesos.** Las tres se escriben **con todo el formato de `./formato de proceso.md`**, y cada una declara además lo suyo.

| Pieza | `Entra` | `Sale` | Su marca | Su condicional |
|---|---|---|---|---|
| **Rastro** | qué hay que verificar | el veredicto de qué hay, qué no se toca y cómo se verifica | el cuerpo que no muta | `Sesgo` desde dónde se verifica |
| **Ruta** | una petición | la ruta que se carga, o `[VACÍO - SIN RUTA]` | la tabla `Si se va a… Se carga` | `Sesgo` desde dónde se carga |
| **Carga** | el ente en uso | qué se pierde si el ente deja de servir | la tabla `Si pasa esto | Se pierde | Y el síntoma es` | `Sesgo` desde dónde se pierde |

**Lo que cada pieza debe tener, y sin ello no es proceso del ente:**

1. Los **nueve campos**: `Variables`, `Peor`, `Quién`, `Entra`, `Falla`, `Sale`, `Consume`, `Prueba`, `Falsificador`.
2. Los **cuatro condicionales**: `Sesgo`, `Límite`, `Firma`, `Continuidad`. Las tres piezas del ente son de la base: **ninguna puede declararse sin `Sesgo`.**
3. El **cuerpo en forma**: compuertas numeradas, sin verbos de sugerencia, con rama por defecto.

**Lo que cada pieza no necesita.** No se le pide que repita lo que el formato ya dice: **cita el formato y declara solo lo suyo.**

**Un archivo del ente que no sea una de las tres piezas también es un proceso.** `integridad`, `decisión`, `PROMETEA`, el índice de formas: se escriben igual, con los nueve campos y su cuerpo. **La diferencia es que no son el cuerpo del ente:** el ente se lee con sus tres piezas, y sin ellas es fantasma.

**Prueba:** ¿las tres piezas tienen los nueve campos? ¿las tres declararon su `Sesgo` y su `Firma`? ¿tienen cuerpo en forma y no prosa? ¿los demás procesos del ente siguen el formato?
**Falsificador:** una pieza del ente sin `Sesgo` o sin `Firma`; una pieza escrita como texto y no como proceso; un proceso del ente cuyo cuerpo es una lista de viñetas; una pieza que copia el formato en vez de citarlo.

## Cómo se lee un ente

1. **Abrir `rastro.md`.** Qué hay, qué no se toca, cómo se verifica.
2. **Abrir `ruta.md`.** Qué se carga y cuándo.
3. **Abrir `carga.md`.** Qué se pierde, desde dónde se pierde.
4. **Si falta una de las tres:** se declara fantasma y se pregunta. Rige `./CRITERIO.md`, `Cómo se lee`.
5. **Declarar el criterio y su límite.** `No se aplica a` es obligatorio.

## La identidad del ente

**La identidad es funcional: un nombre y una tarea, no una persona.** Sin identidad no hay sujeto; sin tarea no hay fin.

**Es ente si tiene las tres piezas.** Un paso de `Ouroboros/` lo es. Una sub-tarea es una carpeta de procesos **dentro** de un ente, y no necesita las tres.

## Prueba

¿El ente tiene `rastro.md`, `ruta.md` y `carga.md`? ¿Cada pieza declara su sesgo? ¿El cuerpo sigue sin mutar? ¿El criterio tiene límite declarado?

**Falsificador:** un ente sin una de las tres piezas; una `ruta.md` que no cambia aunque el hoy cambió; una `carga.md` que sobrevive a su fin; un cuerpo abierto sin declarar qué se conserva; un ente que explica en vez de ejecutar.
