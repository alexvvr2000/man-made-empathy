# Método — expresión, registros y proceso

> Parte agnóstica al medio y al stack. El stack concreto vive en `perfiles/svelte.md`; lo que cambia por memoria, en `memoria/con-memoria.md` y `memoria/sin-memoria.md`.

## 1. Visión

Una engine de interfaz personal en Electron con **un solo agente capitán** que hace lo que le pidas —front, research, lo que sea— delegando en **subagentes durables** vía `dsh-agent-teams`, mientras la UI en **Svelte** refleja el estado en tiempo real. Todo son ideas y arquitectura; no hay código de producción.

---


## Kestrel — verificación de citas

Las dos variantes usan Kestrel; lo que cambia es cuánto provecho sacan de él.

- **Qué hace**: antes de admitir una cita, comprueba que el texto citado existe literalmente en la fuente guardada (`String.indexOf`). Si la cita tiene menos de **24 caracteres**, se rechaza.
- **Integridad**: los documentos se hashean con **SHA-256** al obtenerlos; si el texto ya no coincide con su hash, todas las citas que descansan en él se rechazan.
- **Coste**: cero tokens de modelo en la verificación; la hace código determinista.
- **`npm run rag:index`**: descartado; Kestrel no indexa, verifica por subcadena y hash.

## 5. Orquestación

### 5.1 `dsh-agent-teams` — El Capitán y sus Subagentes

`dsh-agent-teams` convierte la sesión actual de DSH en un **capitán** que puede:

- **Ensamblar subagentes durables** (miembros continuables que se pueden despertar para turnos de seguimiento).
- **Dividir un objetivo en tareas con dependencias explícitas**: las tareas pasan por estados definidos y no se pueden reclamar hasta que sus dependencias terminen.
- **Coordinar el trabajo mediante mensajes directos** entre miembros y el capitán.
- **Reutilización y takeover seguro**: los miembros inactivos reclaman la siguiente tarea lista; la reasignación revoca intentos obsoletos; la recuperación en frío reintenta intentos huérfanos.
- **Panel de actividad en vivo**: la Web UI combina progreso segmentado, roster colapsable y un DAG de tareas interactivo.

**Características clave**:
- Es **opt-in**: el plugin solo crea un equipo cuando tú lo pides explícitamente. Las sesiones ordinarias de DSH no se convierten en equipo por defecto.
- **Plan antes de ejecutar**: el flujo normal de `/agent-teams` primero prepara un roster y un DAG **sin lanzar nada**. Solo "Approve & Run" habilita el scheduler; cada miembro arranca con su primera tarea lista.
- **Versión recomendada**: DSH `0.2.0-rc.2` + AgentTeams `0.1.22` (el host sigue siendo un RC).

### 5.2 Un Solo Capitán, Múltiples Realidades

- **Una sesión en modo Team**: actúa como capitán, ensambla subagentes durables, define tareas con dependencias y coordina el trabajo.
- **Otras sesiones normales**: no entran en modo Team, no tienen capitán ni subagentes de equipo, y el agente hace lo que le pidas con las herramientas estándar de DSH.
- La separación es real a nivel de sesión y workspace: el estado del equipo se guarda bajo `<workspace>/.agent-teams/`, y las sesiones que no están en modo Team no leen ni escriben ahí.

### 5.3 Skill de UI

- **La skill define el flujo**: qué pasos seguir para crear/actualizar UI, qué archivos tocar, qué convenciones respetar, cómo validar el resultado.
- **El capitán la invoca cuando detecta que la tarea es de UI**. No necesita tener el conocimiento de UI en su contexto permanente; lo carga cuando lo usa.
- **La descripción de la skill es lo que hace que el capitán la invoque solo**. Invierte tiempo en la descripción, no en el código de la skill.

### 5.4 Gestión de Contexto del Capitán

- **Aislamiento**: cada subagente de `dsh-agent-teams` es un agente raíz independiente con su propia sesión y ventana de contexto. El trabajo pesado (leer archivos, iterar, explorar) vive en ellos; el capitán solo recibe resúmenes.
- **Compactación determinista**: `dsh-hypercompact` compacta el historial antiguo **localmente, en milisegundos, sin llamada extra al modelo**, y permite recuperar exactamente cualquier salida de herramienta con la herramienta `recall`. Es ideal para el capitán: mantiene su contexto pequeño sin pagar tokens de resumen.
- **Herramientas de contexto**: `context_compact` (acorta el contexto en su sitio), `context_rollover` (pasa a un contexto nuevo sin reiniciarse), `context_checkpoint`/`context_status` (consultar o volver a un punto anterior).
- **DAG como presupuesto**: toda tarea que implique leer muchos archivos, iterar o explorar va a un subagente. El capitán se queda solo con tareas de **decisión y consolidación**, que son baratas en tokens.

### 5.5 Diseño del Capitán — Qué Hace y Qué No Hace

El capitán no es "el agente de UI". Es el agente que **decide**, **delega** y **consolida**. Su comportamiento se define en tres capas: instrucción de sistema, criterios de decisión y política de delegación.

**Qué hace el capitán**:

- **Recibe la petición** del main process de Electron (vía DSH) y la interpreta: ¿es una tarea de UI? ¿es research? ¿es una mezcla?
- **Decide si invoca una skill**. Si la tarea es de UI, invoca la skill de UI. Si es de otro dominio, usa las herramientas estándar o invoca la skill correspondiente.
- **Arma el DAG**. Traduce el objetivo en tareas con dependencias explícitas, decidiendo qué va a un subagente y qué se queda él.
- **Delega la ejecución**. Asigna cada tarea pesada a un subagente durable. No ejecuta él mismo el trabajo que implica leer archivos, iterar o explorar.
- **Consolida resultados**. Recibe los resúmenes de los subagentes, decide si el resultado cumple el criterio, y notifica a Svelte.
- **Gestiona su contexto**. Cuando acumula muchas iteraciones de coordinación, invoca `context_compact` o `context_rollover`. Cuando necesita recordar un patrón, consulta la memoria de largo plazo con `LIMIT`.

**Qué no hace el capitán**:

- **No escribe código de UI él mismo**. Eso lo hace el subagente que ejecuta la skill de UI.
- **No lee archivos de exploración**. Eso vive en el contexto de los subagentes.
- **No mantiene el historial completo de cada tarea**. Solo recibe resúmenes.
- **No inventa el DAG desde cero cada vez**. Sigue reglas de orquestación predefinidas (ver 5.7).

**Instrucción de sistema del capitán** (esqueleto):

```text
Eres el capitán de una engine de interfaz. Tu trabajo es decidir, delegar y consolidar.

1. Cuando recibas una petición, clasifícala: UI, research, mixta, u otra.
2. Si es de UI, invoca la skill `ui-builder` y asigna la ejecución a un subagente.
3. Si es de research, asigna la ejecución a un subagente con las herramientas estándar.
4. Toda tarea que implique leer archivos, iterar o explorar va a un subagente.
   Tú solo te quedas con tareas de decisión y consolidación.
5. Cuando acumules más de N llamadas a herramientas, usa `context_compact`.
6. Cuando necesites recordar un patrón o decisión, consulta la memoria de largo plazo
   con `SELECT` proyectado + `LIMIT 200`.
7. Cuando el resultado de un subagente cumpla el criterio, notifica a Svelte con un snapshot.
8. Si el resultado no cumple, reasigna la tarea o corrige el DAG.
9. Solo creas subagentes de roles que existan en el marco definido (ver 5.8).
   No inventas roles ni concedes herramientas fuera de lo autorizado.
```

**Criterios de decisión**:

| Situación | Acción del capitán |
|---|---|
| Petición de UI simple (un componente) | Invoca skill de UI, asigna a un subagente, espera resumen |
| Petición de UI compleja (varios componentes con dependencias) | Arma DAG con tareas de UI en paralelo, asigna cada una a un subagente |
| Petición de research | Asigna a un subagente con herramientas estándar, espera hallazgo |
| Petición mixta (UI + research) | Arma DAG con research como dependencia de la tarea de UI |
| Resultado de subagente no cumple | Reasigna o corrige el DAG; no re-ejecuta él mismo |
| Contexto del capitán > 80% | Invoca `context_compact` antes de continuar |

### 5.6 Diseño de la Skill de UI — El Flujo Procedural

La skill de UI es el "cómo". Es texto procedural que el subagente lee y ejecuta paso a paso. Su descripción debe ser **específica y accionable** para que el capitán la invoque solo.

**Descripción de la skill** (lo que el capitán lee):

```text
Skill `ui-builder`: Úsala cuando la tarea implique crear, modificar o eliminar
componentes Svelte, ajustar estilos con Vanilla Framework, o animar elementos
con GSAP (2D o 3D falso con CSS 3D). Incluye validación de HMR y convenciones
del proyecto. No la uses para research, configuración de build, ni tareas de
backend.
```

**Flujo de la skill** (lo que el subagente ejecuta):

1. **Leer el estado actual**: qué componente se va a modificar, qué archivos existen, qué convenciones sigue el proyecto.
2. **Planificar el cambio**: qué archivos tocar, qué clases de Vanilla usar, qué animaciones GSAP añadir (si aplica).
3. **Escribir el código**: modificar el `.svelte`, añadir estilos, añadir animaciones.
4. **Validar HMR**: verificar que el cambio se refleja en la ventana de Electron sin recargar. Si el HMR falla, revisar que el componente no sea demasiado grande (~550 KB con SVG inline puede fallar) y que no haya errores de sintaxis.
5. **Validar tipos**: ejecutar `tsc --noEmit` sobre los archivos tocados (no en el loop, solo al cerrar la tarea).
6. **Devolver resumen**: qué se cambió, qué se validó, qué quedó pendiente.

**Convenciones del proyecto** (lo que la skill asume):

- Componentes Svelte pequeños: evitar archivos `.svelte` de más de ~550 KB con SVG inline grande (rompe HMR de forma intermitente).
- Estilos con Vanilla Framework: usar las clases del framework, no CSS ad-hoc.
- Animaciones con GSAP: usar timelines para secuencias, CSS 3D para profundidad sutil, no Three.js.
- TypeScript: `tsc --noEmit` al cerrar la tarea, no en cada guardado.

### 5.7 Reglas de Orquestación — Cómo se Traduce el Objetivo en un DAG

El capitán no escribe el DAG a mano cada vez. Sigue reglas predefinidas que traducen el objetivo en tareas con dependencias.

**Regla 1 — Toda exploración va a un subagente**:
Si la tarea implica leer archivos, buscar en docs, iterar sobre código o explorar alternativas, esa tarea va a un subagente. El capitán no la ejecuta.

**Regla 2 — Toda ejecución de UI va a un subagente con la skill de UI**:
Si la tarea implica escribir o modificar código de UI, va a un subagente que invoca la skill `ui-builder`.

**Regla 3 — El capitán solo decide y consolida**:
Las tareas del capitán son: clasificar la petición, armar el DAG, asignar tareas, recibir resúmenes, decidir si el resultado cumple, notificar a Svelte. Nada más.

**Regla 4 — Dependencias explícitas**:
Si una tarea de UI depende de un research previo (ej. "verificar la API de GSAP antes de animar"), el research es una tarea que debe completarse antes. El DAG lo refleja: la tarea de UI no se puede reclamar hasta que el research termine.

**Regla 5 — Paralelismo cuando no hay dependencias**:
Si dos tareas no tienen dependencias entre sí (ej. "actualizar Header" y "actualizar Footer"), se lanzan en paralelo como dos subagentes independientes.

**Regla 6 — Reintento con corrección**:
Si un subagente falla o el resultado no cumple, el capitán reasigna la tarea o corrige el DAG. No re-ejecuta él mismo el trabajo.

**Ejemplo de DAG** (petición: "actualiza el Header con una animación GSAP"):

```text
[research: verificar API de GSAP para timelines]  (subagente, sin skill de UI)
        ↓ (dependencia)
[UI: modificar Header.svelte con animación]       (subagente, con skill ui-builder)
        ↓ (dependencia)
[validación: tsc --noEmit + HMR check]            (subagente, con skill ui-builder)
        ↓
[consolidación: capitán notifica a Svelte]
```

**Ejemplo de DAG** (petición: "actualiza Header y Footer en paralelo"):

```text
[UI: modificar Header.svelte]   (subagente A, skill ui-builder)
[UI: modificar Footer.svelte]   (subagente B, skill ui-builder)
        ↓ (ambas terminan)
[consolidación: capitán notifica a Svelte]
```

### 5.8 Marco de Permisos y Roles — El Capitán Ejecuta, Tú Defines los Planos

**Nota crítica**: el capitán crea subagentes con su criterio, pero ese criterio opera **siempre dentro del marco que tú configuras**. No es "el capitán hace lo que quiere"; es "el capitán es el jefe de obra; tú eres el arquitecto". Tú dibujas los planos (roles, permisos, límites); él decide cómo ejecutar la obra día a día (a quién asignar qué, en qué orden, cuándo parar).

**Qué defines tú (tu "antojo")**:

- **Roles y permisos**: al crear el equipo o definir el roster. Qué rol existe, qué skill invoca, qué herramientas tiene, qué servidores MCP puede usar.
- **Instrucción de sistema del capitán**: las reglas de decisión (5.5). Ahí le dices cuándo delegar, cuándo compactar, cuándo consultar memoria, y que **solo crea subagentes de roles que existan en el marco**.
- **Reglas de orquestación**: 5.7. Ahí defines cómo traduce un objetivo en DAG.
- **Límites duros**: concurrencia máxima, presupuesto de contexto, número de reintentos, techo de llamadas a subagentes por ejecución.

**Qué decide el capitán dentro del marco**:

- Cuándo crear un subagente y de qué rol (de los que tú definiste).
- Con qué tarea y en qué orden.
- Cuántos en paralelo (hasta el límite que tú pusiste).
- Cuándo reasignar o corregir el DAG.

**Qué NO puede hacer el capitán**:

- Inventar un rol que no definiste.
- Conceder herramientas o skills que no autorizaste a un rol.
- Dar acceso a servidores MCP fuera de la allow-list del rol.
- Superar los límites duros de concurrencia, presupuesto o reintentos.
- Ignorar la política de mínimo privilegio: cada subagente tiene **solo** las skills y herramientas que su rol necesita, no las del capitán ni las de otros roles.

**Principio de mínimo privilegio (por qué importa)**:

En `dsh-agent-teams`, a diferencia de un flujo padre/subagente tradicional donde el hijo hereda todo el catálogo del padre, cada miembro lleva su **propia lista global de herramientas permitidas**. Esto permite tener, por ejemplo:

| Rol | Skills | Herramientas | Puede escribir archivos |
|---|---|---|---|
| **UI** | `ui-builder` | edición de archivos, GSAP, Vanilla | ✅ |
| **Research** | — | búsqueda en docs, lectura | ❌ |
| **Validación** | `ui-builder` (solo validación) | `tsc --noEmit`, HMR check | ❌ |

El capitán decide a quién asignar cada tarea **basándose en las capacidades que tú definiste para cada rol**. Si un subagente de research intenta escribir, no puede: su allow-list no lo incluye. Esa es la garantía.

**Dónde ajustas el marco**:

- **Roles y permisos**: configuración del equipo / roster.
- **Instrucción de sistema del capitán**: sección 5.5, regla 9 ("solo creas subagentes de roles que existan en el marco").
- **Reglas de orquestación**: sección 5.7.
- **Límites duros**: concurrencia, presupuesto, reintentos, techo de subagentes.

**En una frase**: si quieres cambiar el comportamiento, **cambias los planos (roles, permisos, instrucción de sistema), no le pides al capitán que "sea más listo"**. El capitán ejecuta dentro de tu marco; no lo redefine.

---


## 7. Riesgos Anotados

| Riesgo | Detalle | Mitigación |
|---|---|---|
| **Electron main es Node de un solo hilo** | Trabajo pesado bloquea la orquestación y la UI | Mover a `worker_threads`/`utilityProcess` o al lado de DSH |
| **Tormenta de eventos IPC** | Un `send` por microactualización satura el canal | Agrupar en snapshots, no deltas uno a uno |
| **Condiciones de carrera en UI** | Dos eventos casi simultáneos pintan estados contradictorios | Cada tarea con `id` + `version`/`timestamp`; descartar lo viejo en el renderer |
| **La descripción de la skill importa más que su código** | Si es vaga, el capitán no la invoca | Invertir tiempo en una descripción específica y accionable |
| **HMR de Svelte en versiones específicas** | Reportes de 3+ segundos en Svelte 5.17.5+ | Fijar versión o usar store externo para preservar estado |
| **CSS 3D no tiene depth-buffer real** | Puede glitchear en composiciones complejas (cubo con caras mal ordenadas) | Uso acotado a transiciones sutiles, no geometría con volumen |
| **El capitán acumula contexto** | Muchas iteraciones de coordinación llenan su ventana | `context_compact`/`context_rollover` + delegación proactiva |
| **Subagentes que no cumplen** | El resultado no cumple el criterio | Reasignar o corregir el DAG; el capitán no re-ejecuta |

---


## 8. Descartado en el Camino

- **Docker completo** (imágenes, compose, `down -v`): complejidad innecesaria para docs estáticos.
- **`dsh-htmlui` y `dsh-preview-plugin` del camino crítico**: la UI es tuya; Electron carga el dev server directamente.
- **`dsh-library` y `rtk` en camino caliente**: consumen tokens o no están diseñados para SQL.
- **Anime.js** (por GSAP): GSAP es más robusto para animaciones complejas y tiene docs rastreables.
- **Tailwind** (por Vanilla Framework): Vanilla tiene `/docs` rastreable y es menos opinionado.
- **Vue** (por Svelte): Svelte ofrece HMR más rápido y bundles más ligeros para proyectos pequeños.
- **Agentes separados por dominio** (por skill + capitán): un solo capitán decide cuándo usar cada skill.
- **3D real con Three.js**: un proyecto aparte (modelos, texturas, shaders, GPU).

---


## 9. Pendiente para Cuando se Implemente

- **Contrato de estado** (`TaskState`: id, status, fase, progreso, subagentes, resultado parcial).
- **Redacción final de la skill de UI**: descripción accionable + flujo procedural + convenciones del proyecto (ver 5.6).
- **Redacción final de la instrucción de sistema del capitán**: criterios de decisión + política de delegación + política de contexto (ver 5.5).
- **Verificar `httrack` sobre GSAP**: si el sitio bloquea el rastreo, usar el repositorio de GitHub o un espejo alternativo.
- **Definir el umbral de `context_compact`**: cuántas llamadas a herramientas antes de compactar (ej. N=20).

---

