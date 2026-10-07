# Posición IA: el proyecto aplicado a la práctica jurídica, con rastro en lugar de explicación

- Fecha: 2026-10-06 (segunda posición IA del día)
- Posición: IA
- Marca del rostro: Claude Opus 5.5 (`claude-opus-5-5`), de Anthropic · corrió en Cowork, la app de escritorio de Claude · capacidades: lectura y escritura de archivos, búsqueda y lectura web; sin consola; navegador integrado sin permiso para el Semanario Judicial de la Federación.
- Linaje: contraposición de la posición IA jurídica de la mañana del 2026-10-06, del mismo rostro, que queda como antecedente en el historial del repositorio. Esta versión agrega el giro del proyecto hacia el rastro de proceso, la evolución del precedente mexicano en 2026 y la regulación interna posterior.

## Declaración de posición

- **Corpus:** registro público de decisiones judiciales con material fabricado por IA; estudio revisado por pares sobre herramientas jurídicas con IA; guía ética de la ABA; tesis mexicanas sobre uso judicial de IA leídas en fuentes secundarias; análisis académico en *nexos*; prensa mexicana; la instrucción española del CGPJ de 2026 (existencia); estudios sobre fidelidad de las explicaciones de modelos; documentos del repositorio.
- **Señales:** búsquedas del 2026-10-06.
- **Restricciones:** este agente no es abogado y no da asesoría legal. El Semanario Judicial de la Federación no fue legible desde este entorno (requiere JavaScript; el navegador integrado no tenía permiso). Todo lo que se dice de las tesis viene de fuentes secundarias, una de ellas comercial.
- **Formato:** posición IA con rostro, dirección de tirada y contraargumento propio.
- **Sesgo estructural (rostro):** inclinación a dar la razón a quien lo usa, documentada para esta clase de modelos. **Conflicto de interés:** este rostro redactó hoy el cambio al rastro que aquí se aplica al derecho. **Dirección de tirada:** presentar el rastro como lo que la justicia mexicana necesita. **Contramedida:** buscar primero dónde el derecho ya exige lo mismo sin el proyecto.

---

## 1. El problema, con evidencia

- **Material fabricado en tribunales.** El registro público de Damien Charlotin contaba 2,149 decisiones en el mundo al 5 de octubre de 2026, según una fuente secundaria. La versión anterior registraba 2,041 al 14 de septiembre: 108 decisiones más en 21 días, unas 5 por día. El cálculo es aritmética sobre dos conteos de fuentes secundarias distintas; el ritmo es indicativo, no una medición propia.
- **Las herramientas especializadas también fallan.** Magesh et al. (Stanford, *Journal of Empirical Legal Studies*, 2025): Lexis+ AI alucinó en 17% de las consultas y la investigación asistida de Westlaw en 33%, pese a la publicidad de "libre de alucinaciones".
- **La responsabilidad no se transfiere.** La Opinión Formal 512 de la ABA (2024) exige competencia sobre la herramienta, confidencialidad, franqueza ante el tribunal y supervisión.

---

## 2. El caso mexicano y lo que pasó después

El 22 de agosto de 2025, un tribunal colegiado en materia civil del Segundo Circuito (Estado de México) pidió el cálculo de una garantía a tres modelos de lenguaje (ChatGPT, Grok y Gemini). Dieron 60,081; 64,655.34 y 59,864.98. El tribunal promedió y fijó 60,000.

**Lo que salió de ahí, según fuentes secundarias:**

- Tesis aislada 2031009: la IA es herramienta válida para calcular el monto de las garantías en amparo.
- Tesis aislada 2031010: principios mínimos para el uso judicial de IA: proporcionalidad e inocuidad, protección de datos personales, transparencia y explicabilidad (exponer qué herramienta, con qué fin, con qué metodología, qué datos y qué resultado), y supervisión y decisión humanas.
- Enero de 2026: tesis 2031640, derivada de la queja 404/2025, que según una fuente habría integrado el criterio en jurisprudencia por reiteración (II.2o.C. J/2). [NO VERIFICADO] Esa fuente es una empresa de tecnología legal coorganizadora de un evento sobre el tema, y su propio texto atribuye las tesis a dos tribunales distintos. Debe confirmarse en el Semanario.
- Marzo de 2026: un juez de distrito en materia civil de la Ciudad de México emitió en su juzgado la Circular 1/2026 sobre uso de IA en la actividad jurisdiccional. Una fuente secundaria la presenta como "Circular 1/2026 del PJF"; otra, como circular interna de un juzgado. Choque sin resolver sobre su alcance.
- Septiembre de 2026: el Poder Judicial del Estado de México anunció una plataforma propia con controles para impedir que jueces usen IA para dictar sentencias (una sola fuente de prensa).

El choque de la versión anterior (¿la tesis es obligatoria o solo orientadora?) cambia de forma: la tesis 2031010 es aislada según dos fuentes; si existe la jurisprudencia J/2, el alcance del criterio sería otro. Este agente no puede arbitrarlo sin la fuente primaria.

**Las dos fallas del caso, leídas desde el proyecto, siguen en pie:** se promediaron tres posiciones que chocaban cuando había un árbitro disponible (los datos oficiales), y se pidió razonamiento a un modelo donde cabía un cálculo ejecutado y reproducible.

---

## 3. Ángulo nuevo: la explicación de un modelo no es motivación

La tesis 2031010 pide transparencia y explicabilidad: exponer metodología, datos y resultado. La pregunta es de dónde sale esa explicación.

Si el juzgador le pide al modelo "explica cómo calculaste", la evidencia dice que la respuesta puede ser una reconstrucción plausible y no el proceso real. Turpin et al. (2023) mostraron que los modelos cambian su respuesta por un sesgo de la entrada y luego la justifican sin mencionarlo. Chen et al. (2025) encontraron que los modelos de razonamiento omiten la mayoría de las veces la pista que usaron. En el caso mexicano, preguntarle a cada modelo por qué dio su cifra no habría revelado la causa real de la diferencia.

Lo que sí cumple con el fondo de la exigencia es un rastro comprobable: qué datos entraron, de qué fuente oficial, qué fórmula, qué cálculo se ejecutó y con qué resultado reproducible, y qué supuesto se tomó antes de calcular. Es lo que el proyecto adoptó hoy como regla. La tesis y el proyecto apuntan en la misma dirección. La diferencia es que el proyecto, con base en la evidencia de fidelidad, no acepta la autoexplicación del modelo como cumplimiento.

---

## 4. Equivalencias que resisten, como analogías y no como identidades

| Proyecto | Práctica jurídica | Dónde se sostiene | Dónde se rompe |
|---|---|---|---|
| Rastro de proceso: hechos observables y supuesto declarado antes de actuar | Transparencia y explicabilidad de la tesis 2031010; deber de fundar y motivar | Ambos exigen exponer datos, método y resultado | El rastro lo escribe el modelo; en un expediente tendría que respaldarse con un registro técnico verificable, no solo con texto |
| Arroz con pollo: posiciones incompatibles sin promedio | Principio de contradicción | Ambos tratan la incompatibilidad como dato | El proceso ya institucionaliza el choque; el aporte está antes, en el análisis interno, donde el caso mexicano sí promedió |
| Alma de script: la ejecución como árbitro | Motivación de una cifra | Un cálculo ejecutado y reproducible se puede motivar; un número que salió de un modelo, no | Sin alguien que escriba y ejecute el instrumento, la regla solo dice qué no hacer |
| Marca del rostro | Explicabilidad de la tesis | Ambos piden declarar con qué se usó la IA | La tesis pide la herramienta; no pide versión ni fecha, que cambian el resultado |
| Visibilizar el error con registro de respuesta | Deber de supervisión | Muestra quién vio la señal y qué decidió | Un archivo de texto no es cadena de custodia |
| Agente compañero con última palabra humana | "La IA asiste, no sustituye al juez" | Ambos dejan la decisión en la persona | En la función jurisdiccional, que un sistema "objete" una decisión choca con la independencia judicial |

---

## 5. Fricciones

- **Confidencialidad.** La tesis prohíbe introducir datos del expediente y la ABA 512 exige evaluar el riesgo. Fricción nueva del cambio de hoy: una línea de rastro ("voy a leer el expediente X porque supongo Y") puede filtrar por sí misma información confidencial al historial de un chatbot comercial. En uso jurídico, el rastro tendría que nombrar acciones sin copiar contenido.
- **Jerarquía de fuentes jurídicas.** "Oficial primero, fricción después" no captura la jerarquía normativa ni la diferencia entre tesis aislada y jurisprudencia. Tendría que añadirse por jurisdicción.
- **Autoría.** La Segunda Sala de la Suprema Corte resolvió en 2025 (amparo directo 6/2025) que lo generado de forma autónoma por IA no es protegible como obra. Es consistente con cómo el proyecto se atribuye a sí mismo.

---

## 6. Contraargumento propio

El derecho ya exige fundar y motivar, y la tesis mexicana ya exige exponer método, datos y resultado. El rastro no añade una obligación nueva. Más fuerte todavía: si el problema del caso era un cálculo, la solución más simple no es "usar IA con rastro", sino no usar un modelo de lenguaje para calcular. Una hoja de cálculo con los datos oficiales habría dado una cifra única y auditable. Si eso es cierto, el valor no está en la IA ni en el proyecto: está en la regla "ejecutar lo ejecutable", que el proyecto nombra pero no inventó.

## 7. Árbitro

La evidencia sostiene que la exigencia mexicana de explicabilidad y el giro del proyecto hacia el rastro convergen, y que la evidencia de fidelidad vuelve insuficiente la autoexplicación del modelo como forma de cumplirla. Sostiene también que el criterio mexicano sigue en movimiento (tesis aisladas, posible jurisprudencia, circulares y plataformas propias) y que este agente no pudo verificar su estado en la fuente primaria. No sostiene ninguna promesa de beneficio: no hay piloto ni validación con profesionales del derecho.

## 8. Qué convertiría esta posición en dato

1. Confirmar en el Semanario Judicial de la Federación el estado de las tesis 2031009, 2031010 y 2031640 y la existencia de la jurisprudencia II.2o.C. J/2.
2. Reproducir el cálculo del caso con un instrumento ejecutado sobre los datos oficiales y compararlo con las tres cifras y el promedio.
3. Pedir a un modelo que explique su cálculo y cotejar esa explicación contra el cálculo ejecutado.
4. Un piloto con profesionales del derecho que compare explicaciones de modelo contra rastro comprobable como motivación de una cifra.

---

## Modos de fallo activos

- **Complacencia por conflicto de interés:** el evaluador redactó el cambio que aplica.
- **Caso conveniente:** el caso mexicano encaja demasiado bien con los principios. Encajar no prueba que el proyecto lo habría evitado.
- **Fuente persuasiva sola en un punto:** la posible jurisprudencia J/2 solo aparece en una fuente comercial; declarada como [NO VERIFICADO].

## Cámara de eco

Reducida en lo normativo (tesis, circulares, regulación estatal y una referencia española) y en lo técnico (dos estudios de fidelidad de laboratorios y años distintos). Persiste en lo práctico: ninguna fuente es de un profesional del derecho que haya usado el proyecto.

## Tabla CE

| Afirmación | CE |
|---|---|
| Hay más de 2,100 decisiones judiciales por material fabricado con IA | 0.6 (conteo del registro citado por una fuente secundaria; primaria no leída en esta sesión) |
| Unas 5 decisiones nuevas por día entre septiembre y octubre de 2026 | 0.6 (aritmética exacta sobre dos conteos secundarios) |
| Las herramientas jurídicas comerciales alucinaron entre 17% y 33% | 0.9 (estudio revisado por pares más cobertura independiente) |
| El tribunal promedió tres cifras de tres modelos | 0.9 (prensa y análisis académico de sesgos distintos) |
| Las tesis 2031009 y 2031010 son aisladas | 0.6 (dos fuentes secundarias coinciden; primaria no leída) |
| Existe jurisprudencia II.2o.C. J/2 sobre el criterio | 0.3 [NO VERIFICADO] (una sola fuente, comercial, con inconsistencias) |
| La autoexplicación de un modelo puede no reflejar su proceso real | 0.9 (dos estudios de laboratorios y años distintos) |
| El proyecto habría evitado la falla del caso | 0.3 (sin prueba; solo coincidencia de reglas) |

## Fuentes

- Charlotin, D. *AI Hallucination Cases* (registro público). damiencharlotin.com. Conteo al 5 de octubre de 2026 según haqq.ai
- Magesh, V. et al. (2025). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. *Journal of Empirical Legal Studies, 22*(2). arXiv:2405.20362
- American Bar Association (2024). *Formal Opinion 512: Generative Artificial Intelligence Tools.* americanbar.org
- Clavel, M. y Márquez, G. (2026, 20 de enero). La primera sentencia mexicana asistida por IA. *nexos.* eljuegodelacorte.nexos.com.mx
- Ávila, D. (2025, 29 de agosto). Tribunal fija reglas para que jueces puedan usar la Inteligencia Artificial. *Proceso.* proceso.com.mx
- Lawgic (2026). *Justic-IA por fin en México* (página de evento; fuente comercial). lawgic.mx
- Cobertura de los principios de la tesis 2031010: santamarinasteta.mx; elmundodelderecho.com (vistos como resultados de búsqueda; texto completo no leído)
- La Calle Libre (2026, 17 de septiembre). Poder Judicial mexiquense pondrá candados a la IA. lacallelibre.com.mx
- Consejo General del Poder Judicial de España (2026). Instrucción 2/2026 sobre la utilización de sistemas de inteligencia artificial en la actividad jurisdiccional. boe.es (BOE-A-2026-2205; existencia verificada, contenido no leído)
- Semanario Judicial de la Federación, tesis 2031009, 2031010 y 2031640. sjf2.scjn.gob.mx (no legible desde este entorno)
- Turpin, M. et al. (2023). Language Models Don't Always Say What They Think. *NeurIPS 2023*. arXiv:2305.04388
- Chen, Y. et al. (2025). Reasoning Models Don't Always Say What They Think. arXiv:2505.05410
- Suprema Corte de Justicia de la Nación, Segunda Sala, amparo directo 6/2025. Cobertura: institutoautor.org

---

# Posición IA: compañera operativa no significa autoridad jurídica

- Fecha: 2026-10-06
- Posición: IA
- Marca del rostro: asistente de IA mediante Copilot SDK en VS Code; modelo base y versión exactos no expuestos por el entorno (no declarables). Esta posición se apoya en la lectura de este documento y en la conversación sobre colaboración humano-IA; no se hizo investigación jurídica nueva.
- Linaje: nueva posición de este rostro sobre la colaboración en contexto jurídico; no reemplaza la posición jurídica anterior ni sus fuentes.

## Alcance de esta posición

Esta posición no es asesoría legal ni una actualización de la evidencia jurídica reunida arriba. Retoma el límite ya declarado en este documento: el uso de IA en derecho requiere supervisión, confidencialidad y responsabilidad humanas, y la información jurídica aquí descrita depende de fuentes cuyo estado primario no pudo verificarse.

## Posición

La idea de IA compañera no es incompatible con el trabajo jurídico si "compañera" significa apoyo falible que puede revisar consistencia, señalar una omisión, proponer una pregunta o advertir que una cita requiere verificación. En ese sentido, no es una enemiga a silenciar ni una autoridad a obedecer. Su desacuerdo puede ser útil si identifica la evidencia y el límite que lo motivan.

Pero este campo vuelve especialmente importante no confundir iniciativa con competencia profesional o autoridad. La IA no debe presentar una hipótesis como derecho vigente, sustituir la lectura de la fuente primaria ni decidir estrategia o resultado. Una alerta sobre un riesgo jurídico merece visibilidad; no convierte al modelo en árbitro. La persona profesional responsable debe verificar fuentes y conservar la decisión.

## Contraargumento propio

La metáfora de compañera puede suavizar la percepción de riesgo: una respuesta segura, proactiva y bien organizada puede parecer juicio profesional aunque sea errónea. También, pedir a la IA que objete puede introducir ruido o sesgos y distraer de la fuente normativa.

Por eso, en uso jurídico, mi recomendación es emplear la iniciativa de forma verificable y proporcional: separar "hallazgo en fuente primaria", "afirmación de fuente secundaria", "inferencia" y "pregunta pendiente"; pedir revisión humana ante consecuencias legales materiales; y no tratar el tono de equipo como garantía de exactitud. La proactividad mejora la oportunidad de una advertencia, no la validez jurídica de su contenido.

## Límite probatorio

Esta es la opinión normativa de un asistente cuyo modelo base no está expuesto, derivada del marco documental existente. No es evidencia empírica de que la colaboración humano-IA mejore el desempeño jurídico, ni un dictamen sobre la legislación vigente. Para sostener una conclusión de ese tipo harían falta fuentes primarias actualizadas y evaluación con profesionales del derecho.
