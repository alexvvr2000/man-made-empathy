# Blueprint: ARES Worker Exchange — Intercambio de REX por Agentes Especializados

## PARTE 0: DEFINICIONES Y CONCEPTO

### 0.1. Qué es el Worker Exchange

En los blueprints anteriores, REX era el único worker de A.R.E.S. APRIL siempre delegaba en él. Eso funciona para tareas de razonamiento general, pero no para tareas especializadas (revisión de código, análisis de datos, investigación, etc.).

**Worker Exchange** significa que APRIL ya no tiene un worker fijo, sino un **roster de workers** (un catálogo de roles). Según la intención del usuario, APRIL selecciona el worker adecuado: REX para razonamiento general, un Code Reviewer para código, un Data Analyst para SQL, etc.

- **S.A.R.A.** sigue siendo la madre: genera cada worker como una mutación (o como un rol del roster).
- **A.P.R.I.L.** sigue siendo el capitán: pero ahora su decisión incluye *qué worker* usar, no solo *si delegar*.
- **A.R.E.S.** sigue siendo el sistema: el equipo o el roster que contiene a los workers.
- **R.E.X.** deja de ser el único worker: pasa a ser **un rol más** del roster, el genérico de razonamiento.

### 0.2. Dos implementaciones posibles

| Enfoque | Plugin | Cómo funciona | Cuándo usarlo |
|---|---|---|---|
| **Roster de roles** | `dsh-subagent-library` o `dsh-roles-zeta` | APRIL tiene una herramienta `delegate` y un catálogo de roles. Elige un rol y le pasa la tarea. | Intercambio rápido, workers bajo demanda, sin equipo persistente. |
| **Equipo multi-miembro** | `dsh-agent-teams` | APRIL agrega varios miembros al equipo (uno por rol) y asigna tareas. | Trabajo paralelo, estado compartido, workers persistentes. |

**Recomendación**: si lo que quieres es **intercambiar** a REX por otro agente según la tarea, el **roster de roles** es más ligero y directo. Si quieres que varios workers trabajen **simultáneamente** en partes distintas, usa el equipo multi-miembro.

---

## PARTE 1: IMPLEMENTACIÓN CON ROSTER DE ROLES (la vía directa)

### 1.1. Instalar el plugin de roster

Dos opciones verificadas:

- **`dsh-subagent-library`**: roster persistente de subagentes nombrados. El modelo usa `list_subagents` para ver el catálogo y `delegate` para elegir uno por `library_id`[reference:0].
- **`dsh-roles-zeta`**: una carpeta de archivos de rol. El modelo usa una herramienta `delegate` que recibe el nombre del rol; el archivo de rol define persona, ruta de modelo, esfuerzo de razonamiento y superficie de herramientas[reference:1].

Instala uno de los dos en el perfil de APRIL:

    dsh plugin --profile april add dsh-subagent-library

o

    dsh plugin --profile april add dsh-roles-zeta

### 1.2. Definir el roster de workers

Cada worker es un rol con su propia configuración. El roster debe contener al menos:

| `id` del rol | `description` (para que APRIL elija) | `persona` (resumen) | `model` / `provider` | Herramientas |
|---|---|---|---|---|
| **rex** | Razonamiento general, principios y skills base | "Eres R.E.X. Aplicas los principios y skills del usuario." | El que ya usas | Lectura, skills |
| **code-reviewer** | Revisión de código, regresiones, edge cases | "Eres un revisor independiente. Priorizas corrección y regresiones." | Opcional: otro modelo | Solo lectura (`read`, `grep`, `glob`) |
| **data-analyst** | Análisis de datos, SQL, métricas | "Eres un analista de datos. Escribes y validas consultas." | Opcional: modelo con contexto largo | Lectura, SQL |
| **researcher** | Búsqueda web, síntesis de información | "Eres un investigador. Buscas, citas y sintetizas." | Opcional: modelo con web | `web_search`, `web_fetch` |

**Con `dsh-subagent-library`**: cada rol es un archivo YAML en `~/.dsh/subagents/`. Ejemplo para `code-reviewer.yaml`:

    description: Revisión independiente de código, regresiones y edge cases
    provider: deepseek-official
    model: deepseek-flash
    persona: |
      Eres un revisor independiente. Priorizas corrección, regresiones,
      edge cases y concurrencia. No modificas código; solo reportas.
    toolFilter:
      deny: [write, edit, subagent, delegate]
    backgroundMode: continuable

**Con `dsh-roles-zeta`**: cada rol es un archivo Markdown en `$DSH_HOME/agents/`. Ejemplo para `code-reviewer.md`:

    ---
    id: code-reviewer
    when: Revisión independiente de código, regresiones y edge cases.
    route: deepseek-official/deepseek-flash
    effort: high
    allow: [read, glob, grep]
    ---
    Eres un revisor independiente. Priorizas corrección, regresiones,
    edge cases y concurrencia. No modificas código; solo reportas.

### 1.3. Adaptar el contrato de caja negra para incluir el rol

El contrato que APRIL pasa al worker ahora debe incluir un campo que indique **qué rol se necesita**. Tú defines el formato; el blueprint no impone JSON.

Ejemplo conceptual (no es un formato obligatorio):

    # Documento de caja negra (ejemplo)
    required_role: "code-reviewer"
    intent: "revisar_commit"
    parameters: { commit: "a1b2c3" }
    conversation_context: [ ... ]

**Regla**: APRIL decide el rol basándose en la intención del usuario. Si la intención es ambigua, puede preguntar antes de delegar. REX (o el rol elegido) solo acepta el contrato si el `required_role` coincide con su propio `id`.

### 1.4. Ajustar el `persona` de APRIL

En el `persona` de APRIL, añade la instrucción de selección:

> "Tienes un roster de workers. Antes de delegar, inspecciona el roster (`list_subagents` o el catálogo de roles) y selecciona el worker cuyo `description` mejor coincida con la intención del usuario. Si ningún worker coincide, usa `rex` como genérico. Formaliza el contrato de caja negra incluyendo el `required_role`."

### 1.5. Flujo con roster

    Tú hablas
        │
        ▼
    A.P.R.I.L. (capitán)
        │ 1. Transcribe (STT)
        │ 2. Clasifica la intención
        │ 3. Inspecciona el roster
        │ 4. Selecciona el worker (rex, code-reviewer, etc.)
        │ 5. Formaliza el contrato con required_role
        ▼
    Worker seleccionado (ej. code-reviewer)
        │ 6. Valida el contrato (required_role == su id)
        │ 7. Aplica su persona y herramientas
        │ 8. Devuelve la solución
        ▼
    A.P.R.I.L. presenta (UI + voz)

**Criterio**: si pides "revisa este commit", APRIL debe seleccionar `code-reviewer`, no `rex`. Si pides "analiza este problema general", debe seleccionar `rex`.

---

## PARTE 2: IMPLEMENTACIÓN CON EQUIPO MULTI-MIEMBRO (para trabajo paralelo)

### 2.1. Agregar múltiples miembros a A.R.E.S.

Con `dsh-agent-teams`, APRIL puede agregar **varios miembros** al equipo, cada uno con su propio rol, modelo y herramientas[reference:2][reference:3].

El comando de equipo permite agregar miembros con `provider` y `model` opcionales. Si no se especifican, el miembro hereda el modelo de APRIL[reference:4][reference:5].

**Ejemplo de equipo**:

| Miembro | Rol | Modelo | Herramientas |
|---|---|---|---|
| **REX** | Razonamiento general | El de APRIL | Lectura, skills |
| **Code Reviewer** | Revisión de código | `deepseek-flash` | Solo lectura |
| **Data Analyst** | Análisis SQL | Modelo con contexto largo | Lectura, SQL |

### 2.2. Cómo APRIL asigna tareas a cada miembro

APRIL (capitán) recibe la tarea, inspecciona la intención y usa `agent_teams_add_member` o asigna la tarea al miembro correspondiente mediante el bus del equipo[reference:6].

**Ventaja**: los miembros son durables y pueden trabajar en paralelo. **Desventaja**: el equipo es más pesado y requiere más configuración que un roster.

---

## PARTE 3: CÓMO DECIDE APRIL QUÉ WORKER USAR

### 3.1. Señales para la selección

APRIL debe basar la selección en la **intención** del usuario, no en palabras clave rígidas. Señales típicas:

| Intención | Worker recomendado |
|---|---|
| "Revisa este código / commit" | `code-reviewer` |
| "Analiza estos datos / escribe una consulta" | `data-analyst` |
| "Busca información sobre X" | `researcher` |
| "Resuelve este problema / aplica mis principios" | `rex` (genérico) |

### 3.2. Fallback a REX

Si la intención no coincide claramente con ningún worker especializado, APRIL debe usar **REX** como genérico. REX sigue existiendo en el roster; no se elimina, solo deja de ser el único.

### 3.3. Ambigüedad

Si la intención es ambigua (por ejemplo, "revisa esto" sin especificar si es código o datos), APRIL debe **preguntar** antes de delegar, no adivinar.

---

## PARTE 4: VERIFICACIÓN DEL WORKER EXCHANGE

| # | Prueba | Criterio |
|---|---|---|
| 1 | El roster está cargado | `list_subagents` (o el catálogo de roles) muestra `rex`, `code-reviewer`, etc. |
| 2 | APRIL selecciona por intención | "Revisa este commit" → `code-reviewer`; "analiza el problema" → `rex` |
| 3 | El contrato incluye `required_role` | El worker recibe el rol y lo valida |
| 4 | Fallback a REX | Intención ambigua o no especializada → `rex` |
| 5 | Ambigüedad manejada | APRIL pregunta antes de delegar si no está claro |
| 6 | Intercambio sin reescribir A.R.E.S. | Cambiar un worker no requiere rehacer el blueprint del equipo |
| 7 | (Equipo multi-miembro) Asignación correcta | Cada tarea va al miembro adecuado |

---

## PARTE 5: ADVERTENCIAS

- **No elimines a REX del roster**. Sigue siendo el worker genérico y el fallback natural. Si lo quitas, te quedas sin worker para tareas no especializadas.
- **El contrato sigue siendo interno**. El usuario no ve el `required_role` ni el formato de caja negra. Solo ve que APRIL responde de forma distinta según la tarea.
- **La selección no es perfecta**. Al principio, APRIL puede equivocarse al elegir el worker. Ajusta las `description` del roster para que sean claras y distintas entre sí.
- **Verifica la compatibilidad de versiones**. `dsh-subagent-library` apunta a DSH `0.2.0-rc.2`; `dsh-roles-zeta` y `dsh-agent-teams` tienen sus propias matrices de compatibilidad. Una versión desalineada no falla visiblemente: simplemente no expone las herramientas.
- **Empieza con dos workers**. REX + un especialista (por ejemplo, `code-reviewer`). Valida la selección antes de añadir más roles.

---

## PARTE 6: FUENTES

- **`dsh-subagent-library`**: roster persistente de subagentes nombrados; el modelo usa `list_subagents` para ver el catálogo y `delegate` por `library_id`[reference:7]. Cada entrada define modelo, persona, filtro de herramientas y modo de ejecución[reference:8].
- **`dsh-roles-zeta`**: herramienta `delegate` sobre una carpeta de archivos de rol; cada archivo define persona, ruta de modelo, esfuerzo y herramientas[reference:9]. Los roles se cargan desde `$DSH_HOME/agents` y se editan desde la página de settings[reference:10].
- **`dsh-agent-teams`**: el capitán agrega miembros específicos por rol, respaldados por subagentes continuables[reference:11]. Los miembros pueden tener `provider` y `model` propios; si no se especifican, heredan el del capitán[reference:12].
- **`dsh-plugin-subagent-director`**: alternativa con plantillas de rol y selección de proveedor/modelo por subagente[reference:13].
- **`dsh-subagent-pro`**: alternativa con enrutamiento por rol y cadena de fallback de cuatro niveles[reference:14].