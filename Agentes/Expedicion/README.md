# Framework Expedición — Manual de Arquitectura, Flujo y Mecánica Operativa

Documento maestro para la inspección, estructuración, aceleración relacional y unificación de conocimiento técnico sobre cualquier proyecto o corpus analizado.

---

## 1. Principio Fundamental: Markdown como Verdad, SQLite como Acelerador

El sistema resuelve la tensión entre legibilidad humana y consumo de tokens bajo una regla de desacoplamiento estricto:

- **La Fuente Canónica de Verdad (`Source of Truth`):** El sistema de archivos local (`.md`). Toda nota, análisis, mapa o nodo redactado es editable a mano con cualquier editor de texto plano, inspeccionable con utilidades del sistema (`grep`, `cat`), y versionable directamente en Git.
- **El Índice y Caché Efímera (`expedicion.db`):** SQLite no es el dueño de la información. Opera como un motor relacional descartable que indexa hashes, dependencias, proposiciones atómicas y grados de conexión. Su único propósito es que los agentes realicen agregaciones, cruces matriciales y proyecciones de subgrafos en milisegundos sin verse obligados a devorar ventana de contexto abriendo decenas de archivos Markdown completos. Si `expedicion.db` se corrompe o se borra (`rm expedicion.db`), el repositorio no pierde información: se regenera a partir de los archivos `.md` en disco.
- **El Operador en el Centro:** La entidad con autoridad (el usuario) valida o edita en Markdown y toma las decisiones arquitectónicas. Los agentes no asumen autoridad técnica ni ejecutan promociones destructivas sin confirmación formal `[GO]`.

---

## 2. Topografía Completa del Espacio de Trabajo

La suite delimita su accionar a la carpeta `expedicion/`, tratando la raíz del proyecto auditado (`../`) como un terreno de solo lectura:

```text
raiz_del_proyecto/              # El terreno físico auditado (../)
│
└── expedicion/                 # Perímetro operativo positivo
    ├── expedicion.db           # Caché relacional e índice SQLite
    ├── schema.sql              # Esquema SQL canónico del acelerador
    │
    ├── readme/                 # Capa de documentación técnica pública
    │   ├── LEVANTAMIENTO.md    # Inventario métrico físico (generado por Topógrafo)
    │   ├── README.md           # Explicación técnica de entrada (generado por Geólogo)
    │   └── MAPA.md             # Índice y mapa de dominios (compilado por Cartógrafo)
    │
    ├── notas_[participante]/   # Notas estructuradas de campo (generadas por Guía)
    │   └── [dominio].md
    │
    ├── cambios/                # Historial de cambios y mutaciones de posición (Guía)
    │   └── [timestamp]_[dominio].md
    │
    ├── conocimiento/           # Nodos de conocimiento consolidados (Cartógrafo)
    │   └── [nodo].md
    │
    └── conocimiento_unificado/ # Unificación de N repositorios y arbitraje (Aeróstato)
        ├── [nodo].md
        └── conocimiento_unificado.MAPA.md
```

---

## 3. Catálogo Operativo de Agentes

Cada agente ejecuta una función acotada y canónica dentro del ciclo de vida del repositorio:

### Topógrafo
- **Propósito:** Ejecuta el barrido físico e instrumental del terreno sin emitir juicios de valor ni interpretaciones.
- **Entrada:** Inspección directa del sistema de archivos en `../`.
- **Salida:** Poblado de la tabla `manifiesto` en SQLite y redacción de `expedicion/readme/LEVANTAMIENTO.md`.

### Geólogo
- **Propósito:** Sintetiza el propósito, arquitectura observable, dependencias y ausencias técnicas del terreno para que cualquier persona entienda el proyecto.
- **Entrada:** `expedicion/readme/LEVANTAMIENTO.md`, metadatos en tabla `manifiesto` y artefactos de configuración (`package.json`, `pyproject.toml`, etc.).
- **Salida:** Redacción de `expedicion/readme/README.md` y siembra inicial de `expedicion/readme/MAPA.md` (únicamente en ciclo 1).

### Guía
- **Propósito:** Conduce el diálogo operativo con el interlocutor, detectando tensiones, alertas técnicas y extrayendo notas estructuradas sin psicologizar.
- **Entrada:** Diálogo con el operador, lecturas de `README.md`/`LEVANTAMIENTO.md` y consulta rápida de alertas abiertas en tabla `puntas`.
- **Salida:** Notas de campo en `expedicion/notas_[participante]/[dominio].md`, mutaciones en `expedicion/cambios/` y actualización de tabla `puntas`.

### Cartógrafo
- **Propósito:** Compila las notas en nodos de conocimiento interconectados, detecta densidad relacional y proyecta subgrafos dinámicos bajo demanda sin abrir archivos ajenos.
- **Entrada:** Notas en `expedicion/notas_[participante]/` y tablas relacionales.
- **Salida:** Nodos individuales en `expedicion/conocimiento/[nodo].md`, índice en `expedicion/readme/MAPA.md` y proyecciones de subgrafo en terminal.

### Aeróstato
- **Propósito:** Cruza N carpetas de conocimiento heterogéneas (`conocimiento_equipoA/`, `conocimiento_equipoB/`), unifica convergencias y formula el contraargumento adversarial más destructivo ante contradicciones técnicas.
- **Entrada:** Repositorios de conocimiento múltiples y tablas temporales SQLite.
- **Salida:** Archivos en `expedicion/conocimiento_unificado/[nodo].md`, mapa de tensiones en `conocimiento_unificado.MAPA.md` y alertas de conflicto.

---

## 4. Desglose Exhaustivo del Motor SQLite (`schema.sql`)

El motor de base de datos se rige por pragmas de concurrencia y un conjunto de tablas diseñadas para desacoplar el cálculo del almacenamiento textual masivo:

```sql
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
```
*Justificación técnica:* `journal_mode = WAL` (Write-Ahead Logging) permite lecturas concurrentes sin bloqueo mientras un agente escribe métricas o notas, previniendo errores de `database is locked`.

### A. Tabla `manifiesto` (Inventario del Terreno)
Poblada por el **Topógrafo** y consultada por el **Geólogo**. Evita que el sistema recorra el disco repetidamente.
```sql
CREATE TABLE IF NOT EXISTS manifiesto (
    ruta_relativa TEXT PRIMARY KEY,
    categoria TEXT NOT NULL,         -- 'codigo', 'metadato', 'documentacion', 'activo', 'binario'
    tamano INTEGER NOT NULL,
    mtime REAL NOT NULL,
    hash_contenido TEXT,
    anomalia TEXT DEFAULT NULL,      -- 'bloqueado', 'roto', 'ilegible'
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_manifiesto_cat ON manifiesto(categoria);
```
- `mtime` y `hash_contenido`: Permiten detectar si un archivo del proyecto mutó desde el último corte sin abrir su contenido.
- `categoria`: Permite al Geólogo hacer agregaciones instantáneas (`SELECT categoria, COUNT(*), SUM(tamano) FROM manifiesto GROUP BY categoria;`) para dimensionar el proyecto en 1 milisegundo.

### B. Tabla `nodos` (Índice de Archivos de Conocimiento)
Administrada por el **Cartógrafo**. Contiene únicamente metadatos y un resumen breve, manteniendo el cuerpo íntegro en disco (`.md`).
```sql
CREATE TABLE IF NOT EXISTS nodos (
    id TEXT PRIMARY KEY,             -- Identificador slug del nodo
    dominio TEXT NOT NULL,
    archivo_path TEXT NOT NULL,      -- Puntero exacto al archivo .md en disco
    mtime REAL NOT NULL,             -- Fecha de modificación del .md
    hash_md TEXT NOT NULL,           -- Hash para reconciliación automática de cambios manuales
    resumen TEXT,                    -- Extracto breve para contextualización sin tokens extra
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_nodos_dominio ON nodos(dominio);
```
- **Reconciliación de Arranque:** Cuando el Cartógrafo arranca, corre:
  `SELECT archivo_path, hash_md, mtime FROM nodos;`
  Si el `mtime` del archivo en disco es superior al de la tabla, significa que un humano editó el `.md` a mano; el agente procesa solo ese archivo modificado y sincroniza la tabla.

### C. Tabla `afirmaciones` (Desglose Atómico Epistémico)
Permite auditar la solidez lógica de lo asentado en los nodos sin leer el texto completo.
```sql
CREATE TABLE IF NOT EXISTS afirmaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nodo_id TEXT NOT NULL,
    proposicion TEXT NOT NULL,
    respaldo TEXT NOT NULL,          -- 'empirico', 'deduccion', 'no verificado'
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE CASCADE
);
```
- Permite detectar afirmaciones sin sustento o contrastar contradicciones lógicas entre dos nodos distintos mediante consultas directas.

### D. Tabla `bordes` (Grafo de Conexiones Dirigidas)
Registra la topología relacional entre conceptos para proyecciones de subgrafos.
```sql
CREATE TABLE IF NOT EXISTS bordes (
    origen_id TEXT NOT NULL,
    destino_id TEXT NOT NULL,
    tipo_relacion TEXT DEFAULT 'conecta',
    PRIMARY KEY (origen_id, destino_id),
    FOREIGN KEY (origen_id) REFERENCES nodos(id) ON DELETE CASCADE,
    FOREIGN KEY (destino_id) REFERENCES nodos(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_bordes_origen ON bordes(origen_id);
```

### E. Vista `v_densidad_nodos` (Cálculo Dinámico de Radio)
Calcula en tiempo real la conectividad de cada nodo sin procesar código externo:
```sql
CREATE VIEW IF NOT EXISTS v_densidad_nodos AS
SELECT 
    n.id AS nodo_id,
    COUNT(b.destino_id) AS total_bordes
FROM nodos n
LEFT JOIN bordes b ON n.id = b.origen_id
GROUP BY n.id;
```
- **Lógica de Radio Dinámico del Cartógrafo:**
  Al solicitar la proyección de un nodo:
  `SELECT total_bordes FROM v_densidad_nodos WHERE nodo_id = 'auth_jwt';`
  - Si `total_bordes > 5`: El nodo es de alta densidad (hub crítico); el Cartógrafo fija **Radio = 1** para evitar una explosión combinatoria de contexto.
  - Si `total_bordes <= 5`: El nodo es periférico o específico; se fija **Radio = 2 o 3** para traer el contexto circundante necesario.

### F. Consulta Recursiva de Subgrafo (Proyección sin Lectura de Disco)
Una vez determinado el radio $N$, el agente ejecuta un Common Table Expression (CTE) recursivo directamente en SQLite:
```sql
WITH RECURSIVE subgrafo(id, nivel) AS (
    SELECT 'nodo_raiz', 0
    UNION
    SELECT b.destino_id, s.nivel + 1 
    FROM bordes b 
    JOIN subgrafo s ON b.origen_id = s.id 
    WHERE s.nivel < 2  -- Radio dinámico fijado
)
SELECT DISTINCT n.id, n.dominio, n.archivo_path, n.resumen 
FROM nodos n 
JOIN subgrafo s ON n.id = s.id;
```
*Resultado:* El agente obtiene la estructura, dependencias y resúmenes exactos del tema consultado en un solo turno, consumiendo una fracción mínima de tokens y sin tocar los archivos `.md` del disco.

### G. Tabla `puntas` (Incógnitas, Alertas y Fricciones)
Utilizada principalmente por el **Guía** y el **Aeróstato**.
```sql
CREATE TABLE IF NOT EXISTS puntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origen_archivo TEXT NOT NULL,
    borde TEXT NOT NULL,             -- Descripción técnica de la alerta o disenso
    impacto TEXT NOT NULL,           -- 'alto', 'medio', 'bajo'
    nivel TEXT NOT NULL,             -- 'sondeo', 'alerta', 'desafio'
    estado TEXT DEFAULT 'abierta',   -- 'abierta', 'explorada', 'bloqueada', 'resuelta'
    resolucion TEXT DEFAULT NULL,
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_puntas_estado ON puntas(estado, impacto);
```
- **Vista `v_conflictos_abiertos`:**
```sql
CREATE VIEW IF NOT EXISTS v_conflictos_abiertos AS
SELECT id, origen_archivo, borde, impacto 
FROM puntas 
WHERE estado = 'abierta' AND impacto = 'alto';
```
Permite al Guía arrancar el diálogo técnico priorizando exactamente las tensiones de alto impacto sin tener que preguntar "¿por dónde empezamos?".

### H. Tabla `anclas` (Registro de Verificación Externa)
Garantiza el cumplimiento del protocolo determinista de búsqueda web.
```sql
CREATE TABLE IF NOT EXISTS anclas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    termino TEXT NOT NULL,
    dominio TEXT NOT NULL,
    url TEXT,
    verificado INTEGER DEFAULT 0,    -- 1 = contrastado externamente, 0 = no verificado
    nodo_id TEXT,
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE SET NULL
);
```

### I. Tabla `bitacora_sesiones` (Trazabilidad)
```sql
CREATE TABLE IF NOT EXISTS bitacora_sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agente TEXT NOT NULL,
    evento TEXT NOT NULL,            -- 'INICIO', 'CIERRE', 'CHECKPOINT'
    corte_id TEXT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
);
```

---

## 5. El Flujo de Trabajo Operativo de Principio a Fin

```text
======================================================================
CAPA 1: INSPECCIÓN FÍSICA Y ARQUITECTURA (Sin interacción humana)
======================================================================
Terreno (../) ──► [ TOPÓGRAFO ] ──► LEVANTAMIENTO.md + tabla manifiesto
                         │
                         ▼
                  [ GEÓLOGO ]   ──► README.md + semilla MAPA.md

======================================================================
CAPA 2: EXTRACCIÓN Y DIÁLOGO TÉCNICO (Interacción directa con el operador)
======================================================================
Operador      ──► [ GUÍA ]      ──► notas_[participante]/*.md + tabla puntas

======================================================================
CAPA 3: ESTRUCTURACIÓN Y CRUCE RELACIONAL (Aceleración relacional)
======================================================================
notas/*.md    ──► [ CARTÓGRAFO ] ──► conocimiento/*.md + MAPA.md
                                 └─► Proyección de Subgrafos (bajo demanda)

conocimiento_N ─► [ AERÓSTATO ]  ──► conocimiento_unificado/*.md
                                 └─► MAPA unificado (Arbitraje adversarial)
```

### Paso 1: Inicialización e Inspección Física
1. Se genera la base de datos vacía ejecutando el esquema:
   ```bash
   sqlite3 expedicion/expedicion.db < expedicion/schema.sql
   ```
2. Se invoca al **Topógrafo**:
   - Barre la raíz del terreno (`../`).
   - Inserta los metadatos en la tabla `manifiesto`.
   - Emite el archivo humano `expedicion/readme/LEVANTAMIENTO.md` con los totales métricos, extensiones y anomalías de acceso detectadas.

### Paso 2: Creación del Piso de Entrada
1. Se invoca al **Geólogo** (Pipeline Piso):
   - Lee `LEVANTAMIENTO.md` y consulta la tabla `manifiesto` para analizar los archivos categorizados como metadatos (`package.json`, `Cargo.toml`, `.env.example`, etc.).
   - Ejecuta búsqueda web para validar versiones y estándares si es necesario.
   - Redacta `expedicion/readme/README.md` explicando el propósito técnico, arquitectura física, flujo de datos y ausencias observables.
   - Siembra la primera versión de `expedicion/readme/MAPA.md` con los dominios base detectados.

### Paso 3: Sesiones de Trabajo y Extracción de Notas
1. Se invoca al **Guía** para trabajar sobre un problema o diseño técnico específico:
   - El agente ejecuta:
     `SELECT borde, impacto FROM puntas WHERE estado = 'abierta' ORDER BY impacto DESC LIMIT 3;`
     Inicia el diálogo con los temas críticos identificados.
   - Intercambia planteamientos técnicos con el operador. Si el operador propone algo que choca con mediciones previas, el Guía marca la discrepancia objetiva.
   - Al cerrar el intercambio, redacta la nota de campo estructurada en `expedicion/notas_[operador]/[dominio].md` bajo el esquema canónico (origen, posiciones analizadas, afirmaciones, tecnologías y puntas abiertas).
   - Persiste las nuevas incógnitas en la tabla `puntas` de SQLite.

### Paso 4: Compilación del Grafo e Índices
1. Se invoca al **Cartógrafo** (Pipeline Compilación):
   - Revisa qué notas cambiaron en disco comparando hashes contra la tabla `nodos`.
   - Procesa los archivos `.md`, extrayendo afirmaciones y relaciones hacia `bordes` y `anclas`.
   - Escribe los nodos consolidados en `expedicion/conocimiento/[nodo].md`.
   - Reescribe `expedicion/readme/MAPA.md` agregando los dominios actualizados directamente desde SQLite.

### Paso 5: Consultas Rápidas de Subgrafo (Ahorro Máximo de Tokens)
1. Durante cualquier punto del desarrollo, se solicita al **Cartógrafo** proyectar un concepto (ej. `proyecta auth_core`):
   - Consulta `v_densidad_nodos` para fijar el radio de búsqueda (1, 2 o 3).
   - Ejecuta la consulta recursiva CTE sobre la tabla `bordes`.
   - Emite en la respuesta exactamente el subgrafo de dependencias, títulos y resúmenes sin leer ni abrir ningún archivo `.md` de la carpeta `conocimiento/`.

### Paso 6: Cruce de Múltiples Fuentes y Arbitraje
1. Si existen repositorios de notas de múltiples equipos (`conocimiento_frontend/`, `conocimiento_backend/`), se invoca al **Aeróstato**:
   - Ingesta encabezados a tablas temporales en SQLite.
   - Identifica coincidencias y desacuerdos relacionales.
   - Donde hay coincidencia, compila nodos consolidados en `expedicion/conocimiento_unificado/[nodo].md`.
   - Donde hay desacuerdo irreconciliable, no fuerza un consenso: crea ambos nodos enlazados recíprocamente y redacta un nodo de contraste con el contraargumento técnico más destructivo contra ambas posturas respaldado por búsqueda externa.
   - Genera `expedicion/conocimiento_unificado.MAPA.md` documentando las tensiones activas.

---

## 6. Procedimientos de Mantenimiento y Recuperación

### Edición Humana Libre
Un humano puede abrir cualquier archivo `.md` dentro de `notas/` o `conocimiento/` y modificarlo directamente. No se requiere correr comandos especiales ni actualizar SQL a mano. En la siguiente sesión, el agente detecta la disparidad en el campo `mtime` / `hash_md` y sincroniza las tablas de inmediato.

### Reconstrucción de Desastre (Caché Corrupta o Eliminada)
Si el archivo `expedicion.db` se destruye, la reconstrucción toma dos pasos:
1. Re-inicializar el esquema:
   ```bash
   sqlite3 expedicion/expedicion.db < expedicion/schema.sql
   ```
2. Ejecutar al **Topógrafo** en barrido físico y al **Cartógrafo** en compilación general. Ambos agentes leerán los `.md` existentes en disco y re-poblarán la totalidad de las tablas relacionales (`manifiesto`, `nodos`, `afirmaciones`, `bordes`, `puntas` y `anclas`) dejando el acelerador 100% operativo sin pérdida de información histórica.