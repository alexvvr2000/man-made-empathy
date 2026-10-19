# Atlas — intenciones a formas

**Unidad:** tarea.
**Aplica a:** expresar
**Lector:** humano (investigador). El índice declara su lector: humano para decisión, máquina para transferencia.

> Índice caliente. Las docs no se leen: se verifican contra `verifica`.

## Cómo se lee una fila

`intención | capa | primitiva | ejemplo mínimo | límite | compone | verifica`

- **intención:** en palabras de quien pide, no de la API.
- **primitiva:** el mecanismo del stack, o del medio.
- **límite:** cuándo NO usarla. Sin esto, la fila queda como corazonada.
- **compone:** con qué otras filas se combina.
- **verifica:** `ruta-del-doc#ancla` + hash del documento. Sin ruta y hash no hay fila: queda como hipótesis.

## Reglas

1. Se busca por intención, nunca por nombre de método.
2. Tope de ~25 filas por capa. Si pasa, hay duplicados.
3. Crece por fallo: se agrega cuando una tarea no se resolvió con lo existente.
4. Nada se edita: se reemplaza.
5. Una fila sin `límite` o sin `verifica` no entra al índice; va a `hipótesis`.

## Estado

**Índice: vacío (0 filas).** No hay docs espejados aún, así que no hay hash, así que nada cumple la regla 5. El atlas nace vacío a propósito: se llena cuando aparece el primer espejo.

## Franjas

### Hipótesis

`Hipótesis: [intención] | propuesta: [forma] | prueba: [cómo se falsifica] | estado: abierta`

Candidatas no verificadas. Se intentan; si funcionan y se consigue su hash, se promueven a fila. Si no, se descartan y se anota el descarte.

### Opaco

`Opaco: [firma] | efecto: [lo que produce] | invariante: [lo que se conserva] | transfiere: [sí/no] | compone: [...]`

Formas nacidas del ejecutor que quizá no traduzcan. Pasan si una instancia limpia las reproduce leyendo solo el registro. Si no transfieren ni componen, pasan a ruido y se descartan.

## Capas e intenciones

| Capa | Intenciones |
|---|---|
| Estructura y estado | mostrar/ocultar, derivar, compartir estado, persistir, cargar datos, rutas |
| Estilo | layout, responsive, tema, tipografía, espaciado, foco |
| Movimiento | entrar, salir, secuenciar, escalonar, scroll, transformar estado |
| Plataforma | pedir datos, actualizar UI, eventos del sistema, ventana |
| Docs | traer un docset, actualizar, filtrar ruido |
| Memoria | verificar cita, decidir corto/largo, consolidar |

## Propuestas iniciales — ninguna indexada

Las seis quedan como `hipótesis` hasta que haya docs espejados y su hash. La columna `verifica` dice qué doc habría que espejar para poder promoverlas.

| Intención | Capa | Primitiva | Ejemplo mínimo | Límite | Compone | Verifica (pendiente) |
|---|---|---|---|---|---|---|
| que no se pierda al recargar | estado | store persistido | `writable` + `localStorage` | no para datos sensibles | con «cargar datos» | doc de Svelte: stores |
| que no se rompa en móvil | estilo | grid + container queries | `grid` + `@container` | no para una sola columna | con «tema» | doc de CSS: grid |
| que entre desde abajo | movimiento | tween de entrada | `gsap.from(el, {y:24, opacity:0})` | listas largas: virtualizar | con «escalonar» | doc de GSAP: `from` |
| que la UI pida datos | plataforma | canal invoke | `ipcRenderer.invoke('task:start')` | no para estado masivo | con «actualizar UI» | doc de Electron: IPC |
| traer un docset | docs | espejo local | `httrack` con profundidad y filtros | sitios con login o JS obligatorio | con «verificar cita» | doc de httrack: opciones |
| recordar una decisión | memoria | fila de largo | `INSERT` con `disparador` y `vigencia` | no para actividad | con «consolidar» | esquema de memorias |
