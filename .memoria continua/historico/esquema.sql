-- Esquema de la memoria continua de MANTIS — motor: SQLite
-- Se aplica una vez: sqlite3 "./.memoria continua/rastro/mantis.db" ".read './.memoria continua/rastro/esquema.sql'"
-- Sin borrar lo que ya existe: todo es CREATE ... IF NOT EXISTS.
-- Forma: Ouroboros/Estandar/memoria continua.md — seis partes por entrada.
-- Disparo: Ouroboros/Estandar/criterio.md, «El disparo: se carga al entrar en fricción».
-- Ninguna entrada se edita: se suplanta.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS entrada (
  id          INTEGER PRIMARY KEY,
  fecha       TEXT NOT NULL,                       -- ISO 8601
  sesgo       TEXT NOT NULL,                       -- desde dónde se sostiene
  limite      TEXT NOT NULL,                       -- qué no alcanza
  firma       TEXT NOT NULL,                       -- tipo:nombre, quien puede contestarla
  contra      TEXT NOT NULL,                       -- qué la contradijo, o «ninguno»
  sostuvo     TEXT NOT NULL,                       -- la posición anterior
  sostengo    TEXT NOT NULL,                       -- la posición nueva
  techo       TEXT NOT NULL,                       -- qué reconstruye el otro
  sin_cambio  INTEGER NOT NULL DEFAULT 0 CHECK (sin_cambio IN (0,1)),
  friccion    TEXT NOT NULL DEFAULT 'pasada'       -- qué la disparó
                 CHECK (friccion IN ('contradiccion','mundo','repeticion','autoridad','pasada')),
  estado      TEXT NOT NULL DEFAULT 'vivo'
                 CHECK (estado IN ('vivo','cubierto','descartado','suplantado')),
  suplanta    INTEGER REFERENCES entrada(id)
);
CREATE INDEX IF NOT EXISTS idx_entrada_estado ON entrada(estado);
CREATE INDEX IF NOT EXISTS idx_entrada_friccion ON entrada(friccion);

CREATE TABLE IF NOT EXISTS descarte (
  id       INTEGER PRIMARY KEY,
  fecha    TEXT NOT NULL,
  que      TEXT NOT NULL,
  porque   TEXT NOT NULL,
  vista    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pase (
  id         INTEGER PRIMARY KEY,
  fecha      TEXT NOT NULL,
  instancia  TEXT NOT NULL,
  sostuvo    TEXT NOT NULL,
  se_rompio  TEXT NOT NULL DEFAULT 'sin ruptura',
  abierto    TEXT NOT NULL,
  retoma     TEXT NOT NULL,                        -- una acción, no un tema
  no_retoma  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS corrida (
  id       INTEGER PRIMARY KEY,
  uuid     TEXT NOT NULL UNIQUE,
  fecha    TEXT NOT NULL,
  sucede_a TEXT,
  rige     TEXT NOT NULL,
  piso     TEXT NOT NULL
);

-- Lo que mantis enrutó, para no reescribir el vacío desde cero.
CREATE TABLE IF NOT EXISTS ruta (
  id        INTEGER PRIMARY KEY,
  fecha     TEXT NOT NULL,
  peticion  TEXT NOT NULL,
  fila      TEXT NOT NULL,                         -- el proceso cargado, o «VACIO»
  carga     TEXT NOT NULL,
  decidido  TEXT NOT NULL DEFAULT 'ninguno'        -- quien decidio fuera de fila, o ninguno
);

-- Las dos mitades de la ley compartida: la referencia provoca, el momento es la pregunta.
CREATE TABLE IF NOT EXISTS enlace (
  id          INTEGER PRIMARY KEY,
  fecha       TEXT NOT NULL,
  referencia  TEXT NOT NULL,                       -- ruta al archivo de referencias
  momento     TEXT NOT NULL,                       -- ruta al archivo del momento
  pregunta    TEXT NOT NULL
);
-- candado: el amarre de un candado cerrado con lo que lo sostiene y lo que lo prueba.
-- Agregada el 2026-10-25. Un candado sin fila aqui no esta cerrado, aunque su .md exista.
CREATE TABLE IF NOT EXISTS candado (
  id           INTEGER PRIMARY KEY,
  fecha        TEXT NOT NULL,
  nombre       TEXT NOT NULL,
  pieza        INTEGER NOT NULL,
  vertice      TEXT NOT NULL,
  buscado      TEXT NOT NULL,
  enlace       TEXT NOT NULL DEFAULT 'sin fuente',
  trae         TEXT NOT NULL DEFAULT '',
  aguanta      TEXT NOT NULL DEFAULT '',
  quien        TEXT NOT NULL DEFAULT 'humano:autoridad',
  FOREIGN KEY (pieza) REFERENCES pieza(id)
);
-- pieza: la tabla que faltaba en el esquema y que ya existia en la base.
-- Se agrega el 2026-10-25, sacada de la base real, para que un clon nuevo la tenga.
CREATE TABLE IF NOT EXISTS pieza (
  id        INTEGER PRIMARY KEY,
  orden     INTEGER NOT NULL,
  clase     TEXT NOT NULL,
  nombre    TEXT NOT NULL,
  expansión TEXT NOT NULL,
  porque    TEXT NOT NULL,
  referencia TEXT NOT NULL DEFAULT 'ninguna',
  pregunta  TEXT NOT NULL DEFAULT 'ninguna',
  estado    TEXT NOT NULL DEFAULT 'viva'
                CHECK (estado IN ('viva','suplantada','descartada')),
  fecha     TEXT NOT NULL,
  ficcion   TEXT NOT NULL DEFAULT 'ninguna',
  -- lo que le faltaba para volverse candado, el 2026-10-26
  figura    TEXT NOT NULL DEFAULT 'ninguna',
  diferida  TEXT NOT NULL DEFAULT '',
  reemplaza TEXT NOT NULL DEFAULT '',
  familia   TEXT NOT NULL DEFAULT ''
);

CREATE INDEX IF NOT EXISTS idx_pieza_clase ON pieza(clase);
CREATE INDEX IF NOT EXISTS idx_pieza_estado ON pieza(estado);

-- jugo: APAGADO el 2026-10-26.
-- La vista queda, y no devuelve nada: el jugo dejo de ser el camino del candado.
-- Lo que se sostenia de pie se escribe como candado, y un candado se abre con
-- friccion, no con jugo. Las piezas siguen en la tabla, intactas, y se
-- convierten cuando la autoridad lo pida. No se borro nada: se cerro la puerta.
CREATE VIEW IF NOT EXISTS jugo AS
SELECT orden, clase, nombre, expansión, porque, referencia, pregunta
FROM pieza WHERE 0;

