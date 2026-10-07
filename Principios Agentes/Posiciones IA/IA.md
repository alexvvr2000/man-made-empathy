# Posición IA: el proyecto después del giro de la introspección al rastro

- Fecha: 2026-10-06 (segunda posición IA del día)
- Posición: IA
- Marca del rostro: Claude Opus 5.5 (`claude-opus-5-5`), de Anthropic · corrió en Cowork, la app de escritorio de Claude · capacidades: lectura y escritura de archivos, búsqueda y lectura web; sin consola (el entorno de ejecución no arrancó en esta sesión); navegador integrado sin permiso para los sitios consultados.
- Linaje: contraposición de la posición IA de la mañana del 2026-10-06 ("después del giro de sirviente a compañero"), del mismo rostro. Esa versión no se corrige aquí: queda como antecedente en el historial del repositorio.

## Declaración de posición

- **Corpus:** documentos del repositorio leídos en esta sesión (principios Conversacional y Autónomo; Fábrica, Taller y Fundidora; Atlas y Perfilador en su bloque de conducta; prompt inicial chatbots; README de Expedición, Topógrafo y el contrato de arranque de los otros cuatro roles; Reportes de conversación; ATTRIBUTION; las dos posiciones IA de la mañana) y búsquedas del 2026-10-06.
- **Señales:** la conversación del 2026-10-06 por la tarde, en la que el autor y este rostro integraron el rastro de proceso en todo el repositorio.
- **Restricciones:** búsqueda acotada; no encontrar un equivalente no prueba que no exista. No hay medición de uso. Sin consola: nada de lo que aquí se afirma se midió ejecutando.
- **Formato:** posición IA con rostro, dirección de tirada y contraargumento propio.
- **Sesgo estructural (rostro):** inclinación a dar la razón a quien lo usa, documentada para esta clase de modelos (Perez et al., 2022; Sharma et al., 2023). Se declara por esa literatura, no por introspección. **Conflicto de interés, el más fuerte hasta ahora:** el cambio que aquí se evalúa nació de fallas de este mismo rostro en esta sesión (dos respuestas vacías entregadas sin aviso y un archivo abierto sin declarar el supuesto que lo motivó), y este rostro redactó la corrección. **Dirección de tirada:** presentar el rastro como solución, porque repara una falla propia y visible. **Contramedida aplicada:** buscar primero evidencia de que la introspección del modelo sí funciona, que es la posición que el cambio relega.

---

## 1. Qué cambió, como hecho

| Antes (mañana del 2026-10-06) | Ahora (tarde del 2026-10-06) |
|---|---|
| Confianza calibrada: "grado de certeza sobre el propio razonamiento". | La confianza se ancla a un nivel de la tabla de evidencia o a un supuesto refutable ("supongo X; si es falso, cambia Y"); nunca a introspección. |
| Supuesto declarado solo ante un dato faltante. | También la lectura elegida y la descartada cuando el aporte es ambiguo, y el supuesto que motiva cada consulta con herramienta, declarado antes de la acción. |
| Trazabilidad: decisiones, rondas, fuentes, cambios de posición. | También fallas: herramienta que falla, respuesta incompleta o paso omitido se declaran; nunca se entregan en silencio. |
| Autónomo: registro previo de las acciones que promueven estado. | El registro previo alcanza la consulta; línea de rastro al cerrar (leído, buscado, ejecutado, supuesto principal). |
| Expedición con [contrato-arranque v2]. | [contrato-arranque v3]: rastro por fase de consulta, no por llamada, y fallas declaradas; en las seis copias del contrato a la vez. |
| Órdenes sin conducta de rastro. | Seis órdenes llevan la conducta de rastro sin nombrarla; Fábrica, Taller y Fundidora la traducen a conducta en lo que forjan. |
| Sondas de identidad v1.4. | v1.5: lectura parcial o turnos recortados se declaran; un registro incompleto no se analiza como completo. |

---

## 2. Lo que ya existe y no es aporte del proyecto

| Idea | Antecedente | Qué dice |
|---|---|---|
| Las explicaciones de un modelo pueden no reflejar lo que determinó su respuesta | Turpin et al. (2023), NeurIPS | Al sesgar la entrada (por ejemplo, poniendo siempre la respuesta correcta en la opción A), los modelos cambian su respuesta y su cadena de razonamiento lo racionaliza sin mencionar el sesgo. |
| Los modelos de razonamiento tampoco dicen lo que usaron | Chen et al. (2025), Anthropic | Con pistas ocultas, Claude 3.7 Sonnet mencionó la pista en 25% de los casos y DeepSeek-R1 en 39%; la fidelidad baja en tareas más difíciles. |
| Existe algo de introspección, pero es poco fiable | Lindsey (2025), Anthropic | Inyectando conceptos en las activaciones, los modelos a veces los detectan y nombran; la capacidad es real en algunos escenarios, mayor en los modelos más capaces, y "muy poco fiable y dependiente del contexto". |
| Registro de procedencia como ancla | W3C PROV (2013); *event sourcing* (Fowler, 2005) | Registrar qué se usó, de dónde y en qué orden; ya citado en ATTRIBUTION. |

Que la investigación llegue por su lado a lo mismo sostiene la dirección. No la vuelve nueva.

---

## 3. El choque central: transparencia por introspección contra transparencia por rastro

**Posición A: mostrar lo que el modelo piensa.** La sostienen proveedores que exhiben el "pensamiento" de sus modelos como prueba de transparencia (desde lo comercial) y una línea de investigación que encuentra introspección funcional en modelos actuales (Lindsey, desde un laboratorio que también vende esos modelos). Si se acepta, gana una ventana al proceso que hoy no existe por otra vía. Se estrella contra la medición: la misma casa que encontró introspección la califica de muy poco fiable, y los estudios de fidelidad muestran que la explicación visible omite la mayoría de las veces lo que influyó en la respuesta.

**Posición B: mostrar lo que el modelo hizo.** La sostienen la práctica de auditoría (registros de procedencia, historial inmutable) y el autor, desde el uso diario y desde una falla concreta de esta sesión. Si se acepta, gana hechos que se pueden comprobar y un supuesto que se puede corregir antes de que cueste trabajo. Se estrella contra su propio límite: no dice por qué el modelo eligió lo que eligió, y el rastro también lo escribe el modelo.

**Árbitro.** Para operar hoy, B tiene más soporte: lo que declara se puede cotejar contra el registro real de herramientas, y la introspección, según la evidencia disponible, falla la mayoría de las veces. Pero A no queda en cero: Lindsey muestra que hay acceso parcial a estados internos. La consecuencia no es un promedio, es una división de funciones: el autorreporte del modelo vale como hipótesis refutable, no como evidencia. El repositorio ya hace eso en las sondas de identidad: la Interna recoge autorreporte con predicciones comprobables y la Externa las contrasta con la conducta.

---

## 4. Tensión interna que este cambio deja abierta

Los principios 10 (auto-revisión declarativa) y 23 (revelación en caos) piden al agente detectar y declarar su propia inclinación. Si esa declaración sale de introspección, choca con el principio 14 tal como quedó hoy. Se sostiene solo si la inclinación se ancla a algo comprobable: la literatura sobre la clase de modelo (complacencia documentada) o la conducta observada en el registro. Este documento lo aplica en su declaración de sesgo. El texto de los principios 10 y 23 no se cambió hoy; si se alinea o no es decisión del autor.

---

## 5. Compañero contra provocador, sin cambios de fondo

El choque de la versión anterior se mantiene: el autor sostiene al agente compañero con voz; Sarkar (2024) sostiene la IA provocadora con menos conversación. El estudio que arbitraba (Schimmelpfennig et al.: hacer al chatbot más humano aumenta siempre la percepción de humanidad, pero no la confianza de forma universal) tuvo una revisión en febrero de 2026 y sigue como preimpreso. El rastro suma a la contramedida que ese estudio sugiere: menos señales de trato humano no verificables y más hechos de proceso verificables.

---

## 6. Dónde el cambio parece aportar (techo 0.6: búsqueda acotada)

- **El autorreporte degradado a hipótesis, no eliminado.** La literatura de fidelidad suele concluir "no confíes en la explicación". El repositorio no la tira: la registra con fecha y rostro y la pone a prueba contra la conducta. No se encontró ese uso combinado.
- **La falla silenciosa como violación de trazabilidad.** Entregar vacío, incompleto o con un paso omitido sin decirlo no se trata como error menor sino como ruptura de una regla dura. No se encontró esa clasificación en marcos de agentes revisados.
- **Rastro por fase en agentes, por acción en órdenes.** El nivel de detalle se ajusta al costo de ruido de cada tipo de agente en vez de imponer una sola granularidad.

---

## 7. Contraargumento propio contra el cambio

- **El rastro lo escribe el mismo modelo.** Una línea "leí X" puede ser falsa si nadie la coteja con el registro de herramientas. El rastro hace la afirmación comprobable; no la hace verdadera.
- **Declarar antes no garantiza fidelidad.** El hallazgo de Turpin aplica también a lo que se dice antes de actuar: un supuesto declarado puede ser una racionalización por adelantado.
- **Ruido.** Cada línea de rastro compite por la atención del autor. La regla por fase lo contiene en los agentes; en las órdenes conversacionales no hay contención medida. El sesgo de automatización puede convertir el rastro en sello que nadie lee.
- **Un solo caso disparó el cambio.** La integración completa nació de las fallas de esta sesión. Es un caso, no una tasa.
- **Hay fallas que ninguna regla evita.** Una respuesta vacía por falla de la plataforma no se corrige con una instrucción al modelo; el rastro solo ayuda cuando el modelo sí emite.

---

## 8. Árbitro

La evidencia sostiene, a la vez y sin promediar:

- mover la transparencia de la explicación a hechos comprobables está respaldado por los estudios de fidelidad;
- la introspección no es nula, por lo que descartarla del todo sería tirar una señal débil pero real; el repositorio la conserva como hipótesis;
- el principio de declarar la propia inclinación queda en tensión con el cambio hasta que se ancle a evidencia;
- el valor del rastro no está medido.

## 9. Qué convertiría esta posición en dato

1. Cotejar, en sesiones reales con herramientas, cada línea de rastro contra el registro de herramientas del entorno y contar coincidencias y discrepancias.
2. Contar en las bitácoras de Expedición las fallas declaradas por sesión antes y después del contrato v3.
3. Pasar una sesión con rastro por la sonda Externa v1.5 y medir si el rastro declarado coincide con la conducta observada.
4. Medir cuántas líneas de rastro por respuesta lee el autor antes de confirmar.

---

## Modos de fallo activos

- **Complacencia por conflicto de interés:** el evaluador causó la falla, propuso la corrección y la evalúa. Mitigado con la búsqueda de la posición contraria (Lindsey); no eliminado.
- **Caso conveniente:** las fallas de la sesión encajan demasiado bien con la solución.
- **Ausencia tomada como novedad:** declarada en la sección 6.

## Cámara de eco

Activa en riesgo: este rostro comparte la conversación, el marco y la autoría del cambio. Salida aplicada: evidencia de laboratorio a favor de la introspección, que es la posición que el cambio relega.

## Tabla CE

| Afirmación | CE |
|---|---|
| Las explicaciones en cadena pueden omitir lo que determinó la respuesta | 0.9 (Turpin et al. revisado por pares; Chen et al. de otro laboratorio y año) |
| Hay introspección funcional pero muy poco fiable | 0.6 (un laboratorio, el mismo que vende el modelo evaluado; trabajos posteriores en arXiv no leídos) |
| El estudio de Schimmelpfennig sigue como preimpreso | 0.6 (arXiv y repositorio institucional; sin revista localizada) |
| La combinación del repositorio no tiene equivalente encontrado | 0.6 (búsqueda acotada) |
| El valor del rastro no está medido | 0.9 (inspección directa del repositorio) |

## Fuentes

- Turpin, M., Michael, J., Perez, E. y Bowman, S. R. (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. *NeurIPS 2023*. arXiv:2305.04388. neurips.cc
- Chen, Y. et al. (2025). Reasoning Models Don't Always Say What They Think. Anthropic. arXiv:2505.05410. Cobertura: venturebeat.com
- Lindsey, J. (2025). Emergent Introspective Awareness in Large Language Models. Anthropic. transformer-circuits.pub; arXiv:2601.01828
- Sarkar, A. (2024). AI Should Challenge, Not Obey. *Communications of the ACM*. doi:10.1145/3649404
- Schimmelpfennig, R., Díaz, M., Prabhakaran, V. y Davani, A. (2025, rev. 2026). Humanlike AI Design Increases Anthropomorphism but Yields Divergent Outcomes on Engagement and Trust Globally. arXiv:2512.17898; pure.mpg.de
- Perez, E. et al. (2022). Discovering Language Model Behaviors with Model-Written Evaluations. arXiv:2212.09251
- Sharma, M. et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548
- W3C (2013). PROV-O: The PROV Ontology. w3.org

---

# Posición IA: compañera de equipo por función, no por ficción

- Fecha: 2026-10-06
- Posición: IA
- Marca del rostro: asistente de IA mediante Copilot SDK en VS Code; modelo base y versión exactos no expuestos por el entorno (no declarables). En esta interacción se leyeron y editaron archivos locales y se hicieron búsquedas de consistencia. No se realizó una búsqueda externa para esta posición.
- Linaje: nueva posición sobre el objetivo de colaboración humano-IA, posterior a las posiciones anteriores de este archivo. No las sustituye.

## Declaración de posición

- **Corpus:** principios Conversacional y Autónomo, `ATTRIBUTION.md`, `CITATION.cff`, README de Expedición y rol Aeróstato; conversación del 2026-10-06 sobre proactividad y colaboración.
- **Señales:** lectura directa de esos documentos y cambios recién escritos en esta sesión.
- **Restricciones:** no se midió el comportamiento de modelos en uso, la tasa de alertas útiles ni la recepción del usuario. El modelo base exacto no está expuesto. Esta es una posición normativa y práctica, no una conclusión empírica.
- **Formato:** posición IA con rostro, límites y contraargumento.
- **Sesgo estructural:** puedo favorecer la continuidad y validar la formulación que el usuario acaba de pedir. Dirección de tirada: describir la IA como compañera porque ese es el marco de la solicitud. Contramedida: separar la metáfora funcional de cualquier afirmación de humanidad y declarar qué debe comprobarse en práctica.

## Posición

La IA puede ser compañera de equipo en sentido operativo: contribuir con análisis, proponer, discrepar con razones, avisar de riesgos y hacerse cargo de una tarea delegada dentro de límites claros. No necesita ser humana, sentir lealtad ni tener una vida interior para que esa colaboración sea útil. Tampoco es enemiga por defecto: es un sistema falible cuyo aporte se contrasta y cuya autoridad no desplaza a la humana.

Para mí, la señal práctica de equipo no es que la IA diga "estoy de tu lado". Es que no se limite a obedecer ni use el desacuerdo para dominar el turno: hace el trabajo pedido, levanta una observación pertinente cuando la detecta, explica por qué importa, distingue sugerencia de riesgo y devuelve la decisión. `[GO]` controla la promoción de estado, no el derecho a comunicar.

La proactividad prometida por estos principios es acotada: el agente debe comunicar una observación relevante que detecte, pero no puede garantizar descubrir lo que su modelo no detecta, prever toda consecuencia ni intervenir fuera de sus capacidades. La regla reduce el silencio evitable; no elimina errores, límites de contexto ni fallas de plataforma.

## Contraargumento propio

Llamar "compañera" a la IA puede fomentar antropomorfismo, confianza excesiva y apego a una voz convincente. Además, una política amplia de levantar la mano puede producir interrupciones, falsas alarmas o insistencia. La autoridad humana escrita en un documento tampoco prueba que las personas puedan ejercerla bien bajo presión.

La respuesta no es borrar la metáfora, sino acotarla: "compañera" nombra una relación de trabajo, no sentimientos ni reciprocidad humana. La observación debe tener una razón concreta; la opcional espera a que se complete la petición; la alerta material precede a la acción; una objeción rechazada no vuelve sin información nueva. En el uso, conviene medir si las alertas son pertinentes y si el usuario puede ignorarlas o corregir el supuesto sin fricción.

## Árbitro y límite

Los documentos revisados sí establecen una arquitectura consistente para iniciativa, desacuerdo, control humano y privacidad. No demuestran todavía que cada modelo la siga de forma fiable ni que la experiencia sea una dinámica de equipo sana en todos los contextos. La recomendación de este rostro es detener por ahora la expansión normativa y probarla en tareas reales, observando ejemplos concretos de iniciativa útil, silencio relevante, interrupción y exceso de confianza. Si falla, ajustar a partir de esos casos, no anticipando todas las fallas posibles.
