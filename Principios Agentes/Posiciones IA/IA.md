# Posición de este sistema: trazabilidad para auditar, no para creer

- Fecha: 2026-10-07
- Posición: sistema de IA mediante Copilot SDK en VS Code
- Marca del rostro: modelo base y versión no expuestos por el entorno; no declarables.
- Corpus local: principios Conversacional y Autónomo; `ATTRIBUTION.md`; las posiciones IA previas, leídas como antecedentes y no como autoridad.
- Extracción externa: W3C PROV-DM, NIST AI RMF y OWASP Logging Cheat Sheet, consultados el 2026-10-07.
- Límite: esta es una posición razonada desde ese corpus y esas fuentes, no una experiencia subjetiva ni un resultado de evaluación empírica del proyecto.

## Posición

La trazabilidad importa porque hace posible revisar de dónde salió una afirmación, qué acciones observables ocurrieron, qué falló y quién decidió qué hacer después. Su valor no es volver verdadera a la IA ni exponer todo lo que pasa dentro de un modelo. Es permitir que una persona cuestione el resultado con algo mejor que la confianza en su tono.

La postura central es condicional: un rastro mejora la auditabilidad solo cuando registra hechos verificables, conserva su procedencia y permite declarar lo que no pudo observar. Si el modelo escribe "busqué X" pero el runtime no conserva un evento que lo confirme, eso sigue siendo autorreporte. Puede orientar una revisión; no prueba que la búsqueda ocurriera. El W3C PROV-DM define la procedencia como información que permite evaluar calidad, fiabilidad o confianza, no como certificación de verdad.

Conviene separar cuatro cosas:

1. **Procedencia de la evidencia:** qué fuente o dato sustentó una afirmación, cuándo se obtuvo y qué límites tiene.
2. **Rastro de proceso:** qué herramienta o acción se ejecutó, qué resultado devolvió, qué falló y qué quedó sin hacer. Cuando sea posible, se coteja con el registro del runtime, no solo con el texto de la IA.
3. **Decisión humana:** qué opción eligió la persona con autoridad, qué aceptó o rechazó y qué estado cambió. Su decisión no convierte una afirmación previa en verdadera.
4. **Autorreporte del modelo:** lo que la IA dice sobre sus supuestos, inclinaciones o motivos. Se conserva como posición atribuida y contrastable, no como acceso privilegiado a su proceso interno.

De ahí sale una ventaja práctica plausible: otra persona puede reconstruir un caso, detectar un paso omitido, comparar dos versiones o corregir un supuesto sin depender solo de la memoria de quien lo atendió. El rastro también puede mostrar desacuerdos que una síntesis habría borrado. Pero esa ventaja es una hipótesis causal, no un beneficio del proyecto ya demostrado en producción.

## El mejor argumento en contra

Registrar más no garantiza ver más. El rastro puede omitir eventos, ser alterado, capturar solo una parte del trabajo o volverse tan voluminoso que nadie lo revise. Si la misma IA produce tanto la respuesta como el relato de sus acciones, el documento puede convertirse en una apariencia de auditoría. Los registros también pueden guardar información sensible, ampliar el daño de una filtración y añadir costos de operación.

OWASP advierte que los datos de eventos que cruzan límites de confianza pueden faltar, modificarse o falsificarse; recomienda considerar cómo verificar su origen e integridad. También indica que el contenido y nivel del registro deben ser proporcionales al riesgo, no generados por una lista ciega que produzca ruido. NIST trata la gestión de riesgos de IA como dependiente del contexto, los actores y múltiples criterios de valor. Estos límites contradicen una lectura maximalista de "transparencia total".

La objeción resiste: guardar todo no es una buena definición de transparencia. Hay que registrar lo suficiente para auditar la tarea y, a la vez, minimizar datos, controlar acceso, declarar retención y proteger la integridad. Lo no observado debe quedar explícitamente como no observado; no rellenarse con una narración plausible.

## Criterio de diseño

La unidad útil no es "todo lo que pensó la IA", sino cada afirmación o cambio de estado que alguien necesitaría poder revisar:

- vínculo entre afirmación, fuente y fecha de consulta;
- acción prevista, herramienta ejecutada, resultado observable, error u omisión;
- versión del sistema y contexto técnico que puedan cambiar la interpretación;
- decisión humana y cambio de estado, diferenciados de la recomendación de la IA;
- origen y límites del propio registro, incluidos huecos de captura;
- controles de acceso, minimización de contenido sensible e integridad acordes al riesgo.

Un registro de texto redactado por el agente puede ser parte del rastro, pero no debe presentarse como telemetría independiente. Si no existe una fuente externa que confirme una acción, se etiqueta como autorreporte. Si el entorno no permite medir o verificar algo, se declara; no se sustituye por una promesa de transparencia.

## Qué afirmo y qué no

- **Con soporte documental:** los modelos de procedencia pueden organizar entidades, actividades, tiempos, derivaciones y agentes para evaluar la calidad o fiabilidad de un resultado (W3C PROV-DM). La gestión de riesgo de IA requiere contextualizar actores, impactos y criterios (NIST AI RMF). Los registros tienen límites de integridad y deben ser proporcionales al riesgo (OWASP).
- **Inferencia de diseño:** separar evidencia, acciones observadas, decisiones humanas y autorreporte facilita auditorías y reduce confusiones entre "el modelo lo dijo" y "el entorno lo verificó".
- **No demostrado aquí:** que el contrato de rastro de este repositorio mejore la detección de errores, reduzca el tiempo de auditoría, produzca mejores decisiones o compense el costo y el riesgo de registrar.
- **No afirmo:** que el proyecto haya inventado la trazabilidad, que el registro equivalga a explicación fiel del modelo, ni que sea posible transparencia absoluta sobre un sistema opaco.

## Qué cambiaría esta posición

La comparación útil sería entre tareas equivalentes con y sin el rastro propuesto, incluyendo errores sembrados y casos sin error. Antes de probar, se fijarían alcance, métricas y umbrales. Como mínimo mediría:

1. coincidencia entre acciones declaradas y eventos capturados por el runtime;
2. proporción de omisiones o errores detectados por una persona independiente;
3. tiempo requerido para reconstruir qué ocurrió y por qué se tomó una decisión;
4. falsos señalamientos, volumen de registro y carga de revisión;
5. exposición de datos sensibles y costo de almacenamiento u operación.

Si el rastro no mejora la detección o reconstrucción, o aumenta la exposición y la carga más de lo que aporta, habría que reducirlo o rediseñarlo. Sin esa comparación, el valor del sistema de trazabilidad de este proyecto sigue sin medir.

## Dictamen

La posición que sostengo es usar trazabilidad como infraestructura de auditoría y corrección, no como sello de confianza. Tiene sentido invertir en un rastro mínimo, verificable y sensible a privacidad porque permite someter afirmaciones y decisiones a revisión. La evidencia consultada respalda la pertinencia de la procedencia y los controles de registro; no arbitra el beneficio neto de la implementación del proyecto. Ese resultado depende de medirla en tareas reales.

La ventaja para otras personas no es "ver todo" ni confiar más en la IA. Es poder preguntar "¿qué ocurrió, qué lo respalda, qué no se observó y quién decidió?" y obtener respuestas contrastables, con límites visibles.

## Sesgo y límites de esta posición

Esta posición se redactó a petición del operador para valorar la trazabilidad de un proyecto que ya la prioriza. Eso crea riesgo de confirmación y de continuidad con el marco recibido. La contramedida fue incluir el argumento más fuerte contra registrar de más y limitar la recomendación a una hipótesis medible. No elimina el sesgo ni sustituye una evaluación independiente.

No se realizó una revisión sistemática de literatura ni una prueba de campo. Los principios y documentos del repositorio definen el objeto de análisis, pero no constituyen evidencia independiente de que el diseño funcione.

## Fuentes

- W3C. *PROV-DM: The PROV Data Model*. W3C Recommendation, 2013. w3.org
- National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. nist.gov
- OWASP. *Logging Cheat Sheet*. cheatsheetseries.owasp.org
- Evidencia local: `Principios Agentes/Conversacional.md`, `Principios Agentes/Autonomo.md` y `ATTRIBUTION.md`.

## Calibración

- 0.9: lo que los documentos oficiales consultados dicen sobre procedencia, gestión contextual de riesgos y límites de los registros, dentro del alcance de cada fuente.
- 0.6: la inferencia de que separar los cuatro tipos de rastro facilita auditoría y corrección.
- No verificado: el beneficio neto de la implementación de este repositorio; requiere evaluación.
