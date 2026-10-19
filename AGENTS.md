# AGENTS.md — Disparador de tareas

**Tipo:** disparador. Máquina primero. Se carga la fila que coincide; el resto no se carga.
**Alcance:** todo artefacto de este repositorio.
**Base:** `./Bases de diseño/`.
**Consecuencia:** esto no es un token; cada fila carga una tarea que puede cambiar archivos, agentes o reglas. Sin ruta, la respuesta no se emite.
**Disparador:** apunta, no contiene — ver `./Bases de diseño/constitucion.md` (LEY 1 y LEY 2).

`Ruta: [fila] | Documento: [doc] | Sistema: [sí|no] | Consecuencia: [qué se rompe]`

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se piensa o diseña una tarea | `./Bases de diseño/README.md` y `./Bases de diseño/constitucion.md` | la tarea queda sin sistema |
| Se ejecuta una tarea | `./Bases de diseño/README.md` y el documento de la tarea | la tarea no ocurre |
| Se agrega, revisa o admite una norma | `./Bases de diseño/constitucion.md` | la norma no entra |
| Se cambia una idea de la base | `./Bases de diseño/constitucion.md` §8 y el documento cambiado | la implementación deriva sin reporte |
| Se transforma una tarea | `./Bases de diseño/Reglas de mutación.md` | el cambio queda sin origen |
| Se escribe una tarea | `./Bases de diseño/Reglas de escritura.md` | la tarea no se lee |
| Se evalúa una tarea | `./Bases de diseño/Pruebas/readme.md` | el veredicto no cuenta |
| Se expresa una tarea | `./Bases de diseño/A.R.E.S/protocolo.md` | la forma no transfiere |
| Se ejecuta SARA o el runtime de la era | `./Agentes/Proyecto S.A.R.A/Componentes/AGENTS.md.tmp` | la operación no ocurre |
| Se encuentra un `AGENTS.md` anidado | — | no enruta; la raíz manda y el otro pasa a `.tmp` |
| Falta contexto de la autoridad o del estado del proyecto | `./.contexto/notas.md` | se repite lo ya dicho o lo ya descartado |
| No coincide y no toca la base | — | responde y cierra |
| No coincide y toca la base | — | `[VACÍO - SIN RUTA]`; pregunta |

**Lectura:** si `Sistema: no` y la petición toca la base, se emite `[VACÍO - SIN LECTURA]`; no se responde.
