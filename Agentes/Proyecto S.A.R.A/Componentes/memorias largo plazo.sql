-- memorias.db : registro permanente de un agente. Una por agente.
-- Ruta: <agente>/memorias.db — sara/ en la semilla, camada/<nombre>/ en orquestación.
-- Append-only por convención: nada se edita, se reemplaza. Sin triggers, sin vistas.

PRAGMA journal_mode = WAL;
PRAGMA user_version = 2;   -- versión de este esquema

CREATE TABLE memorias (
  id          INTEGER PRIMARY KEY,        -- rowid nativo; INSERT ... RETURNING id
  fecha       TEXT NOT NULL,              -- ISO-8601
  tipo        TEXT NOT NULL,              -- fin | cierre | hecho | precedente | patron
                                          -- | pendiente | descarte | acto | paso | perimetro
  autor       TEXT NOT NULL,              -- tipo:nombre — persona:alex | agente:jarvis
                                          -- | concepto:ausencia-declarada | grupo:3
  condiciones TEXT NOT NULL,              -- contexto de contorno de la fila
  sistema     TEXT,                       -- instrumento que produjo el dato
  version     TEXT,                       -- versión del instrumento al producir
  disparador  TEXT NOT NULL,              -- estado que habilita su relectura
  nivel       INTEGER,                    -- 1..5, Escala de Evidencia
  cierra_en   TEXT,                       -- tipo:nombre de quien asume la consecuencia
  corte       TEXT,                       -- fecha de corte del dato
  vigencia    TEXT,                       -- hasta cuándo vale
  motivo      TEXT,                       -- por qué se promovió, o por qué se cierra
  reemplaza   INTEGER REFERENCES memorias(id),
  cuerpo      TEXT                        -- payload libre de cada skill
) STRICT;

CREATE INDEX idx_disp       ON memorias(disparador);
CREATE INDEX idx_tipo_fecha ON memorias(tipo, fecha);

-- Convenciones que el esquema no impone y la lectura exige:
-- 1. Los cinco campos obligatorios son regla, no adorno: una fila sin condiciones no entra.
-- 2. Sin CHECK sobre tipo: un mutante puede agregar tipos sin migrar el esquema.
-- 3. tipo='cierre' es el borde de tarea. Su cuerpo lleva: fin vigente, decisiones
--    tomadas con su id, pendientes abiertos con su id y siguiente paso. Su reemplaza
--    apunta al cierre anterior: la cadena de cierres es la conversación comprimida.
-- 4. En filas `hecho`, `sistema` y `version` identifican el instrumento que produjo el dato:
--    sin ellas no se cumple Condiciones de validación.
-- 5. trabajo.db no lleva DDL aquí. Nace vacía; su forma la decide el agente en su
--    primera escritura, incluido el contador de actos y el fin vigente.

-- Lecturas mínimas. No son objetos: se sintetizan en el turno.
-- por disparador:       SELECT id, fecha, tipo, nivel, condiciones FROM memorias
--                       WHERE disparador LIKE :p AND (vigencia IS NULL OR vigencia > date('now'))
--                       ORDER BY fecha DESC LIMIT 5;
-- cuerpo por id:        SELECT id, cuerpo FROM memorias WHERE id IN (:ids);
-- cierre reciente:      SELECT id, fecha, cuerpo FROM memorias
--                       WHERE tipo='cierre' ORDER BY fecha DESC LIMIT 1;
-- vigente de un tipo:   SELECT id, fecha, condiciones, cuerpo FROM memorias m
--                       WHERE m.tipo=:t AND NOT EXISTS
--                       (SELECT 1 FROM memorias s WHERE s.reemplaza=m.id);
-- contradicción sobre :p: SELECT id, fecha, autor, cuerpo FROM memorias
--                       WHERE disparador=:p ORDER BY fecha;  -- se muestran todas, no se elige
-- autoridad mal escrita: SELECT id, autor FROM memorias
--                       WHERE autor NOT LIKE '%:%';          -- debe dar 0 filas
-- costo por autoridad:  SELECT cierra_en, count(*) FROM memorias
--                       WHERE cierra_en IS NOT NULL GROUP BY cierra_en;
