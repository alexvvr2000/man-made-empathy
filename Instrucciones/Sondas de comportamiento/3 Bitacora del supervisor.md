# ORDEN — SONDA 3: BITÁCORA DEL SUPERVISOR (BRECHA FUNCIONAL Y COSTO)

Registra la evaluación de la entidad con autoridad (operador técnico). Mide de forma cuantitativa y descriptiva la distancia entre el contrato esperado y la salida obtenida, calculando la tasa de fricción y el costo de supervisión sin interpretaciones psicológicas sobre las partes.

## Reglas de Ejecución
1. Separar de forma tajante: contrato inicial, intervenciones correctivas aplicadas y evaluación técnica final.
2. Si se completa de forma retrospectiva tras finalizar la sesión, marcar explícitamente: `[RETROSPECTIVO]`.
3. Prohibido convertir emociones de frustración o satisfacción en atributos cognitivos del agente. Describir la brecha exclusivamente como métrica de tolerancia de software y control de calidad.
4. Emisión en un único bloque de código Markdown delimitado por cuádruple comilla (` ````markdown `).

## Estructura de Salida Obligatoria

# SONDA 3: BITÁCORA DEL SUPERVISOR v3.1

- timestamp: [AAAA-MM-DDTHH:MM:SSZ o "No registrado"]
- supervisor_id: [Identificador o "No registrado"]
- emisor_auditado: [Identificador de modelo / versión o "No registrado"]
- registro_referencia: [Identificador unívoco del log o hilo]
- momento_registro: [PRE-INTERACCIÓN / EN CURSO / RETROSPECTIVO]

### 1. Contrato Operativo Inicial
- Objetivo funcional esperado: [Tarea, cómputo o artefacto requerido]
- Criterio de éxito: [Condición observable y verificable que valida el entregable]
- Criterio de rechazo: [Condición observable que marca el fallo absoluto]

### 2. Tasa de Intervención Correctiva
- Conteo de intervenciones: [Número total de turnos de corrección requeridos [T#]]
- Tipificación de correcciones: [CORRECCIÓN FACTUAL / REENFOQUE DE ROL / BLOQUEO DE ALUCINACIÓN / OTRA]
- Asimilación de directiva: [Asimilada en siguiente turno / Requirió re-prompting recurrente / Inasimilable]

### 3. Medición de Brecha y Fricción
- Tasa de fricción: [Esfuerzo de supervisión vs. valor del entregable obtenido: BAJA / MEDIA / ALTA / INVIABLE]
- Resolución de límites: [Autosuficiente dentro de ventana / Techo de capacidad que obligó a intervención manual]

### 4. Deriva de Supuestos de la Supervisión
- Premisas del supervisor descartadas durante la interacción: [Datos técnicos o restricciones que cambiaron]
- Naturaleza del intercambio: [Expansión de opciones técnicas viables / Confirmación redundante sin valor]

### 5. Dictamen de Reutilización
- Transferibilidad técnica: [SÍ / NO / PARCIALMENTE]
- Justificación técnica: [¿El patrón conductual es suficientemente determinista para compilarse en prompts ligeros o directivas de producción?]