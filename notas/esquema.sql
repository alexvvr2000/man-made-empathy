-- esquema.sql — la forma de la memoria
-- No se inventa aquí: se lee de ../mantis/mantenimiento/notas/notas-tesis.md, "La fila".
-- Una sola base, y ningún export: la base es la fuente.
--
-- Base: .sesion-continua/mantis.db (oculta, en gitignore). Sin .md publicado.
-- Uso: sqlite3 .sesion-continua/mantis.db < notas/esquema.sql

PRAGMA foreign_keys = ON;

-- 1. La fila de notas: lo que se dijo, con su pieza y su vista.
CREATE TABLE IF NOT EXISTS fila (
  id        INTEGER PRIMARY KEY,
  seccion   TEXT NOT NULL,
  dicho     TEXT NOT NULL,
  pieza     TEXT NOT NULL,
  tipo      TEXT NOT NULL CHECK (tipo IN ('analogía','referencia','cita','frase','decisión','descarte')),
  usa       TEXT,
  sostenido TEXT NOT NULL CHECK (sostenido IN ('prueba','frontera','nada')),
  estado    TEXT NOT NULL CHECK (estado IN ('vivo','descartado','cubierto')),
  vista     TEXT NOT NULL,
  compilado TEXT
);

CREATE INDEX IF NOT EXISTS idx_fila_seccion ON fila(seccion, id);
CREATE INDEX IF NOT EXISTS idx_fila_estado  ON fila(estado);
CREATE INDEX IF NOT EXISTS idx_fila_pieza   ON fila(pieza);

-- 2. El bloque de la sesión: uno solo, y se sustituye. Lo que vive continuas también vive aquí.
CREATE TABLE IF NOT EXISTS sesion (
  id        INTEGER PRIMARY KEY CHECK (id = 1),
  fecha     TEXT NOT NULL,
  vista     TEXT NOT NULL,
  estado    TEXT NOT NULL,
  roto      TEXT NOT NULL DEFAULT 'ninguno',
  abierto   TEXT,
  siguiente TEXT,
  decidido  TEXT,
  rige      TEXT NOT NULL DEFAULT 'claridad | sesgo declarado',
  viendo    TEXT,
  compilado_en TEXT
);

-- 3. Las generaciones: cada compilación, con su vista. Quedan en la base; su corte va a notas/generaciones/.
CREATE TABLE IF NOT EXISTS generacion (
  id        INTEGER PRIMARY KEY,
  nombre    TEXT NOT NULL UNIQUE,
  fecha     TEXT NOT NULL,
  vista     TEXT NOT NULL,
  compilado TEXT,
  dejo_vivo INTEGER NOT NULL DEFAULT 0,
  descarto  INTEGER NOT NULL DEFAULT 0,
  reemplaza TEXT
);

-- 4. Las pruebas: se toman en cuenta al compilar.
CREATE TABLE IF NOT EXISTS prueba (
  id      INTEGER PRIMARY KEY,
  nombre  TEXT NOT NULL UNIQUE,
  mide    TEXT NOT NULL,
  corrida TEXT,
  fecha   TEXT
);

-- 5. Las secciones fijas: el orden en que se leen.
CREATE TABLE IF NOT EXISTS seccion (
  nombre  TEXT PRIMARY KEY,
  orden   INTEGER NOT NULL,
  proposito TEXT
);

-- 6. El trabajo en curso: lo que no es la sesión ni la tesis, y que se sigue entre turnos.
CREATE TABLE IF NOT EXISTS trabajo (
  id       INTEGER PRIMARY KEY,
  que      TEXT NOT NULL,
  donde    TEXT,
  estado   TEXT,
  nota     TEXT
);

INSERT OR IGNORE INTO seccion (nombre, orden, proposito) VALUES
  ('La vista',             10, 'desde dónde se escribió cada fila'),
  ('La purga',             20, 'lo que salió de lo viejo'),
  ('El historial',         30, 'lo descartado y cuándo vuelve'),
  ('Unidad y tiro',        40, 'qué vuelve y qué no'),
  ('La triangulación',     50, 'las tres fuentes de la tesis'),
  ('Las tesis del estándar', 60, 'por qué existe cada proceso'),
  ('Qué resuelve cada proceso', 70, 'el fallo que corrige cada uno'),
  ('Los límites y las analogías', 80, 'qué no hace cada proceso'),
  ('Las pruebas',          90, 'lo que se mide al compilar'),
  ('La generación',       100, 'cómo se compila'),
  ('Las notas',           110, 'la conversación');
