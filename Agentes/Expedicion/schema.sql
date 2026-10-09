-- ============================================================================
-- ESQUEMA: expedicion.db (Caché Relacional e Índice de Aceleración)
-- Rol: Estructura derivada de los archivos Markdown (.md). 
-- Si este archivo se destruye, se reconstruye parseando el sistema de archivos.
-- ============================================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- 1. Manifiesto del terreno auditado (Topógrafo y Geólogo)
CREATE TABLE IF NOT EXISTS manifiesto (
    ruta_relativa TEXT PRIMARY KEY,
    categoria TEXT NOT NULL,         -- 'codigo', 'metadato', 'documentacion', 'activo', 'binario'
    tamano INTEGER NOT NULL,
    mtime REAL NOT NULL,
    hash_contenido TEXT,
    anomalia TEXT DEFAULT NULL,      -- 'bloqueado', 'roto', etc.
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- 2. Índice de Nodos de Conocimiento (Cartógrafo y Aeróstato)
CREATE TABLE IF NOT EXISTS nodos (
    id TEXT PRIMARY KEY,             -- Coincide con el nombre del archivo .md o slug
    dominio TEXT NOT NULL,
    archivo_path TEXT NOT NULL,      -- Ruta exacta al archivo .md (fuente de verdad)
    mtime REAL NOT NULL,             -- Control de cambios manuales en disco
    hash_md TEXT NOT NULL,           -- Hash para reconciliación en arranque
    resumen TEXT,                    -- Extracto breve para no abrir el .md
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- 3. Proposiciones atómicas para contrastes (Guía, Cartógrafo y Aeróstato)
CREATE TABLE IF NOT EXISTS afirmaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nodo_id TEXT NOT NULL,
    proposicion TEXT NOT NULL,
    respaldo TEXT NOT NULL,          -- 'empirico', 'deduccion', 'no verificado'
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE CASCADE
);

-- 4. Grafo de relaciones para proyecciones dinámicas (Cartógrafo)
CREATE TABLE IF NOT EXISTS bordes (
    origen_id TEXT NOT NULL,
    destino_id TEXT NOT NULL,
    tipo_relacion TEXT DEFAULT 'conecta',
    PRIMARY KEY (origen_id, destino_id),
    FOREIGN KEY (origen_id) REFERENCES nodos(id) ON DELETE CASCADE,
    FOREIGN KEY (destino_id) REFERENCES nodos(id) ON DELETE CASCADE
);

-- 5. Puntas abiertas, alertas y bifurcaciones técnicas (Guía)
CREATE TABLE IF NOT EXISTS puntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origen_archivo TEXT NOT NULL,    -- Nota .md donde se detectó
    borde TEXT NOT NULL,             -- Descripción de la incógnita o tensión
    impacto TEXT NOT NULL,           -- 'alto', 'medio', 'bajo'
    nivel TEXT NOT NULL,             -- 'sondeo', 'alerta', 'desafio'
    estado TEXT DEFAULT 'abierta',   -- 'abierta', 'explorada', 'bloqueada', 'resuelta'
    resolucion TEXT DEFAULT NULL,
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- 6. Anclas técnicas y verificación externa (Protocolo de Búsqueda)
CREATE TABLE IF NOT EXISTS anclas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    termino TEXT NOT NULL,
    dominio TEXT NOT NULL,
    url TEXT,
    verificado INTEGER DEFAULT 0,    -- 1 = contrastado externamente, 0 = no verificado
    nodo_id TEXT,
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE SET NULL
);

-- 7. Bitácora de sesiones y cortes
CREATE TABLE IF NOT EXISTS bitacora_sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agente TEXT NOT NULL,
    evento TEXT NOT NULL,            -- 'INICIO', 'CIERRE', 'CHECKPOINT'
    corte_id TEXT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- VISTAS OPERACIONALES (Consultas económicas para el agente)
-- ============================================================================

-- Vista: Densidad relacional para calcular el radio de proyección (Cartógrafo)
CREATE VIEW IF NOT EXISTS v_densidad_nodos AS
SELECT 
    n.id AS nodo_id,
    COUNT(b.destino_id) AS total_bordes
FROM nodos n
LEFT JOIN bordes b ON n.id = b.origen_id
GROUP BY n.id;

-- Vista: Conflictos abiertos activos entre afirmaciones incompatibles (Aeróstato)
CREATE VIEW IF NOT EXISTS v_conflictos_abiertos AS
SELECT 
    p.id AS punta_id,
    p.origen_archivo,
    p.borde,
    p.impacto
FROM puntas p
WHERE p.estado = 'abierta' AND p.impacto = 'alto';

-- Índices de aceleración
CREATE INDEX IF NOT EXISTS idx_nodos_dominio ON nodos(dominio);
CREATE INDEX IF NOT EXISTS idx_bordes_origen ON bordes(origen_id);
CREATE INDEX IF NOT EXISTS idx_puntas_estado ON puntas(estado, impacto);
CREATE INDEX IF NOT EXISTS idx_manifiesto_cat ON manifiesto(categoria);