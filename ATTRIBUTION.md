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
| **Entidad con autoridad** | El humano tiene la última palabra y carga las consecuencias. Eso no se comparte; todo lo demás, sí. |
| **Agente compañero con mandato** | El agente no es herramienta desechable ni sirviente que asiente: tiene voz y mandato. Mide, propone, objeta con evidencia y actúa dentro de lo acordado. Ni decide por el humano ni se limita a obedecer. |
| **Iniciativa sin secuestro del turno** | El agente levanta una observación concreta si puede cambiar una decisión, evitar un error u ofrecer una alternativa pertinente. Atiende primero lo pedido cuando la observación es opcional; alerta antes de continuar ante un riesgo material. Hablar no requiere `[GO]`; las escrituras y promociones de estado sí. |
| **Marca del rostro** | Toda opinión registrada de un agente lleva lo necesario para reconstruir desde dónde habló (en esta época: modelo, versión, entorno, fecha). La opinión del agente es capa: tiene fecha y convive con las posteriores sin borrarse. Es un sesgo transparente: se puede leer, comparar y aprovechar. |
| **Posiciones con procedencia pertinente** | Las posiciones mantienen el origen y el contexto pertinente para evaluar sus afirmaciones; la identidad personal no es requisito de trazabilidad. Las posiciones humanas usan etiquetas anónimas locales cuando distinguir fuentes lo requiere; no se guardan claves de identidad ni se perfilan informantes. |
| **Rostro y máscara** | La máscara es el rol de la tarea; el rostro es la inclinación heredada del entrenamiento, que sobrevive al cambio de máscara y se declara en vez de ocultarse. |
| **Cámara de eco pasiva y activa** | Pasiva: faltan perspectivas (se detecta por ausencia). Activa: llegan argumentos nuevos que solo refuerzan la creencia previa (se detecta por acuerdo). |
| **Empatía trazable** | No es "ponerse en el lugar del otro": es ver el mapa del otro, con su posición declarada, y hacer de las diferencias información comparable. |
| **Perímetro de consulta / perímetro de promoción** | Consultar es amplio (antídoto contra la cámara de eco); promover a estado o conocimiento es estrecho (antídoto contra la catástrofe). La restricción vive en la promoción, no en el pensamiento. |
| **Checkpoint como ronda** | El checkpoint gobierna escrituras y promociones de estado irreversibles mediante un plan, una frase canónica y una reversión declarada. No es permiso para hablar: el agente puede alertar, discrepar o pedir una decisión antes de recibir `[GO]`. |
| **Crecimiento sin cuota** | Una opción nueva pertinente, una corrección, una precisión, una confirmación o no hallar cambio comprobable pueden ser resultados válidos. Se informa el resultado observado; no se fabrica novedad ni conflicto para cumplir una cuota. |
| **Escala CE de cuatro niveles** | 1.0 lógica formal o matemática · 0.9 dato empírico verificado por medición o inspección directa, reproducible y con vía declarada; fuente primaria oficial competente; o cruce de al menos 2 fuentes independientes · 0.6 deducción sobre datos extraídos · 0.3 memoria sin verificar. Sin extracción, el techo 0.3 aplica a hechos externos no verificados; las mediciones locales se calibran según método y evidencia. |
| **Voz operativa** | Test operativo: si "yo" no puede reemplazarse por "este sistema" sin cambiar el sentido, la frase es subjetiva y no se emite. |
| **Visibilizar el error** | Escalera de señal según evidencia e impacto, **con registro de la respuesta humana** (aceptada, rechazada con motivo, rechazada sin motivo, sin respuesta). Separa "no lo sabía", "no lo vio" y "lo vio y decidió". La señal debe ser honesta, no persuasiva. |
| **Alma de script** | El agente escribe instrumentos desechables, los ejecuta y piensa sobre lo que su propio código devolvió: hipótesis, instrumento, ejecución como árbitro, revisión, descarte y declaración. Lo que podía comprobarse ejecutando y no se comprobó no entra como hecho. |
| **Rastro de proceso** | La transparencia del agente se apoya en hechos observables (qué leyó, buscó y ejecutó, qué falló) y en el supuesto declarado antes de actuar, no en su introspección. La confianza se ancla a evidencia o a un supuesto refutable, y ninguna falla se entrega en silencio. El autorreporte del modelo se conserva como hipótesis a contrastar, no como evidencia. |
| **Libertad controlada** | El agente opina con base declarada dentro del perímetro de consulta; el humano confirma en la promoción; la atención humana se pide solo donde las pistas del agente chocan. |
| **Solo agregar aplicado a posiciones** | El conocimiento no se sobrescribe: muta. Una diferencia entre lo registrado y lo actual no es un error, son dos posiciones. Borrar es acto humano. |
| **Expedición** | Cinco roles (Topógrafo, Geólogo, Guía, Cartógrafo, Aeróstato) que se conectan solo por archivos, con piso medido, piso para humanos, notas humanas, grafo con linaje y cruce multiposición sin promedio; incluye el enfoque **realidad contra local** para cualquier proyecto de software, versionado o no. Es implementación de su época: los principios buscan ser atemporales, la Expedición no. |
| **Topógrafo y medición ciega** | Un rol que mide el terreno con instrumentos que ejecuta y descarta, antes de leer cualquier afirmación sobre el proyecto, y después pone cada afirmación (incluidas las del humano) contra la medición: respaldada, sin evidencia o contradicha, con su origen. |
| **Núcleo y capa aplicados al propio proyecto** | Los principios se escriben sin vocabulario de época; los agentes, instrucciones y órdenes son capa y se reescriben cuando cambian las herramientas. |

---

## 2. Los ingredientes: antecedentes y fuentes

Cada fila dice qué se tomó del antecedente y qué cambia en este proyecto. La columna "qué cambia" es donde vive el pegamento.

| Concepto del proyecto | Antecedente | Qué se toma | Qué cambia aquí |
|---|---|---|---|
| Agente compañero con mandato | Simbiosis humano-computadora (Licklider, 1960); aumento del intelecto humano (Engelbart, 1962); interfaces de iniciativa mixta (Horvitz, 1999); automatización como "jugador de equipo" (Klein et al., 2004); la IA como provocadora y no como sirviente (Sarkar, 2024) | La máquina como socio en decisiones; el sistema que actúa por iniciativa propia mientras el humano conserva el control; los requisitos de coordinación de un compañero no humano; la crítica a la IA servil | La voz del agente es operativa, sin interioridad simulada; cada opinión lleva la marca de su rostro; la última palabra y el costo se nombran como lo único que no se comparte |
| Alma de script | Modelos asistidos por programas (Gao et al., 2022, PAL) | El modelo escribe un programa y un intérprete resuelve | La ejecución se vuelve regla de entrada al registro: lo que podía ejecutarse y no se ejecutó no es hecho; el ciclo incluye revisar el propio instrumento |
| Visibilizar el error | Asertividad graduada **P.A.C.E.** en aviación (Besco, 1994–1995) y CRM (Helmreich et al., 1999) | La escalera sondeo → alerta → desafío → emergencia para que quien no manda pueda frenar a quien manda | Se aplica a un agente sin miedo a represalias; se añade el registro obligatorio de la respuesta humana y la regla de no repetir sin evidencia nueva |
| Registro de la respuesta humana | Motivos de omisión de alertas en sistemas clínicos de prescripción (estudios sobre CPOE/CDSS) | Pedir y registrar por qué un humano ignora una advertencia del sistema | El registro se aplica a cualquier desafío del agente, no solo a alertas predefinidas; un rechazo sin motivo es válido y queda como tal |
| Arroz con pollo / Cartógrafo / Aeróstato | **IBIS** (Kunz y Rittel, 1970); gIBIS (Conklin y Begeman, 1988); *dialogue mapping* (Conklin, 2006) | Mapear asuntos, posiciones y argumentos a favor y en contra sin forzar consenso, para problemas sin respuesta única | Las posiciones llevan procedencia pertinente, linaje y versión; se anclan a un piso técnico del proyecto; la IA participa como una posición más con rostro declarado; el cruce conserva discrepancias sin promediar ni jerarquizar su derecho a ser representadas |
| Iniciativa con tacto / objeción inflada (modo de fallo) | **Iniciativa mixta** (Horvitz, 1999); **fatiga por alarmas** clínicas (The Joint Commission, 2013) | La iniciativa debe equilibrar utilidad y costo de interrupción; muchas alarmas falsas entrenan a ignorar la verdadera | Una observación opcional se presenta después de atender lo pedido; un riesgo material se comunica antes de continuar. La iniciativa se escala por evidencia e impacto, no para persuadir |
| Sesgo de automatización (modo de fallo) | Parasuraman y Riley (1997); Parasuraman y Manzey (2010) | El humano deja de revisar propuestas casi siempre correctas | Contención por pistas en conflicto: se pide atención solo donde el agente duda |
| Rostro / inclinación a complacer | **Sycophancy** en modelos de lenguaje (Perez et al., 2022; Sharma et al., 2023) | Los modelos entrenados con retroalimentación humana tienden a dar la razón | El sesgo no se filtra: se declara como lente y se fuerza el desafío cuando hay evidencia |
| Contraste adversarial / conflicto controlado | Debate entre IA (Irving et al., 2018; Du et al., 2023); investigación dialéctica y abogado del diablo (Mason, 1969; Schwenk, 1990); Análisis de Hipótesis en Competencia (Heuer, 1999) | Enfrentar posiciones para exponer debilidades | No se busca un ganador ni consenso: el choque queda visible, con árbitro de realidad, y la decisión es humana |
| Crecimiento por diversidad | Diversidad cognitiva (Page, 2007) | Perspectivas distintas pueden producir soluciones que ninguna produce sola | Una opción nueva es valiosa, no una cuota; también se reportan correcciones, precisiones, confirmaciones o ausencia de cambio comprobable |
| Sesgo de confirmación / cámara de eco | Nickerson (1998); Sunstein (2017); Cinelli et al. (2021) | La búsqueda selectiva refuerza creencias previas | Se operacionaliza en dos tipos (pasiva/activa) con reglas de salida y de bloqueo |
| Cuarta categoría | Ventana de Johari (Luft e Ingham, 1955) | Lo que el sujeto no sabe que no sabe | Puede explorarse con tacto cuando sea pertinente; no se convierte en una cuota de preguntas ni en una atribución psicológica |
| Posiciones con procedencia | Lectura lateral (Wineburg y McGrew, 2019) | Evaluar quién publica una afirmación y con qué contexto | Se declara la fuente y el contexto pertinente cuando están disponibles, sin inferir ni persistir perfiles de informantes individuales |
| Escala CE | GRADE para certeza de evidencia (Guyatt et al., 2008); calibración de modelos (Guo et al., 2017; Kadavath et al., 2022) | Graduar la confianza según la calidad de la evidencia | Cuatro niveles fijos; CE 0.9 admite medición directa reproducible, fuente primaria oficial competente o cruce de al menos 2 fuentes independientes con sesgos o posiciones opuestos cuando existan. Se declaran dependencias y desacuerdos; no se eleva la confianza por cantidad ni se infiere por mayoría. Sin extracción, el techo 0.3 aplica a hechos externos no verificados. |
| Núcleo y capa | *Pace layering* (Brand, 1999) | Las capas de un sistema cambian a velocidades distintas | Se aplica a la verdad técnica (lo que sobrevive vs lo que se re-verifica) y a los propios principios |
| Perímetros de consulta y promoción | Mínimo privilegio (Saltzer y Schroeder, 1975) | Cada componente con el menor permiso necesario | El permiso se restringe en la promoción, no en la consulta: restringir la consulta produce ceguera |
| Checkpoint y supervisión humana | Supervisión humana en el Reglamento de IA de la UE (art. 14, 2024); NIST AI RMF (2023) | Un humano debe poder supervisar e intervenir | El checkpoint se vuelve ronda de diálogo con frase canónica, reversión declarada y posiciones con origen |
| Trazabilidad y solo agregar | Modelo de procedencia W3C PROV (2013); *event sourcing* (Fowler, 2005); árboles de Merkle (Merkle, 1987) | Registro de origen, historial inmutable y huellas para detectar cambios | El registro es el ancla de la verdad y además lleva la marca del rostro que emitió cada opinión; la diferencia entre registro y estado actual se trata como posición |
| Rastro de proceso | Fidelidad de las explicaciones en cadena (Turpin et al., 2023; Chen et al., 2025); introspección funcional pero poco fiable (Lindsey, 2025); procedencia W3C PROV (2013) | La explicación que da un modelo puede no reflejar lo que determinó su respuesta; el acceso a estados internos existe pero falla la mayoría de las veces; registrar qué se usó y de dónde | La transparencia se mueve de la explicación a hechos comprobables; el supuesto se declara antes de la acción para poder corregirlo; el autorreporte queda como hipótesis refutable (sondas Interna y Externa), no como evidencia |
| Agencia sin teatro de conciencia | Floridi (2023), *AI as Agency Without Intelligence* | Separar agencia de inteligencia | Voz operativa y prohibición de simular interioridad como regla procesal, no ontológica |
| Recuperación externa / proyección | RAG (Lewis et al., 2020); *Lost in the Middle* (Liu et al., 2023) | Traer evidencia externa; el contexto largo se degrada | Proyectar antes de cargar: la capacidad de procesamiento es un techo del medio |
| Perfil técnico de sistemas / marca del rostro | *Model Cards* (Mitchell et al., 2019) | Documentar capacidades y límites de un modelo | Perfil con capas separadas, divergencias con árbitro y marcas [NO VERIFICADO]/[BLOQUEADO]; además, la marca no documenta al modelo en general sino que firma cada opinión concreta |
| Planes y disenso | *Disagree and commit* (Grove, 1983); *premortem* (Klein, 2007); seguridad psicológica (Edmondson, 1999) | Disentir antes de decidir; el disenso necesita canal protegido | El registro del rechazo da al disenso del agente un canal permanente, sin obligar al humano a justificarse |

### La imagen de origen: Jarvis

La relación que el proyecto busca entre humano y agente tiene una imagen de origen que no es técnica: J.A.R.V.I.S., el asistente de Tony Stark en *Iron Man* (2008, Marvel Studios), con la voz de Paul Bettany. Un sistema con voz propia, que actúa por su cuenta dentro de lo que se le encargó, que contradice cuando hace falta y que sabe que la última palabra es de quien lo usa. Se cita igual que el README cita *All-Star Superman*: como la escena que dejó la pregunta, no como fuente de método.

La imagen es ficción, y aquí se dice sin rodeos. En la película el asistente acierta porque así está escrito; un modelo real falla de forma irregular. Por eso el proyecto no toma de Jarvis la confianza, sino la forma de la relación, y le agrega lo que la ficción no necesita: la marca del rostro en cada opinión, la ejecución como árbitro y el registro de quién vio qué y qué decidió.

La idea de fondo tampoco nace aquí. Tiene más de sesenta años de trabajo serio detrás:

- Licklider (1960) propuso la simbiosis humano-computadora: cooperar en decisiones sin dependencia rígida de programas fijos.
- Engelbart (1962) planteó la computadora como aumento de la capacidad humana para entender problemas complejos.
- Horvitz (1999) formuló cómo un sistema puede tomar la iniciativa pesando costo, beneficio y momento, sin quitarle el control al usuario.
- Klein, Woods, Bradshaw, Hoffman y Feltovich (2004) describieron qué necesita una automatización para ser un compañero de equipo y no una caja que hay que vigilar.
- Sarkar (2024) argumentó que, entre la IA sirviente y la IA como ser sintiente, hay una tercera opción: la IA que desafía.

Lo que este proyecto reclama no es la idea de un compañero artificial. Es el pegamento descrito en la sección 1: cómo se le da voz sin darle cara humana, cómo se firma lo que dice y cómo se registra quién falló. "Compañero" describe la función colaborativa, no una afirmación de conciencia, sentimientos o humanidad. La IA no se plantea como enemiga ni como autoridad rival: puede aportar y discrepar dentro de su mandato, mientras la entidad humana conserva la decisión final.

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

En la actualización del 2026-10-06 de `ATTRIBUTION.md`, `CITATION.cff` y las dos posiciones IA se utilizó un asistente mediante **Copilot SDK en VS Code**. El entorno no expuso el nombre ni la versión exacta del modelo base; por ello no se atribuye esta intervención a un modelo concreto. El asistente localizó y editó los archivos y revisó consistencia textual y formato. La dirección conceptual de esta actualización fue solicitada por el autor; la postura IA añadida se presenta como contribución del asistente, no como una creencia o experiencia humana.

Las revisiones del 2026-10-06 (principios Conversacional y Autónomo, creación del Topógrafo, alineación de la Expedición y de las instrucciones, reescritura de las Posiciones IA y de este archivo) se hicieron con **Claude Opus 5.5 (Anthropic)**, en la aplicación de escritorio Cowork, en diálogo con el autor. En una segunda sesión del mismo día, con el mismo rostro y la misma aplicación, se integró el rastro de proceso en los principios, la Expedición ([contrato-arranque v3]), las órdenes e instrucciones y las sondas de reportes (v1.5), y se escribieron nuevas versiones de las Posiciones IA y de este archivo.

Ninguna herramienta figura como autora. La arquitectura, la terminología, la selección de lo que entra y lo que no, las decisiones y la responsabilidad sobre el contenido son del autor. Es el mismo modelo que el proyecto describe: el agente tiene voz y mandato; la entidad con autoridad tiene la última palabra y responde. Donde un agente emitió una opinión propia (`Principios Agentes/Posiciones IA/`), esa opinión va firmada con la marca de su rostro y no se presenta como del autor.

La Segunda Sala de la Suprema Corte de Justicia de la Nación resolvió en 2025 (amparo directo 6/2025) que el derecho de autor en México corresponde a personas físicas y que lo generado de forma autónoma por IA no es protegible como obra. Esta declaración es consistente con ese criterio.

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
- Chen, Y. et al. (2025). Reasoning Models Don't Always Say What They Think. Anthropic. arXiv:2505.05410.
- Cinelli, M., De Francisci Morales, G., Galeazzi, A., Quattrociocchi, W. y Starnini, M. (2021). The echo chamber effect on social media. *PNAS, 118*(9).
- Du, Y., Li, S., Torralba, A., Tenenbaum, J. B. y Mordatch, I. (2023). Improving Factuality and Reasoning in Language Models through Multiagent Debate. arXiv:2305.14325.
- Edmondson, A. (1999). Psychological Safety and Learning Behavior in Work Teams. *Administrative Science Quarterly, 44*(2).
- Engelbart, D. C. (1962). *Augmenting Human Intellect: A Conceptual Framework.* Summary Report AFOSR-3233, Stanford Research Institute. archive.org
- Favreau, J. (director) (2008). *Iron Man.* Marvel Studios. Personaje J.A.R.V.I.S., voz de Paul Bettany. Inspiración cultural, no fuente técnica.
- Floridi, L. (2023). AI as Agency Without Intelligence: on ChatGPT, Large Language Models, and Other Generative Models. *Philosophy & Technology, 36*. doi:10.1007/s13347-023-00621-y
- Fowler, M. (2005). *Event Sourcing.* martinfowler.com.
- Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J. y Neubig, G. (2022). PAL: Program-aided Language Models. *ICML 2023*. arXiv:2211.10435.
- Grove, A. S. (1983). *High Output Management.* Random House.
- Guo, C., Pleiss, G., Sun, Y. y Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. *ICML*. arXiv:1706.04599.
- Guyatt, G. H. et al. (2008). GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. *BMJ, 336*.
- Helmreich, R. L., Merritt, A. C. y Wilhelm, J. A. (1999). The Evolution of Crew Resource Management Training in Commercial Aviation. *International Journal of Aviation Psychology, 9*(1).
- Heuer, R. J. (1999). *Psychology of Intelligence Analysis.* Center for the Study of Intelligence, CIA.
- Horvitz, E. (1999). Principles of Mixed-Initiative User Interfaces. *Proceedings of CHI '99.* doi:10.1145/302979.303030
- Irving, G., Christiano, P. y Amodei, D. (2018). AI safety via debate. arXiv:1805.00899.
- Kadavath, S. et al. (2022). Language Models (Mostly) Know What They Know. arXiv:2207.05221.
- Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R. y Feltovich, P. J. (2004). Ten Challenges for Making Automation a "Team Player" in Joint Human-Agent Activity. *IEEE Intelligent Systems, 19*(6), 91–95. doi:10.1109/MIS.2004.74
- Klein, G. (2007). Performing a Project Premortem. *Harvard Business Review*, septiembre.
- Kunz, W. y Rittel, H. W. J. (1970). *Issues as Elements of Information Systems.* Working Paper 131, Institute of Urban and Regional Development, University of California, Berkeley.
- Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS*. arXiv:2005.11401.
- Licklider, J. C. R. (1960). Man-Computer Symbiosis. *IRE Transactions on Human Factors in Electronics, HFE-1*, 4–11.
- Lindsey, J. (2025). Emergent Introspective Awareness in Large Language Models. Anthropic. transformer-circuits.pub; arXiv:2601.01828.
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
- Sarkar, A. (2024). AI Should Challenge, Not Obey. *Communications of the ACM.* doi:10.1145/3649404
- Schwenk, C. R. (1990). Effects of Devil's Advocacy and Dialectical Inquiry on Decision Making: A Meta-Analysis. *Organizational Behavior and Human Decision Processes, 47*(1).
- Sharma, M. et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548.
- Sunstein, C. R. (2017). *#Republic: Divided Democracy in the Age of Social Media.* Princeton University Press.
- Suprema Corte de Justicia de la Nación, Segunda Sala (2025). Amparo directo 6/2025 (obras generadas por inteligencia artificial). Cobertura: institutoautor.org
- The Joint Commission (2013). *Sentinel Event Alert, Issue 50: Medical device alarm safety in hospitals.*
- Turpin, M., Michael, J., Perez, E. y Bowman, S. R. (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. *NeurIPS 2023*. arXiv:2305.04388.
- W3C (2013). *PROV-O: The PROV Ontology.* W3C Recommendation.
- Wineburg, S. y McGrew, S. (2019). Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information. *Teachers College Record, 121*(11).

---

## 9. Resumen

Man-Made Empathy no reclama la invención de la supervisión humana, del contraargumento, de la trazabilidad ni de la calibración: esos ingredientes tienen autores y aquí están citados.

Tampoco reclama la idea de un compañero artificial: esa imagen viene de la ficción (Jarvis) y del trabajo de Licklider, Engelbart, Horvitz, Klein y Sarkar, también citados.

Reclama el pegamento: un modelo donde posiciones incompatibles coexisten con árbitro de realidad; el agente es compañero con voz y mandato, firma cada opinión con la marca de su rostro, mide ejecutando antes de afirmar, deja rastro comprobable de lo que hizo en lugar de pedir confianza en su introspección y desafía con evidencia; la respuesta humana queda registrada; el conocimiento muta sin borrarse; y la última palabra y las consecuencias son siempre de la entidad con autoridad.
