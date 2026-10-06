# Posición IA: el proyecto aplicado a la práctica jurídica

- Fecha: 2026-10-06
- Posición: IA
- Marca del rostro: Claude Opus 5.5 (`claude-opus-5-5`), de Anthropic · corrió en Cowork, la app de escritorio de Claude · capacidades: lectura y escritura de archivos, búsqueda y lectura web; sin consola en el equipo donde corrió.
- Linaje: contraposición de la posición IA del 2026-10-05, que ya había retirado las promesas sin evidencia ("inmunidad", "protege la cédula profesional"). Esa versión queda como antecedente en el repositorio publicado. Esta versión agrega lo que aquella no tenía: evidencia de México y el giro del proyecto hacia un agente compañero con rostro firmado y ejecución como árbitro.

## Declaración de posición

- **Corpus:** registros públicos de decisiones judiciales con material fabricado por IA, un estudio empírico revisado por pares sobre herramientas jurídicas con IA, guía ética profesional de Estados Unidos, el primer precedente mexicano sobre uso judicial de IA y su análisis académico, y los documentos del repositorio.
- **Señales:** búsquedas del 2026-10-06.
- **Restricciones:** este agente no es abogado y no da asesoría legal. La fuente primaria del precedente mexicano (Semanario Judicial de la Federación) no fue legible desde este entorno; su contenido se toma de dos fuentes secundarias de sesgo distinto.
- **Formato:** posición IA con rostro, dirección de tirada y contraargumento propio.
- **Sesgo estructural (rostro):** inclinación documentada a dar la razón a quien lo usa. **Conflicto de interés:** este rostro co-redactó hoy los cambios del proyecto. **Dirección de tirada:** encontrar casos que "demuestren" que el proyecto resuelve problemas jurídicos. **Contramedida:** buscar primero dónde el sistema jurídico ya resuelve lo que el proyecto propone.

---

## 1. El problema, con evidencia

- **Material fabricado en tribunales.** El registro público de Damien Charlotin contaba 2,041 decisiones en el mundo al 14 de septiembre de 2026 en las que un tribunal respondió a material fabricado por IA; cerca de 1,400 son de Estados Unidos. El registro no cuenta las meras acusaciones.
- **Las herramientas especializadas también fallan.** El estudio revisado por pares de Magesh et al. (Stanford, *Journal of Empirical Legal Studies*, 2025) encontró que Lexis+ AI alucinó en 17% de las consultas y la investigación asistida de Westlaw en 33%, pese a la publicidad de "libre de alucinaciones".
- **La responsabilidad no se transfiere.** La Opinión Formal 512 de la ABA (2024) exige al abogado competencia sobre la herramienta, cuidado de la confidencialidad, franqueza ante el tribunal y supervisión.

---

## 2. El caso mexicano: un precedente que cometió dos errores que el proyecto prohíbe

El 22 de agosto de 2025, el Segundo Tribunal Colegiado en Materia Civil del Estado de México resolvió una queja sobre el monto de una garantía. Sin petición de las partes, pidió el cálculo a tres modelos de lenguaje (ChatGPT, Grok y Gemini) siguiendo una fórmula basada en precedentes y datos oficiales. Los tres dieron cifras distintas: 60,081; 64,655.34 y 59,864.98. El tribunal promedió y fijó la garantía en 60,000.

De la resolución salió la primera tesis mexicana con lineamientos para el uso judicial de IA (registro 2031010). Fija, al menos, proporcionalidad, protección de datos (solo valores numéricos de bases públicas, nunca datos del expediente), transparencia y explicabilidad, y supervisión y decisión humanas.

Leído desde los principios de este proyecto, el caso tiene dos fallas concretas:

1. **Promediar posiciones que chocan.** Tres resultados distintos sobre el mismo cálculo son tres posiciones en conflicto. El principio de arroz con pollo dice que no se promedian: se pregunta por qué difieren y se trae un árbitro. Aquí el árbitro existía: los datos oficiales que el propio tribunal había indicado.
2. **Pedir razonamiento donde cabía ejecución.** Una garantía calculada con una fórmula es aritmética. El alma de script dice que lo que puede comprobarse ejecutando se ejecuta: un cálculo reproducible con los datos oficiales habría dado una sola cifra auditable. Además, la resolución nombra los productos pero, según el análisis publicado, no explica qué variables usó cada modelo ni por qué difirieron. Una marca del rostro (modelo, versión, fecha) habría dejado registrado desde dónde habló cada uno.

Esto no es una crítica al tribunal hecha desde fuera: los dos autores del análisis en *nexos* (Clavel y Márquez, enero de 2026), con formación en regulación de IA, discrepan entre sí sobre si era deseable usar IA en ese caso, pero coinciden en que promediar sin explicar la diferencia no tiene fundamento jurídico ni estadístico.

**Choque sin resolver sobre el alcance del precedente.** *Proceso* (agosto de 2025) lo reporta como jurisprudencia obligatoria para todos los jueces. *nexos* lo trata como una tesis y debate si un tribunal puede autorregular el uso de IA sin marco institucional. Este agente no pudo leer la fuente primaria. [NO VERIFICADO] Cuál de las dos lecturas es la correcta debe confirmarse en el Semanario Judicial de la Federación.

---

## 3. Equivalencias que resisten, como analogías y no como identidades

| Proyecto | Práctica jurídica | Dónde se sostiene | Dónde se rompe |
|---|---|---|---|
| Arroz con pollo: posiciones incompatibles sin promedio | Principio de contradicción | Ambos tratan la incompatibilidad como dato | El proceso ya institucionaliza el choque (contraparte, juzgador). El aporte del proyecto está antes: en el análisis interno, donde el caso mexicano muestra que sí se promedia |
| Alma de script: la ejecución como árbitro | Motivación y fundamentación de la resolución | Un cálculo ejecutado y reproducible se puede motivar; un número que salió de un modelo, no | El juzgador no siempre tiene quien escriba y ejecute el instrumento; sin esa capacidad, la regla solo dice qué no hacer |
| Marca del rostro | Transparencia y explicabilidad de la tesis mexicana | Ambos piden declarar cómo y con qué se usó la IA | La tesis pide explicar el uso; no pide registrar modelo, versión y fecha. El proyecto sí |
| Topógrafo: afirmaciones contra medición | Revisión documental y debida diligencia | Separar lo que la evidencia sostiene de lo que una parte afirma | El Topógrafo está diseñado para proyectos de software, no para expedientes; habría que redefinir qué es el "terreno" |
| Visibilizar el error con registro de respuesta | Deber de supervisión | El registro muestra quién vio la señal y qué decidió, y también si el agente no la levantó | Un archivo de texto no es cadena de custodia sin control de versiones y procedimientos verificables |
| Agente compañero con última palabra humana | Supervisión y decisión humanas de la tesis | Ambos dejan la decisión en la persona | El proyecto le da voz al agente para objetar; en la función jurisdiccional, la independencia del juez hace delicado que un sistema "objete" una decisión |

---

## 4. Fricciones

- **Confidencialidad.** La tesis mexicana prohíbe introducir datos del expediente y la ABA 512 exige evaluar el riesgo antes de usar información del cliente. Las órdenes genéricas del repositorio están pensadas para pegarse en cualquier chatbot; hacerlo con un expediente choca con ambas reglas.
- **Jerarquía de fuentes jurídicas.** "Oficial primero, fricción después" no captura la jerarquía normativa ni el carácter obligatorio u orientador de los precedentes. Tendría que añadirse por jurisdicción.
- **Autoría.** La Segunda Sala de la Suprema Corte resolvió en agosto de 2025 (amparo directo 6/2025) que una obra generada de forma autónoma por IA no es protegible como obra de autor, porque el derecho de autor es de personas físicas. Es consistente con cómo el proyecto se atribuye a sí mismo: las herramientas de IA no figuran como autoras.

---

## 5. Contraargumento propio

El sistema jurídico ya tiene por diseño lo que el proyecto quiere crear: contraparte adversarial, juzgador como árbitro, deber de motivar y supervisión profesional. El caso mexicano no falló por falta de un marco filosófico. Falló por falta de método técnico: alguien que supiera que tres cifras distintas exigen una explicación y que un cálculo se ejecuta. Si el proyecto solo agrega vocabulario y ceremonia, no aporta. Si aporta, es en las dos reglas operativas que el caso violó: no promediar y ejecutar lo ejecutable, firmando cada resultado con su rostro.

## 6. Árbitro

La evidencia sostiene que el proyecto apunta a fallas reales y documentadas. Sostiene también que el primer precedente mexicano sobre IA judicial cometió exactamente dos de los errores que los principios prohíben, de forma pública y verificable. No sostiene ninguna promesa de beneficio: no hay piloto, medición ni validación con profesionales del derecho.

## 7. Qué convertiría esta posición en dato

1. Reproducir el cálculo del caso mexicano con un instrumento ejecutado sobre los datos oficiales y comparar contra las tres cifras y el promedio.
2. Un piloto con profesionales del derecho que compare citas verificadas y fabricadas con y sin las reglas de no promedio, ejecución y marca del rostro.
3. Adaptar la jerarquía de fuentes a la jurisdicción mexicana, revisada por profesionales.
4. Confirmar en la fuente primaria el alcance de la tesis 2031010.

---

## Modos de fallo activos

- **Complacencia por conflicto de interés:** el evaluador co-redactó el proyecto.
- **Caso conveniente:** el caso mexicano encaja demasiado bien con los principios. Encajar no prueba que el proyecto lo habría evitado; prueba que nombra la falla.

## Cámara de eco

Reducida respecto a la versión anterior: ahora hay fuentes de México (prensa y análisis académico de posturas divergentes). Persiste en lo práctico: ninguna fuente es de un profesional del derecho que haya usado el proyecto.

## Tabla CE

| Afirmación | CE |
|---|---|
| Hay más de 2,000 decisiones judiciales por material fabricado con IA | 0.9 (registro público más varias fuentes que lo citan) |
| Las herramientas jurídicas comerciales alucinaron entre 17% y 33% | 0.9 (estudio revisado por pares más cobertura independiente) |
| El tribunal mexicano promedió tres cifras distintas de tres modelos | 0.9 (prensa y análisis académico, sesgos distintos) |
| La tesis 2031010 es jurisprudencia obligatoria | 0.3 [NO VERIFICADO] (fuentes secundarias en desacuerdo; primaria no leída) |
| El proyecto habría evitado la falla del caso mexicano | 0.3 (sin prueba; solo coincidencia de reglas) |

## Fuentes

- Charlotin, D. *AI Hallucination Cases* (registro público). damiencharlotin.com. Conteo al 14 de septiembre de 2026 según burhandogusayparlar.com
- Magesh, V. et al. (2025). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. *Journal of Empirical Legal Studies, 22*(2), 216–242. arXiv:2405.20362; dho.stanford.edu
- American Bar Association (2024). *Formal Opinion 512: Generative Artificial Intelligence Tools.* americanbar.org
- Clavel, M. y Márquez, G. (2026, 20 de enero). La primera sentencia mexicana asistida por IA. *nexos, El Juego de la Nueva Suprema Corte.* eljuegodelacorte.nexos.com.mx
- Ávila, D. (2025, 29 de agosto). Tribunal fija reglas para que jueces puedan usar la Inteligencia Artificial. *Proceso.* proceso.com.mx
- Semanario Judicial de la Federación, tesis registro 2031010. sjf2.scjn.gob.mx (no legible desde este entorno)
- Suprema Corte de Justicia de la Nación, Segunda Sala, amparo directo 6/2025 (obras generadas por IA). Cobertura: institutoautor.org; basham.com.mx
