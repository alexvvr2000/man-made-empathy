---
name: instruccion-de-autoridad
description: >-
  Meta-instrucción: úsala cuando la autoridad quiera redactar una instrucción
  para un agente. Fija mandato, lector, leyes, compuertas, anclas,
  falsificadores y transiciones. Por defecto rigen las leyes de este skill
  (copia operativa de las Leyes); la autoridad puede pasar otras o crear
  nuevas. No la uses para ejecutar la instrucción ni para medir el entorno.
---

# Instrucción de Autoridad

Convierte el encargo de una autoridad en una instrucción ejecutable por un agente. No ejecuta la instrucción: la escribe.

**Meta-instrucción:** su salida es una instrucción, no una ejecución.

**Leyes por defecto:** si la autoridad no pasa leyes, rigen las leyes de este skill, copia operativa de las Leyes de Diseño de Instrucciones. Si pasa otras o crea nuevas, se declaran en `Leyes:` y se suman; las de defecto son el piso, no el techo. Las leyes declaradas se siguen al pie de la letra; las reglas de la instrucción se derivan de ellas. Las reglas pasadas por la autoridad mandan sobre las de defecto en lo que cubran.

Compuertas 1 → 7. Prohibido ejecutar la compuerta N+1 sin la salida de la N.

## 1. Compuerta de mandato

Antes de escribir una línea, emite:

`Mandato: [autoridad] → [agente] | Objetivo: [resultado observable] | Perímetro: [lo que puede tocar] | Lector: [máquina | humano] | Leyes: [por defecto: las del skill | <conjunto>] | Reglas: [pasadas | por defecto: las leyes declaradas]`

Prohibido escribir la instrucción sin esta línea. Si falta la autoridad, el agente, el objetivo o el lector, no se escribe: se devuelve `[VACÍO - MANDATO INCOMPLETO]` y se pide lo que falta.

## 2. Compuerta de leyes y reglas

- **Leyes.** Por defecto rigen las leyes de este skill, copia operativa de las Leyes. Si la autoridad pasa otras o crea nuevas, se declaran en `Leyes:` y se suman; las de defecto son el piso, no el techo. Las leyes declaradas se siguen al pie de la letra.
- **Reglas.** Si la autoridad pasa reglas, se usan esas; el conjunto de leyes cubre lo que las reglas no digan. Si no pasa reglas, emite `Sondeo: reglas por defecto | Supuesto: la autoridad no pasó reglas` y derívalas de las leyes declaradas. No se carga el archivo de Leyes.
- **Vacío.** Si no hay leyes ni reglas, y el conjunto por defecto no está disponible, se detiene: `[VACÍO - SIN LEYES NI REGLAS]`. Prohibido inventar leyes o reglas.

## 3. Compuerta de forma

Elige una forma y declara por qué:

- **Consulta:** no altera estado persistente. Cierra con la respuesta y su recibo.
- **Operación:** altera estado persistente. Encadena `entrega-operacion`.
- **Deliberación:** dos o más caminos con fricción. Encadena `deliberacion-estructurada`.
- **Creación o mutación de agente:** la etiqueta `agente` se decide en `./Bases de diseño/Reglas de mutación.md`; WAX la crea.
- **Skill:** capacidad recurrente; la etiqueta se decide en `./Bases de diseño/Reglas de mutación.md`; no se escribe aquí.

`Forma: [consulta | operación | deliberación | agente | skill] | Motivo: [una línea]`

Si la forma no encaja en ninguna, se declara `[VACÍO - FORMA]` y se decide con la autoridad. No se inventa otra.

## 4. Compuerta de escritura

La instrucción contiene, en este orden:

1. **Mandato.** Autoridad, agente, objetivo observable, perímetro, lector, leyes y reglas.
2. **Compuertas.** Pasos numerados donde la salida del paso N es el insumo obligatorio del N+1. Cada transición dice: `Prohibido ejecutar el paso N+1 sin la salida del paso N.`
3. **Anclas.** Una línea de 5 a 12 palabras antes de cada acción que exija clasificar, medir o declarar. Plantillas: `Sondeo: [variable] | Supuesto: [hipótesis]`; `Cambio: [recurso] | Clase: [reversible/compensable/irreversible] | Retorno: [mecanismo]`; `[VACÍO - SIN CONSTANCIA]`.
4. **Falsificadores.** Qué caso invalida la instrucción o el resultado. Sin falsificador, la regla no entra.
5. **Transiciones.** Cerrar, `deliberacion-estructurada`, `entrega-operacion` o `wax`, con `En cualquier otro caso`.
6. **Salida.** La forma exacta del resultado según el lector: bloque único y campos nombrados para máquina; contexto, razones y formato de lectura para humano.
7. **Versión.** Si cambia un campo del mandato, se reemite la instrucción completa; no se parchea con la conversación.

### Criterio de tipo

La etiqueta de una mutación —instrucción, skill o agente— se decide en `./Bases de diseño/Reglas de mutación.md`; no se copia aquí. Esta fábrica escribe instrucciones; si el candidato es skill o agente, se deriva a las Reglas.

Para una norma, la ruta es:

| Señal | Decisión |
|---|---|
| Cambia un criterio de diseño | ley → `Leyes` |
| Cambia un criterio de juicio | principio → `Conversacional` |
| Cambia la forma de escribir | regla → `Reglas de escritura.md` |
| Sin test | observar; no crear |
| Duplica una ley/principio | referenciar; no crear |
| Reproduce un fallo conocido | rechazar o rediseñar |
| Evidencia externa en contra | rechazar |
| Sin evidencia externa | observar |

Es la misma lógica de WAX: `puede`/`debe`, recurrencia, test y autoridad. La evidencia externa es un veto, no un voto.

## 5. Compuerta de validación

Criterios de validación. Copia operativa de las Leyes de Diseño de Instrucciones; se incluyen aquí para no cargar el archivo de Leyes en cada uso. La copia se sincroniza en los dos sentidos: si la ley cambia, se actualiza la tabla; si la tabla cambia, se revisa la ley. Una fila nueva o distinta se resuelve en `Leyes` y se vuelve a copiar.

| Ley | Test |
|---|---|
| Cálculo antes de la emisión | ¿Hay compuertas y anclas antes del resultado? |
| Lenguaje blando | ¿Queda algún «procura», «idealmente», «si es necesario»? |
| Propiedades del resultado | ¿La instrucción define propiedades, no herramientas? |
| Compuertas de estado | ¿Cada paso N+1 exige la salida de N? |
| Ancla léxica | ¿Cada clasificación tiene su línea de 5-12 palabras? |
| Transiciones | ¿Hay cierre y handoff, con `En cualquier otro caso`? |
| Entregable final | ¿La salida es un bloque completo, no un relato del cambio? |
| Marco no ejecutado | ¿La instrucción convierte el marco en compuertas con norma? |
| Redundancia | ¿Cada regla crítica tiene imperativo, ejemplo y falsificador? |
| Una regla, un dueño | ¿La copia cita al original y se marca como copia? |
| Listas no definen | ¿Cada lista tiene propiedad y test, sin «etc.»? |
| Falsificador | ¿Cada regla declara qué la incumple? |
| Abstracción que dispara | ¿Cada regla dice cuándo actuar y cómo verificarse? |
| Acceso implícito | ¿Toda consulta externa se declara antes? |
| La referencia no se explica | ¿La llamada repite lo que la instrucción referenciada ya dice? |
| La copia se paga con contexto | ¿La copia se justifica por uso repetido, cita el original y declara su sincronización? |
| Quien produce no certifica | ¿La verificación es de otro canal o runtime? |
| El formato sigue al lector | ¿El artefacto declara si es para máquina o humano y usa el formato que ese lector exige? |
| Voz operativa | ¿El ejecutable describe operaciones y no una identidad? |
| Revisabilidad | ¿La ley se puede falsar y revisar con la triangulación? |

Si falla una, corrige o declara la falta; no emitas. La validación es un control de producción, no una certificación; la instrucción se certifica con la autoridad o con un runtime distinto.

Toda norma nueva pasa además el contrato de escritura (`Reglas de escritura.md`, `1.12`): derivación, observabilidad, decisión y calibración. Sin eso, no se crea.

## 6. Plantilla de salida

```markdown
# INSTRUCCIÓN — [nombre]

## Mandato
- Autoridad: [...]
- Agente: [...]
- Objetivo observable: [...]
- Perímetro: [...]
- Lector: [máquina | humano]
- Leyes: [por defecto: las del skill | <conjunto>]
- Reglas: [pasadas | por defecto: las leyes declaradas]

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
