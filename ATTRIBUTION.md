# Atribución y contexto intelectual

## Man-Made Empathy

**Man-Made Empathy** es una síntesis de ideas, prácticas, conceptos y patrones de diseño provenientes de distintas áreas, entre ellas inteligencia artificial, ingeniería de software, seguridad de sistemas, interacción humano-computadora, epistemología, ciencia de la información y teoría de decisiones.

Este proyecto no afirma que los conceptos generales utilizados en sus principios hayan sido inventados por su autor. Muchos de ellos cuentan con antecedentes en investigación, ingeniería y práctica profesional anteriores a este repositorio.

La contribución de este proyecto consiste en la **selección, combinación, organización, terminología y formalización** de esos elementos dentro de una arquitectura coherente para agentes conversacionales y autónomos.

En términos simples:

> **Los ingredientes tienen antecedentes. La síntesis y la forma de conectarlos en este sistema constituyen la contribución de este proyecto.**

---

## 1. Naturaleza de la contribución

Man-Made Empathy debe entenderse como una **síntesis de diseño**, no como una afirmación de autoría exclusiva sobre cada mecanismo o concepto individual que aparece en el repositorio.

Entre los conceptos y prácticas que tienen antecedentes independientes se encuentran, entre otros:

* supervisión humana de sistemas automatizados;
* aprobación humana para acciones consecuentes o irreversibles;
* checkpoints y mecanismos de autorización;
* separación entre razonamiento y ejecución;
* trazabilidad y registros de auditoría;
* procedencia y evaluación de fuentes;
* mitigación del sesgo de confirmación;
* razonamiento adversarial y generación de contraargumentos;
* calibración de confianza;
* recuperación externa de información;
* reversibilidad y recuperación;
* separación de responsabilidades;
* restricciones de ejecución;
* evaluación de incertidumbre;
* interacción humano-computadora.

Estos conceptos no se presentan como invenciones exclusivas de este proyecto.

Lo que este repositorio propone es una organización particular de estos elementos dentro de un mismo modelo operacional.

---

## 2. Contribución del proyecto

La contribución de Man-Made Empathy se encuentra principalmente en la **arquitectura de relaciones entre sus componentes**.

El proyecto desarrolla y conecta, entre otros, los siguientes conceptos y términos:

* **Entidad con autoridad**
* **Conflicto controlado**
* **Posiciones, no fuentes**
* **Rostro y máscara**
* **Cámara de eco pasiva y activa**
* **Empatía trazable**
* **Perímetro de consulta**
* **Perímetro de promoción**
* **Checkpoint como ronda de diálogo**
* **Crecimiento real**
* **Contraste adversarial**
* **Núcleo y capa**
* **Techo**
* **Ruptura de ciclo**
* **Cruce de fuentes**

Estos conceptos forman parte del vocabulario y de la estructura propia del proyecto.

La propuesta central es que un agente puede utilizar posiciones incompatibles, evidencia externa, trazabilidad y contraste para **ampliar el espacio de decisión de la entidad con autoridad sin sustituir su criterio**.

Los documentos correspondientes al agente conversacional y al agente autónomo forman parte de esta misma arquitectura.

---

## 3. Relación con trabajos anteriores

Algunos mecanismos utilizados por el proyecto tienen antecedentes ampliamente establecidos.

### Supervisión humana y acciones irreversibles

La aprobación humana antes de determinadas acciones, los mecanismos de autorización y los checkpoints previos a acciones irreversibles son prácticas conocidas en sistemas automatizados y agentes de IA.

Man-Made Empathy no reclama haber inventado estos mecanismos.

La particularidad del proyecto está en integrarlos dentro de un modelo donde el checkpoint funciona como una **ronda de decisión**: antes de ejecutar, el agente presenta la acción, su reversibilidad, las posiciones relevantes, su procedencia y las limitaciones que reconoce.

### Razonamiento adversarial

La generación de contraargumentos, el *steelman*, la evaluación adversarial y la búsqueda de evidencia que contradiga una posición tienen antecedentes anteriores a este proyecto.

Man-Made Empathy los incorpora dentro del concepto de **conflicto controlado**, donde las posiciones incompatibles permanecen visibles en lugar de reducirse prematuramente a una síntesis o consenso.

### Sesgo de confirmación y cámaras de eco

El sesgo de confirmación, las cámaras de eco y la búsqueda selectiva de evidencia son conceptos establecidos en distintas áreas de investigación.

El proyecto los aplica al comportamiento de agentes mediante mecanismos como la **cámara de eco pasiva**, la **cámara de eco activa**, la búsqueda de posiciones externas y la utilización de evidencia externa como mecanismo de corrección.

### Trazabilidad y auditoría

La trazabilidad, la procedencia de datos, los registros de acciones y la auditoría son prácticas establecidas en ingeniería de software, seguridad y sistemas críticos.

Man-Made Empathy las incorpora dentro de un modelo en el que el **registro constituye el ancla de trazabilidad**, en lugar de utilizar la identidad del agente como garantía de continuidad.

---

## 4. Fuentes e influencias

El desarrollo del proyecto se sitúa dentro de un conjunto amplio de disciplinas y prácticas, entre ellas:

* ingeniería de agentes de IA;
* ingeniería de software;
* seguridad de sistemas;
* inteligencia artificial;
* interacción humano-computadora;
* epistemología;
* ciencia de la información;
* teoría de decisiones;
* análisis de riesgos;
* razonamiento adversarial;
* recuperación y evaluación de información;
* sistemas con supervisión humana.

Estas áreas constituyen el contexto intelectual y técnico en el que se desarrolla el proyecto.

La existencia de un antecedente conceptual no implica necesariamente que una formulación concreta del repositorio haya sido tomada de dicho antecedente.

---

## 5. Originalidad textual

El contenido del proyecto fue revisado específicamente en busca de reutilización textual o cuasi-textual en material públicamente disponible, con atención particular a:

* repositorios de GitHub;
* colecciones de prompts de sistema;
* benchmarks de agentes;
* guías de diseño de prompts;
* documentación técnica;
* documentación pública de proveedores de modelos;
* artículos y trabajos técnicos relacionados con agentes y seguridad.

La revisión se centró en **coincidencias textuales específicas**, no en la existencia de conceptos generales compartidos.

No se identificó una fuente que reproduzca de manera sustancial los dos documentos del proyecto ni una fuente clara para su terminología y estructura distintivas.

Esto no constituye una afirmación de que todas las ideas utilizadas sean nuevas. Significa que, dentro de las fuentes revisadas, no se identificó una reutilización textual sustancial de las formulaciones distintivas del proyecto.

---

## 6. Ideas, influencias y material reutilizado

Este repositorio distingue entre tres situaciones diferentes:

### Idea o concepto establecido

Una idea general puede ser utilizada de forma independiente por múltiples autores y proyectos.

Su utilización no implica que este repositorio reclame haberla inventado.

### Influencia o antecedente

Un trabajo puede haber servido como referencia intelectual o técnica para una decisión de diseño.

Cuando corresponda, estas influencias pueden documentarse mediante referencias bibliográficas o enlaces a la obra correspondiente.

### Material reutilizado o adaptado

Cuando se incorpora texto, código, documentación, prompts, datos u otro material perteneciente a terceros, se debe identificar la fuente y respetar la licencia aplicable.

La reutilización directa o adaptación de material de terceros no debe presentarse como material original de Man-Made Empathy.

---

## 7. Material de terceros

Los materiales de terceros incorporados al repositorio, cuando existan, deben conservar su atribución y condiciones de licencia correspondientes.

Cuando sea necesario, la atribución deberá indicar:

* autor u organización;
* título de la obra;
* fuente o URL;
* licencia;
* naturaleza de la reutilización o adaptación.

La licencia de Man-Made Empathy no sustituye ni modifica las licencias aplicables a materiales pertenecientes a terceros.

Si una versión futura del repositorio incorpora material de terceros que requiera atribución específica, dicha información deberá añadirse a este archivo o a un archivo `NOTICE` correspondiente.

---

## 8. Licencia de Man-Made Empathy

Salvo que se indique expresamente lo contrario en un archivo específico, el material original de Man-Made Empathy se distribuye bajo:

**CC-BY-4.0 — Creative Commons Attribution 4.0 International.**

La reutilización, adaptación y redistribución del material original están permitidas de acuerdo con los términos de dicha licencia y sus requisitos de atribución.

La licencia de este repositorio no implica que el material perteneciente a terceros pase a estar cubierto por CC-BY-4.0.

---

## 9. Principio de atribución

El objetivo de esta política no es atribuir artificialmente cada concepto general a una persona o publicación concreta.

El objetivo es mantener una distinción clara entre:

* **ideas existentes;**
* **influencias intelectuales;**
* **síntesis y formulaciones propias;**
* **material reutilizado o adaptado de terceros.**

Cuando un concepto sea ampliamente establecido, no se presenta como una invención de este proyecto.

Cuando una formulación, estructura, terminología o combinación sea propia del proyecto, se considera parte de la contribución original del autor.

Cuando se reutilice material específico de terceros, se deberá proporcionar la atribución correspondiente.

---

## 10. Posición intelectual del proyecto

Man-Made Empathy no se presenta como una obra creada en aislamiento.

Se presenta como una **síntesis deliberada de conocimientos y prácticas existentes**, organizada alrededor de una arquitectura y un conjunto de principios desarrollados específicamente para este proyecto.

La intención no es afirmar:

> "Estas ideas existían antes y por lo tanto no aporto nada."

Ni tampoco:

> "Todo lo que aparece aquí fue inventado desde cero."

La posición del proyecto es intermedia y deliberada:

> **Los conceptos tienen una historia. La contribución está en cómo se seleccionan, relacionan, formalizan y convierten en un sistema operativo coherente.**

Esta distinción permite reconocer la deuda intelectual con trabajos anteriores sin atribuir a terceros formulaciones o estructuras que fueron desarrolladas específicamente para Man-Made Empathy.

---

## 11. Referencias

Las referencias específicas a trabajos, documentación, investigaciones o materiales de terceros utilizados directamente por el proyecto deben mantenerse aquí cuando resulte apropiado.

Cuando una referencia corresponda a material reutilizado o adaptado, deberá indicarse además la licencia y la naturaleza de la reutilización.

Las referencias de carácter exclusivamente contextual o académico no deben interpretarse automáticamente como fuentes textuales de los contenidos del repositorio.

---

## 12. Resumen

Man-Made Empathy es una **síntesis original de diseño**, no una afirmación de que todos sus conceptos individuales sean originales.

El proyecto reconoce los antecedentes técnicos e intelectuales de sus componentes y, al mismo tiempo, reivindica como trabajo propio la selección, organización, terminología, formalización y arquitectura mediante las cuales dichos componentes se integran.

En términos simples:

> **No se reclama la invención de cada ingrediente. Se reclama la autoría de esta combinación, esta estructura y esta forma de convertirlos en un sistema coherente.**
