CREATE TABLE fila (
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
CREATE INDEX idx_fila_seccion ON fila(seccion, id);
CREATE INDEX idx_fila_estado  ON fila(estado);
CREATE INDEX idx_fila_pieza   ON fila(pieza);
CREATE TABLE sesion (
  id        INTEGER PRIMARY KEY CHECK (id = 1),
  fecha     TEXT NOT NULL,
  vista     TEXT NOT NULL,
  estado    TEXT NOT NULL,
  roto      TEXT NOT NULL DEFAULT 'ninguno',
  abierto   TEXT,
  siguiente TEXT,
  decidido  TEXT,
  rige      TEXT NOT NULL DEFAULT 'claridad | sesgo declarado'
, viendo TEXT, compilado_en TEXT);
CREATE TABLE generacion (
  id        INTEGER PRIMARY KEY,
  nombre    TEXT NOT NULL UNIQUE,
  fecha     TEXT NOT NULL,
  vista     TEXT NOT NULL,
  compilado TEXT,
  dejo_vivo INTEGER NOT NULL DEFAULT 0,
  descarto  INTEGER NOT NULL DEFAULT 0,
  reemplaza TEXT
);
CREATE TABLE prueba (
  id      INTEGER PRIMARY KEY,
  nombre  TEXT NOT NULL UNIQUE,
  mide    TEXT NOT NULL,
  corrida TEXT,
  fecha   TEXT
);
CREATE TABLE seccion (
  nombre  TEXT PRIMARY KEY,
  orden   INTEGER NOT NULL,
  proposito TEXT
);
CREATE TABLE trabajo(
  id INT,
  que TEXT,
  donde TEXT,
  estado TEXT,
  nota TEXT
);
CREATE TABLE esquema (id INTEGER PRIMARY KEY CHECK (id=1), uuid TEXT NOT NULL, fecha TEXT NOT NULL, sucede_a TEXT);
