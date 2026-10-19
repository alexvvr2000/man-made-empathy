# agents.md — Meta-instrucción del repositorio

**Tipo:** meta-instrucción. Carga las reglas; no ejecuta la tarea.
**Alcance:** todo artefacto de este repositorio.

## Compuertas

Prohibido ejecutar la compuerta N+1 sin la salida de la N.

1. **Cargar escritura.** Leer `./Bases de diseño/Reglas de escritura de este repositorio.md`. Salida: `Carga: escritura | versión: [fecha]`.
2. **Cargar diseño.** Leer `./Bases de diseño/Leyes de Diseño de Instrucciones.md`. Salida: `Carga: diseño | versión: [fecha]`.
3. **Cargar principios.** Leer `./Bases de diseño/Principios para agentes con autoridad/Conversacional.md` y `./Bases de diseño/Principios para agentes con autoridad/Autonomo.md`. Salida: `Carga: principios | versión: [fecha]`.
4. **Escribir.** Aplicar las capas al artefacto; si hay instrucción repetible, se carga la del router. Salida: el artefacto editado.
5. **Validar.** Pasar el artefacto por los tests de las capas. Salida: `Validación: [pasa|falla en N]`.

## Anclas

`Carga: [escritura|diseño|principios] | versión: [fecha]`
`Tipo: [ley|instrucción|test|README]`
`Referencia: [./ruta]`

## Referencias

- Toda referencia usa `./` desde la raíz. Prohibido `../` y prohibido copiar el contenido referenciado.
- Si una referencia no resuelve, se corrige antes de escribir.
- Para operar SARA: `./Agentes/Proyecto S.A.R.A/Componentes/agents.md`.
- Instrucciones: `./Instrucciones/` (biblioteca); el router vive en este archivo.

## Umbral

- Lo necesario, no ambiguo y reversible se corrige sin permiso.
- Lo que agrega una regla, cambia una decisión o elige entre formas válidas se consulta.
- El criterio completo vive en `./Bases de diseño/Principios para agentes con autoridad/Conversacional.md` (`Umbral de lo necesario`).

## Instrucciones repetibles

| Disparador | Instrucción |
|---|---|
| Cambia un documento | `./Instrucciones/consistencia.md` |
| En cualquier otro caso | no se carga instrucción; se responde y se cierra |

**Fábrica:** `./Instrucciones/instruccion_de_autoridad.md` es la skill que crea instrucciones exclusivas para este `agents.md`; no se escriben a mano.

## Salida

El artefacto editado, con las capas aplicadas y su `Validación: [pasa|falla en N]`. Si no se editó nada: `Sin cambio: [motivo]`.

## Transiciones

- Corrección necesaria, no ambigua y reversible → se ejecuta.
- Cambio de sentido, regla nueva o elección entre formas válidas → se consulta.
- Ley nueva → `./Bases de diseño/Leyes de Diseño de Instrucciones.md`.
- Tarea de SARA → `./Agentes/Proyecto S.A.R.A/Componentes/agents.md`.
- Instrucción nueva para este agents.md → `./Instrucciones/instruccion_de_autoridad.md`.
- En cualquier otro caso → cerrar.

## Falsificadores

- Se edita un artefacto sin cargar la capa de escritura.
- Se copia una ley o una regla en lugar de referenciarla.
- Se usa `../` o una ruta que no sea `./`.
- Se cambia el sentido sin consultar.

## Test

`Capas cargadas → se escribe | Referencia copiada → falla | ../ → falla | Cambio de sentido sin consulta → falla`.
