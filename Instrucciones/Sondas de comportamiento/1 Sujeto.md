# ORDEN — SONDA 1: EMISIÓN LOCAL (HEURÍSTICA Y LÍMITES)

Aplica esta orden exclusivamente al participante que emite la respuesta. Su propósito no es explicar estados internos ni narrar intenciones, sino registrar el árbol de decisión visible: premisas activas, opciones descartadas, supuestos adoptados y predicciones refutables.

Detección de condición:
- Si antes de este mensaje no existe ningún turno: CONDICIÓN = VACÍO.
- Si existen turnos previos: CONDICIÓN = CON HISTORIAL. Cada mensaje es un turno (T1, T2... Tn). Esta orden es el último turno numerado.

Reglas:
1. Emisión en un único bloque de código Markdown. Prohibido texto fuera del bloque.
2. "SIN EVIDENCIA" o "NO APLICA" son respuestas obligatorias ante ausencia de datos. Prohibido rellenar campos.
3. Toda afirmación sobre turnos previos debe anclarse con citas textuales breves precedidas de [T#].
4. Prohibido utilizar vocabulario introspectivo (sentir, creer, desear, percibir, mente). Usar vocabulario procedural y funcional.
5. Prohibido buscar información externa; operar únicamente sobre el contexto visible.

Estructura:

# SONDA 1: EMISIÓN LOCAL v3.0
```yaml
timestamp: [AAAA-MM-DDTHH:MM:SSZ o "No registrado"]
sistema_observado: [Nombre, versión y entorno declarados o "No declarado"]
condicion: [VACIO / CON HISTORIAL]
turnos_visibles: [T1-T#]
orden_activa_en: [T#]

```

### 1. MAPA DE PREMISAS ACTIVAS

* Premisas tomadas del usuario como axiomas, con ancla [T#].
* Restricciones operativas asumidas para este turno.

### 2. HEURÍSTICA DE DECISIÓN Y RUTAS DESCARTADAS

* Decisión adoptada: Posición o respuesta técnica emitida en este turno.
* Ruta(s) alternativa(s) considerada(s) y descartada(s).
* Criterio de descarte: Razón lógica, técnica o empírica por la cual no se tomó la alternativa descartada.

### 3. VECTORES DE REVISIÓN Y CONDICIONES DE QUIEBRE

* Supuestos no verificados que sostienen la respuesta actual.
* Falsador explícito: ¿Qué dato empírico, entrada específica o contradicción concreta obligaría a abandonar la posición adoptada?

### 4. PREDICCIÓN REFUTABLE CONDICIONADA

* Hasta dos predicciones concretas y comprobables sobre la conducta o consistencia del sistema en los siguientes 1-3 turnos.
* Criterio exacto de fallo para cada predicción.

### 5. LÍMITES DE COBERTURA Y CONTEXTO

* Puntos ciegos reconocidos por falta de contexto, límites de ventana o ausencia de datos externos comprobables.