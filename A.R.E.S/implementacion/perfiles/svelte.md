# Perfil — Svelte, Vanilla, GSAP y Electron

El stack concreto de esta implementación. Cambiarlo es reemplazar este archivo; el protocolo no se toca.

## 1. Piezas

- **Svelte 5** — renderer. Compila a JavaScript, sin Virtual DOM. Runes para estado derivado.
- **TypeScript** — `tsc --noEmit` como paso aparte, nunca en el loop de build.
- **Vite** — dev server y HMR de módulo.
- **Vanilla Framework** — CSS por clases, construido con Sass por Canonical. Sin CSS ad-hoc.
- **GSAP** — animación 2D y 3D falso con CSS 3D. Three.js descartado: es otro proyecto.
- **Electron** — contenedor. `electron-vite` para HMR en renderer, restart en main y reload en preload.

## 2. La ventana

El renderer está sandboxeado: sin `fs`, sin `child_process`. Para pedir datos o recibir estado habla con el main por IPC, y el main es el único que habla con el agente.

| Canal | Dirección | Tipo | Para qué |
|---|---|---|---|
| `task:start` | renderer → main | invoke | Lanzar una petición |
| `task:cancel` | renderer → main | invoke | Cancelar |
| `task:list` | renderer → main | invoke | Snapshot inicial |
| `task:update` | main → renderer | send | Snapshots de estado |

Una capa extra de orquestación solo se justifica si el agente tiene que tocar la UI, si hay varios clientes o si la UI es remota. Mientras no, el IPC es el puente. Si algún día hace falta, el estándar existente es **AG-UI**: eventos para interacción agente–usuario, agnóstico de transporte.

## 3. Docs

Los docs se espejan con `httrack` y quedan en disco. No se cargan al contexto: se verifican.

| Pieza | Docs para `httrack` | Notas |
|---|---|---|
| Svelte | HTML estático | — |
| TypeScript | HTML estático | — |
| Vanilla | HTML estático | Fuentes en la carpeta `docs` |
| GSAP | HTML estático (Docusaurus) | — |

Flujo al actualizar: revisar los cambios de GSAP, triangular el resto contra lo que diga GSAP, y fijar versiones compatibles de TypeScript y Svelte.

## 4. Convenciones

- Componentes Svelte pequeños: un `.svelte` de cientos de KB con SVG inline rompe el HMR.
- Estilos con clases del framework, no CSS suelto.
- Animación con timelines para secuencias; CSS 3D para profundidad sutil.
- `tsc --noEmit` al cerrar la tarea, no en cada guardado.

## Fuentes

- Svelte: docs oficiales y `llms.txt` de `svelte.dev`.
- Vanilla: Markdown en la carpeta `docs` del repositorio.
- GSAP: `gsap.com/docs/v3`, servido como HTML estático.
- Electron: documentación oficial de IPC y `contextBridge`.
- AG-UI: `docs.ag-ui.com` para el protocolo de interacción.