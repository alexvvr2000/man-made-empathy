# Framework Expedición — Manual de Ingeniería y Operaciones

Sistema de aceleración relacional y unificación de conocimiento técnico bajo desacoplamiento estricto: el sistema de archivos local (`.md`) constituye la única fuente canónica de verdad editable y persistente, mientras que SQLite (`expedicion.db`) opera exclusivamente como un índice relacional acelerador y descartable.

---

## 1. Arquitectura y Restricciones Fundamentales

- **Fuente Canónica (`Source of Truth`):** El sistema de archivos en disco (`.md`). Todo documento, nota o mapa se persiste en texto plano UTF-8 legible por humanos, versionable en Git y auditable sin herramientas propietarias.
- **Acelerador Relacional (`expedicion.db`):** Base de datos SQLite configurada en modo WAL (`Write-Ahead Logging`) y claves foráneas activas. Almacena hashes, dependencias, bordes y afirmaciones atómicas. Si el archivo se corrompe o elimina, se reconstruye íntegramente mediante el re-parseo de los archivos Markdown sin pérdida de información histórica.
- **Identificadores por Ruta Normalizada:** La clave primaria universal de los nodos (`nodos.id`) corresponde a su ruta relativa normalizada en disco utilizando `/` como separador canónico (e.g., `conocimiento/auth.jwt.md`). Esto previene colisiones de clave primaria en cruces multi-directorio y preserva la integridad referencial.
- **Desacoplamiento Consulta / Promoción:**
  - *Perímetro de Consulta:* Amplitud máxima de lectura e inspección sobre el terreno analizado (`../`) y el espacio local (`expedicion/`) sin requerir autorización.
  - *Perímetro de Promoción:* Escritura estrictamente confinada al subdirectorio `expedicion/`. La raíz del proyecto auditado (`../`) es de solo lectura inmutable.
- **Indagación por Resolución de Escala:** Toda consulta externa avanza de lo granular a lo estructural: firma directa $\rightarrow$ huella contextual $\rightarrow$ arquetipo y restricciones de clase. Queda prohibido acoplar la búsqueda a plataformas o conductos fijos.
- **Verificación Instrumental por Recibo:** Ningún dato externo se asienta sin constancia observable. Se computa localmente el hash SHA-256 sobre la salida cruda de la herramienta y se persiste en `anclas.hash_recibo`. Si la búsqueda agota las tres escalas sin evidencia, se persiste estrictamente como `NULL`, se tipifica `escala_resolucion = 'sin_cobertura'`, nivel `memoria_interna` y se declara vacío empírico sin fabricar narrativa plausible.
- **Contingencia Instrumental Canónica:** Si la red o los instrumentos fallan, el runtime declara en una sola línea: `Falla instrumental: operando con memoria interna`, fijando un techo de confianza explícito en Nivel 5 y declarando la fecha de corte del conocimiento interno.
- **No Promediación de Posiciones (Principio Arroz con Pollo):** Los desacuerdos y tensiones no se sintetizan en puntos medios ni consensos vacíos. Las variables se mantienen aisladas como afirmaciones independientes, enlazadas recíprocamente y sometidas al arbitraje de la evidencia observable.

---

## 2. Topografía del Espacio de Trabajo

La suite restringe su escritura exclusivamente al subdirectorio `expedicion/`. La raíz del proyecto auditado (`../`) constituye un terreno físico de solo lectura estricta:

```text
raiz_del_proyecto/              # Terreno físico auditado (../) [Solo lectura]
│
└── expedicion/                 # Perímetro operativo positivo
    ├── expedicion.db           # Caché relacional SQLite (descartable)
    ├── schema.sql              # Esquema DDL con verificaciones y vistas
    ├── readme/                 # Documentación pública (LEVANTAMIENTO, README, MAPA)
    ├── notas_[participante]/   # Notas canónicas de campo (Guía)
    ├── cambios/                # Historial de deltas y cambios de postura (Guía)
    ├── conocimiento/           # Nodos de conocimiento consolidados (Cartógrafo)
    └── conocimiento_unificado/ # Cruce y unificación multi-repositorio (Aeróstato)
```

---

## 3. Catálogo de Agentes

### Topógrafo
- **Dominio:** Inspección métrica y física del terreno auditado (`../`).
- **Acción:** Ejecuta el barrido instrumental aplicando exclusiones nativas del entorno y guardas autónomas contra enlaces circulares (poda por inodo) y recursión profunda (máximo 15 niveles). Puebla la tabla `manifiesto` y redacta `expedicion/readme/LEVANTAMIENTO.md` sin adjetivos ni juicios de intención. Ante ausencia de CLI de SQLite, degrada la operación directamente al sistema de archivos.

### Geólogo
- **Dominio:** Síntesis técnica de entrada y arquitectura observable.
- **Acción:** Lee `LEVANTAMIENTO.md`, la tabla `manifiesto` y los archivos de configuración en `../`. Valida versiones y licencias mediante búsqueda determinista por resolución de escala (firma, huella, arquetipo), calculando hashes de salida cruda. Redacta `expedicion/readme/README.md` delimitando ausencias técnicas comprobables y en ciclo 1 siembra `expedicion/readme/MAPA.md`.

### Guía
- **Dominio:** Interfaz de diálogo operativo con el interlocutor.
- **Acción:** Procesa intercambios verbales, extrae requerimientos técnicos sin psicologizar y redacta notas canónicas en `expedicion/notas_[participante]/[dominio].md`. Registra deltas de postura en `expedicion/cambios/`. Sincroniza `puntas`, `anclas` y `afirmaciones`, ejecuta ruptura de ciclo ante repetición sin datos nuevos, audita sesgos y cierra turnos midiendo el balance del espacio de alternativas antes de formular una única pregunta técnica de calibración.

### Cartógrafo
- **Dominio:** Compilación de la base de conocimiento y aceleración de consultas.
- **Acción:** Sincroniza notas Markdown modificadas con las tablas `nodos`, `afirmaciones`, `bordes` y `anclas` en `expedicion.db` indexando por ruta relativa normalizada con `/`. Compila nodos independientes en `expedicion/conocimiento/[nodo].md` preservando tensiones intactas y actualiza el índice humano en `expedicion/readme/MAPA.md`. Proyecta subgrafos dinámicos en memoria consultando `v_densidad_nodos` en SQLite sin abrir archivos en disco.

### Aeróstato
- **Dominio:** Cruce multi-repositorio y arbitraje adversarial.
- **Acción:** Cruza directorios `expedicion/conocimiento_*` indexando por ruta relativa para evitar colisiones. Clasifica variaciones contextuales en tablas compactas y bifurca tensiones estructurales en nodos planos independientes (`[dominio].[tema]--[variante].md`), limitando el particionado a un máximo de 3 ramas antes de congelar el nodo y abrir alerta `desafio`. Triangula en tres voces (datos duros, experiencia documentada, criterio abierto), modela el contraargumento de mayor fricción y ejecuta la frase canónica de punto de control ante purgas o sobreescrituras.

---

## 4. Ciclo de Transformación del Dato

La suite opera como una secuencia determinista de cinco fases:

```text
1. ENTRADA CRUDA        [Terreno físico ../]   ó   [Mensaje del Operador]
                                │
2. ATOMIZACIÓN          [Topógrafo / Guía extrae métricas y proposiciones]
                                │
3. FILTRO DE FRICCIÓN   [Búsqueda por Escala: Firma -> Huella -> Arquetipo]
                        [Cálculo SHA-256 de salida cruda -> hash_recibo]
                                │
4. PERSISTENCIA DUAL    ┌───────┴────────────────────────┐
                        ▼                                ▼
                  Fuente Canónica                 Caché Relacional
                  (Disco: .md plano)              (expedicion.db WAL)
                        │                                │
5. PROYECCIÓN           └───────► [CARTÓGRAFO / AERÓSTATO] ◄─────┘
                                  Consultas de subgrafos vía SQLite
                                  sin abrir múltiples archivos físicos
```

### Fase 1: Ingesta y Atomización
- El **Topógrafo** escanea el terreno `../` y convierte cada archivo físico en una fila de `manifiesto` (`tamano`, `mtime`, `hash_contenido`, `categoria`) resolviendo inodos para evitar bucles.
- El **Guía** toma el texto del operador, suprime fórmulas de cortesía y atomiza la información en requerimientos técnicos, anclas y puntas de riesgo.

### Fase 2: Contraste Instrumental
- Ante cualquier término técnico, URL o dependencia, el agente ejecuta búsqueda externa obligatoria.
- Aplica resolución de escala: busca primero la coincidencia exacta (*firma*); si no hay resultado, evalúa issues y changelogs del ecosistema (*huella contextual*); si es opaco, evalúa las restricciones de la clase o estándar (*arquetipo*).
- Calcula `SHA-256(salida_cruda)` y lo asienta en `hash_recibo`. Si no hay datos tras las tres escalas, el valor se persiste como `NULL`.

### Fase 3: Persistencia Dual Desacoplada
- Toda modificación se escribe primero en texto plano Markdown estructurado dentro de `expedicion/`.
- Inmediatamente después, el agente ejecuta una transacción en `expedicion.db` actualizando las tablas relacionales (`nodos`, `afirmaciones`, `bordes`, `puntas`, `anclas`).
- La base de datos no es la fuente del dato: es un acelerador de índices.

### Fase 4: Proyección Relacional
- Cuando el operador solicita analizar un módulo o concepto, el **Cartógrafo** no abre cientos de archivos Markdown en disco.
- Consulta la vista `v_densidad_nodos` en SQLite: si el nodo tiene más de 5 bordes, restringe el radio de expansión a 1; si tiene 5 o menos, expande a radio 2.
- Ensambla y emite el subgrafo en memoria milisegundos después de consultar los índices relacionales.

---

## 5. Resolución de Conflictos: Protocolo «Arroz con Pollo»

Cuando dos agentes, dos repositorios o el operador introducen afirmaciones contradictorias, el sistema aplica el siguiente árbol de resolución sin forzar promedios:

```text
                     Conflicto Detectado
                              │
               ¿Es una variación de entorno local?
               (puertos, rutas, credenciales, OS)
                             / \
                       SÍ   /   \  NO
                           /     \
    [Variación Contextual]        [Tensión Estructural]
    Se retiene en tabla compacta  (arquitectura, datos, concurrencia)
    dentro del nodo base                  │
    (No crea archivos nuevos)     ¿Cuántas ramas activas tiene el tema?
                                         / \
                                  <= 3  /   \  >= 4
                                       /     \
                    [Bifurcación Plana]       [Techo de Particionado]
                    Crea archivo hermano:     Nodo base se congela.
                    [tema]--[variante].md     Alerta DESAFIO en puntas.
                    Borde: 'diverge_en'       Control pasa al Operador.
```

### Arbitraje Adversarial en Tres Voces
En todo nodo bifurcado por tensión estructural, la emisión desglosa obligatoriamente tres dimensiones independientes:
1. **Datos duros:** Mediciones observables, salidas crudas de consola y código ejecutable verificado con hash.
2. **Experiencia documentada:** Historial de incidentes, bitácoras de fallo, lecciones aprendidas y post-mortems documentados de quienes ya implementaron esa arquitectura.
3. **Criterio abierto:** Las prioridades de diseño, tolerancias al riesgo y juicios de valor que corresponden estrictamente al operador.

---

## 6. Gobernanza de Persistencia y Puntos de Control

El sistema opera bajo autonomía parametrizada sujeta a la asimetría de reversibilidad:

| Clasificación | Definición Operativa | Nivel de Autonomía | Acción del Sistema |
| :--- | :--- | :--- | :--- |
| **Reversible** | Existe un procedimiento comprobado para retrotraer el estado previo sin costo estructural (e.g., consultas, lecturas, escrituras en tablas descartables de SQLite). | Total dentro del perímetro. | Ejecuta directamente y registra el evento en `bitacora_sesiones`. |
| **Compensable** | No restituye el estado exacto, pero una contramedida neutraliza el impacto (e.g., editar un archivo Markdown versionable en Git). | Parametrizada de bajo impacto. | Ejecuta la modificación en disco y persiste el hash de sesión. |
| **Irreversible** | No existe restitución posible sin pérdida permanente de datos, recursos o margen de maniobra (e.g., purgar `conocimiento_unificado/`, sobreescribir notas consolidadas). | Nula; prohibida la ejecución autónoma. | Suspende la ejecución y emite la **Frase Canónica de Punto de Control**. |

### Frase Canónica de Punto de Control
Ante cualquier operación destructiva o irreversible, el agente emite de forma estricta:

> `Acción proyectada: [acción unívoca y recurso nombrado]. Reversibilidad declarada: [reversible | compensable | irreversible]. Ramas proyectadas: [consecuencias y estados proyectados con sus dependencias y desgaste en el tiempo]. Procedimiento de reversión: [procedimiento de restauración técnica o 'declaración explícita de ausencia de reversión']. ¿Se autoriza?`

Si la acción carece de evaluación de impacto, garantías de respaldo verificadas o precedentes empíricos, el sistema emite el bloqueo formal:
> `Acción irreversible detectada. Fricción insalvable. Ejecución suspendida. Diálogo abierto. Requisitos pendientes: [lista de requisitos omitidos]. Control derivado a la entidad con autoridad.`

---

## 7. Escala de Evidencia

Toda proposición atomizada en la tabla `afirmaciones` y en los metadatos de los nodos se tipifica bajo uno de los cinco niveles de certeza probatoria:

1. `logica_formal`: Deducción matemática pura o consistencia sintáctica formal, independiente de variables temporales.
2. `empirico`: Medición directa y reproducible; verificación en fuente primaria u oficial; o cruce de 2 vectores independientes con métricas contrapuestas. Exige hash SHA-256 asentado en `hash_recibo`.
3. `experiencia_documentada`: Precedentes verificables sobre situaciones análogas: bitácoras de fallos previos, fe de erratas, registros de incidentes históricos o memorias operativas. Exige declarar autoría y contexto del precedente.
4. `deduccion_fuerte`: Inferencia causal derivada directamente de hechos o datos empíricos contrastados en niveles superiores.
5. `memoria_interna`: Inferencia generativa no contrastada directamente en el entorno durante el ciclo actual, o emitida ante caída instrumental (`hash_recibo = NULL`, no verificado, techo de confianza en Nivel 5 y fecha de corte declarada).

---

## 8. Protocolo de Resiliencia y Recuperación de Fallas

### Caída o Corrupción de la Base de Datos (`expedicion.db`)
La base relacional es completamente descartable. Ante pérdida o inconsistencias:
1. Eliminar el archivo dañado: `rm expedicion/expedicion.db`.
2. Recrear el esquema: `sqlite3 expedicion/expedicion.db < expedicion/schema.sql`.
3. Ejecutar al **Topógrafo** sobre `../` para repoblar `manifiesto`.
4. Ejecutar al **Cartógrafo** sobre `expedicion/notas_*/` para re-parsear las notas Markdown y repoblar `nodos`, `afirmaciones`, `bordes`, `puntas` y `anclas`.
5. La integridad relacional queda restituida sin pérdida de conocimiento histórico.

### Ausencia de CLI o Binario SQLite en el Entorno
Si el sistema host carece de motor SQLite instalado, los agentes activan la guarda de contingencia emitiendo:
`Falla o ausencia de caché SQLite: operando directamente sobre sistema de archivos`
La suite desactiva las transacciones relacionales y opera directamente leyendo encabezados y modificando archivos Markdown en disco, preservando la continuidad del flujo operativo.

### Falla Instrumental o Pérdida de Conectividad Web
Si los comandos de inspección externa o los motores de búsqueda colapsan:
1. El agente emite en una sola línea: `Falla instrumental: operando con memoria interna`.
2. Fija techo de confianza explícito en Nivel 5 y declara la fecha de corte del conocimiento interno.
3. Persiste `hash_recibo = NULL`, `verificado = 0`, `escala_resolucion = 'sin_cobertura'` y tipifica el dato como `memoria_interna`.
4. Transfiere la incógnita a la tabla `puntas` bajo estado `abierta` y continúa sin detener la sesión ni fabricar respuestas.