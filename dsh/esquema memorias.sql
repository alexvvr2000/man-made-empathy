-- memorias_trazables — esquema definitivo
-- memorias.db : registro permanente. Una por workspace. Append-only por convención, no por restricción.
-- trabajo.db  : mesa de trabajo, 100% mutable, sin esquema fijo. Una por workspace.
-- Sin triggers, sin checks de contenido, sin vistas. La disciplina vive en la lectura.

PRAGMA journal_mode = WAL;

CREATE TABLE memorias (
  id          INTEGER PRIMARY KEY,
  fecha       TEXT NOT NULL,
  tipo        TEXT,          -- hecho | precedente | patron | pendiente | descarte | acto | paso | perimetro | fin
  autor       TEXT,          -- quién responde por la fila
  nivel       INTEGER,       -- N1..N5 de la Escala de Evidencia
  cierra_en   TEXT,          -- autoridad | agente | externo
  condiciones TEXT,          -- contexto de contorno
  corte       TEXT,          -- fecha de corte del dato
  vigencia    TEXT,          -- hasta cuándo vale
  disparador  TEXT,          -- condición que habilita su relectura
  motivo      TEXT,          -- por qué se promovió
  reemplaza   INTEGER REFERENCES memorias(id),
  cuerpo      TEXT           -- payload libre de cada skill
);

-- trabajo.db — sin esquema fijo. Se crea, se rehace y se tira a voluntad.
-- Única convención: al abrir, una fila de fin.
--   CREATE TABLE fin (id INTEGER PRIMARY KEY, fecha TEXT, fin TEXT);
-- Si el propósito cambia, fila nueva de fin. La anterior queda fechada con sus filas.
-- La mesa no se cita como evidencia. Se lee. Nada más.

-- Lecturas mínimas. No son objetos: se sintetizan en el turno.
-- bucle sobre la autoridad:  SELECT id, fecha, condiciones FROM memorias WHERE cierra_en='autoridad' ORDER BY fecha DESC;
-- filas incompletas:         SELECT id FROM memorias WHERE autor IS NULL OR fecha IS NULL OR disparador IS NULL;
-- vigente por disparador:    SELECT id, fecha, condiciones, cuerpo FROM memorias WHERE disparador LIKE :p AND (vigencia IS NULL OR vigencia > date('now'));
-- contradicción sobre :p:    SELECT id, fecha, cuerpo FROM memorias WHERE disparador = :p ORDER BY fecha;  -- se muestran todas, no se elige
-- precedente vigente:        SELECT id, fecha, condiciones, cuerpo FROM memorias m WHERE m.tipo='precedente' AND NOT EXISTS (SELECT 1 FROM memorias s WHERE s.reemplaza = m.id);
-- patrones vigentes:         SELECT id, condiciones, cuerpo FROM memorias m WHERE m.tipo='patron' AND NOT EXISTS (SELECT 1 FROM memorias s WHERE s.reemplaza = m.id);
-- secuencia de pasos:        SELECT fecha, condiciones, motivo FROM memorias WHERE tipo='paso' AND fecha >= :desde ORDER BY fecha;
