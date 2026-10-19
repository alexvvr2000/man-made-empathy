# Reglas de mutación

**Tipo:** reglas. Se aplican, no se ejecutan.
**Alcance:** decidir la etiqueta de una mutación: `agente | instrucción | skill`.
**Versión:** 1.
**Autoridad:** la autoridad máxima es la persona; estas reglas no autorizan. La autorización se otorga aparte; el modelo vive en `./Bases de diseño/Principios para agentes con autoridad/Conversacional.md` (`Modelo de autoridad`).

## Principio

Todo lo ejecutable es una mutación. La etiqueta es conveniencia, no esencia: SARA puede mutar desde su punto inicial a lo que sea. La mutación puede agregar, modificar o eliminar. Estas reglas eligen la etiqueta útil; no crean autoridad.

## Modos

| Modo | Qué hace | Alcance | Triangulación |
|---|---|---|---|
| `clasificar` | candidato nuevo → etiqueta + prueba | solo candidatos | internet + usuario |
| `meta-necesidades` | inventario y necesidad → etiqueta + prueba | solo necesidades | internet + usuario |
| `meta-corroborar` | candidato de cualquier lado → corroboración | solo corroboración | internet solo; sin usuario; una corrida |
| `derivar` | recibe el ejecutable de `novedad` → etiqueta | solo derivados | internet + usuario |

## Criterio

| Etiqueta | Cuándo | Dónde | Prueba |
|---|---|---|---|
| `agente` | entidad persistente con roles, autonomía y memoria; coordina o sobrevive al turno | `wax` | Si no necesita persistencia, no es agente |
| `skill` | capacidad recurrente con trigger, entradas y salidas; se invoca | `~/.dsh/skills/` o SARA skills | Si no se puede invocar como capacidad, no es skill |
| `instrucción` | secuencia de una tarea; no necesita persistencia ni invocación | `./Instrucciones/` | Si no es una secuencia, no es instrucción |

La memoria es una parte; no decide sola. Si la memoria es persistente y la entidad tiene roles y autonomía, la etiqueta útil es `agente`. Si es una capacidad invocable, `skill`. Si es una secuencia, `instrucción`. La etiqueta es una decisión de conveniencia; SARA puede mutar a otra después.

## Triangulación

La triangulación es la de `./Instrucciones/novedad.md` (`Triangulación`): cinco fuentes, externo con veto, prior art, fallo conocido y prueba. Se aplica a la etiqueta. `meta-corroborar` es internet solo, sin usuario, una corrida.

La etiqueta se decide por uso, no por esencia. La prueba de la etiqueta es la de `## Criterio`.

## Falsificadores

- Se etiqueta por esencia y no por uso.
- Se ignora la memoria o la persistencia.
- Se duplica una capacidad o una instrucción.
- Se promueve sin evidencia externa.
- Se etiqueta sin prueba.
- Se auto-proclama autoridad o se auto-autoriza.
- Se emite el contrato del instalador.

## Transiciones

- `agente` → `./Agentes/Proyecto S.A.R.A/wax.md`.
- `skill` → `~/.dsh/skills/` o `./Agentes/Proyecto S.A.R.A/Componentes/skills/`.
- `instrucción` → `./Instrucciones/instruccion-de-autoridad.md`.
- `norma` → `./Novedad/candidatos.md`; no es mutación: la trata `novedad`.
- `En cualquier otro caso` → cerrar.
- Instalador → después; no hay contrato.

## Salida

`Etiqueta: [agente|instrucción|skill] | Prueba: [...] | Evidencia: [...] | Estado: [...]`.

## Test

`Etiqueta por uso → pasa | Por esencia → falla | Sin prueba → falla | Sin externo → observa | Duplica → referencia | Agente sin WAX → falla`.
