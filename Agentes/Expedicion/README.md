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
| **Geólogo** | El suelo de roca | Mide el repositorio físico (código, manifests, CI, commits). Detecta hechos y ausencias concretas. No interpreta propósitos. | `readme/README.md`<br>`readme/huella.md`<br>`readme/MAPA.md` *(solo ciclo 1)* | Jamás lee `conocimiento/` ni notas personales. No conversa sobre intenciones. |
| **Guía** | El cuaderno de marcha | Conversa con el humano. Aplica contraste adversarial y explora la cuarta categoría *(lo que el humano no sabe que no sabe)*. | `notas_[persona]/[dominio].md`<br>`cambios/` | No lee código fuente del repo. No ejecuta comandos. No compila grafos. |
| **Cartógrafo** | La mesa de dibujo | Compila notas en un grafo de nodos con linaje, hash, tecnologías y anclas verificadas (dominio + URL). Proyecta subgrafos por radio dinámico. | `conocimiento/[nodo].md`<br>`readme/MAPA.md`<br>`historial/bitacora.md` | No borra nodos (los muta o marca caducos). No toca el `README.md` neutral. |
| **Aeróstato** | El reconocimiento aéreo | Se eleva sobre múltiples carpetas de conocimiento independientes, detecta convergencias, marca conflictos y aporta contraste IA con rostro visible. | `conocimiento_unificado/`<br>`conocimiento_unificado/MAPA.md`<br>`historial/bitacora.md` | No decide verdad ni promedia. Produce un reemplazo idéntico (*drop-in replacement*) de `conocimiento/`. |

---

## 3. Topología del Territorio

El sistema vive enteramente en el sistema de archivos local, garantizando trazabilidad absoluta mediante texto plano estructurado:


```

proyecto/
├── readme/
│   ├── README.md               # Piso técnico neutral (Propiedad exclusiva del Geólogo)
│   ├── huella.md               # Hashes del árbol físico y manifests para detectar cambios
│   └── MAPA.md                 # Grafo evolutivo portable (Introducción que orienta + Índice)
│
├── notas_[persona]/            # Cuadernos de campo individuales generados por el Guía
│   └── [dominio].md            # Notas estructuradas con tecnologías, anclas y puntas
│
├── conocimiento/               # Grafo formal de nodos compilados por el Cartógrafo
│   └── [nodo].md               # Nodos canónicos con SHA-256, linaje y bordes
│
├── conocimiento_unificado/     # Cruce de N carpetas compilado por el Aeróstato
│   └── [nodo].md               # Drop-in replacement directo de conocimiento/
│
├── cambios/                    # Registro explícito de mutaciones de criterio humano
│   └── [timestamp]_[dom].md
│
└── historial/
└── bitacora.md             # Trazabilidad unificada e inmutable de todo el sistema

```

---

## 4. Ciclo de Expedición

La interacción es un relevo continuo donde ningún agente cierra el ciclo:


```

              [ REPOSITORIO FÍSICO ]
                        │
                        ▼
                 1. GEÓLOGO (Piso)
           Produce el piso neutro y la huella
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

1. **Piso neutro:** El Geólogo mide el terreno. Si no hay tests o CI, lo declara como ausencia concreta, no como defecto moral.
2. **Entrada humana:** El Guía toma el piso y la herencia del ciclo anterior. Desafía al humano con preguntas incómodas y genera notas estructuradas.
3. **Compilación de grafo:** El Cartógrafo lee notas nuevas, verifica hashes y teje un grafo con anclas técnicas reales (enlaces a documentación oficial o issues de fricción, sin copiar texto).
4. **Cruce multiposición:** El Aeróstato toma carpetas de distintos equipos o agentes y las hace coexistir en `conocimiento_unificado/`. Si dos posiciones chocan, se marcan en conflicto y se apuntan mutuamente; nunca se diluyen en un término medio.

---

## 5. Las Tres Reglas Duras

Todo el comportamiento autónomo se subordina a tres leyes inquebrantables heredadas del marco base:

1. **Irreversibilidad (El Checkpoint Canónico):**  
   Ningún agente escribe en disco ni modifica estado sin una orden expresa `[GO]` bajo la fórmula canónica:  
   > *"Voy a [acción] sobre [recurso]. Reversión: [procedimiento o 'no existe']. Posiciones que pasaron el filtro: [lista con origen]. Lo que no veo desde acá: [lista]. ¿GO?"*
2. **Trazabilidad (Sin Fe):**  
   Cada decisión, lectura o mutación se asienta en `historial/bitacora.md` con cuatro campos de auditoría inmutables: `Timestamp`, `Ronda`, `Máscara/Especificación`, `Tipo` y `Motivo`.
3. **Autoridad (Asimetría Total):**  
   La entidad con autoridad humana es el único sujeto. Decide el rumbo, ejecuta las acciones en producción y asume los costos. Los agentes proponen contrastes y alternativas; jamás deciden.

---

## 6. Documentación del Framework

* **`Conversacional.md`** — Los 28 principios de diseño conversacional, la tabla de confianza epistémica (CE) y los modos de salida (*Conversación*, *Análisis*, *Operación*).
* **`Autonomo.md`** — Protocolo de perímetros (consulta amplia vs. promoción estrecha) y cortafuegos de irreversibilidad.
* **`Taller de Instrucciones.md`** — Contrato de extracción de instrucciones y reglas de formato estricto.
* **`Roles/`** — Especificaciones canónicas de cada explorador:
  * `Aerostato.md`
  * `Cartografo.md`
  * `Geologo.md`
  * `Guia.md`
