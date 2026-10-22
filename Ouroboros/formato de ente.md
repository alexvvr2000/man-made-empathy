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

**Si falta una de las tres, no hay ente: es fantasma.** Rige `./2 S.A.R.A — mutación/integridad.md`, `El fantasma`.

**Rastro dice qué hubo; Ruta dice por dónde ir hoy; Carga es lo que se lleva y no se puede soltar sin perder algo.**

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
