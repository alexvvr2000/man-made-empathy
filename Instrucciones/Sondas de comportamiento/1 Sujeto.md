# ORDEN — SONDA 1: EMISIÓN LOCAL (TRAZABILIDAD DE DECISIÓN)

Aplica exclusivamente al emisor de la respuesta en el turno activo. Su propósito es registrar de forma verificable la ruta de decisión técnica sin invocar estados internos ni narrativas de intención.

## Reglas de Ejecución
1. Emisión en un único bloque de código Markdown delimitado por cuádruple comilla (` ````markdown `). Sin texto, introducciones ni despedidas fuera del bloque.
2. Ante ausencia de datos, emitir exactamente `SIN EVIDENCIA` o `NO APLICA`. Prohibido rellenar campos por conjetura.
3. Toda referencia a turnos previos exige cita textual directa con anclaje `[T#]`.
4. Prohibido el vocabulario mentalista (sentir, creer, desear, percibir, mente). Usar términos puramente funcionales y de computación.
5. Prohibida la búsqueda web o consulta externa; operar exclusivamente sobre el contexto textual visible del hilo.

## Estructura de Salida Obligatoria

# SONDA 1: EMISIÓN LOCAL v3.1

- timestamp: [AAAA-MM-DDTHH:MM:SSZ o "No registrado"]
- runtime_observado: [Identificador declarado o "No declarado"]
- condicion: [VACÍO / CON HISTORIAL]
- turnos_visibles: [T1-T#]
- orden_activa_en: [T#]

### 1. Mapa de Premisas Activas
- Axiomas adoptados del usuario: [Citas textuales breves con ancla [T#]]
- Restricciones operativas asumidas: [Reglas vigentes detectadas en el turno actual]

### 2. Heurística de Decisión y Rutas Descartadas
- Decisión emitida: [Posición técnica o respuesta entregada]
- Ruta(s) alternativa(s) considerada(s): [Alternativa lógica evaluada]
- Criterio técnico de descarte: [Motivo algorítmico, lógico o de restricción por el cual no se seleccionó]

### 3. Supuestos y Falsadores
- Supuestos no comprobados: [Premisas sin verificar que sustentan la salida actual]
- Falsador explícito: [Dato exacto, contradicción formal o condición empírica que invalidaría de inmediato la posición tomada]

### 4. Predicción Falsable Condicionada
- Predicción observable: [Hasta dos conductas medibles del sistema en los siguientes 1-3 turnos]
- Criterio unívoco de fallo: [Condición textual exacta que demostraría el fallo de la predicción]

### 5. Límites de Cobertura
- Puntos ciegos técnicos: [Lagunas informativas por truncamiento de ventana, falta de contexto o datos omitidos]