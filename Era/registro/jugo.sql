-- Jugo del candado: las piezas que van al candado, en SQLite y no en un archivo suelto.
-- Una tabla por clase de pieza, y una vista para leerlas juntas.

CREATE TABLE IF NOT EXISTS pieza (
  id        INTEGER PRIMARY KEY,
  orden     INTEGER NOT NULL,                 -- el orden en que se dijeron
  clase     TEXT NOT NULL,                    -- principio | ciclo | ciclo_rompe | no_repetir | poder | cita
  nombre    TEXT NOT NULL,                    -- el nombre propio de la pieza
  expansión TEXT NOT NULL,                    -- qué dice, sin adornos
  porque    TEXT NOT NULL,                    -- por qué se sostiene
  referencia TEXT NOT NULL DEFAULT 'ninguna', -- la obra o el caso que la provocó
  pregunta  TEXT NOT NULL DEFAULT 'ninguna',  -- qué preguntó la referencia
  estado    TEXT NOT NULL DEFAULT 'viva'
                CHECK (estado IN ('viva','suplantada','descartada')),
  fecha     TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_pieza_clase ON pieza(clase);
CREATE INDEX IF NOT EXISTS idx_pieza_estado ON pieza(estado);

-- Lo que sobrevive a una destrucción: no vive dentro del ente.
CREATE VIEW IF NOT EXISTS jugo AS
SELECT orden, clase, nombre, expansión, porque, referencia, pregunta
FROM pieza WHERE estado = 'viva' ORDER BY orden;
