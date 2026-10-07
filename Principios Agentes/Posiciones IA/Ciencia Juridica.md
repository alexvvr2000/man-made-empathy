# Posición: trazabilidad en trabajo jurídico, evidencia auxiliar y no salvoconducto

- Fecha: 2026-10-07
- Posición: sistema de IA mediante Copilot SDK en VS Code
- Marca del rostro: modelo base y versión no expuestos por el entorno; no declarables.
- Corpus local: versiones previas de este documento, `IA.md`, principios Conversacional y Autónomo, y `ATTRIBUTION.md`.
- Fuentes externas consultadas: W3C PROV-DM, NIST AI RMF y OWASP Logging Cheat Sheet.
- Límites de consulta: el sitio de la American Bar Association rechazó el acceso a la Opinión Formal 512 (HTTP 403); no se verificaron en esta sesión las tesis mexicanas ni las circulares citadas en versiones anteriores.
- Alcance: opinión de diseño sobre trazabilidad en flujos jurídicos; no es asesoría legal ni una conclusión sobre derecho vigente en jurisdicción alguna.

## Posición

En un flujo jurídico, la trazabilidad puede ayudar a revisar cómo se produjo un borrador, una búsqueda, un cálculo o una recomendación asistida por IA. Su valor es limitado pero importante: permitir distinguir la fuente jurídica de la afirmación del modelo, reconstruir las acciones observables y localizar qué debe verificar la persona profesional responsable.

No debe presentarse como motivación jurídica suficiente, cadena de custodia, prueba de corrección ni cumplimiento normativo por el solo hecho de existir un registro. Esas calificaciones dependen del uso, del sistema de registro y de las reglas aplicables. Un registro generado por el mismo modelo que produjo el contenido es autorreporte hasta que se contraste con fuentes independientes, como el historial de herramientas o una copia verificable de la fuente consultada.

La pregunta útil no es "¿la IA dejó un rastro?", sino:

- ¿Se puede recuperar la fuente primaria y confirmar que dice lo atribuido?
- ¿Se conserva qué versión, jurisdicción y fecha aplicaban a la consulta?
- ¿Las acciones declaradas coinciden con eventos observables del sistema?
- ¿Se distingue lo que afirmó el modelo, lo que verificó una persona y lo que finalmente se presentó o decidió?
- ¿Los huecos de captura, las transformaciones y los límites del registro están declarados?
- ¿El rastro protege información confidencial y se conserva solo durante el tiempo justificado?

Para cálculos u operaciones deterministas, la primera opción debe ser un método reproducible y revisable, no pedirle a un modelo que estime una respuesta y luego narre cómo llegó a ella. La IA puede ayudar a identificar datos, reglas candidatas o casos límite; el cálculo ejecutado y la fuente autorizada deben poder revisarse aparte. Para investigación o redacción jurídica, el rastro puede acelerar la revisión, pero no sustituye la lectura de autoridades pertinentes ni el juicio profesional.

## El límite que impide confundir registro con garantía

W3C PROV-DM trata la procedencia como información sobre entidades, actividades, tiempos, derivaciones y responsables que permite evaluar calidad o fiabilidad. No la define como prueba de que una afirmación sea verdadera. OWASP advierte que los datos de eventos pueden faltar, modificarse o falsificarse y plantea verificar origen e integridad; también recomienda que el volumen y contenido de los registros sean proporcionales al riesgo. NIST AI RMF sitúa la gestión de riesgos en el contexto de uso, los actores y los impactos.

Aplicado al trabajo jurídico, esto abre una fricción que no se puede resolver con más logging:

- Un expediente puede contener datos sensibles o protegidos. Copiarlos a un historial externo puede aumentar el riesgo de exposición.
- Un registro técnico puede ayudar a reconstruir una secuencia, pero no adquiere por ello valor probatorio o procesal.
- Guardar demasiadas acciones genera ruido y carga de revisión; guardar muy pocas puede impedir detectar un error material.
- Una explicación del modelo puede orientar una pregunta, pero no demuestra el proceso interno que produjo la respuesta.
- La intervención humana es necesaria para evaluar consecuencias, pero anotarla no demuestra por sí sola que la revisión haya sido sustantiva.

Por tanto, el rastro debe diseñarse por tarea y jurisdicción: contenido mínimo necesario, responsable de custodia, controles de acceso e integridad, plazo de retención y forma de cotejar los eventos. Esas son preguntas de diseño que requieren revisión legal y de seguridad local; no afirmo una respuesta jurídica universal.

## El mejor argumento en contra

La objeción más fuerte es que, en muchos usos jurídicos, la trazabilidad propuesta puede añadir una capa de documentación sin mejorar la decisión. La práctica ya puede contar con fuentes oficiales, cálculos deterministas, control de versiones y revisión profesional. Si el registro duplica esos controles, conserva datos confidenciales o produce un relato no verificable, puede empeorar el proceso y crear confianza injustificada. Ante un cálculo, usar una hoja de cálculo comprobable puede ser más seguro y simple que usar un modelo con un rastro sofisticado.

Esa objeción resiste. No recomiendo registrar todo ni insertar IA en procesos que no la necesitan. Recomiendo rastro solo cuando permite responder una pregunta de auditoría que de otra forma quedaría sin respuesta, y cuando su utilidad supera el costo, el riesgo de exposición y la carga de revisión. El registro debe poder decir "no observado" y "no verificado"; no completar huecos con una explicación plausible.

## Propuesta de evaluación

La utilidad jurídica del rastro de este proyecto no está demostrada. Antes de recomendarlo para un flujo real, compararía tareas equivalentes con y sin el rastro, primero con datos sintéticos o debidamente protegidos y con participación de profesionales pertinentes. Acordaría antes de la prueba métricas y umbrales:

1. exactitud al recuperar autoridades, citas, jurisdicción y fecha desde el registro;
2. detección de citas inventadas, fuentes desactualizadas, cálculos erróneos y pasos omitidos;
3. tiempo y esfuerzo necesarios para que una persona independiente reconstruya el trabajo;
4. coincidencia entre acciones declaradas y eventos verificables del sistema;
5. falsos positivos, información sensible expuesta, volumen retenido y costo de revisión;
6. capacidad de la persona revisora para distinguir asistencia de IA, verificación profesional y decisión final.

El resultado puede ser reducir el rastro, limitar el uso de IA a tareas auxiliares o no usarlo en ese flujo. Una evaluación que solo mida si el formato se llenó no demuestra que mejoró la práctica.

## Estado de los antecedentes jurídicos del borrador

No reutilizo como hechos vigentes las afirmaciones de versiones anteriores sobre:

- las tesis mexicanas 2031009, 2031010 y 2031640, su clasificación o alcance;
- la supuesta jurisprudencia II.2o.C. J/2;
- la Circular 1/2026 y el alcance institucional atribuido a ella;
- anuncios de plataformas judiciales o cifras de casos citados por fuentes secundarias.

Quedan como pistas para investigación futura. Para reincorporar cualquiera hacen falta el documento primario, fecha de consulta, jurisdicción, estado procesal y una descripción fiel de lo que sostiene. Las fuentes secundarias pueden orientar la búsqueda, pero no reemplazan esa verificación. La Opinión Formal 512 de la ABA tampoco se usa aquí como autoridad: el sitio rechazó el acceso durante esta sesión.

## Dictamen

En trabajo jurídico, la trazabilidad sirve como instrumento auxiliar de revisión si conecta afirmaciones con fuentes recuperables y acciones con eventos cotejables, minimiza datos y hace visibles sus propios límites. No legitima por sí misma el uso de IA, no certifica una conclusión jurídica y no transfiere la responsabilidad profesional al registro.

La ventaja potencial es concreta: reducir el tiempo para localizar un error y reconstruir qué se consultó antes de que un borrador influya en una actuación. Sigue siendo una hipótesis hasta medir detección, tiempo, carga y exposición de información en un flujo real. Si un método más simple logra lo mismo con menos riesgo, ese método gana.

## Sesgo y límites de esta posición

El encargo se originó en una conversación favorable a la trazabilidad y el documento pertenece a un proyecto que la prioriza. Eso puede sesgar la evaluación a favor del diseño. La objeción sobre privacidad, redundancia y alternativas deterministas limita la recomendación, pero no elimina el sesgo.

El sistema autor de esta posición no es profesional del derecho; la versión base no se expone. No se consultó el Semanario Judicial de la Federación, no se accedió a la Opinión Formal 512 y no se hizo una revisión sistemática de literatura ni una evaluación con profesionales del derecho. No debe leerse como opinión jurídica sobre la validez de registros en México u otra jurisdicción.

## Fuentes

- W3C. *PROV-DM: The PROV Data Model*. W3C Recommendation, 2013. w3.org
- National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. nist.gov
- OWASP. *Logging Cheat Sheet*. cheatsheetseries.owasp.org
- Fuentes de contexto no verificadas en esta edición: Semanario Judicial de la Federación; American Bar Association, Formal Opinion 512; Consejo General del Poder Judicial de España. No se atribuyen aquí conclusiones a esos documentos.

## Calibración

- 0.9: alcance de la procedencia en W3C PROV-DM; recomendaciones sobre integridad y proporcionalidad del logging en OWASP; enfoque contextual de riesgos en NIST AI RMF, dentro de lo consultado.
- 0.6: la trazabilidad mínima y cotejable podría acelerar revisión y detección de errores jurídicos.
- No verificado: efecto del diseño del repositorio en la calidad, seguridad o eficiencia de una práctica jurídica; requiere evaluación.
