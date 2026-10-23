# El estándar

**Unidad:** nivel.
**Aplica a:** fijar la forma.
**Tipo:** estándar. No decide, no ejecuta: fija la forma de lo que se puede sostener.
**Lector:** quien va a mutar los tres pasos, y quien va a leer el conjunto sin poder preguntar.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el estándar se lee desde la tesis que lo sostiene, no desde el catálogo de procesos que lo llenan.
**Límite:** no produce implementación. Fija la forma; los tres pasos la mutan.
**Cuelga de:** `../Tesis/LA-TESIS.md`. Sin ella, estos procesos son una lista.
**Deja de valer:** cuando la tesis que los sostiene cae. Si la tesis se tumba, los procesos se revisan en el mismo acto.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** forma · tesis · proceso · acuñación · pegamento
**Peor:** el estándar tiene procesos completos y ningún principio que los una. Se lee entero, no se entiende nada, y cada paso de los tres lo interpreta distinto.
**Quién:** quien muta un paso y no sabe si el proceso que aplica sigue colgando de la tesis.

## Qué es

**El estándar no es un catálogo de procesos. Es la forma que la tesis le da a todo lo que se puede sostener.**

**La tesis dice qué se sostiene. El estándar dice con qué forma. Los tres pasos dicen qué se hace hoy.**

```
TESIS        →   ESTÁNDAR        →   LOS TRES PASOS
qué se sostiene     con qué forma       qué se hace hoy
LA-TESIS.md         Ouroboros/Estandar  Guantelete → VIDERE → ATLAS
```

**Y ahí está lo que faltaba:** el estándar **estaba metido dentro de los tres pasos**, y por eso se borraba cuando un paso se borraba. **Ahora es una pieza propia, y los tres se mutan contra él.**

## El pegamento, y por qué es la fricción

**Los procesos de este estándar no se unen porque compartan campos. Se unen porque la misma fricción los atraviesa.**

| En la tesis | En el estándar |
|---|---|
| **verbalizar es el primitivo** | `./verbalizar.md`: sin eso no hay fricción posible |
| **una pieza sin fricción no existe** | `./friccion.md`: lo que hace que algo exista |
| **el error tiene dónde ser visto** | `./sesgo.md`: desde dónde se mira, y quién lo contesta |
| **mutar, no cambiar** | `./mutacion.md`: transformar desde un punto de referencia |
| **sin registro no hay reparación** | `./memoria.md`: la posición, no el hecho |

**Cada uno de esos cinco es un proceso que se ejecuta y deja veredicto.** **Ninguno es definición: todos se corren.**

## Cómo se lee

1. **`../Tesis/LA-TESIS.md`.** Qué se sostiene. Sin esto, el estándar es una lista.
2. **`./proceso.md`.** La forma: nueve campos, cuatro condicionales, cuerpo en compuertas.
3. **`./ente.md`**, **`./piso.md`**, **`./criterio.md`.** La forma del ente, del piso y de la decisión.
4. **Los cinco primitivos del pegamento.** `verbalizar`, `friccion`, `sesgo`, `mutacion`, `memoria`.
5. **Los cinco que la tesis produjo.** `tiempo`, `diferencia`, `union`, `entrega`, `flujo`.
6. **`./ACERO.md`.** La regla de cierre: cuándo algo está terminado de verdad.

**Un proceso que no cuelga de ninguno de los seis se declara, y no se aplica.**

## Qué hay aquí

| Archivo | Qué fija | Cuelga de |
|---|---|---|
| `proceso.md` | la forma de todo proceso: nueve campos y cuatro condicionales | la forma, no la tesis |
| `ente.md` | qué es un ente: tres piezas, no tres textos | `proceso.md` |
| `piso.md` | qué hace a una unidad piso | `friccion.md` |
| `criterio.md` | la puerta entre los tres pasos | `sesgo.md` |
| `ACERO.md` | cuándo algo se sostiene: no «tiene los campos», sí «resistió» | `friccion.md` |
| `verbalizar.md` | el primitivo de la tesis | `../Tesis/LA-TESIS.md` |
| `friccion.md` | la fuerza que hace que algo exista | `verbalizar.md` |
| `sesgo.md` | desde dónde se sostiene una pieza | `friccion.md` |
| `mutacion.md` | transformar desde un punto de referencia | `sesgo.md` |
| `memoria.md` | guardar posiciones, no hechos | `mutacion.md` |
| `tiempo.md` | el tiempo del otro, y el prestado | `memoria.md` |
| `diferencia.md` | lo pedido, el puente, el intento, la holgazanería | `tiempo.md` |
| `union.md` | trazabilidad, entendibilidad, repetibilidad | `tesis` |
| `entrega.md` | cinco piezas y una pregunta | `union.md` |
| `flujo.md` | Guantelete → VIDERE → ATLAS y la existencia | `piso.md` |

## Lo que el estándar no hace

**No ejecuta nada.** Fija la forma; los tres pasos la aplican.

**No juzga si sirve.** Un proceso puede tener todo el formato y no servir; eso lo decide `./ACERO.md` con la fricción que resistió.

**No crece por acumulación.** Si un proceso nuevo no nombra una resistencia que ninguno otro atiende, **no entra.**

## Prueba

¿Cada archivo de este estándar cuelga de la tesis o de otro que sí cuelga? ¿Cada proceso tiene los nueve campos y su `Falsificador`? ¿Cada pieza declara `Deja de valer`? ¿Puede leerse el conjunto sin el que lo escribió?

**Falsificador:** un proceso sin `Falsificador`; un archivo que no declara de qué cuelga; un estándar que es un catálogo sin pegamento; un proceso escrito como ensayo; una pieza sin `Deja de valer`.

## Transiciones

- La tesis muta → el estándar se revisa en el mismo acto.
- Un proceso nuevo no nombra resistencia nueva → no entra: es acumulación.
- Un proceso deja de oponerse a algo → se retira, con su porqué anotado.
- Los tres pasos mutan → lo hacen **contra** este estándar, no por su cuenta.
- En cualquier otro caso → se entrega con su forma y se cierra.
