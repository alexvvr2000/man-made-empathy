# Perfil de stack — Svelte, Vanilla, GSAP y Electron

> Todo lo que depende del medio elegido. Cambiar de stack es reemplazar este archivo; el método no se toca.

## 2. Stack Frontend

### 2.1 Svelte + TypeScript + Vite

- **Svelte 5**: compila a JavaScript puro, sin Virtual DOM. Proyecto pequeño de una sola página → te quedas con el mejor caso de Svelte (bundle ligero, rendimiento superior).
- **TypeScript**: `tsc --noEmit` como script separado, **nunca en el loop de build**.
- **Vite + esbuild**: dev server en `localhost:5173`, HMR real de módulo con latencias reportadas de **10–20 ms** en Vite frente a 500–1,600 ms de Webpack. Svelte 5 añade Runes (signals) para un DX aún mejor.

**Nota sobre HMR de Svelte**: Existen reportes de que, en versiones específicas de Svelte 5 (5.17.5+), el HMR puede tardar 3 o más segundos dependiendo de cuántas instancias de un componente se hayan renderizado. Es un riesgo conocido y acotado a esa versión; se mitiga fijando la versión o usando un store externo para el estado que se quiera preservar entre recargas.

### 2.2 Vanilla Framework (CSS)

- Framework CSS **extensible, construido con Sass** por el equipo de Canonical (Ubuntu).
- Filosofía: CSS sencillo, poco abstraído, "vieja confiable". Se usa directamente o mediante temas que extienden sus patrones.
- **Documentación**: vive en `https://vanillaframework.io/docs`, y los archivos Markdown fuente están en la carpeta `docs` del repositorio oficial. Esto lo hace **rastreable con `httrack`**.

### 2.3 GSAP (Animación 2D y 3D Falso)

- **GSAP** reemplaza a Anime.js. Es el estándar de la industria para animaciones complejas y secuencias orquestadas; Anime.js es más bien una "navaja suiza ligera" para interacciones rápidas.
- GSAP tiene un sistema de **timelines** con control de offsets preciso, y plugins como MorphSVG, DrawSVG, MotionPath, CustomEase y ScrollTrigger que Anime.js no cubre de serie.
- En escenarios de carga pesada, GSAP suele ser **más fiable y con mejor rendimiento** que Anime.js.

**Decisión sobre 3D**:
- **2D**: GSAP lo cubre de sobra. Es su terreno natural.
- **3D falso (CSS 3D)**: `rotateX/Y`, `translateZ`, `perspective` sobre elementos HTML. GSAP lo maneja de forma nativa. **Vía elegida para la UI.**
- **3D real (Three.js)**: **Descartado**. Implica modelos, texturas, shaders, gestión de GPU — un proyecto aparte que no pertenece a esta engine.

**Por qué 3D falso y no Three.js**:
- CSS 3D **no trabaja realmente en espacio 3D**: hace una transformación 3D y luego proyecta de vuelta a un plano. No hay contabilidad de profundidad real.
- Forzar al DOM a manejar composiciones espaciales complejas suele terminar en **caídas de frames y una estética rígida**; WebGL (Three.js) prioriza rendimiento y renderizado cinematográfico, pero es un monstruo aparte.
- CSS 3D es ideal para **transiciones sutiles en la UI** (tarjetas que giran, paneles que se pliegan, parallax simple). La falta de depth-buffer puede causar glitches en composiciones complejas, pero se acepta porque el uso es acotado.

### 2.4 Electron

- **Electron** carga `http://localhost:5173` en desarrollo. La "ventana en blanco" es solo el contenedor: no te preocupas por menús, notificaciones ni empaquetado.
- **`electron-vite`** (o `vite-plugin-electron`) para:
  - **HMR en el renderer** (tu UI Svelte).
  - **Hot Restart en el main process**: Electron se reinicia solo cuando cambias el código que crea la ventana o gestiona la app.
  - **Hot Reload en el preload**: el puente entre main y renderer se recarga sin reiniciar toda la app.
- `electron-vite` tiene soporte out-of-the-box para **TypeScript, Vue, React, Svelte y SolidJS**.

---


## 3. Docs Offline (Manual, sin Docker, sin scripts)

### 3.1 Estrategia: `httrack` sobre `/docs`

`httrack` permite descargar un sitio web completo a un directorio local, **construyendo recursivamente todos los directorios** y obteniendo HTML, imágenes y otros archivos. Es lo que necesitas para tener los docs en disco.

### 3.2 Estado de cada docset

| Pieza | URL de docs | Docs para `httrack` | Notas |
|---|---|---|
| **Svelte** | `svelte.dev/docs` | ✅ HTML estático | — |
| **TypeScript** | `typescriptlang.org/docs` | ✅ HTML estático | — |
| **Vanilla Framework** | `vanillaframework.io/docs` | ✅ HTML estático | Los fuentes viven en la carpeta `docs` |
| **GSAP** | `gsap.com/docs/v3/` | ✅ HTML estático | — |

### 3.3 Flujo manual al actualizar

1. **Revisar los últimos cambios de GSAP.** Qué cambió, qué rompe, qué se renombró.
2. **Triangular el resto del stack contra lo que dice GSAP.** Verificar qué dice GSAP sobre compatibilidad con Svelte, TypeScript, Vite y CSS. Si hay contradicción con la doc de otra pieza, gana la versión más conservadora hasta que lo pruebes.
3. **Revisar qué versiones de TypeScript y Svelte son compatibles** con lo que tienes instalado. Aplicar cambios y recordar lo importante (lo que va a largo plazo).

---


## 6. Arquitectura de la Engine

### 6.1 Capas

1. **Svelte (renderer)**: UI reactiva. Pinta snapshots de estado.
2. **Electron main**: orquestador de la app. Habla con DSH, reenvía snapshots al renderer. Trabajo pesado va a `worker_threads`/`utilityProcess` o al lado de DSH.
3. **DSH + `dsh-agent-teams`**: capitán + subagentes durables ejecutan el trabajo. Emiten eventos de estado (fase, roster, DAG, mensajes).
4. **`dsh-frontend-tools`**: puente WebSocket loopback para que los agentes invoquen funciones de tu app como herramientas si necesitan consultar/modificar la UI.

### 6.2 Contrato Mínimo de IPC (para cuando llegue el momento)

| Canal | Dirección | Tipo | Para qué |
|---|---|---|---|
| `task:start` | renderer → main | `invoke` | Lanzar una petición al capitán |
| `task:cancel` | renderer → main | `invoke` | Cancelar una tarea en curso |
| `task:list` | renderer → main | `invoke` | Snapshot inicial al montar la UI |
| `task:update` | main → renderer | `send` | Snapshots de estado (fase, roster, DAG, resultado) |

- **Preload**: expone solo esas cuatro funciones vía `contextBridge`. Nada de `fs`, `child_process` ni `require`.
- **Main**: es el único que habla con DSH. El renderer nunca lo ve.
- **Renderer**: Svelte solo refleja el snapshot que le llega. No sabe qué es DSH, ni qué es un subagente, ni qué es un DAG.

### 6.3 Por qué hace falta IPC

La "ventana en blanco" es el contenedor, no la app. Dentro corre Svelte, que está **sandboxeado a propósito**: no tiene `require`, no tiene `fs`, no puede lanzar procesos. Para que la UI lance una tarea o reciba estado, necesita hablar con el main process, que es donde vive el agente. Sin IPC, la ventana sería literalmente blanca.

---


## Fuentes

- **Svelte + Vite HMR**: Latencias de 10–20 ms en Vite frente a 500–1,600 ms de Webpack. Runes (signals) en Svelte 5. Reporte de HMR lento en Svelte 5.17.5+.
- **GSAP vs Anime.js**: GSAP es el estándar para animaciones complejas y secuencias orquestadas; Anime.js es una "navaja suiza ligera". GSAP tiene mejor rendimiento bajo carga pesada. Timelines de GSAP con control de offsets preciso.
- **CSS 3D vs Three.js**: CSS 3D no trabaja realmente en espacio 3D; proyecta de vuelta a un plano y no contabiliza profundidad real. Forzar el DOM a layouts espaciales complejos termina en caídas de frames y estética rígida; WebGL prioriza rendimiento cinematográfico.
- **Vanilla Framework**: Framework CSS extensible construido con Sass por Canonical. Los Markdown de documentación viven en la carpeta `docs` del repositorio.
- **`dsh-agent-teams`**: Convierte la sesión en capitán con subagentes durables, tareas con dependencias, mensajería directa, estado persistente y scheduler automático. Plan antes de ejecutar; solo "Approve & Run" habilita el scheduler. Versión recomendada: DSH `0.2.0-rc.2` + AgentTeams `0.1.22`.
- **`dsh-hypercompact`**: Compactación determinista, zero-LLM, con recall byte-exacto de lo compactado.
- **`electron-vite`**: HMR para renderer, hot reload para main y preload; soporte out-of-the-box para Svelte, TypeScript y más.
- **`httrack`**: Descarga recursiva de sitios web a un directorio local, construyendo todos los directorios y obteniendo HTML, imágenes y otros archivos.
