# AGENTS.md — Disparador de tareas

**Tipo:** disparador. Máquina primero. Se cargan las filas que coinciden; el resto no se carga.
**Alcance:** todo artefacto de este repositorio.
**Base:** `./Bases de diseño/`.
**Cuerpo:** `./Bases de diseño/Principios para alineación de tareas/Conversacional.md`, `./Bases de diseño/Principios para alineación de tareas/Autonomo.md` y `./Bases de diseño/Registro.md`; un documento, tres partes (`./Bases de diseño/constitucion.md` §4).
**Consecuencia:** cada fila carga una tarea; sin fila no hay tarea, y sin tarea no hay respuesta.
**Disparador:** apunta, no contiene (`./Bases de diseño/constitucion.md`, LEY 1 y LEY 2).

`Ruta: [filas] | Documento: [doc] | Sistema: [sí|no] | Consecuencia: [qué se rompe]`

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se piensa o diseña una tarea | `./Bases de diseño/README.md`, `./Bases de diseño/constitucion.md` y el cuerpo | la tarea queda sin sistema |
| Se ejecuta una tarea | `./Bases de diseño/README.md` y el cuerpo | la tarea no ocurre |
| Se conserva una tarea | el cuerpo | la tarea no sobrevive |
| Se escribe una tarea | `./Bases de diseño/Reglas de escritura.md` | la tarea no se lee |
| Se instruye una tarea | `./Bases de diseño/Leyes de Diseño de Instrucciones.md` | la tarea no se ejecuta sin preguntar |
| Se transforma una tarea | `./Bases de diseño/Reglas de mutación.md` | el cambio queda sin origen |
| Se evalúa una tarea | `./Bases de diseño/Pruebas/readme.md` | el veredicto no cuenta |
| Se expresa una tarea | `./Bases de diseño/A.R.E.S/protocolo.md` | la forma no transfiere |
| Se agrega, revisa o admite una norma | `./Bases de diseño/constitucion.md` §7 | la norma no entra |
| Se cambia una idea de la base | `./Bases de diseño/constitucion.md` §8 y el documento cambiado | la implementación deriva sin reporte |
| Se encuentra un `AGENTS.md` anidado | — | no enruta; la raíz manda y el otro pasa a `.tmp` |
| Se emite una respuesta | `./notas/README.md` | la nota no se escribe y la sesión no sobrevive |
| No coincide y no toca la base | — | responde y cierra |
| No coincide y toca la base | — | `[VACÍO - SIN RUTA]`; pregunta |

**Lectura:** `Sistema: no` con petición que toca la base → `[VACÍO - SIN LECTURA]`; no se responde.
