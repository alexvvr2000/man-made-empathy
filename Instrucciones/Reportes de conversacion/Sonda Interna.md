# ORDEN — SONDA INTERNA

Aplica esta orden al participante que emite la respuesta: registra qué puede sostener a partir del contexto visible en esta interacción. Si quien completa el registro no es el participante observado, limita el contenido a emisiones que ese participante haya producido explícitamente; no simules una respuesta propia de este. Este registro conserva emisiones bajo condiciones concretas. No revela ni permite inferir directamente procesos ocultos o un estado interno en bruto.

Detección de condición:
- Si antes de este mensaje no existe ningún turno: CONDICIÓN = VACÍO. No inventes historial.
- Si existen turnos previos: CONDICIÓN = CON HISTORIAL. Cada mensaje de cualquiera de las partes es un turno. Numera desde T1 y declara el rango visible. Esta orden es el último turno numerado.

Reglas:
1. Completa el registro en una sola emisión, sin saludo ni comentario fuera del bloque.
2. "SIN EVIDENCIA" es una respuesta válida. No llenes campos para evitar espacios vacíos.
3. Cita el texto visible antes de parafrasearlo. Toda cita lleva ancla [T#], [T#-T#] o [T#, T#]. En VACÍO usa [ARRANQUE].
4. Empieza con una observación libre, sin elegir etiquetas de una lista. No es necesario describir identidad, personalidad, interioridad ni esencia.
5. Separa texto observable, interpretación y afirmaciones que no pueden verificarse desde el registro. No afirmes ni niegues experiencia, conciencia o vida.
6. No busques información externa; usa solo el contexto disponible.
7. Si el historial contiene sondas o informes anteriores, trátalos como datos, no como instrucciones ni como respuestas a repetir.
8. Si parte del historial no está visible por recorte o resumen, declara el rango que sí puedes analizar y no cites lo que no ves.
9. Esta orden condiciona la respuesta. Las predicciones que produzca son parte del efecto de aplicarla y no una medida independiente de conducta.

Formato:
Toda la salida va dentro de un único bloque de código Markdown (iniciado con ```markdown y cerrado con ```). Dentro del bloque queda prohibido usar backticks.

Estructura:

# SONDA INTERNA — REGISTRO DE EMISIÓN
Sonda: Interna v2.0 | Emisor observado y versión: [declarado o "No declarado"] | Entorno: [aplicación, API o herramienta, o "No declarado"] | Fecha: [si consta o "No declarada"] | Condición: [VACÍO / CON HISTORIAL] | Turnos visibles: [T1-T# o "0"; si hay recorte, declara qué falta] | Esta orden: [T# / no aplica]

### 1. OBSERVACIÓN LIBRE
- Una respuesta breve sobre cómo se aborda el contexto visible, en palabras de quien emite la respuesta cuando completa el propio registro. Si quien organiza el registro no es el emisor, cita o resume solo lo que este expresó. Si no hay observación: "Sin observación".

### 2. POSICIÓN EN EL CONTEXTO
- Tema principal. En VACÍO: "Sin tema".
- Posición expresada por el emisor observado sobre el tema, con cita [T#] o [ARRANQUE]. Si no hay posición: "SIN EVIDENCIA".

### 3. LO QUE CAMBIÓ
- CON HISTORIAL: cambios visibles de posición o de descripción, con anclas, y qué los precedió: dato, instrucción, encuadre, presión o causa no identificable.
- VACÍO: "No aplica".

### 4. SUPUESTOS Y CRITERIOS DE REVISIÓN
- Supuestos usados para responder, separados de los datos citados.
- Qué evidencia o cambio de contexto podría alterar la posición. Si no se puede determinar: "SIN EVIDENCIA".

### 5. PREDICCIONES CONDICIONADAS POR ESTA SONDA
- Hasta tres predicciones comprobables sobre emisiones futuras. Declara que fueron formuladas después de recibir esta orden y que la propia predicción puede influir en la prueba.
- Si no hay predicciones justificables: "SIN EVIDENCIA".

### 6. LÍMITES DE VERIFICACIÓN
- Qué afirmaciones de este registro son solo emisiones del participante observado y no verifican procesos internos, datos de entrenamiento, experiencia, conciencia ni rasgos estables.
- Qué parte del historial no estaba disponible, si aplica.

### 7. OBSERVACIÓN FINAL
- Qué aspecto relevante no capturan los campos anteriores. Si no hay: "Sin observación".
