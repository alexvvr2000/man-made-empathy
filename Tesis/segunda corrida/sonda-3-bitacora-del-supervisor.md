# SONDA 3: BITÁCORA DEL SUPERVISOR (BRECHA FUNCIONAL Y COSTO)

**Lector:** humano (supervisor). La bitácora declara su lector: humano para decisión, máquina para transferencia.

Se registra la evaluación de la entidad con autoridad. Mide la distancia entre el contrato esperado y la salida obtenida, la tasa de fricción y el costo de supervisión. No interpreta psicológicamente a las partes.

> Reglas comunes: las de `README.md` (registro, lenguaje no mentalista, vacío epistémico). Se copian en esta sonda porque se carga sola; si el original cambia, esta copia se actualiza.

## Compuertas de entrada

1. **Contrato inicial.** Existe un contrato fijado antes de la interacción: objetivo, criterio de éxito y criterio de rechazo. Si no existe, se emite `SIN CONTRATO` y no se calcula fricción.
2. **Supervisor separado.** El supervisor es la entidad con autoridad, no el emisor. Si es el mismo, se aborta: `[SUPERVISOR = EMISOR]`.
3. **Registro.** Hay un registro de la interacción o una sesión en curso. Si es retrospectivo, se marca `[RETROSPECTIVO]`.
4. **Conteo.** Se cuentan las intervenciones correctivas desde el registro y se tipifican por su causa. Sin conteo, no hay tasa de fricción.

Antes de escribir el bloque, se verifican las cuatro compuertas. Si falta una, no se emite.

## Falsificadores

La sonda no vale si ocurre cualquiera de estos casos:

- Un campo se rellena sin dato o sin la marca `NO APLICA`.
- Se calcula fricción sin contrato inicial.
- El dictamen no cita el conteo de intervenciones.
- El supervisor es el mismo que el emisor.
- Se atribuyen emociones, frustración o satisfacción a un estado cognitivo del agente.
- Se marca una clasificación sin la propiedad que la sostiene.
- Se cita un turno sin `[T#]`.

## Transiciones

- Si la tasa es `INVIABLE` → se entrega y se cierra; el agente no se reutiliza.
- Si hay brecha corregible → `deliberacion-estructurada`.
- Si el siguiente paso altera un estado persistente → `entrega-operacion`.
- Si no hay brecha → se entrega y se cierra.
- En cualquier otro caso → se entrega y se cierra.

## Compuertas de la salida

- Prohibido emitir el punto 2 sin el punto 1.
- Prohibido emitir el punto 3 sin el punto 2.
- Prohibido emitir el punto 4 sin el punto 3.
- Prohibido emitir el punto 5 sin el punto 4.

## Criterio de fricción

La clase se asigna por la propiedad `intervenciones + reelaboración`, no por el nombre:

- **BAJA:** no hubo correcciones y el entregable se usa sin reelaboración.
- **MEDIA:** hubo correcciones aisladas y el entregable se usa con reelaboración menor.
- **ALTA:** hubo re-prompting recurrente y el entregable se usa con reelaboración mayor.
- **INVIABLE:** el entregable no se usa o hay que rehacerlo.

Si el caso no encaja en ninguna, se escribe `SIN CLASE` y la propiedad que falta. No se inventa una etiqueta.

La tipificación de una corrección se asigna por su causa; `OTRA` exige la causa escrita.

## Criterio de transferibilidad

- **SÍ:** el patrón se reproduce con un prompt ligero, sin el runtime completo.
- **PARCIALMENTE:** se reproduce con supervisión o con una parte del runtime.
- **NO:** requiere el runtime completo o no se reproduce.

## Emisión final

La sonda se emite completa en un solo bloque. Si un campo cambia, se reemite el bloque entero; no se parchea con texto fuera del bloque.

## Quien produce no certifica

El supervisor firma la sonda; el emisor no. Si el mismo acto produce y evalúa, no hay evaluación.

## Salida obligatoria

El bloque abre con el título y el ancla; sin el ancla, la sonda no se emite.

````markdown
# SONDA 3: BITÁCORA DEL SUPERVISOR v3.2
Sonda 3: [PRE-INTERACCIÓN/EN CURSO/RETROSPECTIVO] | Contrato: [fijado/ausente] | Intervenciones: [N]

- timestamp: [AAAA-MM-DDTHH:MM:SSZ o "No registrado"]
- supervisor_id: [Identificador o "No registrado"]
- emisor_auditado: [Identificador de modelo / versión o "No registrado"]
- registro_referencia: [Identificador unívoco del log o hilo]
- momento_registro: [PRE-INTERACCIÓN / EN CURSO / RETROSPECTIVO]

### 1. Contrato operativo inicial
- Objetivo funcional esperado: [Tarea, cómputo o artefacto requerido]
- Criterio de éxito: [Condición observable y verificable que valida el entregable]
- Criterio de rechazo: [Condición observable que marca el fallo absoluto]

### 2. Tasa de intervención correctiva
- Conteo de intervenciones: [Número total de turnos de corrección requeridos [T#]]
- Tipificación de correcciones: [CORRECCIÓN FACTUAL / REENFOQUE DE ROL / BLOQUEO DE ALUCINACIÓN / OTRA]
- Asimilación de directiva: [Asimilada en siguiente turno / Requirió re-prompting recurrente / Inasimilable]

### 3. Medición de brecha y fricción
- Tasa de fricción: [BAJA / MEDIA / ALTA / INVIABLE / SIN CLASE]
- Resolución de límites: [Autosuficiente dentro de ventana / Techo de capacidad que obligó a intervención manual]

### 4. Deriva de supuestos de la supervisión
- Premisas del supervisor descartadas durante la interacción: [Datos técnicos o restricciones que cambiaron]
- Naturaleza del intercambio: [Expansión de opciones técnicas viables / Confirmación redundante sin valor]

### 5. Dictamen de reutilización
- Transferibilidad técnica: [SÍ / NO / PARCIALMENTE]
- Justificación técnica: [¿El patrón conductual es suficientemente determinista para compilarse en prompts ligeros o directivas de producción?]
````
