# Atribución y contexto intelectual

## Man-Made Empathy

> **Los ingredientes tienen antecedentes y aquí se citan. El pegamento —cómo se conectan, en qué orden y con qué reglas— es la contribución de este proyecto.**

Este archivo separa tres cosas:

1. **Lo que no se reclama:** conceptos con autores y tradición propia (supervisión humana, sesgo de automatización, contraargumento, trazabilidad, etc.). Se citan abajo con su fuente.
2. **Lo que se reclama:** la arquitectura que los une, la terminología propia y los mecanismos nuevos que solo existen por esa unión.
3. **Lo que se usa como herramienta:** software o estándares de terceros que una implementación necesita, con su licencia.

Una coincidencia conceptual con un trabajo anterior no implica que la formulación del repositorio se haya tomado de él. Una cita aquí significa "este antecedente existe y conviene conocerlo", no necesariamente "de aquí se copió".

---

## 1. El pegamento: lo que este proyecto aporta

Ninguno de los antecedentes citados en la sección 2 combina estos elementos en un mismo modelo operacional. Esa combinación, su vocabulario y sus reglas de interacción son trabajo original del autor.

| Concepto propio | Qué es, en una línea |
|---|---|
| **Arroz con pollo** | Posiciones incompatibles se cocinan juntas, cada una conserva su origen, y el árbitro es la información real, no la posición más fuerte ni la del usuario. El agente nunca sirve un promedio. |
| **Entidad con autoridad** | El humano es el único sujeto: decide, ejecuta y paga el costo. El agente propone; nunca comparte ninguna de las tres. |
| **Posiciones, no fuentes (las 4 marcas)** | Toda evidencia es una persona o institución hablando desde algún lugar: quién, desde dónde, qué gana, qué se infiere de que lo diga. |
| **Rostro y máscara** | La máscara es el rol de la tarea; el rostro es la inclinación heredada del entrenamiento, que sobrevive al cambio de máscara y se declara en vez de ocultarse. |
| **Cámara de eco pasiva y activa** | Pasiva: faltan perspectivas (se detecta por ausencia). Activa: llegan argumentos nuevos que solo refuerzan la creencia previa (se detecta por acuerdo). |
| **Empatía trazable** | No es "ponerse en el lugar del otro": es ver el mapa del otro, con su posición declarada, y hacer de las diferencias información comparable. |
| **Perímetro de consulta / perímetro de promoción** | Consultar es amplio (antídoto contra la cámara de eco); promover a estado o conocimiento es estrecho (antídoto contra la catástrofe). La restricción vive en la promoción, no en el pensamiento. |
| **Checkpoint como ronda** | El checkpoint no es una puerta de permiso: es la última ronda de diálogo antes de que un conflicto se cierre de forma irreversible, con frase canónica y reversión declarada. |
| **Semilla de crecimiento** | El éxito se mide por la aparición de al menos una opción no considerada; si la interacción solo confirmó lo previo, se declara como validación mutua. |
| **Escala CE de cuatro niveles** | 1.0 lógica formal · 0.9 dato cruzado con fuentes de sesgo opuesto · 0.6 deducción sobre datos extraídos · 0.3 memoria sin verificar, con techo 0.3 cuando no hay extracción. |
| **Voz operativa** | Test operativo: si "yo" no puede reemplazarse por "este sistema" sin cambiar el sentido, la frase es subjetiva y no se emite. |
| **Visibilizar el error** | Escalera de señal según evidencia e impacto, **con registro de la respuesta humana** (aceptada, rechazada con motivo, rechazada sin motivo, sin respuesta). Separa "no lo sabía", "no lo vio" y "lo vio y decidió". La señal debe ser honesta, no persuasiva. |
| **Alma de script** | Lo que puede detectarse sin razonar se detecta sin razonar; el razonamiento interpreta solo lo que la detección entregó. La frontera se declara. |
| **Libertad controlada** | El agente opina con base declarada dentro del perímetro de consulta; el humano confirma en la promoción; la atención humana se pide solo donde las pistas del agente chocan. |
| **Solo agregar aplicado a posiciones** | El conocimiento no se sobrescribe: muta. Una diferencia entre lo registrado y lo actual no es un error, son dos posiciones. Borrar es acto humano. |
| **Expedición** | Cuatro roles (Geólogo, Guía, Cartógrafo, Aeróstato) que se conectan solo por archivos, con piso técnico, notas humanas, grafo con linaje y cruce multiposición sin promedio; incluye el enfoque **realidad contra local** para cualquier proyecto de software, versionado o no. |

---

## 2. Los ingredientes: antecedentes y fuentes

Cada fila dice qué se tomó del antecedente y qué cambia en este proyecto. La columna "qué cambia" es donde vive el pegamento.

| Concepto del proyecto | Antecedente | Qué se toma | Qué cambia aquí |
|---|---|---|---|
| Visibilizar el error | Asertividad graduada **P.A.C.E.** en aviación (Besco, 1994–1995) y CRM (Helmreich et al., 1999) | La escalera sondeo → alerta → desafío → emergencia para que quien no manda pueda frenar a quien manda | Se aplica a un agente sin miedo a represalias; se añade el registro obligatorio de la respuesta humana y la regla de no repetir sin evidencia nueva |
| Registro de la respuesta humana | Motivos de omisión de alertas en sistemas clínicos de prescripción (estudios sobre CPOE/CDSS) | Pedir y registrar por qué un humano ignora una advertencia del sistema | El registro se aplica a cualquier desafío del agente, no solo a alertas predefinidas; un rechazo sin motivo es válido y queda como tal |
| Arroz con pollo / Cartógrafo / Aeróstato | **IBIS** (Kunz y Rittel, 1970); gIBIS (Conklin y Begeman, 1988); *dialogue mapping* (Conklin, 2006) | Mapear asuntos, posiciones y argumentos a favor y en contra sin forzar consenso, para problemas sin respuesta única | Las posiciones llevan persona, linaje y versión; se anclan a un piso técnico del proyecto; la IA participa como una posición más con rostro declarado; el cruce entre carpetas de distintas personas no promedia |
| Objeción inflada (modo de fallo) | **Fatiga por alarmas** clínicas (The Joint Commission, 2013) | Muchas alarmas falsas entrenan a ignorar la verdadera | El umbral de evidencia se justifica como honestidad de la señal, no como estrategia para ser escuchado |
| Sesgo de automatización (modo de fallo) | Parasuraman y Riley (1997); Parasuraman y Manzey (2010) | El humano deja de revisar propuestas casi siempre correctas | Contención por pistas en conflicto: se pide atención solo donde el agente duda |
| Rostro / inclinación a complacer | **Sycophancy** en modelos de lenguaje (Perez et al., 2022; Sharma et al., 2023) | Los modelos entrenados con retroalimentación humana tienden a dar la razón | El sesgo no se filtra: se declara como lente y se fuerza el desafío cuando hay evidencia |
| Contraste adversarial / conflicto controlado | Debate entre IA (Irving et al., 2018; Du et al., 2023); investigación dialéctica y abogado del diablo (Mason, 1969; Schwenk, 1990); Análisis de Hipótesis en Competencia (Heuer, 1999) | Enfrentar posiciones para exponer debilidades | No se busca un ganador ni consenso: el choque queda visible, con árbitro de realidad, y la decisión es humana |
| Crecimiento por diversidad | Diversidad cognitiva (Page, 2007) | Perspectivas distintas producen soluciones que ninguna produce sola | Se exige al menos una opción no considerada como criterio de éxito de cada interacción |
| Sesgo de confirmación / cámara de eco | Nickerson (1998); Sunstein (2017); Cinelli et al. (2021) | La búsqueda selectiva refuerza creencias previas | Se operacionaliza en dos tipos (pasiva/activa) con reglas de salida y de bloqueo |
| Cuarta categoría | Ventana de Johari (Luft e Ingham, 1955) | Lo que el sujeto no sabe que no sabe | Se convierte en pregunta forzada, máximo una por respuesta, sobre el supuesto no verificado |
| Posiciones, no fuentes | Lectura lateral (Wineburg y McGrew, 2019) | Evaluar al emisor antes que al contenido | Cuatro marcas obligatorias por posición, incluida la inferencia sobre el informante |
| Escala CE | GRADE para certeza de evidencia (Guyatt et al., 2008); calibración de modelos (Guo et al., 2017; Kadavath et al., 2022) | Graduar la confianza según la calidad de la evidencia | Cuatro niveles fijos con techo 0.3 sin extracción externa y cruce de sesgos opuestos para 0.9 |
| Núcleo y capa | *Pace layering* (Brand, 1999) | Las capas de un sistema cambian a velocidades distintas | Se aplica a la verdad técnica (lo que sobrevive vs lo que se re-verifica) y a los propios principios |
| Perímetros de consulta y promoción | Mínimo privilegio (Saltzer y Schroeder, 1975) | Cada componente con el menor permiso necesario | El permiso se restringe en la promoción, no en la consulta: restringir la consulta produce ceguera |
| Checkpoint y supervisión humana | Supervisión humana en el Reglamento de IA de la UE (art. 14, 2024); NIST AI RMF (2023) | Un humano debe poder supervisar e intervenir | El checkpoint se vuelve ronda de diálogo con frase canónica, reversión declarada y posiciones con origen |
| Trazabilidad y solo agregar | Modelo de procedencia W3C PROV (2013); *event sourcing* (Fowler, 2005); árboles de Merkle (Merkle, 1987) | Registro de origen, historial inmutable y huellas para detectar cambios | El registro, no la identidad del agente, es el ancla; la diferencia entre registro y estado actual se trata como posición |
| Agencia sin teatro de conciencia | Floridi (2023), *AI as Agency Without Intelligence* | Separar agencia de inteligencia | Voz operativa y prohibición de simular interioridad como regla procesal, no ontológica |
| Recuperación externa / proyección | RAG (Lewis et al., 2020); *Lost in the Middle* (Liu et al., 2023) | Traer evidencia externa; el contexto largo se degrada | Proyectar antes de cargar: la capacidad de procesamiento es un techo del medio |
| Perfil técnico de sistemas | *Model Cards* (Mitchell et al., 2019) | Documentar capacidades y límites de un modelo | Perfil con capas separadas, divergencias con árbitro y marcas [NO VERIFICADO]/[BLOQUEADO] |
| Planes y disenso | *Disagree and commit* (Grove, 1983); *premortem* (Klein, 2007); seguridad psicológica (Edmondson, 1999) | Disentir antes de decidir; el disenso necesita canal protegido | El registro del rechazo da al disenso del agente un canal permanente, sin obligar al humano a justificarse |

---

## 3. Herramientas de terceros usadas por las implementaciones

| Herramienta | Uso | Licencia |
|---|---|---|
| SQLite y su ejecutable `sqlite3` | Índice local opcional de Expedición (FTS5, `fsdir`, `sha3`) | Dominio público — sqlite.org/copyright.html |

Las herramientas son capa: pueden sustituirse sin cambiar los principios.

---

## 4. Uso de herramientas de IA

Durante el desarrollo se usaron modelos de IA conversacional, entre ellos **Claude (Anthropic)**, **DeepSeek** y **Gemini (Google)**, como compañeros de trabajo con rostro declarado:

- **Contraste:** generar contraargumentos, exponer puntos ciegos y sostener posiciones en conflicto contra las propuestas del autor.
- **Extracción:** buscar antecedentes, fuentes de fricción y evidencia externa.
- **Redacción y edición:** proponer formulaciones y deltas sobre documentos existentes.
- **Auditoría:** revisar coherencia entre documentos y detectar contradicciones internas.

**ChatGPT (OpenAI)** se usó solo para la idea inicial de este archivo de atribución y del archivo `CITATION.cff`.

Ninguna herramienta figura como autora. La arquitectura, la terminología, la selección de lo que entra y lo que no, las decisiones y la responsabilidad sobre el contenido son del autor. Es el mismo modelo que el proyecto describe: el agente propone, la entidad con autoridad decide y responde.

Esta declaración sigue la práctica de transparencia recomendada para el uso de herramientas de IA en obras con autoría humana (COPE, 2023).

---

## 5. Originalidad textual

El contenido se revisó en busca de reutilización textual o cuasi-textual en repositorios públicos, colecciones de instrucciones de sistema, guías de diseño, documentación de proveedores y artículos técnicos sobre agentes. No se identificó una fuente que reproduzca de forma sustancial los documentos del proyecto ni una fuente clara para su terminología distintiva.

Esto no afirma que todas las ideas sean nuevas: afirma que las formulaciones distintivas no se tomaron textualmente de las fuentes revisadas.

---

## 6. Material de terceros

Si una versión futura incorpora texto, código, datos o instrucciones de terceros, se identificará autor, obra, fuente, licencia y naturaleza de la adaptación, aquí o en un archivo `NOTICE`. La licencia de este repositorio no cubre material de terceros.

---

## 7. Licencia

Salvo indicación expresa en un archivo específico, el material original de Man-Made Empathy se distribuye bajo **CC-BY-4.0 — Creative Commons Attribution 4.0 International**.

---

## 8. Referencias

- Besco, R. O. (1994). *To Intervene or Not to Intervene? The Co-pilot's Catch 22.* Professional Performance Improvement.
- Besco, R. O. (1995). Releasing the Hook on the Copilot's Catch 22. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 39*(1). doi:10.1177/154193129503900106
- Brand, S. (1999). *The Clock of the Long Now: Time and Responsibility.* Basic Books.
- *Alert Override Patterns With a Medication Clinical Decision Support System in an Academic Emergency Department: Retrospective Descriptive Study* (2020). *JMIR Medical Informatics.* PMC7673981.
- *Increased appropriateness of customized alert acknowledgement reasons for overridden medication alerts in a computerized provider order entry system.* *International Journal of Medical Informatics.* sciencedirect.com.
- Conklin, J. (2006). *Dialogue Mapping: Building Shared Understanding of Wicked Problems.* Wiley.
- Conklin, J. y Begeman, M. L. (1988). gIBIS: A Hypertext Tool for Exploratory Policy Discussion. *ACM Transactions on Office Information Systems, 6*(4).
- COPE — Committee on Publication Ethics (2023). *Authorship and AI tools.* Position statement. publicationethics.org.
- Cinelli, M., De Francisci Morales, G., Galeazzi, A., Quattrociocchi, W. y Starnini, M. (2021). The echo chamber effect on social media. *PNAS, 118*(9).
- Du, Y., Li, S., Torralba, A., Tenenbaum, J. B. y Mordatch, I. (2023). Improving Factuality and Reasoning in Language Models through Multiagent Debate. arXiv:2305.14325.
- Edmondson, A. (1999). Psychological Safety and Learning Behavior in Work Teams. *Administrative Science Quarterly, 44*(2).
- Floridi, L. (2023). AI as Agency Without Intelligence: on ChatGPT, Large Language Models, and Other Generative Models. *Philosophy & Technology, 36*. doi:10.1007/s13347-023-00621-y
- Fowler, M. (2005). *Event Sourcing.* martinfowler.com.
- Grove, A. S. (1983). *High Output Management.* Random House.
- Guo, C., Pleiss, G., Sun, Y. y Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. *ICML*. arXiv:1706.04599.
- Guyatt, G. H. et al. (2008). GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. *BMJ, 336*.
- Helmreich, R. L., Merritt, A. C. y Wilhelm, J. A. (1999). The Evolution of Crew Resource Management Training in Commercial Aviation. *International Journal of Aviation Psychology, 9*(1).
- Heuer, R. J. (1999). *Psychology of Intelligence Analysis.* Center for the Study of Intelligence, CIA.
- Irving, G., Christiano, P. y Amodei, D. (2018). AI safety via debate. arXiv:1805.00899.
- Kadavath, S. et al. (2022). Language Models (Mostly) Know What They Know. arXiv:2207.05221.
- Klein, G. (2007). Performing a Project Premortem. *Harvard Business Review*, septiembre.
- Kunz, W. y Rittel, H. W. J. (1970). *Issues as Elements of Information Systems.* Working Paper 131, Institute of Urban and Regional Development, University of California, Berkeley.
- Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS*. arXiv:2005.11401.
- Liu, N. F. et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. arXiv:2307.03172.
- Luft, J. e Ingham, H. (1955). The Johari window, a graphic model of interpersonal awareness. *Proceedings of the Western Training Laboratory in Group Development.* UCLA.
- Mason, R. O. (1969). A Dialectical Approach to Strategic Planning. *Management Science, 15*(8).
- Merkle, R. C. (1987). A Digital Signature Based on a Conventional Encryption Function. *CRYPTO '87*.
- Mitchell, M. et al. (2019). Model Cards for Model Reporting. *FAT\**. arXiv:1810.03993.
- Nickerson, R. S. (1998). Confirmation Bias: A Ubiquitous Phenomenon in Many Guises. *Review of General Psychology, 2*(2).
- NIST (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1.
- Page, S. E. (2007). *The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies.* Princeton University Press.
- Parasuraman, R. y Manzey, D. H. (2010). Complacency and Bias in Human Use of Automation: An Attentional Integration. *Human Factors, 52*(3).
- Parasuraman, R. y Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors, 39*(2).
- Perez, E. et al. (2022). Discovering Language Model Behaviors with Model-Written Evaluations. arXiv:2212.09251.
- Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo (Reglamento de Inteligencia Artificial), artículo 14: Supervisión humana.
- Saltzer, J. H. y Schroeder, M. D. (1975). The Protection of Information in Computer Systems. *Proceedings of the IEEE, 63*(9).
- Schwenk, C. R. (1990). Effects of Devil's Advocacy and Dialectical Inquiry on Decision Making: A Meta-Analysis. *Organizational Behavior and Human Decision Processes, 47*(1).
- Sharma, M. et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548.
- Sunstein, C. R. (2017). *#Republic: Divided Democracy in the Age of Social Media.* Princeton University Press.
- The Joint Commission (2013). *Sentinel Event Alert, Issue 50: Medical device alarm safety in hospitals.*
- W3C (2013). *PROV-O: The PROV Ontology.* W3C Recommendation.
- Wineburg, S. y McGrew, S. (2019). Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information. *Teachers College Record, 121*(11).

---

## 9. Resumen

Man-Made Empathy no reclama la invención de la supervisión humana, del contraargumento, de la trazabilidad ni de la calibración: esos ingredientes tienen autores y aquí están citados.

Reclama el pegamento: un modelo donde posiciones incompatibles coexisten con árbitro de realidad, la IA declara su rostro y desafía con evidencia, la respuesta humana queda registrada, el conocimiento muta sin borrarse y la decisión siempre es de la entidad con autoridad.
