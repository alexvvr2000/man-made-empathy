# Blueprint: A.R.E.S. Multi-Usuario — Equipo Multiagente con Diarización de Hablantes

## PARTE 0: DEFINICIONES Y DIFERENCIA CON LA VERSIÓN SINGLE-USER

### 0.1. Qué cambia respecto a la versión de un solo hablante

La versión anterior asumía que solo tú hablabas. El VAD (como el Silero de `dsh-kitt-voice`) detectaba "voz humana" y segmentaba por silencio, pero no distinguía entre personas. Si había otra voz en el entorno, se transcribía como si fueras tú.

En la versión multi-usuario, el sistema debe:

1. **Identificar al hablante** (diarización o *voiceprint*): saber que la voz A es de la persona 1 y la voz B es de la persona 2.
2. **Inyectar el hablante en el contexto**: el texto que llega a APRIL (y luego a REX) debe llevar una marca de quién lo dijo, por ejemplo `[Speaker: Alice] <texto>`.
3. **Gestionar turnos entre múltiples personas**: si dos personas hablan a la vez o se interrumpen, el sistema debe decidir qué hacer (descartar, priorizar al hablante autorizado, o pedir aclaración).

### 0.2. Componentes (los mismos nombres, roles ampliados)

- **S.A.R.A.**: la madre universal. Genera las mutaciones. No cambia.
- **A.P.R.I.L.**: sigue siendo el capitán. Ahora su entrada de voz no es un solo stream, sino un stream **etiquetado por hablante**. Sigue sin razonar la solución de negocio.
- **R.E.X.**: sigue siendo el worker lógico. Ahora recibe en el contrato no solo la intención, sino también **quién la emitió** y el contexto de la conversación multi-turno.
- **A.R.E.S.**: el equipo. El protocolo de equipo (`dsh-agent-teams`) no cambia, pero el flujo de entrada sí.

---

## PARTE 1: ELECCIÓN DEL CANAL DE VOZ MULTI-USUARIO

`dsh-kitt-voice` **no soporta multi-hablante**. Su VAD segmenta por silencio, pero no identifica personas. Para multi-usuario necesitas una de estas dos rutas:

### Ruta A: `@xp1024/dsh-voice-gateway` (voiceprint filtering)

Este plugin está diseñado explícitamente para **声纹过滤与多发言人管理 (voiceprint enrollment & multi-speaker management)**. Permite:

- **Registrar la huella de voz** de cada persona autorizada mediante un asistente guiado.
- **Filtrar voces no autorizadas**: si alguien que no está registrado habla, el audio se descarta y no llega al agente.
- **Inyectar el hablante en el prompt**: el resultado del STT se formatea como `[<speaker>] <text>` y se inyecta en la sesión activa.

**Limitación**: no hace diarización completa (separar hablantes no registrados); solo filtra contra un conjunto de *voiceprints* registrados. Si necesitas distinguir entre personas **no registradas**, necesitas la Ruta B.

**Instalación**:
    dsh plugin --profile april add @xp1024/dsh-voice-gateway

**Requisito**: necesita un **gateway daemon** local (`local-voice-gateway`) corriendo en el puerto 8765 (WebSocket/REST). Sin él, el plugin no funciona.

### Ruta B: Voxtral Mini Transcribe Realtime (diarización completa)

Si el entorno tiene personas que **no vas a registrar previamente** (por ejemplo, una reunión con invitados), necesitas un motor de STT con **speaker diarization** nativa. **Voxtral Mini Transcribe Realtime 2602** (de Mistral, disponible vía Opper) ofrece:

- Transcripción en streaming con **13 idiomas**.
- **Diarización de hablantes** integrada.
- Modelo de 4B, desplegable en el borde.

**Cómo se integra en DSH**: DSH permite sustituir el modelo de STT por un proveedor externo. Configuras Voxtral como proveedor de transcripción en el perfil de APRIL, y el resultado del STT llega a la sesión ya etiquetado con el hablante.

**Ventaja**: no requiere registro previo de voces; distingue hablantes en tiempo real.
**Desventaja**: depende de un servicio externo (Opper/Mistral) y tiene coste por uso.

### Cuál elegir para tu caso

| Escenario | Ruta recomendada |
|---|---|
| Solo tú y un grupo pequeño de personas **conocidas** (familia, equipo fijo) | **Ruta A** (`dsh-voice-gateway`): registras sus voces y filtras intrusos. |
| Entorno abierto, personas **no registradas**, reuniones con invitados | **Ruta B** (Voxtral): diarización completa sin registro previo. |
| Quieres máxima privacidad y todo local | **Ruta A**: el gateway y el STT pueden ser locales (Piper/Whisper). |

---

## PARTE 2: PRERREQUISITOS

Antes de montar el equipo multi-usuario:

1. **S.A.R.A. ya generó a REX y APRIL** como mutaciones independientes y funcionan en single-user.
2. **El equipo A.R.E.S. ya está montado** con `dsh-agent-teams`: APRIL como capitán, REX como miembro durable.
3. **El canal de voz multi-usuario está instalado y funcionando**: puedes ver en la consola que llegan transcripciones con etiqueta de hablante (`[Alice] hola`, `[Bob] qué tal`).

**Criterio**: si en single-user el flujo voz → contrato → lógica → voz funciona, y en multi-user ves las etiquetas de hablante en el log, estás listo para conectar ambos.

---

## PARTE 3: ADAPTAR EL CONTRATO DE DELEGACIÓN (CAJA NEGRA) PARA MÚLTIPLES HABLANTES

El contrato de caja negra que definiste para single-user sigue siendo válido, pero debe **ampliarse** para incluir el hablante y el contexto multi-turno.

### 3.1. Lo que APRIL debe añadir al contrato

APRIL recibe del canal de voz un texto etiquetado (`[Speaker: Alice] <texto>`). Antes de delegar a REX, debe:

1. **Extraer el hablante** del texto.
2. **Mantener un contexto de conversación**: si Alice dijo algo y Bob responde, el contrato debe incluir el historial reciente de quién dijo qué.
3. **Formalizar el documento** en tu formato de caja negra, añadiendo los campos de hablante y contexto.

**Ejemplo conceptual** (tú defines el formato real):
    # Documento de caja negra (ejemplo)
    speaker: "Alice"
    intent: "solicitar_analisis"
    parameters: { ... }
    conversation_context:
      - speaker: "Alice", text: "necesito el reporte de ventas"
      - speaker: "Bob", text: "¿de qué mes?"
      - speaker: "Alice", text: "del último trimestre"

### 3.2. Lo que REX debe hacer con el hablante

- **Validar que el hablante está autorizado** (si usas `dsh-voice-gateway`, el filtrado ya lo hizo, pero REX puede verificarlo de nuevo contra una lista de confianza).
- **Usar el contexto multi-turno** para resolver referencias ambiguas ("el reporte", "eso", "lo que dijo Bob").
- **Devolver la solución etiquetada** con el hablante al que va dirigida, para que APRIL sepa a quién responder (si hay varias personas presentes).

### 3.3. Regla de oro

El contrato **sigue siendo interno**. El usuario no ve el JSON ni el formato de caja negra. Solo ve la interfaz de APRIL y escucha sus respuestas. La diferencia es que ahora APRIL puede dirigirse a personas distintas: "Alice, aquí tienes el reporte" / "Bob, la respuesta a tu pregunta es...".

---

## PARTE 4: EL FLUJO MULTI-USUARIO

    [Persona A habla]  [Persona B habla]
           │                  │
           ▼                  ▼
    ┌─────────────────────────────────┐
    │  Canal de voz multi-usuario     │
    │  (voice-gateway o Voxtral)     │
    │  → [Speaker: A] texto          │
    │  → [Speaker: B] texto          │
    └──────────────┬──────────────────┘
                   │
                   ▼
    ┌─────────────────────────────────┐
    │  A.P.R.I.L. (capitán)           │
    │  1. Recibe texto etiquetado     │
    │  2. Mantiene contexto de quién  │
    │     dijo qué                    │
    │  3. Formaliza contrato con      │
    │     hablante + contexto         │
    └──────────────┬──────────────────┘
                   │
                   ▼
    ┌─────────────────────────────────┐
    │  R.E.X. (worker durable)        │
    │  1. Valida contrato             │
    │  2. Usa contexto multi-turno    │
    │  3. Aplica skills               │
    │  4. Devuelve solución etiquetada│
    └──────────────┬──────────────────┘
                   │
                   ▼
    ┌─────────────────────────────────┐
    │  A.P.R.I.L. presenta            │
    │  - Renderiza en UI              │
    │  - Habla dirigiéndose a la      │
    │    persona correcta             │
    └─────────────────────────────────┘

**Puntos críticos del flujo multi-usuario**:

- **Turn-taking entre personas**: si A y B hablan a la vez, el canal de voz debe decidir qué hacer. `dsh-voice-gateway` filtra por *voiceprint*; Voxtral puede separar las voces. Si no hay separación, el sistema recibe un texto mezclado y debe pedir aclaración.
- **Memoria de conversación por hablante**: REX necesita saber que "el reporte" que pidió Alice es distinto del "reporte" que pidió Bob. El contrato debe incluir el historial reciente por hablante.
- **Respuesta dirigida**: si hay varias personas, APRIL debe decidir a quién responde. Lo natural es responder al último hablante, pero si la pregunta era para otra persona, el contrato debe reflejarlo.

---

## PARTE 5: CONFIGURACIÓN DEL EQUIPO (`dsh-agent-teams`) SIN CAMBIOS ESTRUCTURALES

El protocolo de equipo no cambia: APRIL sigue siendo capitán, REX sigue siendo miembro durable. Lo que cambia es **qué recibe REX en el contrato** y **cómo APRIL gestiona la conversación**.

- **Mailboxes**: siguen siendo el canal entre APRIL y REX. Los mensajes ahora incluyen el hablante y el contexto.
- **Tareas con dependencias**: si una petición de Alice requiere una respuesta de Bob antes de continuar, APRIL puede crear una tarea bloqueada por la respuesta de Bob.
- **Panel en vivo**: sigue mostrando el estado del equipo. Útil para ver qué hablante está activo en cada momento.

**Límites del equipo** (por defecto): `maxMembers` 8, `memberMaxDepth` 1. Para multi-usuario no necesitas más miembros; los hablantes son **entradas**, no miembros del equipo. A.R.E.S. sigue siendo un equipo de dos (APRIL + REX).

---

## PARTE 6: VERIFICACIÓN DEL SISTEMA MULTI-USUARIO

| # | Prueba | Criterio |
|---|---|---|
| 1 | Canal de voz etiqueta hablantes | El log muestra `[Speaker: A]` y `[Speaker: B]` en transcripciones separadas |
| 2 | Filtrado de voces no autorizadas (Ruta A) | Una voz no registrada no genera transcripción |
| 3 | Diarización sin registro (Ruta B) | Dos personas no registradas se distinguen correctamente |
| 4 | Contrato incluye hablante | El documento de caja negra que recibe REX tiene el campo `speaker` |
| 5 | Contexto multi-turno | REX resuelve correctamente una referencia ("el reporte") usando el historial de hablante |
| 6 | Respuesta dirigida | APRIL responde a la persona correcta, no siempre al último que habló |
| 7 | Interrupciones manejadas | Si dos personas hablan a la vez, el sistema no se cuelga y pide aclaración si es necesario |
| 8 | Persistencia | Al reiniciar, el equipo y el contexto de hablantes se mantienen |

---

## PARTE 7: ADVERTENCIAS ESPECÍFICAS PARA MULTI-USUARIO

- **`dsh-kitt-voice` no sirve para multi-usuario**. Su VAD segmenta por silencio, pero no identifica personas. Si lo usas en un entorno con varias voces, todas se transcribirán como si fueran la misma persona.
- **El filtrado por *voiceprint* no es diarización completa**. `dsh-voice-gateway` filtra contra voces registradas, pero no separa hablantes desconocidos. Si necesitas distinguir entre dos personas no registradas, necesitas Voxtral u otro motor con diarización.
- **La latencia aumenta en multi-usuario**. La diarización y el filtrado añaden procesamiento. El ciclo completo (voz → contrato → lógica → voz) será más lento que en single-user. Diseña la UI de APRIL para mostrar "procesando" con el nombre del hablante.
- **El contrato de caja negra debe incluir el hablante**. Si REX recibe solo el texto sin saber quién lo dijo, no puede mantener contexto multi-turno ni dirigir la respuesta correctamente.
- **Empieza con dos hablantes**. No intentes gestionar cinco personas a la vez desde el día uno. Valida el flujo con dos voces registradas (Ruta A) o dos hablantes claramente diferenciados (Ruta B), y luego escala.

---

## PARTE 8: FUENTES

- **`dsh-agent-teams`**: protocolo de equipo capitán + miembros durables, mailboxes, tareas con dependencias. Compatible con DSH `0.2.0-rc.2` y AgentTeams `0.1.22`/`0.1.23`.
- **`@xp1024/dsh-voice-gateway`**: plugin de voz con *voiceprint enrollment & filtering* y multi-speaker management. Inyecta `[<speaker>] <text>` en la sesión. Requiere gateway daemon local en puerto 8765.
- **Voxtral Mini Transcribe Realtime 2602** (vía Opper): STT en streaming con speaker diarization, 13 idiomas, modelo 4B. Integrable como proveedor de transcripción externo en DSH.
- **`dsh-kitt-voice`**: plugin de voz single-user (Whisper + Piper + Silero VAD). **No soporta multi-hablante**; se menciona solo para contraste.
- **A2UI**: especificación de interfaces generativas que soporta *multi-party rooms* vía WebRTC, relevante si en el futuro quieres que varias personas interactúen con la misma superficie de UI.