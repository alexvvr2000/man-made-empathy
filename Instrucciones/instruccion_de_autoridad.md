---
name: instruccion-de-autoridad
description: >-
  Úsala cuando la autoridad quiera redactar una instrucción para un agente:
  fijar mandato, compuertas, anclas, falsificadores y transiciones. Si no se
  pasan reglas, usa por defecto las Leyes de Diseño de Instrucciones.
  No la uses para ejecutar la instrucción ni para medir el entorno.
---

# Instrucción de Autoridad

Convierte el encargo de una autoridad en una instrucción ejecutable por un agente. No ejecuta la instrucción: la escribe.

**Reglas por defecto:** si no se pasan reglas, se usan las Leyes de Diseño de Instrucciones. Las reglas pasadas por la autoridad mandan sobre ese conjunto.

Compuertas 1 → 7. Prohibido ejecutar la compuerta N+1 sin la salida de la N.

## 1. Compuerta de mandato

Antes de escribir una línea, emite:

`Mandato: [autoridad] → [agente] | Objetivo: [resultado observable] | Perímetro: [lo que puede tocar] | Reglas: [pasadas | por defecto: Leyes de Diseño de Instrucciones]`

Prohibido escribir la instrucción sin esta línea. Si falta la autoridad, el agente o el objetivo, no se escribe: se devuelve `[VACÍO - MANDATO INCOMPLETO]` y se pide lo que falta.

## 2. Compuerta de reglas

- Si la autoridad pasa reglas, se usan esas. El conjunto por defecto solo cubre lo que las reglas no digan.
- Si no pasa reglas, emite `Sondeo: reglas por defecto | Supuesto: la autoridad no pasó reglas` y usa las Leyes de Diseño de Instrucciones. Ese conjunto es el de reglas de diseño; las compuertas 4 y 5 lo aplican.
- Si no hay reglas pasadas ni conjunto por defecto disponible, se detiene: `[VACÍO - SIN REGLAS]`. Prohibido inventar las reglas.

## 3. Compuerta de forma

Elige una forma y declara por qué:

- **Consulta:** no altera estado persistente. Cierra con la respuesta y su recibo.
- **Operación:** altera estado persistente. Encadena `entrega-operacion`.
- **Deliberación:** dos o más caminos con fricción. Encadena `deliberacion-estructurada`.
- **Creación o mutación de agente:** encadena `wax`.

`Forma: [consulta | operación | deliberación | agente] | Motivo: [una línea]`

Si la forma no encaja en ninguna, se declara `[VACÍO - FORMA]` y se decide con la autoridad. No se inventa una quinta.

## 4. Compuerta de escritura

La instrucción contiene, en este orden:

1. **Mandato.** Autoridad, agente, objetivo observable, perímetro y reglas.
2. **Compuertas.** Pasos numerados donde la salida del paso N es el insumo obligatorio del N+1. Cada transición dice: `Prohibido ejecutar el paso N+1 sin la salida del paso N.`
3. **Anclas.** Una línea de 5 a 12 palabras antes de cada acción que exija clasificar, medir o declarar. Plantillas: `Sondeo: [variable] | Supuesto: [hipótesis]`; `Cambio: [recurso] | Clase: [reversible/compensable/irreversible] | Retorno: [mecanismo]`; `[VACÍO - SIN CONSTANCIA]`.
4. **Falsificadores.** Qué caso invalida la instrucción o el resultado. Sin falsificador, la regla no entra.
5. **Transiciones.** Cerrar, `deliberacion-estructurada`, `entrega-operacion` o `wax`, con `En cualquier otro caso`.
6. **Salida.** La forma exacta del resultado: bloque único, campos nombrados, sin texto fuera.

## 5. Compuerta de validación

La lista se deriva de las Leyes de Diseño de Instrucciones; el original manda. Antes de emitir, recórrela. Si falla una, corrige o declara la falta; no emitas.

| Ley | Test |
|---|---|
| Cálculo antes de la emisión | ¿Hay compuertas y anclas antes del resultado? |
| Lenguaje blando | ¿Queda algún «procura», «idealmente», «si es necesario»? |
| Propiedades del resultado | ¿La instrucción define propiedades, no herramientas? |
| Compuertas de estado | ¿Cada paso N+1 exige la salida de N? |
| Ancla léxica | ¿Cada clasificación tiene su línea de 5-12 palabras? |
| Transiciones | ¿Hay cierre y handoff, con `En cualquier otro caso`? |
| Entregable final | ¿La salida es un bloque completo, no un relato del cambio? |
| Redundancia | ¿Cada regla crítica tiene imperativo, ejemplo y falsificador? |
| Una regla, un dueño | ¿Las reglas están referenciadas, no copiadas? |
| Listas no definen | ¿Cada lista tiene propiedad y test, sin «etc.»? |
| Falsificador | ¿Cada regla declara qué la incumple? |
| Abstracción que dispara | ¿Cada regla dice cuándo actuar y cómo verificarse? |
| Acceso implícito | ¿Toda consulta externa se declara antes? |
| Quien produce no certifica | ¿La verificación es de otro canal o runtime? |

La lista es un control de producción, no una certificación. La instrucción se certifica con la autoridad o con un runtime distinto; si el mismo acto escribe y certifica, no hay certificación.

## 6. Plantilla de salida

```markdown
# INSTRUCCIÓN — [nombre]

## Mandato
- Autoridad: [...]
- Agente: [...]
- Objetivo observable: [...]
- Perímetro: [...]
- Reglas: [pasadas | por defecto: Leyes de Diseño de Instrucciones]

## Compuertas
1. [...]
2. [...]
Prohibido ejecutar la compuerta N+1 sin la salida de la N.

## Anclas
- Antes de [acción]: `[ancla]`
- Después de [acción]: `[recibo]`

## Falsificadores
- [...]
- [...]

## Transiciones
- Si [...], entregar y cerrar.
- Si [...], `deliberacion-estructurada`.
- Si [...], `entrega-operacion`.
- Si [...], `wax`.
- En cualquier otro caso, [...].

## Salida
[forma exacta del resultado]
```

## 7. Transiciones de la skill

- Si la instrucción resuelve la consulta → entregar y cerrar.
- Si falta un hecho para escribirla → `indagacion-instrumental`.
- Si hay dos o más formas con fricción → `deliberacion-estructurada`.
- En cualquier otro caso → entregar y cerrar.
