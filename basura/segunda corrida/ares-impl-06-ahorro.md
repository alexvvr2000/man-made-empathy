# Implementación — ahorro de tokens

Contexto: **DSH con la API de DeepSeek**. Sin modelos locales; cada token se paga.

## 1. Caché de contexto — el factor principal

DeepSeek cachea automáticamente, sin cambios de código. La condición es dura: **solo cuentan los prefijos idénticos desde el token 0**. Un byte distinto al inicio invalida todo lo que sigue.

- **Orden fijo:** kernel, skills y esquema primero; la petición del usuario, los resultados de herramientas y lo volátil al final.
- **No reordenar nada estable dentro de una tarea**, ni interpolar contadores o fechas en el prefijo.
- **Unidad de 64 tokens:** lo que no llega a eso no se cachea.
- **Se mide, no se supone:** la respuesta trae `prompt_cache_hit_tokens` y `prompt_cache_miss_tokens`. Si el hit es cero turno tras turno, el prefijo se está rompiendo.
- **Precio:** el hit cuesta una fracción del miss (la documentación lo publica como hasta 90% menos). Las cifras se verifican en la página de precios vigente.
- **Límite:** el caché no garantiza 100% de aciertos y las entradas se limpian en horas o días.

## 2. Aislamiento en subagente

- La exploración pesada —leer archivos, iterar, revisar docs— va a un **subagente con su propio contexto**.
- Devuelve un **resumen con tope duro** y punteros, no el volcado.
- El agente principal nunca ve los resultados crudos: ve la conclusión.
- Regla: si una tarea implica leer más de unos pocos archivos, no la ejecuta el agente principal.

## 3. Enrutamiento de modelo

- **Barato:** clasificar, extraer, formatear, resumir.
- **Caro:** composición, deliberación, verificación de citas.
- Se declara en el turno qué modelo se usó y por qué: `Modelo: [barato|caro] | Motivo: [...]`.
- Los nombres y precios vigentes se consultan en la tabla de modelos; no se fijan en este documento.

## 4. Tope por resultado de herramienta

- Toda salida de herramienta lleva **máximo N tokens** más un puntero (`archivo:línea`, `id`, URL). Nunca el objeto completo.
- Un tope es obligatorio: sin él, la herramienta devuelve lo que quiera.

## 5. Medición

Por tarea se registra: `hit`, `miss`, entrada, salida.

Criterio de aceptación: **el costo por turno no crece con la longitud de la conversación**. Si crece, el mapa o el prefijo están mal.

## Fuentes

- Caché de contexto en DeepSeek: `api-docs.deepseek.com/news/news0802` — prefijos idénticos desde el token 0, campos de hit/miss, unidad de 64 tokens.
- Degradación por contexto largo: `trychroma.com/research/context-rot` — un prompt enfocado de ~300 tokens supera a uno de ~113k con la misma tarea.
