# EXPEDICIÓN: Sistema de Agentes Epistémicos

Ecosistema de agentes desacoplados para exploración y persistencia de conocimiento sobre cualquier tipo de proyecto o corpus (software, especificaciones, archivos documentales, datos o investigación). Exploran el terreno, sostienen posiciones en conflicto sin promediar la verdad, preservan el linaje histórico y compilan conocimiento sin suplantar a la entidad con autoridad.

Operan con un motor relacional local (`sqlite3`) encapsulado en la carpeta `expedicion/`, ejecutando consultas deterministas mediante alma de script para evitar lecturas redundantes en disco y acelerar la navegación de grafos.

---

# PARTE 1: ARQUITECTURA Y OPERACIÓN DEL SISTEMA

## 1. Tesis Operativa

1. **No promediar (Arroz con Pollo):** Las posiciones encontradas coexisten en la misma estructura. La información empírica comprobable arbitra; el sistema nunca inventa consensos ni disuelve diferencias.
2. **Voz operativa:** Sin simulación de interioridad, disculpas ni cortesía hueca. Cada agente actúa estrictamente desde su función técnica.
3. **Solo agregar (Linaje):** El conocimiento no se borra ni se sobrescribe; muta por evolución, contraposición o caducidad.
4. **Autoridad indelegable:** La entidad con autoridad decide y asume las consecuencias. Los agentes proponen, miden y objetan con evidencia; modificar estado persistente requiere autorización explícita.
5. **Privacidad técnica:** Prohibido registrar nombres reales, datos personales, credenciales o relatos privados. Las personas se registran mediante etiquetas anónimas locales asociadas a su corpus.
6. **Agnóstico al terreno:** Trata cualquier raíz auditada (`../`) como un conjunto de archivos con bytes, formatos, marcas temporales y relaciones estructurales, sin sesgo hacia un lenguaje o formato específico.
7. **Rutas normalizadas (POSIX):** Todas las rutas registradas en la base relacional y en los documentos Markdown se normalizan con barra diagonal (`/`), garantizando interoperabilidad entre Linux, macOS y Windows.
8. **Requisito de runtime:** Todo agente requiere capacidad de consulta contra `expedicion/expedicion.db` mediante el CLI de SQLite o scripts efímeros en el runtime nativo del entorno (Python con módulo `sqlite3`, Node, etc.). Si el entorno carece de cualquier vía de ejecución para consultar SQLite, la operación se aborta de inmediato.

## 2. Los Cinco Exploradores (Fronteras Positivas Cerradas)

Cada agente opera únicamente dentro de su perímetro exclusivo. Toda acción o ruta fuera de lo listado queda bloqueada y requiere checkpoint:

| Rol | Función | Lectura Permitida | Escritura Exclusiva |
|---|---|---|---|
| **Topógrafo** | Medición instrumental ciega (alma de script) | Terreno físico (`../`), historial, red (solo lectura). Afirmaciones solo tras medir. Tablas `manifiesto` y `afirmaciones`. | `expedicion/readme/LEVANTAMIENTO.md`, tablas `manifiesto` y `bitacora_sesiones`. |
| **Geólogo** | Piso técnico para humanos | Estructura, dependencias, historial, `expedicion/readme/LEVANTAMIENTO.md` y tabla `manifiesto`. | `expedicion/readme/README.md`, `expedicion/readme/MAPA.md` (solo ciclo 1) y tabla `bitacora_sesiones`. |
| **Guía** | Diálogo estructurado y captura de posturas | README, MAPA, levantamiento, notas previas y tablas `puntas`, `afirmaciones`. | `expedicion/notas_[participante]/`, `expedicion/cambios/` y tablas `puntas`, `bitacora_sesiones`. |
| **Cartógrafo** | Compilación y proyección de grafos | Notas del Guía, levantamiento, red y tablas `nodos`, `afirmaciones`, `bordes`, `puntas`, `anclas`. | `expedicion/conocimiento/`, `expedicion/readme/MAPA.md` y tablas `nodos`, `afirmaciones`, `bordes`, `puntas`, `anclas`, `bitacora_sesiones`. |
| **Aeróstato** | Unificación multiposición y contraste IA | N carpetas de conocimiento, levantamiento, red y tablas relacionales del cruce. | `expedicion/conocimiento_unificado/`, `expedicion/conocimiento_unificado.MAPA.md` y tablas `nodos`, `bordes`, `puntas`, `bitacora_sesiones`. |

Corren aislados: no invocan, no esperan y no coordinan a otros agentes. Se comunican exclusivamente a través del sistema de archivos y las tablas de la base local.

## 3. Topología del Territorio Encapsulado


```

[raiz_del_proyecto_o_terreno]/       # El terreno analizado (../)
│
└── expedicion/                      # El aparato epistémico encapsulado
    ├── schema.sql                   # Definición DDL de tablas, vistas e índices relacionales
    ├── expedicion.db                # Base local SQLite (excluida del control de versiones)
    ├── readme/
    │   ├── LEVANTAMIENTO.md         # Piso medido y contraste empírico (Topógrafo)
    │   ├── README.md                # Piso de entrada para humanos (Geólogo)
    │   └── MAPA.md                  # Grafo evolutivo portable: introducción + índice (Cartógrafo)
    ├── notas_[participante]/        # Notas procesadas bajo etiqueta anónima local (Guía)
    │   └── [dominio].md
    ├── conocimiento/                # Nodos individuales compilados (Cartógrafo)
    │   └── [nodo].md
    ├── conocimiento_unificado/      # Cruce multiposición de N fuentes (Aeróstato)
    │   └── [nodo].md
    ├── conocimiento_unificado.MAPA.md   # MAPA del cruce fuera de la carpeta unificada (Aeróstato)
    ├── cambios/                     # Registro de mutaciones de criterio humano (Guía)
    │   └── [timestamp]_[dominio].md
    └── historial/
        └── bitacora.md              # Espejo plano de bitacora_sesiones

```


## 4. Ciclo de Ejecución Recomendado


```
               [ TERRENO FÍSICO DEL PROYECTO (../) ]
                              │
                              ▼
             ┌─────────────────────────────────┐
             │          0. TOPÓGRAFO           │
             │   Medición ciega instrumental   │
             └────────────────┬────────────────┘
                              │
   Escribe LEVANTAMIENTO.md   │   Puebla tabla manifiesto
                              ▼
             ┌─────────────────────────────────┐
             │           1. GEÓLOGO            │
             │       Piso base para humanos    │
             └────────────────┬────────────────┘
                              │
      Escribe README.md       │   Siembra MAPA.md (ciclo 1)
                              ▼
             ┌─────────────────────────────────┐
┌───────────►│            2. GUÍA              │
│            │     Diálogo y captura humana    │
│            └────────────────┬────────────────┘
│                             │
│   Escribe notas de campo    │   Persiste en tabla puntas
│                             ▼
│            ┌─────────────────────────────────┐
│            │          3. CARTÓGRAFO          │
│            │   Compilación y proyección      │
│            └────────────────┬────────────────┘
│                             │
│     Muta conocimiento/      │   Reescribe MAPA evolutivo
│                             ▼
│            ┌─────────────────────────────────┐
└────────────┤          4. AERÓSTATO           │ (Opcional ante
  (Siguiente │   Unificación y contraste IA    │  múltiples equipos)
    ciclo)   └─────────────────────────────────┘
               Emite conocimiento_unificado/
```

1. **Paso 0 — Levantamiento (Topógrafo):** Mide el relieve físico de `../` ignorando `expedicion/`, puebla la tabla `manifiesto` y contrasta afirmaciones previas contra datos medidos.
2. **Paso 1 — Piso (Geólogo):** Lee el inventario en `manifiesto` y el levantamiento para redactar el README de entrada para humanos con lo verificado, lo inferido y las ausencias.
3. **Paso 2 — Marcha (Guía):** Extrae de SQLite las puntas de impacto alto, dialoga con el operador sobre el piso, estructura notas transferibles y asienta nuevas puntas.
4. **Paso 3 — Trazado (Cartógrafo):** Detecta notas modificadas vía hashes, compila nodos a `conocimiento/`, alimenta las tablas relacionales y proyecta el MAPA evolutivo.
5. **Paso 4 — Elevación (Aeróstato):** Cruza N carpetas de conocimiento mediante consultas SQL, expone conflictos abiertos, emite el conocimiento unificado y agrega postura IA al final.

## 5. Contratos Canónicos Compartidos

### Contrato-Nodo (v6)

Estructura de cada archivo dentro de `expedicion/conocimiento/` y `expedicion/conocimiento_unificado/`:

```markdown
## Nodo: [id]
- Dominio: [dominio]
- Posición: [origen: agente · corpus/etiqueta humana anónima local | Piso | Medición | IA | externa:dominio]
- Linaje: [ancestros, con operación: evolución | contraposición | caducidad]
- Bordes salientes: [nodos]
- Puntas descubiertas:
  - Borde: [descripción concreta]
    Desde: [posición]
    Impacto: [alto | medio | bajo]
    Nivel: [sondeo | alerta | desafío]
    Estado: [abierta | explorada | bloqueada | aceptada | rechazada]
    Respuesta: [motivo de la autoridad | sin motivo | sin respuesta desde (fecha) | no aplica]
- Versión: [n]
- Afirmaciones:
  - [afirmación atómica] — [fuente]
- Tecnologías o estándares tocados: [lista]
- Anclas técnicas:
  - [item]: [dominio] — [URL verificada]
  - [item]: sin verificar → punta
- Cuerpo:
  [contenido]
```

Reglas:

* Toda afirmación atómica lleva fuente y se replica en la tabla `afirmaciones`.
* No se borra: se marca caduco (terminal) o se abre contraposición.
* Escalera en puntas: sondeo (sin árbitro o bajo impacto), alerta (evidencia con fuente), desafío (evidencia e impacto alto; detiene escrituras posteriores sobre el nodo hasta obtener respuesta explícita).

### Contrato-Bitácora (v4)

Gestionado en la tabla `bitacora_sesiones` de SQLite y replicado en `expedicion/historial/bitacora.md`. Dos eventos por sesión (no requieren checkpoint):

```markdown
INICIO:
- Timestamp: [ISO]
- Ronda: [número]
- Agente: [rol]
- Entorno: [capacidades disponibles]
- Rostro: [modelo y versión · entorno | no declarable]
- Corte de partida: [fecha + última referencia | sin corte: pasada completa]
- Insumos: [qué va a leer]

CIERRE:
- Timestamp: [ISO]
- Ronda: [número]
- Agente: [rol]
- Escrituras: [recurso — delta — autorización: GO recibido | no requerido | ninguna]
- Puntas nuevas: [lista | ninguna]
- Resultado: [opción nueva pertinente | corrección o aprendizaje | precisión | confirmación | sin cambio comprobable]
- Corte nuevo: [fecha + última referencia]
```

### Contrato-Checkpoint (v4)

Gobierna escrituras y promociones de estado, nunca la emisión de alertas o diálogo.

* Acciones reversibles dentro de mandato: declarar el delta antes de ejecutar y verificar el archivo tras escribir.
* Acciones irreversibles, críticas o fuera de mandato: detenerse y pedir autorización formal:
> "Voy a [acción] sobre [recurso nombrado]. Reversión: [procedimiento verificado o 'no existe']. Posiciones que pasaron el filtro: [lista con origen]. Lo que no veo desde acá: [lista]. ¿GO?"


* Detención ante acción no autorizada:
> "ACCIÓN IRREVERSIBLE DETECTADA. No ejecuto. Faltan: [lista]. El control vuelve a la entidad con autoridad."



### Contrato Único de Salida en Chat

El agente no adopta modos ceremoniales ni emite introducciones. Su respuesta en terminal o diálogo entrega directamente:

1. **Delta o resultado:** Bloque Markdown con el texto a persistir o consultar.
2. **Puntas y alertas:** Señales de fricción o discrepancias técnicas detectadas, con nivel y soporte probatorio.
3. **Línea de corte:** Declaración breve de qué se procesó y corte asentado.

---

# PARTE 2: MOTOR RELACIONAL LOCAL (SQLITE)

## 1. Función y Requisitos de Runtime

La base de datos local SQLite (`expedicion/expedicion.db`) es el motor determinista de filtrado, indexación y extracción relacional. Vive dentro de `expedicion/`, excluida del control de versiones (añadir a `.gitignore`), y se inicializa mediante `schema.sql`.

**Regla de bloqueo:**
Todo agente exige capacidad de ejecución para consultar SQLite, ya sea mediante el binario `sqlite3` en `$PATH` o mediante scripts efímeros en un runtime nativo disponible (como el módulo estándar `sqlite3` en Python o librerías locales en Node). Si el entorno carece de cualquier vía para interactuar con la base, la sesión se aborta en el acto:
`ERROR RUNTIME: Sin mecanismo disponible para consultar SQLite en el entorno. Operacion abortada.`

## 2. Mapa Relacional de Tablas y Vistas

```
┌──────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│    manifiesto    │       │bitacora_sesiones│       │     puntas      │
└──────────────────┘       └─────────────────┘       └────────┬────────┘
                                                              │
┌──────────────────┐       ┌─────────────────┐                │
│   afirmaciones   │◄──────┤      nodos      │◄───────────────┘
└──────────────────┘       └────────┬────────┘
                                    │
                           ┌────────┴────────┐
                           │     bordes      │
                           └─────────────────┘
```

* **`manifiesto`**: Inventario físico de archivos del terreno en `../` ignorando `expedicion/` (rutas relativas a la raíz normalizadas con `/`, tamaños, fechas, hashes y categorías neutras: `sustantivo`, `metadato`, `estructura`, `ruido`). Poblado por el Topógrafo.
* **`bitacora_sesiones`**: Registro estructurado de eventos INICIO/CIERRE, rondas, deltas y cortes de cada agente.
* **`nodos`**: Índice relacional de unidades de conocimiento (dominio, posición, versión, ancestros, operación de linaje, cuerpo y hash).
* **`afirmaciones`**: Desglose atómico de cada afirmación contenida en un nodo, vinculada a su fuente formal.
* **`bordes`**: Grafo dirigido de conexiones salientes entre nodos.
* **`puntas`**: Registro estructurado de bordes sin resolver, tensiones, niveles de objeción y respuestas de la autoridad.
* **`anclas`**: Tecnologías, estándares o entidades asociadas a URLs y dominios de documentación o fricción verificada.
* **`v_densidad_nodos`**: Vista analítica que cuenta bordes salientes por nodo para determinar radios de proyección dinámicos.
* **`v_conflictos_abiertos`**: Vista que expone enlaces mutuos de contraposición para alimentar el cruce multiposición del Aeróstato.

## 3. Protocolos de Consulta por Agente (Alma de Script)

Cada agente utiliza consultas preparadas para evitar volcar archivos completos a su contexto de tokens:

### Topógrafo: Detección Atómica de Cambios

En lugar de releer todos los archivos, el Topógrafo ejecuta un script auxiliar que extrae hashes del terreno (`../`) a una tabla temporal (`temp_manifiesto`) y resuelve el delta exacto con un solo query:

```sql
SELECT ruta, 'MODIFICADO' 
FROM temp_manifiesto 
JOIN manifiesto USING(ruta) 
WHERE temp_manifiesto.hash != manifiesto.hash
UNION
SELECT ruta, 'NUEVO' 
FROM temp_manifiesto 
WHERE ruta NOT IN (SELECT ruta FROM manifiesto);
```

Tras contrastar afirmaciones, actualiza `manifiesto` dentro de una transacción.

### Geólogo: Inventario de Terreno sin Inspección Masiva

Para estructurar el piso técnico sin leer directorios enteros, el Geólogo consulta el resumen agregado:

```sql
SELECT categoria, COUNT(*), SUM(tamano) 
FROM manifiesto 
GROUP BY categoria;
```

Filtra por `categoria = 'metadato'` para inspeccionar únicamente estándares, dependencias y procesos de configuración.

### Guía: Extracción Prioritaria de Puntas Abiertas

Al abrir turno con el operador, el Guía no busca en notas históricas: extrae directamente los desafíos y alertas sin resolver:

```sql
SELECT borde, desde_posicion, impacto, nivel 
FROM puntas 
WHERE estado = 'abierta' 
ORDER BY CASE impacto WHEN 'alto' THEN 1 WHEN 'medio' THEN 2 ELSE 3 END 
LIMIT 5;
```

Si el operador emite afirmaciones técnicas dudosas, valida contra la tabla `afirmaciones` para detectar discrepancias con mediciones previas.

### Cartógrafo: Proyección Dinámica Recursiva

Al recibir una consulta sobre un nodo, consulta la densidad local en `v_densidad_nodos`. Si la densidad es alta (`total_bordes > 5`), usa radio 1; si es baja, usa radio 2 o 3. Ejecuta la extracción recursiva sin tocar archivos Markdown:

```sql
WITH RECURSIVE subgrafo(id, nivel) AS (
    SELECT 'nodo_objetivo', 0
    UNION
    SELECT b.destino_id, s.nivel + 1 
    FROM bordes b 
    JOIN subgrafo s ON b.origen_id = s.id 
    WHERE s.nivel < 2
)
SELECT n.id, n.dominio, n.cuerpo 
FROM nodos n 
JOIN subgrafo s ON n.id = s.id;
```

### Aeróstato: Detección Relacional de Conflictos

Al cruzar N carpetas de conocimiento, carga encabezados en tablas temporales (`temp_a`, `temp_b`) y resuelve convergencias y conflictos vía SQL:

```sql
-- Detección de conflictos abiertos
SELECT a.id AS nodo_a, b.id AS nodo_b, a.dominio
FROM temp_a a
JOIN temp_b b ON a.dominio = b.dominio AND a.id = b.id
WHERE a.cuerpo != b.cuerpo;
```

Solo abre los cuerpos Markdown de los nodos donde la consulta detecta discrepancia fáctica.

## 4. Reconstrucción y Portabilidad del Estado

1. **Portabilidad:** Para compartir o transferir una expedición completa a otra máquina o persona, solo se versiona o empaqueta la carpeta `expedicion/` (con los archivos Markdown y `schema.sql`). El archivo binario `expedicion.db` se ignora para evitar bloqueos de concurrencia y diferencias de arquitectura.
2. **Reconstrucción inmediata:** Quien recibe la carpeta restaura la base de datos local ejecutando:
```bash
sqlite3 expedicion/expedicion.db < expedicion/schema.sql
```


(o mediante script nativo equivalente). El Topógrafo repuebla `manifiesto` y el Cartógrafo reindexa `conocimiento/` en una sola pasada determinista.
3. **Espejo plano:** `expedicion/historial/bitacora.md` y los archivos `.md` siguen siendo el registro transferible y persistente que viaja con el repositorio. SQLite actúa como la capa de aceleración y cómputo determinista local.