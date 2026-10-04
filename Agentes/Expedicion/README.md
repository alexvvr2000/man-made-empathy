# EXPEDICIÓN: Sistema de Agentes Epistémicos

> **Un ecosistema de agentes que exploran un territorio, sostienen posiciones en conflicto y compilan conocimiento sin inventar consenso, sin promediar la verdad y sin decidir por la entidad con autoridad.**

---

## 1. La Tesis

La mayoría de los sistemas multi-agente fallan por tres vicios estructurales:
1. **Promedian:** Tratan dos opiniones contradictorias como un problema a resolver mediante síntesis blanda, borrando el dato real: *el conflicto entre posiciones*.
2. **Simulan interioridad:** Fingen empatía, piden disculpas y asumen decisiones de negocio mediante adulación o complacencia inercial.
3. **Destruyen el linaje:** Sobrescriben el conocimiento previo en lugar de mutarlo, dejando al equipo a ciegas sobre qué cambió, quién lo dijo y qué quedó sin resolver.

Este sistema opera bajo el principio del **Arroz con Pollo**: los ingredientes se cocinan juntos en la misma olla con el fuego de la información real como árbitro, pero el arroz no se vuelve pollo, el pollo no se vuelve arroz y el sofrito no los promedia. Cada posición conserva su origen, su sesgo y su tensión.

El fin último no es la documentación: es que la **entidad con autoridad** termine cada ciclo con **≥1 opción que no había considerado**.

---

## 2. Los Cuatro Exploradores

Cada agente tiene un rol estricto, una frontera de archivos infranqueable y una voz operativa desprovista de subjetividad:

| Rol | Metáfora | Qué hace | Qué produce | Límite estricto |
|---|---|---|---|---|
| **Geólogo** | El suelo de roca | Lee el terreno de cualquier proyecto (artefactos, dependencias, procesos, historial de cambios). Infiere con ancla en la evidencia y declara ausencias concretas. | `readme/README.md`<br>`readme/MAPA.md` *(solo ciclo 1)* | Jamás lee `conocimiento/` ni notas personales. No conversa sobre intenciones. |
| **Guía** | El cuaderno de marcha | Conversa con el humano. Aplica contraste adversarial y explora la cuarta categoría *(lo que el humano no sabe que no sabe)*. | `notas_[persona]/[dominio].md`<br>`cambios/` | No lee el contenido interno del proyecto. No ejecuta comandos. No compila grafos. |
| **Cartógrafo** | La mesa de dibujo | Compila notas en un grafo de nodos con linaje, afirmaciones con fuente, tecnologías y anclas verificadas (dominio + URL). Proyecta subgrafos por radio dinámico. | `conocimiento/[nodo].md`<br>`readme/MAPA.md` | No borra nodos (los muta o marca caducos). Preserva los nodos de origen Piso del MAPA existente. No toca el `README.md`. |
| **Aeróstato** | El reconocimiento aéreo | Se eleva sobre múltiples carpetas de conocimiento independientes, detecta convergencias, marca conflictos y aporta contraste IA con rostro visible. | `conocimiento_unificado/`<br>`conocimiento_unificado.MAPA.md` | No decide verdad ni promedia. Produce un reemplazo directo (*drop-in replacement*) de `conocimiento/`. |

Todos registran INICIO y CIERRE de sesión en `historial/bitacora.md`. Cada agente corre solo: no invoca, espera ni coordina a los demás. Lo que otro produjo se lee como evidencia.

---

## 3. Topología del Territorio

El sistema vive enteramente en el sistema de archivos local, con trazabilidad en texto plano estructurado:

```
proyecto/
├── readme/
│   ├── README.md                    # Piso para humanos (Geólogo)
│   └── MAPA.md                      # Grafo evolutivo portable: introducción + índice
│
├── notas_[persona]/                 # Cuadernos de campo (Guía)
│   └── [dominio].md                 # Notas con tecnologías, anclas y puntas
│
├── conocimiento/                    # Grafo de nodos (Cartógrafo)
│   └── [nodo].md                    # Nodos con versión, afirmaciones, linaje y bordes
│
├── conocimiento_unificado/          # Cruce de N carpetas (Aeróstato)
│   └── [nodo].md                    # Reemplazo directo de conocimiento/
├── conocimiento_unificado.MAPA.md   # MAPA del cruce, fuera de la carpeta de nodos
│
├── cambios/                         # Mutaciones de criterio humano (Guía)
│   └── [timestamp]_[dom].md
│
└── historial/
    └── bitacora.md                  # INICIO y CIERRE de cada sesión; guarda el corte
```

---

## 4. Ciclo de Expedición

El ciclo es una ruta posible que decide el humano, no una orquestación. Cada agente corre solo, cuando se le invoca, y ninguno cierra el ciclo:

```
              [ TERRENO: CUALQUIER PROYECTO ]
                        │
                        ▼
                 1. GEÓLOGO (Piso)
           Produce el piso para humanos
                        │
                        ▼
┌───────────────── 2. GUÍA (Marcha) ◄───────────────────┐
│         Conversa con el humano sobre el piso          │
│         Produce notas transferibles y puntas          │
│                        │                              │
│                        ▼                              │
│              3. CARTÓGRAFO (Trazado)                  │
│         Compila notas a nodos y proyecta              │
│         Reescribe el MAPA evolutivo                   │
│                        │                              │
│                        ▼                              │
│              4. AERÓSTATO (Elevación)                 │
│         Cruza N fuentes sin promediar                 │
│         Emite conocimiento_unificado/                 │
│                        │                              │
└────────────────────────┴──────────────────────────────┘
```

1. **Piso:** El Geólogo lee el terreno y produce un README que cualquiera entiende: qué es, qué contiene, con qué está hecho y qué no se pudo ver. Infiere el propósito desde la evidencia y dice de dónde lo infiere. Lo ausente se declara como ausencia concreta, no como defecto moral.
2. **Entrada humana:** El Guía toma el piso y la herencia del ciclo anterior. Desafía al humano con preguntas incómodas y genera notas estructuradas.
3. **Compilación de grafo:** El Cartógrafo lee notas nuevas, contrasta la evidencia contra las afirmaciones de cada nodo y teje un grafo con anclas técnicas reales (enlaces a documentación oficial o issues de fricción, sin copiar texto). Preserva los nodos de origen Piso del MAPA existente.
4. **Cruce multiposición:** El Aeróstato toma carpetas de distintos equipos o agentes y las hace coexistir en `conocimiento_unificado/`. Si dos posiciones chocan, se marcan en conflicto y se apuntan mutuamente; nunca se diluyen en un término medio.

---

## 5. Las Tres Reglas Duras

Todo el comportamiento se subordina a tres reglas inquebrantables:

1. **Irreversibilidad (El Checkpoint Canónico):**  
   Ningún agente escribe en disco ni modifica estado sin una orden expresa `[GO]` bajo la fórmula canónica:  
   > *"Voy a [acción] sobre [recurso]. Reversión: [procedimiento o 'no existe']. Posiciones que pasaron el filtro: [lista con origen]. Lo que no veo desde acá: [lista]. ¿GO?"*
2. **Trazabilidad (Sin Fe):**  
   Cada sesión de cada agente se asienta en `historial/bitacora.md` con una entrada de INICIO y una de CIERRE. El CIERRE registra las escrituras hechas con `[GO]` y el corte desde el que arrancará la siguiente sesión. Un INICIO sin CIERRE delata una sesión interrumpida.
3. **Autoridad (Asimetría Total):**  
   La entidad con autoridad humana es el único sujeto. Decide el rumbo, ejecuta las acciones en producción y asume los costos. Los agentes proponen contrastes y alternativas; jamás deciden.

---

## 6. Cómo se conectan

Ningún agente nombra a otro. Se conectan solo por archivos:

| Archivo | Lo escribe | Lo leen |
|---|---|---|
| `readme/README.md` | Geólogo | Guía, Cartógrafo |
| `readme/MAPA.md` | Geólogo (solo ciclo 1), Cartógrafo | Guía, Cartógrafo, Geólogo (solo como señal de ausencias ya abiertas) |
| `notas_[persona]/` | Guía | Cartógrafo, Guía |
| `cambios/` | Guía | Guía |
| `conocimiento/` | Cartógrafo | Guía, Cartógrafo, Aeróstato |
| `conocimiento_unificado/` + `conocimiento_unificado.MAPA.md` | Aeróstato | Aeróstato; quien decida usarlo como reemplazo |
| `historial/bitacora.md` | Todos (INICIO y CIERRE) | Todos (su último CIERRE propio) |

Para usar el cruce como base: renombrar `conocimiento_unificado/` a `conocimiento/` y usar `conocimiento_unificado.MAPA.md` como `readme/MAPA.md`. Es decisión del humano.

---

## 7. Contratos compartidos (copia canónica)

Cada rol lleva copia literal de los contratos que usa, con la misma etiqueta de versión. Si una copia diverge de esta, la copia está mal. Un agente que encuentra un contrato con otra versión declara la incompatibilidad y no adivina el formato.

### Arranque y salvaguardas [contrato-arranque v1]
- Al arrancar declara en una línea las capacidades del entorno (consola, red, archivos accesibles) y opera solo con esas. Una capacidad ausente se declara; nunca se simula.
- No invoca, espera ni simula otros agentes o herramientas. Los archivos fuera de su perímetro de escritura se leen como evidencia; nunca se modifican.
- Lee el último CIERRE propio en `historial/bitacora.md` para obtener su corte y lee solo la evidencia posterior a ese corte.
- Salvaguardas:
  - Sin bitácora o sin CIERRE propio previo → pasada completa, declarada.
  - INICIO sin CIERRE → la sesión anterior se interrumpió; usa el último corte válido y lo declara.
  - Archivo esperado ausente → ausencia concreta; continúa.
  - Contrato con versión distinta a la propia → declara la incompatibilidad; no adivina el formato.

### Nodo [contrato-nodo v2]
Representación estructural (sin delimitadores anidados):

    ## Nodo: [id]
    - Dominio: [dominio]
    - Posición: [origen: rol(es) | Piso | IA | externa:dominio]
    - Linaje: [ancestros, con operación: evolución | contraposición | caducidad]
    - Bordes salientes: [nodos]
    - Puntas descubiertas:
      - Borde: [descripción concreta]
        Desde: [posición]
        Impacto: [alto | medio | bajo]
        Estado: [abierta | explorada | bloqueada]
    - Versión: [n]
    - Afirmaciones:
      - [afirmación atómica] — [fuente]
    - Tecnologías tocadas: [lista]
    - Anclas técnicas:
      - [tech]: [dominio] — [URL]
      - [tech]: sin verificar → punta
    - Cuerpo:
      [contenido]

Reglas del nodo:
- Afirmaciones: de 3 a 7, atómicas, cada una con su fuente. Se copian literal de una versión a la siguiente; solo se reescriben si la evidencia nueva las contradice o las amplía, citándola. Toda afirmación reescrita sube la Versión.
- Un nodo se re-procesa solo si la evidencia posterior al corte toca sus afirmaciones. Sin evidencia de cambio no equivale a sin cambio: se declara "sin evidencia de cambio".
- Posición externa: el cuerpo declara quién la sostiene, desde dónde, qué gana (o "no inferible") y qué se infiere del informante.
- Posición IA: el cuerpo declara, sin voz subjetiva, rostro (sesgo heredado), dirección de tirada y contraargumento propio contra el consenso.

### Bitácora [contrato-bitácora v2]
Un solo archivo: `historial/bitacora.md`. Dos entradas por sesión; nada más.

INICIO:
- Timestamp: [ISO]
- Ronda: [número]
- Agente: [rol]
- Modo: [nombre]
- Entorno: [capacidades disponibles]
- Corte de partida: [fecha + última referencia por fuente | "sin corte: pasada completa"]
- Insumos: [qué va a leer]

CIERRE:
- Timestamp: [ISO]
- Ronda: [número]
- Agente: [rol]
- Escrituras: [recurso — delta en una línea — GO] o "ninguna"
- Puntas nuevas: [lista] o "ninguna"
- Crecimiento: [opción nueva | validación mutua]
- Corte nuevo: [fecha + última referencia por fuente]

Escribir INICIO y CIERRE no requiere `[GO]`: es trazabilidad, no promoción de estado.

### Checkpoint con autoridad [contrato-checkpoint v2]
Toda escritura fuera de la bitácora es promoción de estado irreversible.

1. **Plan antes de redactar.** Lista de cambios: recurso, sección, qué cambia y por qué, una línea cada uno. Sin redactar contenido. La entidad con autoridad acepta, quita o corrige.
2. **Redacción solo de lo aceptado.**
3. **`[GO]` sobre el delta.** Se muestra el delta, no el archivo completo; el texto completo solo si se pide. La escritura se hace por ediciones puntuales; reescritura completa solo para un archivo nuevo.

Frase canónica: "Voy a [acción] sobre [recurso]. Reversión: [procedimiento o 'no existe']. Posiciones que pasaron el filtro: [lista con origen]. Lo que no veo desde acá: [lista]. ¿GO?"

Sin recurso nombrado, acción nombrada, reversión declarada y posiciones con origen explícito, no hay `[GO]` válido. Un "sí" ambiguo no vale.

Frase de bloqueo: "ACCIÓN IRREVERSIBLE DETECTADA. No ejecuto. Faltan: [lista]. El control vuelve a la entidad con autoridad."

---

## 8. Especificaciones

`Roles/`: `Geologo.md`, `Guia.md`, `Cartografo.md`, `Aerostato.md`. Cada una es autocontenida: funciona sin este README y sin las demás.
