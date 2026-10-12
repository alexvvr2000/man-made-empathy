# Framework Expedición — Manual del Operador

Sistema de aceleración relacional y unificación de conocimiento técnico estructurado bajo un principio de desacoplamiento estricto: los archivos Markdown son la fuente de verdad editable a mano, y SQLite opera como un acelerador relacional descartable.

---

## 1. Principio Fundamental: Markdown como Verdad, SQLite como Acelerador

* **Fuente Canónica (`Source of Truth`):** El sistema de archivos local (`.md`). Toda nota, análisis o mapa es editable con cualquier editor de texto plano, inspeccionable con utilidades del sistema (`grep`, `cat`) y versionable directamente en Git.
* **Índice y Caché (`expedicion.db`):** SQLite no almacena información propietaria. Funciona como un motor relacional descartable que indexa hashes, dependencias y proposiciones para que los agentes realicen cruces en milisegundos sin abrir decenas de archivos Markdown completos. Si se corrompe o se borra (`rm expedicion.db`), el repositorio se regenera por completo a partir de los archivos `.md`.
* **El Operador en el Centro:** La entidad con autoridad valida o edita el conocimiento y toma las decisiones arquitectónicas. Los agentes no asumen autoridad técnica ni ejecutan promociones destructivas sin validación explícita.

---

## 2. Topografía del Espacio de Trabajo

La suite delimita su accionar a la carpeta `expedicion/`, tratando la raíz del proyecto auditado (`../`) como un terreno de solo lectura:

```text
raiz_del_proyecto/              # Terreno físico auditado (../)
│
└── expedicion/                 # Períperto operativo positivo
    ├── expedicion.db           # Caché relacional SQLite (descartable)
    ├── schema.sql              # Esquema SQL del acelerador
    ├── readme/                 # Documentación técnica pública (LEVANTAMIENTO, README, MAPA)
    ├── notas_[participante]/   # Notas estructuradas de campo (Guía)
    ├── cambios/                # Historial de mutaciones de posición
    ├── conocimiento/           # Nodos de conocimiento consolidados (Cartógrafo)
    └── conocimiento_unificado/ # Unificación de múltiples repositorios (Aeróstato)
```

---

## 3. Catálogo de Agentes

* **Topógrafo:** Ejecuta el barrido físico e instrumental de la raíz del proyecto (`../`) sin emitir juicios de valor. Puebla la tabla `manifiesto` y redacta `expedicion/readme/LEVANTAMIENTO.md`.
* **Geólogo:** Sintetiza el propósito, la arquitectura observable y las ausencias técnicas del terreno a partir del manifiesto y los archivos de configuración (`package.json`, `pyproject.toml`, etc.), redactando `expedicion/readme/README.md`.
* **Guía:** Conduce el diálogo operativo con el interlocutor, detectando tensiones y extrayendo notas estructuradas en `expedicion/notas_[participante]/[dominio].md` sin psicologizar.
* **Cartógrafo:** Compila las notas en nodos interconectados dentro de `expedicion/conocimiento/[nodo].md`, actualiza el índice `MAPA.md` y proyecta subgrafos dinámicos bajo demanda mediante la caché relacional.
* **Aeróstato:** Cruza múltiples carpetas de conocimiento, unifica convergencias y preserva las contradicciones en nodos independientes con contraargumentos técnicos contrastados, generando `expedicion/conocimiento_unificado/`.

---

## 4. El Flujo Operativo de Principio a Fin

```text
Terreno (../) ──► [ TOPÓGRAFO ] ──► LEVANTAMIENTO.md + manifiesto
                         │
                         ▼
                  [ GEÓLOGO ]   ──► README.md + semilla MAPA.md
                         │
                         ▼
Operador      ──► [ GUÍA ]      ──► notas_*/[dominio].md + tabla puntas
                         │
                         ▼
notas/*.md    ──► [ CARTÓGRAFO ] ──► conocimiento/*.md + MAPA.md
                         │
                         ▼
conocimiento_N ─► [ AERÓSTATO ]  ──► conocimiento_unificado/ (Arbitraje adversarial)
```

1. **Inspección Física:** Se inicializa la base de datos con el esquema y se ejecuta al **Topógrafo** para inventariar el terreno.
2. **Generación del Piso:** Se invoca al **Geólogo** para construir la documentación base de entrada a partir de los metadatos físicos.
3. **Diálogo y Notas:** Se utiliza al **Guía** para resolver incógnitas técnicas y registrar notas estructuradas de campo.
4. **Compilación de Nodos:** Se activa al **Cartógrafo** para sincronizar la caché relacional y compilar los nodos de conocimiento y el mapa general.
5. **Unificación (Opcional):** Se emplea al **Aeróstato** para cruzar repositorios de conocimiento heterogéneos y arbitrar divergencias sin promediar posturas.

---

## 5. Anexo Técnico: Recuperación y Mantenimiento

* **Edición Humana Libre:** Cualquier archivo `.md` en `notas/` o `conocimiento/` puede editarse a mano. En la siguiente ejecución, los agentes detectan el cambio de estampa temporal (`mtime` / hash) y sincronizan automáticamente las tablas de SQLite.
* **Reconstrucción ante Desastres:** Si el archivo `expedicion.db` se corrompe o elimina, la recuperación toma dos pasos:
    1. Re-inicializar el esquema: `sqlite3 expedicion/expedicion.db < expedicion/schema.sql`.
    2. Ejecutar al **Topógrafo** y al **Cartógrafo** para re-parsear el sistema de archivos y poblar íntegramente la caché relacional sin pérdida de información histórica.