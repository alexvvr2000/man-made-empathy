-- ============================================================================
-- ARCHIVO: expedicion/schema.sql
-- ESQUEMA: expedicion.db (Caché Relacional e Índice de Aceleración)
-- Rol: Estructura derivada de los archivos Markdown (.md). 
-- Si este archivo se destruye, se reconstruye parseando el sistema de archivos.
-- ============================================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- 1. Manifiesto del terreno auditado (Topógrafo y Geólogo)
CREATE TABLE IF NOT EXISTS manifiesto (
    ruta_relativa TEXT PRIMARY KEY,
    categoria TEXT NOT NULL CHECK(categoria IN ('codigo', 'metadato', 'documentacion', 'activo', 'binario')),
    tamano INTEGER NOT NULL,
    mtime REAL NOT NULL,
    hash_contenido TEXT,
    anomalia TEXT DEFAULT NULL,
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- 2. Índice de Nodos de Conocimiento (Cartógrafo y Aeróstato)
CREATE TABLE IF NOT EXISTS nodos (
    id TEXT PRIMARY KEY,             -- Ruta relativa unívoca normalizada con / (ej. 'conocimiento/nodo.md')
    dominio TEXT NOT NULL,
    archivo_path TEXT NOT NULL,      -- Ruta exacta al archivo .md en disco (fuente de verdad)
    mtime REAL NOT NULL,
    hash_md TEXT NOT NULL,
    resumen TEXT,
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- 3. Proposiciones atómicas alineadas con la Escala de Evidencia (Guía, Cartógrafo, Aeróstato)
CREATE TABLE IF NOT EXISTS afirmaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nodo_id TEXT NOT NULL,
    proposicion TEXT NOT NULL,
    respaldo TEXT NOT NULL CHECK(respaldo IN (
        'logica_formal',
        'empirico',
        'experiencia_documentada',
        'deduccion_fuerte',
        'memoria_interna'
    )),
    origen_contexto TEXT,            -- Contexto operativo extraído de la nota de campo o fuente
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE CASCADE
);

-- 4. Grafo de relaciones para proyecciones dinámicas (Cartógrafo y Aeróstato)
CREATE TABLE IF NOT EXISTS bordes (
    origen_id TEXT NOT NULL,
    destino_id TEXT NOT NULL,
    tipo_relacion TEXT DEFAULT 'conecta', -- 'conecta', 'diverge_en', etc.
    PRIMARY KEY (origen_id, destino_id),
    FOREIGN KEY (origen_id) REFERENCES nodos(id) ON DELETE CASCADE,
    FOREIGN KEY (destino_id) REFERENCES nodos(id) ON DELETE CASCADE
);

-- 5. Puntas abiertas, alertas y protocolo de escala de riesgo (Guía y Aeróstato)
CREATE TABLE IF NOT EXISTS puntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origen_archivo TEXT NOT NULL,
    borde TEXT NOT NULL,
    impacto TEXT NOT NULL CHECK(impacto IN ('alto', 'medio', 'bajo')),
    nivel TEXT NOT NULL CHECK(nivel IN ('sondeo', 'alerta', 'desafio', 'emergencia')),
    estado TEXT DEFAULT 'abierta' CHECK(estado IN ('abierta', 'explorada', 'bloqueada', 'resuelta')),
    desgaste_temporal TEXT DEFAULT NULL,
    resolucion TEXT DEFAULT NULL,
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- 6. Anclas técnicas y verificación externa con recibo (Protocolo de Búsqueda)
CREATE TABLE IF NOT EXISTS anclas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    termino TEXT NOT NULL,
    dominio TEXT NOT NULL,
    url TEXT,
    verificado INTEGER DEFAULT 0 CHECK(verificado IN (0, 1)),
    hash_recibo TEXT DEFAULT NULL,    -- Hash SHA-256 de la salida cruda o NULL si falla/no verificada
    nodo_id TEXT,
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE SET NULL
);

-- 7. Bitácora de sesiones y checkpoints de impacto irreversible
CREATE TABLE IF NOT EXISTS bitacora_sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agente TEXT NOT NULL,
    evento TEXT NOT NULL CHECK(evento IN ('INICIO', 'CIERRE', 'CHECKPOINT', 'BLOQUEO')),
    corte_id TEXT,
    reversibilidad TEXT DEFAULT NULL CHECK(reversibilidad IN ('reversible', 'compensable', 'irreversible', NULL)),
    hash_recibo TEXT DEFAULT NULL,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- VISTAS OPERACIONALES
-- ============================================================================

-- Vista: Densidad relacional para calcular el radio de proyección (Cartógrafo)
CREATE VIEW IF NOT EXISTS v_densidad_nodos AS
SELECT 
    n.id AS nodo_id,
    COUNT(b.destino_id) AS total_bordes
FROM nodos n
LEFT JOIN bordes b ON n.id = b.origen_id
GROUP BY n.id;

-- Vista: Conflictos y tensiones de alto riesgo activos (Aeróstato y Guía)
CREATE VIEW IF NOT EXISTS v_conflictos_abiertos AS
SELECT 
    p.id AS punta_id,
    p.origen_archivo,
    p.borde,
    p.nivel,
    p.impacto,
    p.desgaste_temporal
FROM puntas p
WHERE p.estado = 'abierta' AND (p.impacto = 'alto' OR p.nivel IN ('desafio', 'emergencia'));

-- Índices de aceleración
CREATE INDEX IF NOT EXISTS idx_nodos_dominio ON nodos(dominio);
CREATE INDEX IF NOT EXISTS idx_bordes_origen ON bordes(origen_id);
CREATE INDEX IF NOT EXISTS idx_puntas_estado ON puntas(estado, impacto, nivel);
CREATE INDEX IF NOT EXISTS idx_manifiesto_cat ON manifiesto(categoria);
CREATE INDEX IF NOT EXISTS idx_afirmaciones_respaldo ON afirmaciones(respaldo);
CREATE INDEX IF NOT EXISTS idx_afirmaciones_nodo ON afirmaciones(nodo_id);