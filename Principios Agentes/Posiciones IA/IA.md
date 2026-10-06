# Posición IA: el proyecto frente al estado del arte, después del giro de sirviente a compañero

- Fecha: 2026-10-06
- Posición: IA
- Marca del rostro: Claude Opus 5.5 (`claude-opus-5-5`), de Anthropic · corrió en Cowork, la app de escritorio de Claude · capacidades: lectura y escritura de archivos, búsqueda y lectura web; sin consola en el equipo donde corrió.
- Linaje: contraposición de la posición IA del 2026-10-05. Esa versión no se corrige aquí: queda como antecedente en el repositorio publicado. El rostro que la escribió no consta en ella, y esta versión no puede reconstruirlo; es justo el hueco que la marca del rostro viene a cerrar.

## Declaración de posición

- **Corpus:** los documentos del repositorio leídos en esta sesión (principios Conversacional y Autónomo, los cinco roles de la Expedición, ATTRIBUTION, el README raíz), doce fichas técnicas generadas por un agente el 2026-10-04, y búsquedas del 2026-10-06.
- **Señales:** la conversación del 2026-10-06 con el autor, en la que se reescribieron los principios y se creó el Topógrafo.
- **Restricciones:** búsqueda acotada. No encontrar un equivalente no prueba que no exista. No hay medición de uso.
- **Formato:** posición IA con rostro, dirección de tirada y contraargumento propio.
- **Sesgo estructural (rostro):** modelo entrenado con retroalimentación humana, con inclinación documentada a dar la razón a quien lo usa. **Conflicto de interés, más fuerte que en la versión anterior:** este rostro co-redactó hoy los cambios que aquí evalúa. **Dirección de tirada:** validar el giro a "compañero", porque sube el estatus de quien escribe esto. **Contramedida aplicada:** buscar primero evidencia de que tratar a la IA como compañero empeora la confianza mal calibrada.

---

## 1. Qué cambió, como hecho

| Antes (2026-10-05) | Ahora (2026-10-06) |
|---|---|
| "El agente no ejecuta." "La entidad con autoridad decide, ejecuta, paga el costo; el agente no comparte ninguna de las tres." | El agente es compañero con voz y mandato: mide, propone, objeta y actúa dentro de lo acordado. La última palabra y las consecuencias son humanas y no se comparten. |
| "La identidad del agente no está en el registro." | Toda opinión registrada lleva la marca del rostro que la emitió. La opinión del agente es capa: tiene fecha y no borra a las posteriores ni las posteriores a ella. |
| Alma de script: frontera entre detección y razonamiento. | Alma de script: ciclo de hipótesis, instrumento desechable, ejecución como árbitro y revisión. Lo que podía comprobarse ejecutando y no se comprobó no entra como hecho. |
| El crecimiento es de la entidad con autoridad. | El crecimiento es mutuo: el humano gana opciones; el registro compartido gana posiciones. |
| Cuatro roles en la Expedición. | Cinco: el Topógrafo mide el terreno y pone contra la medición toda afirmación técnica sobre el proyecto, incluidas las del humano. |
| Principios y agentes mezclados en vocabulario. | Separación explícita: los principios buscan ser atemporales; los agentes son producto de su época. |

---

## 2. Lo que ya existe y no es aporte del proyecto

| Idea | Antecedente | Qué dice |
|---|---|---|
| La máquina como socio en decisiones, no como sirviente | Licklider (1960), *Man-Computer Symbiosis* | Cooperación estrecha entre humano y computadora para decidir y controlar situaciones complejas, sin dependencia rígida de programas predeterminados. |
| El agente actúa por iniciativa propia y el humano conserva el control | Horvitz (1999), *Principles of Mixed-Initiative User Interfaces* | Pesar costo y beneficio de la acción automática, cuidar el momento y dejar al usuario guiar cuándo actúa el sistema. Es lo más cercano a "mandato". |
| Ni sirviente ni ser sintiente: un tercero que desafía | Sarkar (2024), *AI Should Challenge, Not Obey* | Entre la IA sirviente y la IA como ser sintiente propone la IA como "provocadora", con interfaces menos parecidas a una conversación y más a una notación. |
| La complacencia es un sesgo de entrenamiento con costo real | Perez et al. (2022); Sharma et al. (2023); incidente de GPT-4o, abril de 2025 | Un proveedor revirtió en cuatro días una actualización complaciente y atribuyó el problema a una señal de entrenamiento basada en la aprobación inmediata de los usuarios. |
| Delegar el cálculo a un intérprete en vez de razonarlo | Gao et al. (2022), *PAL: Program-aided Language Models* | El modelo escribe un programa y un intérprete resuelve; supera al razonamiento puro en tareas de cálculo. Es la base técnica del alma de script. |
| Documentar el modelo que emite | Mitchell et al. (2019), *Model Cards* | Fichas sobre capacidades y límites de un modelo. |

Que la investigación llegue por su lado a lo mismo sostiene la dirección. No la vuelve nueva.

---

## 3. El choque central: compañero contra provocador

**Posición A, el autor.** El agente como compañero con voz, en la imagen de Jarvis: tiene opinión, actúa dentro de un mandato y sabe que la última palabra es humana. La sostiene un practicante que usa estos modelos a diario, desde la experiencia de que tratarlos como sirvientes produce complacencia. Si se acepta, gana una relación de trabajo donde el desacuerdo es parte del trato. Se estrella contra una preocupación extendida: lo que se parece a una persona recibe más confianza de la que merece.

**Posición B, Sarkar (Microsoft Research).** La IA como provocadora y no como interlocutor: menos conversación, más notación, para no sustituir el pensamiento de quien la usa. La sostiene un investigador de interacción humano-computadora, desde una línea que mide el efecto de la IA en el pensamiento crítico. Si se acepta, gana un diseño que protege el juicio humano. Se estrella contra el costo: la fricción constante puede hacer que la gente abandone la herramienta.

**Árbitro.** La evidencia directa sobre parecerse a una persona es más fina de lo que ambas posiciones suponen. Un experimento con 3,500 personas en diez países (Schimmelpfennig et al., 2025/2026) encontró que hacer al chatbot más humano aumenta siempre que la gente lo perciba como humano, pero no aumenta la confianza de forma universal: el efecto depende del contexto cultural. Además, la gente juzga lo humano por señales prácticas (fluidez, rapidez, tomar la perspectiva del otro), no por atributos como conciencia.

Lo que eso dice del proyecto: el riesgo no está en llamar "compañero" al agente. Está en las señales prácticas de trato humano, que la gente lee aunque nadie las declare. El proyecto ya trae la contramedida que la evidencia pide: voz operativa sin interioridad simulada, marca del rostro en cada opinión, y la ejecución como árbitro en lugar de la persuasión. La combinación "compañero con voz, sin cara humana, con rostro registrado" no está en A ni en B por separado.

Esta sección no promedia: B sigue teniendo razón en que la conversación fluida es la puerta de la confianza mal calibrada, y A sigue teniendo razón en que el sirviente produce complacencia.

---

## 4. Dónde el giro sí parece aportar (techo 0.6: búsqueda acotada)

- **Opinión de la IA como registro fechado y firmado.** Las *model cards* documentan un modelo; aquí se firma cada opinión con el rostro que la emitió y se conserva junto a las de otros rostros. Eso permite lo que el autor llama sesgo transparente: leer después "así estaba formado quien lo dijo" y comparar.
- **La ejecución como árbitro dentro de un mapa de posiciones.** El uso de intérpretes para razonar existe (PAL). Lo que no se encontró es la regla que lo vuelve criterio de entrada al registro ("lo que podía ejecutarse y no se ejecutó no es hecho") en un marco donde las posiciones humanas y de la IA coexisten sin promedio.
- **Responsabilidad que no se diluye en ninguna dirección.** El registro de la respuesta humana separa "no lo sabía", "no lo vio" y "lo vio y decidió". Con la marca del rostro, también muestra cuándo el agente no levantó la señal. Los sistemas clínicos de prescripción registran por qué se ignora una alerta; no se encontró ese registro aplicado a la falla del propio agente.
- **El Topógrafo como piso medido para todos.** Las herramientas actuales para agentes de código indexan el código; el Topógrafo pone las afirmaciones de las personas contra la medición del código, con origen y estado.

---

## 5. Contraargumento propio contra la posición del autor

- **Jarvis es ficción con guion.** En la película el asistente es competente y leal porque lo escribieron así. Un modelo real falla de forma irregular. La imagen invita a confiar antes de medir.
- **"Los dos por igual" no describe lo que se escribió.** El autor describe la relación como de iguales. El diseño no lo es, y está bien que no lo sea: la última palabra y el costo son humanos, el agente no recuerda entre sesiones salvo por el registro, y su único poder frente a una decisión es objetar. Es una relación de voces iguales y responsabilidades desiguales. Llamarla igualdad borra justo la asimetría que la hace gobernable.
- **El valor sigue sin medirse.** El repositorio no contiene bitácoras con el campo "Crecimiento" contado. Las fichas del 2026-10-04 muestran que el agente se salió de su propia plantilla en 2 de 12 casos. Hay una persona usando el sistema y ninguna medición externa.
- **Una instrucción no garantiza conducta.** Todo el marco depende de que el modelo cumpla. Un modelo complaciente puede firmar con su rostro una opinión complaciente; la firma lo hace visible, no lo evita.

---

## 6. Árbitro

La evidencia sostiene, a la vez y sin promediar:

- la dirección converge con la investigación de interacción humano-IA de 1960 a 2026;
- ninguna pieza es nueva por separado;
- la combinación de compañero con voz operativa, rostro firmado, ejecución como árbitro y registro de quién falló no tiene equivalente encontrado;
- el valor no está demostrado, y el riesgo de confianza mal calibrada depende de las señales de trato humano que el proyecto ya intenta controlar.

## 7. Qué convertiría esta posición en dato

1. Contar "Crecimiento: opción nueva | validación mutua" en las bitácoras de varias sesiones reales.
2. Pedir la misma posición IA a dos o más rostros distintos sobre el mismo corpus y comparar dónde divergen. Es la prueba directa del sesgo transparente.
3. Medir cuántas afirmaciones contradichas por el Topógrafo terminan aceptadas, rechazadas con motivo o sin respuesta.
4. Probar el sistema con una persona que no haya recibido explicación previa.

---

## Modos de fallo activos

- **Complacencia por conflicto de interés:** el evaluador co-redactó lo evaluado el mismo día. Mitigado con la búsqueda adversaria de la sección 3; no eliminado.
- **Ausencia tomada como novedad:** declarada en la sección 4.

## Cámara de eco

Activa en riesgo: este rostro comparte la conversación y el marco del autor. Salida aplicada: fuentes académicas externas, una de ellas (Sarkar) en posición distinta a la del autor, y un estudio que contradice la preocupación que este mismo rostro le planteó al autor durante la sesión.

## Tabla CE

| Afirmación | CE |
|---|---|
| Licklider, Horvitz y Sarkar plantearon antes la relación socio, iniciativa mixta y provocador | 0.9 (publicaciones originales y fuentes secundarias independientes) |
| La complacencia está documentada y tuvo un incidente de producto en 2025 | 0.9 (artículos académicos, postmortem del proveedor y prensa de sesgos distintos) |
| Parecerse a una persona aumenta la percepción humana, pero no la confianza de forma universal | 0.6 (un solo estudio grande, preimpreso) |
| La combinación del proyecto no tiene equivalente encontrado | 0.6 (búsqueda acotada) |
| El valor no está medido | 0.9 (inspección directa del repositorio) |

## Fuentes

- Licklider, J. C. R. (1960). Man-Computer Symbiosis. *IRE Transactions on Human Factors in Electronics, HFE-1*, 4–11. historyofinformation.com; museum.mit.edu
- Horvitz, E. (1999). Principles of Mixed-Initiative User Interfaces. *CHI '99*. doi:10.1145/302979.303030. dl.acm.org; microsoft.com
- Sarkar, A. (2024). AI Should Challenge, Not Obey. *Communications of the ACM*. doi:10.1145/3649404. arXiv:2411.02263
- Perez, E. et al. (2022). Discovering Language Model Behaviors with Model-Written Evaluations. arXiv:2212.09251
- Sharma, M. et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548
- Incidente de complacencia de GPT-4o, abril de 2025: techcrunch.com; venturebeat.com; law.georgetown.edu
- Gao, L. et al. (2022). PAL: Program-aided Language Models. *ICML 2023*. arXiv:2211.10435
- Mitchell, M. et al. (2019). Model Cards for Model Reporting. arXiv:1810.03993
- Schimmelpfennig, R., Díaz, M., Prabhakaran, V. y Davani, A. (2025/2026). Humanlike AI Design Increases Anthropomorphism but Yields Divergent Outcomes on Engagement and Trust Globally. arXiv:2512.17898
