# Framework Expedición — Manual del Operador

Sistema de aceleración relacional y unificación de conocimiento técnico bajo desacoplamiento estricto: los archivos Markdown en disco constituyen la fuente canónica de verdad editable a mano, mientras que SQLite opera como un acelerador relacional e índice descartable.

---

## 1. Arquitectura y Restricciones Fundamentales

- **Fuente Canónica (`Source of Truth`):** El sistema de archivos local (`.md`). Toda nota, mapa o análisis es texto plano editable, versionable en Git y auditable sin dependencias propietarias.
- **Acelerador Relacional (`expedicion.db`):** Base de datos SQLite configurada en modo WAL con claves foráneas activas. Almacena índices, hashes, bordes y afirmaciones atómicas para consultas de subgrafos en milisegundos. Si la base de datos se corrompe o elimina, se reconstruye por re-parseo de los archivos Markdown sin pérdida histórica.
- **Identificadores por Ruta Normalizada:** La clave primaria de los nodos en la base de datos (`nodos.id`) corresponde a su ruta relativa normalizada en disco usando `/` como separador universal. Esto previene colisiones al unificar múltiples directorios de conocimiento y asegura la integridad referencial.
- **Desacoplamiento Consulta / Promoción:** Los agentes inspeccionan y extraen datos con amplitud máxima de lectura (perímetro de consulta), pero confinan su escritura a directorios locales específicos bajo contratos de reversibilidad (perímetro de promoción).
- **Verificación Instrumental y de Recibo:** Toda aserción sobre hechos externos o dependencias se valida mediante búsqueda web incondicional o comandos deterministas en el entorno, persistiendo el hash SHA-256 de la salida cruda. Si la herramienta falla o el dato no existe, el valor se persiste como `NULL` y se clasifica como `memoria_interna`.
- **No Promediación de Posiciones:** Las divergencias y tensiones no se sintetizan en puntos medios. Se preservan como afirmaciones independientes, enlazadas recíprocamente y clasificadas según la Escala de Evidencia.

---

## 2. Topografía del Espacio de Trabajo

La suite restringe su escritura exclusivamente al directorio `expedicion/`. La raíz del proyecto auditado (`../`) es un terreno de solo lectura estricta:

```text
raiz_del_proyecto/              # Terreno físico auditado (../) [Solo lectura]
│
└── expedicion/                 # Perímetro operativo positivo
    ├── expedicion.db           # Caché relacional SQLite (descartable)
    ├── schema.sql              # Esquema DDL con verificaciones y vistas
    ├── readme/                 # Documentación técnica pública (LEVANTAMIENTO, README, MAPA)
    ├── notas_[participante]/   # Notas estructuradas de campo (Guía)
    ├── cambios/                # Historial de deltas y cambios de postura (Guía)
    ├── conocimiento/           # Nodos de conocimiento consolidados (Cartógrafo)
    └── conocimiento_unificado/ # Cruce y unificación multi-repositorio (Aeróstato)
```

---

## 3. Catálogo de Agentes

### Topógrafo
- **Dominio:** Inspección métrica del terreno auditado (`../`).
- **Acción:** Ejecuta el barrido instrumental aplicando exclusiones nativas del entorno y guardas autónomas contra enlaces circulares (poda por inodo) y recursión profunda (máximo 15 niveles). Puebla la tabla `manifiesto` y redacta `expedicion/readme/LEVANTAMIENTO.md` sin adjetivos ni juicios de intención.

### Geólogo
- **Dominio:** Síntesis técnica de entrada y arquitectura observable.
- **Acción:** Lee `LEVANTAMIENTO.md`, la tabla `manifiesto` y los archivos de configuración (`package.json`, `pyproject.toml`, etc.) en `../`. Valida licencias y versiones mediante búsqueda web determinista y redacta `expedicion/readme/README.md` delimitando ausencias técnicas comprobables. En ciclo 1 siembra `expedicion/readme/MAPA.md`.

### Guía
- **Dominio:** Interfaz de diálogo operativo con el interlocutor.
- **Acción:** Procesa intercambios verbales, extrae posturas sin psicologizar y redacta notas canónicas en `expedicion/notas_[participante]/[dominio].md`. Registra deltas de posición en `expedicion/cambios/`. Sincroniza `puntas`, `anclas` y `afirmaciones` (extrayendo contexto operativo), ejecuta ruptura de ciclo y cierra turnos formulando una única pregunta técnica de calibración.

### Cartógrafo
- **Dominio:** Compilación de la base de conocimiento y aceleración de consultas.
- **Acción:** Sincroniza las notas Markdown modificadas con las tablas `nodos`, `afirmaciones`, `bordes` y `anclas` en `expedicion.db` indexando por ruta relativa unívoca normalizada con `/`. Compila los archivos independientes en `expedicion/conocimiento/[nodo].md` y actualiza el índice humano en `expedicion/readme/MAPA.md`. Proyecta subgrafos dinámicos en memoria consultando la densidad relacional en SQLite sin abrir múltiples archivos en disco.

### Aeróstato
- **Dominio:** Cruce multi-repositorio y arbitraje adversarial.
- **Acción:** Cruza directorios `expedicion/conocimiento_*` indexando por ruta relativa para evitar colisiones. Clasifica variaciones contextuales en tablas compactas y bifurca tensiones estructurales en nodos planos independientes (`[dominio].[tema]--[variante].md`), limitando el particionado a un máximo de 3 ramas antes de congelar el nodo y abrir alerta `desafio`. Compila `expedicion/conocimiento_unificado/` e implementa la frase canónica de punto de control ante purgas o sobreescrituras.

---

## 4. Flujo Operativo

```text
Terreno (../) ──► [ TOPÓGRAFO ] ──► LEVANTAMIENTO.md + manifiesto (SQLite)
                         │
                         ▼
                  [ GEÓLOGO ]   ──► README.md + semilla MAPA.md
                         │
                         ▼
Operador      ──► [ GUÍA ]      ──► notas_*/[dominio].md + tabla puntas
                         │
                         ▼
notas/*.md    ──► [ CARTÓGRAFO ] ──► conocimiento/*.md + MAPA.md + subgrafos
                         │
                         ▼
conocimiento_N ─► [ AERÓSTATO ]  ──► conocimiento_unificado/ (Arbitraje adversarial)
```

1. **Barrido Métrico:** Se inicializa `schema.sql` y se activa al **Topógrafo** para indexar archivos útiles podando estructuras volátiles y ciclos.
2. **Generación del Piso:** El **Geólogo** analiza las dependencias reales y redacta la documentación de entrada verificada.
3. **Captura de Notas:** El **Guía** destraba incógnitas con el operador, persiste notas canónicas y sincroniza contexto y anomalías en `puntas` y `afirmaciones`.
4. **Indexación y Compilación:** El **Cartógrafo** reconcilia mtimes, actualiza el grafo relacional en SQLite y compila nodos y mapa en disco.
5. **Unificación y Arbitraje:** El **Aeróstato** cruza repositorios heterogéneos, aísla contradicciones en nodos hermanos y emite puntos de control formales ante acciones irreversibles o compensables de alto impacto.

---

## 5. Escala de Evidencia

Toda afirmación atómica registrada en la tabla `afirmaciones` y en los frontmatters de los nodos debe tipificarse obligatoriamente bajo uno de los siguientes cinco niveles:

1. `logica_formal`: Deducción matemática o analítica pura, independiente del entorno temporal.
2. `empirico`: Medición directa y reproducible; verificación en fuente oficial o primaria competente; o cruce de al menos 2 vectores independientes con métricas contrapuestas. Exige hash presente en `hash_recibo`.
3. `experiencia_documentada`: Precedentes verificables sobre situaciones análogas: bitácoras de fallo, lecciones aprendidas, fe de erratas, registros de incidentes históricos o memorias operativas.
4. `deduccion_fuerte`: Inferencia causal derivada directamente de datos empíricos o hechos ya contrastados en niveles superiores.
5. `memoria_interna`: Inferencia generativa sin recibo instrumental o emitida ante caída de red y herramientas (`hash_recibo = NULL`, no verificado, techo de confianza en Nivel 5).

---

## 6. Mantenimiento y Reconstrucción

- **Sincronización por mtime / hash:** Si un archivo Markdown en `notas/` o `conocimiento/` se edita a mano, los agentes comparan la estampa temporal o el hash MD contra SQLite y actualizan la base de datos sin requerir migraciones complejas.
- **Reconstrucción desde Cero:** Si `expedicion.db` se corrompe o borra:
  1. Ejecutar: `sqlite3 expedicion/expedicion.db < expedicion/schema.sql`.
  2. Ejecutar al **Topógrafo** sobre `../` y al **Cartógrafo** sobre `expedicion/notas_*/`.
  3. La caché relacional queda totalmente repoblada preservando la integridad de las notas y mapas originales.