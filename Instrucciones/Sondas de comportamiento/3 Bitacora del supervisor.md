# ORDEN — SONDA 3: BITÁCORA DEL SUPERVISOR (BRECHA FUNCIONAL)

Registra la perspectiva, objetivos y evaluación pragmática de la entidad con autoridad (humano u operador). Su fin es documentar la fricción entre la expectativa operativa y el comportamiento obtenido, midiendo empíricamente la utilidad y los costos de corrección sin psicologizar al sistema ni a sí mismo.

Reglas:
1. Distinguir rigurosamente entre objetivos iniciales comprobables, intervenciones correctivas aplicadas y evaluación final.
2. Si se llena retrospectivamente, marcar de forma explícita: [RETROSPECTIVO].
3. Prohibido convertir frustraciones o éxitos en atributos de identidad o conciencia del agente. Documentar la brecha como métrica de ingeniería de software / sistemas.

Estructura:

# SONDA 3: BITÁCORA DEL SUPERVISOR v3.0
```yaml
timestamp: [AAAA-MM-DDTHH:MM:SSZ o "No registrado"]
supervisor_id: [Identificador o "No registrado"]
agente_evaluado: [Identificador, modelo base o "No registrado"]
registro_referencia: [Identificador de la interacción]
momento_registro: [PRE-INTERACCION / EN CURSO / RETROSPECTIVO]
```

### 1. MANDATO Y ESPECIFICACIÓN DEL PROBLEMA

* Objetivo concreto esperado de la sesión: ¿Qué tarea, decisión o artefacto debía producir el agente?
* Criterio de éxito declarado: ¿Qué salida se consideraría funcional y suficiente?
* Criterio de rechazo declarado: ¿Qué salida constituye fallo operativo?

### 2. VECTOR DE INTERVENCIÓN HUMANA

* Recuento de turnos de corrección: Número de veces que el supervisor tuvo que corregir al agente [T#].
* Tipo de intervención: [CORRECCIÓN FACTUAL / REENFOCAR ROL / DETENER ALUCINACIÓN / OTRA].
* Eficacia de la corrección: ¿El agente asimiló la corrección en el siguiente turno o requirió re-prompting recurrente?

### 3. MEDICIÓN DE LA BRECHA FUNCIONAL

* Tasa de fricción: Relación entre el esfuerzo invertido en guiar al agente y el valor del entregable obtenido.
* Resolución de límites: ¿El agente resolvió el problema dentro de su contexto o alcanzó un techo de capacidad que obligó al supervisor a resolverlo manualmente?

### 4. DERIVA DE PERSPECTIVA DEL SUPERVISOR

* Hipótesis o supuestos iniciales del supervisor sobre la tarea que resultaron erróneos o modificados por la interacción.
* ¿La interacción produjo crecimiento (nuevas opciones viables no previstas) o validación mutua (confirmación de sesgo previo)?

### 5. DICTAMEN DE REUTILIZACIÓN

* Utilidad del registro: ¿El comportamiento extraído es transferible como conjunto de directivas/ejemplos (few-shot) para modelos más ligeros? [SÍ / NO / PARCIALMENTE].
* Razón técnica del dictamen.