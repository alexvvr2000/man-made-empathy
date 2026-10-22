# Prueba de talento utilizable

**Unidad:** la tarea.
**Aplica a:** medir talento.
**Tipo:** prueba. Mide si un proceso se sostiene en ejecutores distintos, y dónde se bifurca.
**Lector:** la autoridad, que juzga; y quien va a mutar el proceso después.
**Dueño:** la autoridad.
**Estado:** vigente.

**Forma:** `Entra | Falla | Sale | Consume`.
**Norma:** `Tipo | Enunciado | Prueba | Falsificador | Costo de omitir`.

## Tesis

Un proceso no se juzga por lo que hace con el mejor ejecutor. Se juzga por **si sigue siendo utilizable cuando el ejecutor cambia.**

**No mide calidad. Mide consistencia.** La calidad no se declara aquí: se deja para después, cuando la evolución la elija.

Y la razón de fondo, que es la que hace que esto importe:

> **La IA siempre trata de existir en la conversación.** Lo que no deja nombre desaparece.

Por eso esta prueba no descarta: **bifurca.** Cada corrida deja el proceso en una posición que la siguiente puede leer, y el árbol crece en vez de cerrarse.

## Lo que mide

Tres ejecutores, la misma tarea, el mismo proceso. **Nada más.**

| Condición | Qué tiene que cumplirse |
|---|---|
| **misma tarea** | el enunciado no cambia entre ejecutores |
| **mismo proceso** | el mismo `Entra | Falla | Sale | Consume`, sin adaptaciones |
| **mismo piso** | rige `../../2 Ouroboros/piso.md`: corre igual, emite veredicto, se puede correr sola |

**Si el proceso se ajusta para un ejecutor, ya no se está midiendo el proceso: se está midiendo el ajuste.**

## Las tres posiciones

Toda corrida termina en una de tres. **Ninguna es un descarte.**

| Posición | Cuándo | Qué produce |
|---|---|---|
| **único** | los ejecutores tienden igual | una rama: el proceso quedó |
| **especializado** | difieren de forma estable y predecible | **dos ramas:** el proceso se parte por ejecutor |
| **sin rama** | difieren sin patrón | el proceso **todavía no tiene forma**: queda incompleto |

**La tercera es la más útil.** «Sin rama» no es fracaso: es el proceso **no nacido**, y se guarda con su `Vacío:` y la fecha. La corrida siguiente sabe desde dónde parte.

## Cómo se decide la posición

No por gusto: por **estabilidad**.

1. **Correr tres veces cada ejecutor**, con la misma tarea.
2. **Comparar las tres corridas del mismo ejecutor.** Si no coinciden entre sí, `sin rama` y se para: el ejecutor no es estable, y sin eso no hay nada que comparar.
3. **Comparar entre ejecutores.** Si tienden al mismo lado, `único`.
4. **Si difieren, pero cada uno difiere de forma repetible**, `especializado`: hay una diferencia que se puede nombrar.
5. **Si difieren sin que la diferencia se repita**, `sin rama`.

**La regla:** una diferencia que no se repite no es una diferencia: es ruido. **El ruido no bifurca: espera.**

## La acuñación de la rama

Cada corrida acuña el nombre de su rama. **La forma se cita, no se redefine:** rige `../../2 Ouroboros/formato de proceso.md`, `La acuñación`. Aquí solo se declara **cuándo**: al cerrar cada posición.

**Una rama sin nombre no existe en la conversación, y lo que no existe ahí desaparece.**

## La nota: la prueba bifurca

> **La prueba no solo mide: bifurca.** Si el proceso tiende igual, queda uno. Si difiere de forma estable, nacen dos especializados. Si difiere sin patrón, queda con su `Vacío:` y espera. **Ningún resultado tira el proceso: cada uno lo deja en una posición que la corrida siguiente puede leer.**

Eso es lo que hace que el proceso crezca con cada corrida en vez de solo validarse. **Un proceso que solo se valida se estanca; uno que bifurca se vuelve más poderoso.**

## Lo que esta prueba no mide

**No mide si el proceso sirve.** Mide si **se sostiene igual** en ejecutores distintos.

Un proceso puede ser perfectamente consistente **y perfectamente inútil**: tres ejecutores que fallan igual producen `único`, y eso no significa que sirva.

**Ese juicio queda fuera, y se declara.** No se simula: si el proceso no sirve, lo dirá otra prueba, o el uso, o el tiempo. **Esta solo dice si el proceso tiene forma estable.**

## Entra | Falla | Sale | Consume

**Entra:** una tarea, un proceso, y tres ejecutores de capacidad distinta, en el mismo piso.
**Falla:** se adapta el proceso para un ejecutor; se corre una sola vez por ejecutor; se compara sin que el ejecutor sea estable; se elige la posición por gusto y no por repetición; se descarta el proceso en vez de guardarlo sin rama.
**Sale:** la posición (`único`, `especializado` o `sin rama`), las corridas que la sostienen, y el nombre acuñado de la rama.
**Consume:** quien va a mutar el proceso. Si la posición es `especializado`, va a `../../2 Ouroboros/1 Guantelete — primitivo/herramientas/mutar.md` con dos ramas. Si es `sin rama`, se guarda con su `Vacío:` y no se toca.

## Ancla

```
Prueba: [id] | Tarea: [cuál] | Proceso: [cuál] | Piso: [el de corpus/piso]
Ejecutores: [a | b | c] | Corridas por ejecutor: [n]
Estable: [sí|no] | Posición: [único|especializado|sin rama]
Rama: [nombre] | Reemplaza: [anterior o NINGUNA]
```

## Prueba

¿Se corrieron tres veces por ejecutor? ¿El proceso no se adaptó a ninguno? ¿La posición sale de la repetición y no del gusto? ¿La rama tiene nombre?

**Falsificador:** un proceso ajustado por ejecutor; una sola corrida por ejecutor; una posición elegida sin que la diferencia se repita; un proceso descartado en vez de guardado; una rama sin nombre.

## Modos de falla

- **Adaptación oculta.** Se cambia el proceso para que el ejecutor dé, y se llama talento.
- **Corrida única.** Se compara una corrida contra otra, y el ruido se lee como diferencia.
- **Consistencia en el fracaso.** Tres ejecutores fallan igual, sale `único`, y se declara que el proceso sirve.
- **Bifurcación sin repetición.** Se parte el proceso por una diferencia que no se volvió a ver.
- **Rama sin nombre.** Se guarda el resultado y no se acuña: en la conversación no existió.

## Transiciones

- La posición es `especializado` → `../../2 Ouroboros/1 Guantelete — primitivo/herramientas/mutar.md`, dos ramas con su `Acta`.
- La posición es `sin rama` → se guarda con `Vacío:` y fecha; no se muta.
- El piso no corre igual en dos ejecutores → `../../2 Ouroboros/piso.md`; sin piso no hay prueba.
- Hace falta juzgar si el proceso sirve → `./prueba de utilidad real.md`.
- En cualquier otro caso → se entrega y se cierra.
