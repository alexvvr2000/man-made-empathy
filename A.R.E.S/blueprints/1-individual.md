# Blueprint: A.R.E.S. — Orquestación de Mutaciones de S.A.R.A.

## 1. Qué es A.R.E.S.

**A.R.E.S.** = **A**pril–**R**ex **E**ngine for **S**ynthesis.

A.R.E.S. no es un agente ni un template. Es la **capa de orquestación** que une dos mutaciones ya generadas por S.A.R.A. (R.E.X. y A.P.R.I.L.) para que funcionen como un solo sistema.

- **S.A.R.A.** produce las piezas (genera agentes).
- **A.R.E.S.** las conecta (define quién habla con quién, en qué orden y con qué contrato).

Sin S.A.R.A., no hay mutaciones que orquestar. Sin A.R.E.S., tienes dos agentes aislados que no forman un Jarvis.

## 2. Componentes del Sistema

| Componente | Rol | Qué hace | Qué NO hace |
|---|---|---|---|
| **A.P.R.I.L.** (mutación visual/voz) | Capitán (supervisor) | Te escucha, te habla, renderiza la UI. Decide si una petición es local o delegable. | No razona la solución de negocio. No aplica tus skills lógicos. |
| **R.E.X.** (mutación lógica) | Worker durable | Aplica tus principios y skills. Valida el contrato. Devuelve la solución. | No pinta interfaces. No habla directamente contigo. |
| **A.R.E.S.** | Protocolo y equipo | Define el contrato, el flujo y el estado compartido entre APRIL y REX. | No es un tercer agente. No razona ni pinta por sí mismo. |

## 3. Fundamento Técnico: El Orquestador de Equipos

Para implementar A.R.E.S. se utiliza un plugin de orquestación de equipos. La opción recomendada es **`dsh-agent-teams`**, que convierte la sesión actual de DSH en un **capitán** capaz de ensamblar subagentes durables, dividir un objetivo en tareas con dependencias y coordinarlos mediante mensajes directos[reference:11].

- **Miembros durables**: los miembros del equipo son subagentes "continuables" de DSH que pueden ser despertados para turnos de seguimiento enfocados[reference:12].
- **Tareas con dependencias**: las tareas se mueven por estados explícitos y no se pueden reclamar antes de que sus dependencias terminen[reference:13].
- **Mensajería directa**: los miembros envían mensajes durables (mailboxes) directamente al capitán o a otros miembros, sin necesidad de un relay[reference:14].
- **Panel de actividad en vivo**: la UI web combina progreso segmentado, roster colapsable y un DAG interactivo de tareas[reference:15].

**Compatibilidad**: la versión recomendada de `dsh-agent-teams` (0.1.22-rc.1) está alineada con DeepSeek Harness `0.1.7-rc.2`[reference:16]. Verifica tu versión antes de instalar.

## 4. Fases de Implementación de A.R.E.S.

### Fase 0 — Prerrequisitos (S.A.R.A. ya hizo su parte)

Verifica que las dos mutaciones existen y funcionan de forma aislada:

1. **REX existe y funciona solo**: razona con tus skills, no pinta.
2. **APRIL existe y funciona sola**: te escucha (VAD), te habla (TTS) y renderiza tu HTML.
3. **Ambas declaran** `inherits: sara@X.Y.Z` en su YAML y son reproducibles desde S.A.R.A.

**Criterio**: si borras una mutación y la recreas desde S.A.R.A. + su YAML, obtienes el mismo agente. Si no, no está lista para orquestarse.

### Fase 1 — Instalar el Orquestador en el Perfil de APRIL

    dsh plugin --profile april add @nanmicoder/dsh-agent-teams@0.1.22-rc.1

**Compatibilidad**: verifica que tu versión de DSH sea `0.1.7-rc.2` o esté en la matriz de compatibilidad del plugin[reference:17][reference:18]. Una versión desalineada no falla visiblemente: simplemente no expone las herramientas del equipo.

### Fase 2 — Instalar la Capa Visual y de Voz en APRIL

APRIL necesita dos capacidades que S.A.R.A. no le dio (porque son específicas de su mutación):

1. **Renderizado de UI**: `dsh-htmlui`  monta HTML/CSS/JS en modos `inline`, `dock-right`, `float`, `fullscreen` y `background`. La comunicación es bidireccional: el documento llama a `dshHTML.send(...)` y el modelo responde vía SSE, sin polling[reference:19].
       dsh plugin --profile april add github:mostkia/dsh-htmlui

2. **Voz y turn-taking**: `dsh-kitt-voice` está construido Spanish-first, usa Whisper (multilingüe real) y Piper (voces en español locales). Usa **Silero VAD** para distinguir tu voz del ruido de fondo y segmentar por el silencio final, y tiene una **ventana flotante** que se mantiene encima de lo que estés ejecutando[reference:20][reference:21].
       dsh plugin --profile april add kittcat-lab/dsh-kitt-voice

3. **Estructura de ventana (opcional)**: `dsh-full-view` convierte el chat de REX en un HUD flotante en la esquina, dejando el área principal para la UI de APRIL[reference:22].
       dsh plugin --profile april add github:yfwu2020/dsh-full-view

**Criterio**: tras reiniciar Harness, APRIL puede montar tu HTML en `fullscreen`, y el botón de micrófono está disponible.

### Fase 3 — Definir el Equipo A.R.E.S.

En la sesión de APRIL, crea el equipo. `dsh-agent-teams` proporciona un comando de barra (`/agent-teams`) que activa el protocolo de planificación por etapas[reference:23].

1. Invoca `/agent-teams` y describe el objetivo (por ejemplo: "configurar el equipo A.R.E.S. con APRIL como capitán y REX como worker lógico").
2. El plugin convierte la sesión actual en capitán (APRIL).
3. Añade a **REX** como miembro durable. Su `persona` y `toolFilter` deben ser exactamente los que definiste en su mutación de S.A.R.A.
4. **Criterio**: el panel de actividad muestra a APRIL como capitán y a REX como miembro disponible. Los miembros son subagentes continuables que pueden ser despertados para turnos de seguimiento[reference:24].

### Fase 4 — Definir el Contrato de Delegación (Caja Negra)

El contrato es tuyo. A.R.E.S. no impone un formato (JSON, YAML, etc.). Tú defines cómo APRIL formaliza la petición y cómo REX la valida.

**Reglas**:
1. APRIL produce el documento determinista (tu formato) antes de delegar.
2. REX solo acepta ese formato, lo valida contra tu contrato, y devuelve la solución en tu formato de salida.
3. El contrato es **interno**: no se muestra al usuario. La negociación ocurre en el bus del equipo (mensajes durables)[reference:25].

**Qué añadir en cada `persona`**:
- **APRIL**: "Antes de delegar a REX, formaliza la petición en el formato de caja negra. No resuelvas la lógica de negocio. Si la petición es trivial o de interfaz, resuélvela localmente."
- **REX**: "Solo aceptas peticiones en el formato de caja negra. Valida el documento contra el contrato. Si es inválido, devuelve un error estructurado a APRIL pidiendo corrección. No inventes la petición."

**Criterio**: si APRIL envía algo fuera de formato, REX lo rechaza y pide corrección a través del bus.

### Fase 5 — El Flujo de Trabajo de A.R.E.S.

    Tú hablas
        │
        ▼
    A.P.R.I.L. (capitán)
        │ 1. Transcribe (STT con Whisper/Silero VAD)
        │ 2. Clasifica: local o delegable
        ├── local → lo resuelve APRIL (UI, voz)
        └── delegable → formaliza contrato (caja negra)
                              │
                              ▼
                        R.E.X. (worker durable)
                              │ 3. Valida contrato
                              │ 4. Aplica skills y principios
                              │ 5. Devuelve solución
                              ▼
                        A.P.R.I.L. presenta
                              │ 6. Renderiza en UI (dsh-htmlui)
                              │ 7. Lee en voz alta (Piper TTS)
                              ▼
                            Tú

**Puntos críticos**:
- APRIL no razona la solución: solo decide **si** delegar y **cómo** formular la petición.
- REX no habla contigo: su salida vuelve a APRIL.
- El contrato es la frontera: si es inválido, REX lo rechaza y pide corrección.

### Fase 6 — Comunicación y Estado

`dsh-agent-teams` proporciona:
- **Mailboxes durables**: APRIL envía la petición formalizada a REX; REX responde con la solución o un error. Los mensajes sobreviven a reinicios de sesión[reference:26].
- **Tareas con dependencias**: si una petición requiere varios pasos lógicos, REX puede subdividirla (si tiene `delegate`) o APRIL puede orquestar la secuencia. El scheduler compartido reclama atómicamente una tarea lista por miembro inactivo[reference:27].
- **Panel en vivo**: estado de miembros, mensajes y progreso. Úsalo para depurar el flujo.

### Fase 7 — Verificación de la Integración

| # | Prueba | Criterio |
|---|---|---|
| 1 | APRIL recibe voz | El VAD (Silero) detecta tu pausa y transcribe correctamente[reference:28] |
| 2 | APRIL clasifica | Una petición trivial (ej. "hola") no dispara a REX; una petición lógica sí |
| 3 | Contrato válido | REX acepta el formato de caja negra sin errores de validación |
| 4 | REX ejecuta | La solución devuelta aplica tus skills y principios |
| 5 | APRIL presenta | La solución se renderiza en la UI y se lee en voz alta |
| 6 | Round-trip completo | El ciclo voz → contrato → lógica → voz funciona sin intervención manual |
| 7 | Persistencia | Si reinicias la sesión, el equipo y los miembros siguen disponibles |
| 8 | Rechazo de formato | Un contrato inválido → REX pide corrección a través del bus |

## 5. Advertencias

- **No conviertas a APRIL en un razonador.** Si APRIL empieza a resolver la lógica en lugar de delegar, REX queda sin trabajo y pierdes la separación. El `persona` de APRIL debe ser explícito en que su rol es interfaz, no motor.
- **No expongas el contrato al usuario.** El usuario habla con APRIL, no con REX. Si el usuario empieza a ver formatos internos, la experiencia Jarvis se rompe.
- **Empieza con un solo worker.** No añadas más mutaciones al equipo hasta que el flujo APRIL→REX esté estable. Un equipo de dos es suficiente para validar A.R.E.S.
- **La latencia del ciclo completo es normal.** STT + formalización + razonamiento + TTS suma segundos. Diseña la UI de APRIL para mostrar un estado de "procesando" mientras REX trabaja.
- **Verifica versiones antes de instalar.** `dsh-agent-teams` tiene una matriz de compatibilidad con DSH. Una versión desalineada no falla visiblemente: simplemente no expone las herramientas del equipo[reference:29][reference:30].

## 6. Fuentes

- **Orquestación de equipos**: `dsh-agent-teams` convierte la sesión en capitán, ensambla miembros durables, divide tareas con dependencias y coordina por mensajes directos[reference:31][reference:32].
- **Renderizado de UI**: `dsh-htmlui` soporta cinco modos de montaje, comunicación bidireccional vía `dshHTML.send()` y SSE, y no consume contexto (solo pasa un resumen compacto)[reference:33].
- **Voz y turn-taking**: `dsh-kitt-voice` usa Silero VAD para segmentar por silencio, Whisper para STT multilingüe y Piper para TTS en español, con ventana flotante siempre visible[reference:34][reference:35].
- **Estructura de ventana**: `dsh-full-view` convierte el chat en un widget flotante y deja el área principal para la UI de APRIL[reference:36].
- **Arquitectura de plugins**: DSH es un kernel Cordis donde todo (herramientas, skills, UI) es un plugin, lo que permite que las mutaciones y los plugins de A.R.E.S. se carguen dinámicamente[reference:37].
- **Compatibilidad**: la matriz de `dsh-agent-teams` recomienda DSH `0.1.7-rc.2` con AgentTeams `0.1.22-rc.1`[reference:38][reference:39].