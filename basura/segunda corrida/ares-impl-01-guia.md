# Guía de implementación — A.R.E.S. con memoria

> Documento de trabajo, fuera del repositorio. El repositorio publica `idea.md`, `ares-protocolo.md` y `atlas.md`; este documento describe el cómo.
> Entorno: DSH con la API de DeepSeek. Sin modelos locales; cada token se paga.

## 0. Prerrequisitos

- Node LTS y `pnpm`.
- DSH instalado y funcionando con la clave de DeepSeek cargada.
- Git para el repositorio; estas notas quedan fuera.
- Un editor que muestre Markdown.

Criterio: `node -v`, `pnpm -v` y un turno de DSH respondiendo.

## 1. Esqueleto de la app

Tres procesos: `main` (Node), `preload` (puente), `renderer` (Svelte).

1. Inicializar un proyecto con Vite + Svelte + TypeScript.
2. Añadir Electron y `electron-vite` (o montar `main.ts`, `preload.ts` y el renderer a mano; el scaffold es comodidad, no requisito).
3. Scripts: `dev` (levanta Vite y Electron), `build`, `typecheck` con `tsc --noEmit` aparte.

Criterio: `pnpm dev` abre una ventana con el dev server cargado y HMR funcionando.

Errores comunes: `contextIsolation` apagado (no desactivarlo); rutas relativas en `loadURL` (usar `http://localhost:5173` en desarrollo y archivo en build).

## 2. SQLite

- Driver: `better-sqlite3` (síncrono, simple) o `node:sqlite` si la versión de Node lo trae estable. Elegir uno y no mezclar.
- Rutas: `sara/memorias.db` y `sara/trabajo.db`, creadas al arrancar si no existen.
- `PRAGMA journal_mode = WAL;` y `PRAGMA user_version = 1;` como huella del esquema.
- Tabla `memorias` con: `id`, `fecha`, `tipo`, `autor`, `condiciones`, `disparador`, `nivel`, `cierra_en`, `corte`, `vigencia`, `motivo`, `reemplaza`, `cuerpo`. Los cinco obligatorios con `NOT NULL`.
- Tabla `trabajo`: sin esquema fijo. El agente la crea en su primera escritura; el contador de actos vive ahí.
- Índices: `disparador` y `(tipo, fecha)`.

Criterio: la base se crea sola y `user_version` responde.

## 3. Memoria

- **Escribir:** `INSERT` con `autor` en `tipo:nombre`, `disparador` y, si aplica, `reemplaza`. Ancla: `Mem: guardado | corto id 7 | largo id 12`.
- **Leer:** por `disparador` con `LIMIT` y columnas nombradas. Nunca `SELECT *`. Ancla: `Mem: leído | largo: 2 filas por "..."`.
- **Cerrar tarea:** fila `cierre` con fin, decisiones con su `id`, pendientes con su `id` y siguiente paso; `reemplaza` al cierre anterior; vaciar el corto.
- **Checkpoint:** contador de actos en `trabajo`; al llegar a N (10 por referencia) se genera el mapa **desde una consulta**, no de memoria.

Criterio: al reabrir, el agente lee el último `cierre` y continúa sin que se le explique nada.

## 4. IPC

Cuatro canales, y ninguno más:

| Canal | Dirección | Tipo |
|---|---|---|
| `task:start` | renderer → main | invoke |
| `task:cancel` | renderer → main | invoke |
| `task:list` | renderer → main | invoke |
| `task:update` | main → renderer | send |

- `preload` expone solo esas funciones por `contextBridge`.
- `main` es el único que habla con el agente.
- Tipar los payloads en un archivo compartido.

Criterio: lanzar una petición devuelve un snapshot a la UI.

## 5. UI mínima

- Pintar el snapshot: fase, progreso, resultado, error.
- Sin estilos, sin animación y sin estados decorativos.

Criterio: se ve el ciclo completo sin recargar.

## 6. Docs locales

- `httrack` con directorio de salida, profundidad limitada y filtro a HTML y assets. Las banderas exactas se confirman con `httrack --help` antes de fijarlas en un script.
- Excluir enlaces externos y URLs con parámetros: son la mayor fuente de basura.
- Calcular SHA-256 de cada documento al guardarlo y anotarlo en un índice.

Criterio: existe `docs/` con los archivos y un índice de ruta → hash.

## 7. Verificación tipo Kestrel

- Antes de admitir una cita: `indexOf` de la subcadena en el texto guardado.
- Rechazar citas de menos de 24 caracteres.
- Comparar el hash antes de usar el documento; si no coincide, todas las citas basadas en él se rechazan.
- Coste: cero tokens de modelo; lo hace código.

Criterio: una cita válida pasa, una inventada se rechaza, un doc alterado invalida sus citas.

## 8. APRIL mínima

- Persona: cómo se presenta.
- Registro: legible por defecto; nativo solo si se declara y transfiere.
- La presentación consume lo que el agente resolvió; no lo reinterpreta.

Criterio: la misma respuesta se emite en registro legible y se declara cuál se usó.

## 9. Ahorro de tokens (DSH + DeepSeek)

1. **Caché de prefijo.** DeepSeek cachea automáticamente, pero **solo prefijos idénticos desde el token 0**. Orden fijo: kernel y esquema primero, petición y resultados al final. No reordenar dentro de una tarea. Medir `prompt_cache_hit_tokens` y `prompt_cache_miss_tokens`: si el hit es cero, el prefijo se rompe.
2. **Subagente para exploración.** Leer archivos e iterar va en un contexto aparte; vuelve un resumen con tope y punteros.
3. **Enrutamiento.** Modelo barato para clasificar, extraer y formatear; el caro para composición y verificación.
4. **Tope por herramienta.** Máximo N tokens por salida más puntero al resto.

Criterio: el costo por turno no crece con la longitud de la conversación.

## 10. Pruebas de aceptación

- **Amnesia:** sesión nueva reconstruye la última tarea desde el `cierre`.
- **Transferencia:** otra instancia reproduce una forma nativa leyendo solo el registro.
- **Costo:** mapa + anclas + una lectura por turno, sin importar cuántos turnos lleve.

## 11. Orden de trabajo

1. Esqueleto → 2. SQLite → 3. Memoria (escribir/leer) → 4. Cierre y checkpoint → 5. IPC → 6. UI → 7. Docs → 8. Verificación → 9. Ahorro → 10. APRIL → 11. Pruebas.

No abrir la fase siguiente hasta que la anterior pase su criterio. Una fase que no cabe en una sesión está mal cortada.

## 12. Errores conocidos

- Meter la petición del usuario antes del kernel: mata la caché de prefijo.
- `SELECT *` en `memorias`: arrastra cuerpos completos al contexto.
- Recargar el renderer y perder estado: el snapshot debe venir del main, no de la memoria del componente.
- Escribir el mapa desde lo que el agente recuerda en vez de consultarlo.
- Cargar docs al contexto «para que sepa»: es lo que el diseño evita.
- Cambiar el esquema sin subir `user_version`: la siguiente sesión no detecta el cambio.
