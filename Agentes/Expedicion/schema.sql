PRAGMA foreign_keys = ON;

-- 1. Manifiesto físico y estado de cambios (Topógrafo y Geólogo)
-- Rutas normalizadas siempre con separador '/'
CREATE TABLE IF NOT EXISTS manifiesto (
    ruta TEXT PRIMARY KEY,
    tamano INTEGER NOT NULL,
    mtime TEXT NOT NULL,
    hash TEXT NOT NULL,
    categoria TEXT CHECK(categoria IN ('sustantivo', 'metadato', 'estructura', 'ruido')) NOT NULL,
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bitácora transaccional (Todos los agentes)
CREATE TABLE IF NOT EXISTS bitacora_sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    ronda INTEGER NOT NULL,
    agente TEXT CHECK(agente IN ('Topógrafo', 'Geólogo', 'Guía', 'Cartógrafo', 'Aeróstato')) NOT NULL,
    tipo_evento TEXT CHECK(tipo_evento IN ('INICIO', 'CIERRE')) NOT NULL,
    corte TEXT NOT NULL,
    rostro TEXT,
    escrituras TEXT,
    resultado TEXT,
    detalles TEXT
);

-- 3. Nodos de conocimiento (Cartógrafo y Aeróstato)
CREATE TABLE IF NOT EXISTS nodos (
    id TEXT PRIMARY KEY,
    dominio TEXT NOT NULL,
    posicion_tipo TEXT CHECK(posicion_tipo IN ('humana', 'Piso', 'Medición', 'IA', 'externa')) NOT NULL,
    posicion_origen TEXT NOT NULL,
    version INTEGER NOT NULL DEFAULT 1,
    linaje_ancestro TEXT,
    linaje_operacion CHECK(linaje_operacion IN ('evolución', 'contraposición', 'caducidad')),
    cuerpo TEXT NOT NULL,
    mtime TEXT NOT NULL,
    hash TEXT NOT NULL
);

-- 4. Afirmaciones atómicas
CREATE TABLE IF NOT EXISTS afirmaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nodo_id TEXT NOT NULL,
    afirmacion TEXT NOT NULL,
    fuente TEXT NOT NULL,
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE CASCADE
);

-- 5. Grafo de bordes salientes
CREATE TABLE IF NOT EXISTS bordes (
    origen_id TEXT NOT NULL,
    destino_id TEXT NOT NULL,
    PRIMARY KEY (origen_id, destino_id),
    FOREIGN KEY (origen_id) REFERENCES nodos(id) ON DELETE CASCADE,
    FOREIGN KEY (destino_id) REFERENCES nodos(id) ON DELETE CASCADE
);

-- 6. Puntas descubiertas (Guía, Cartógrafo, Aeróstato)
CREATE TABLE IF NOT EXISTS puntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nodo_id TEXT,
    borde TEXT NOT NULL,
    desde_posicion TEXT NOT NULL,
    impacto TEXT CHECK(impacto IN ('alto', 'medio', 'bajo')) NOT NULL,
    nivel TEXT CHECK(nivel IN ('sondeo', 'alerta', 'desafío')) NOT NULL,
    estado TEXT CHECK(estado IN ('abierta', 'explorada', 'bloqueada', 'aceptada', 'rechazada')) DEFAULT 'abierta',
    respuesta TEXT DEFAULT 'no aplica',
    actualizado_en TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE SET NULL
);

-- 7. Anclas técnicas y normativas externas
CREATE TABLE IF NOT EXISTS anclas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nodo_id TEXT NOT NULL,
    tecnologia TEXT NOT NULL,
    dominio TEXT NOT NULL,
    url TEXT NOT NULL,
    verificada INTEGER CHECK(verificada IN (0, 1)) DEFAULT 1,
    FOREIGN KEY (nodo_id) REFERENCES nodos(id) ON DELETE CASCADE
);

-- Vistas analíticas de aceleración
CREATE VIEW IF NOT EXISTS v_densidad_nodos AS
SELECT 
    n.id AS nodo_id,
    n.dominio,
    COUNT(b.destino_id) AS total_bordes
FROM nodos n
LEFT JOIN bordes b ON n.id = b.origen_id
GROUP BY n.id;

CREATE VIEW IF NOT EXISTS v_conflictos_abiertos AS
SELECT 
    b1.origen_id AS nodo_a, 
    b1.destino_id AS nodo_b, 
    n1.dominio
FROM bordes b1
JOIN bordes b2 ON b1.origen_id = b2.destino_id AND b1.destino_id = b2.origen_id
JOIN nodos n1 ON b1.origen_id = n1.id
JOIN nodos n2 ON b1.destino_id = n2.id
WHERE n1.linaje_operacion = 'contraposición' AND b1.origen_id < b1.destino_id;

-- Índices de aceleración
CREATE INDEX IF NOT EXISTS idx_manifiesto_cat ON manifiesto(categoria);
CREATE INDEX IF NOT EXISTS idx_nodos_dominio ON nodos(dominio);
CREATE INDEX IF NOT EXISTS idx_afirmaciones_nodo ON afirmaciones(nodo_id);
CREATE INDEX IF NOT EXISTS idx_puntas_estado ON puntas(estado, impacto);
CREATE INDEX IF NOT EXISTS idx_anclas_nodo ON anclas(nodo_id);
CREATE INDEX IF NOT EXISTS idx_bitacora_agente ON bitacora_sesiones(agente, timestamp);