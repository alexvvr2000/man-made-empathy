-- Esquema del ciclo mínimo: los dos bancos, sin alma de niño.
-- Se aplica con: python bin/ciclo.py instalar
-- Forma: entes/Ente/memoria continua/banco de memoria.prs y banco de friccion.prs.
-- Motor: SQLite. Las bases viven en .memoria continua/, y están fuera del git.

PRAGMA foreign_keys = ON;

-- Banco de memoria: qué pasó, con su frontera.
-- Dispara sólo si movió el borde de lo que se sabía.
CREATE TABLE IF NOT EXISTS memoria (
  id        INTEGER PRIMARY KEY,
  fecha     TEXT NOT NULL,                       -- ISO 8601, de cuando pasó
  dijo      TEXT NOT NULL,                       -- quién habló, o qué sistema
  texto     TEXT NOT NULL,                       -- literal. No se resume
  frontera  TEXT NOT NULL
            CHECK (frontera IN ('revelación','confirmación','ruptura')),
  sabia     TEXT NOT NULL,                       -- qué no sabía antes. «nada» no entra
  turno     TEXT NOT NULL DEFAULT ''             -- dónde quedó, para volver
);
CREATE INDEX IF NOT EXISTS idx_memoria_fecha ON memoria(fecha);
CREATE INDEX IF NOT EXISTS idx_memoria_frontera ON memoria(frontera);

-- Banco de fricción: dónde se sostuvo, y qué lo refutó. Las seis partes.
-- La anterior no se borra: queda suplantada.
CREATE TABLE IF NOT EXISTS friccion (
  id        INTEGER PRIMARY KEY,
  fecha     TEXT NOT NULL,
  sesgo     TEXT NOT NULL,                       -- desde dónde se sostiene
  limite    TEXT NOT NULL,                       -- qué no alcanza
  firma     TEXT NOT NULL,                       -- quién puede contestarla
  contra    TEXT NOT NULL,                       -- qué la contradijo, o «ninguno»
  sostuve   TEXT NOT NULL,                       -- la posición anterior
  sostengo  TEXT NOT NULL,                       -- la posición nueva
  techo     TEXT NOT NULL,                       -- qué reconstruye el otro
  disparo   TEXT NOT NULL
            CHECK (disparo IN ('contradicción','mundo','repetición','autoridad')),
  estado    TEXT NOT NULL DEFAULT 'vivo'
            CHECK (estado IN ('vivo','sin cambio','suplantado')),
  suplanta  INTEGER REFERENCES friccion(id)
);
CREATE INDEX IF NOT EXISTS idx_friccion_estado ON friccion(estado);
