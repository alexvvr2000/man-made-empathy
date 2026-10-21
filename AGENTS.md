# AGENTS.md — Disparador de tareas

**Tipo:** disparador. Máquina primero. Se cargan las filas que coinciden; el resto no se carga.
**Alcance:** todo artefacto de este repositorio.
**Base:** `./Alineacion de tareas/`.
**Forma:** `./Alineacion de tareas/Derrotero.md`.
**Cuerpo:** `./Alineacion de tareas/Procesos principales/Conversacional.md`, `./Alineacion de tareas/Procesos principales/Autonomo.md` y `./Alineacion de tareas/Procesos principales/Registro.md`; un documento, tres partes (`./faber/constitucion.md` §4).
**Consecuencia:** cada fila carga una tarea; sin fila no hay tarea, y sin tarea no hay respuesta.
**Disparador:** apunta, no contiene (`./faber/constitucion.md`, LEY 1 y LEY 2).

`Sistema: [propósito | frontera | retorno | consecuencia] | Piso: [decisiones] | Vista: [posición | no ve] | Ruta: [filas] | Prueba: [corrida | no corrida] | Cierre: [estado]`

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se piensa o diseña una tarea | `./Alineacion de tareas/README.md`, `./faber/constitucion.md`, `./Alineacion de tareas/Derrotero.md` y el cuerpo | la tarea queda sin sistema |
| Se ejecuta una tarea | `./Alineacion de tareas/README.md` y el cuerpo | la tarea no ocurre |
| Se conserva una tarea | el cuerpo | la tarea no sobrevive |
| Se escribe una tarea | `./Alineacion de tareas/Escritura/Reglas de escritura.md` | la tarea no se lee |
| Se instruye una tarea | `./Alineacion de tareas/Escritura/Leyes de Diseño de Instrucciones.md` | la tarea no se ejecuta sin preguntar |
| Se transforma una tarea | `./Alineacion de tareas/Reglas de mutación.md` | el cambio queda sin origen |
| Se evalúa una tarea | `./Alineacion de tareas/Pruebas/readme.md` | el veredicto no cuenta |
| Se expresa una tarea | `./Alineacion de tareas/A.R.E.S/protocolo.md` | la forma no transfiere |
| Se agrega, revisa o admite una norma | `./faber/constitucion.md` §7 | la norma no entra |
| Se cambia una idea de la base | `./faber/constitucion.md` §8 y el documento cambiado | la implementación deriva sin reporte |
| Se encuentra un `AGENTS.md` anidado | — | no enruta; la raíz manda y el otro pasa a `.tmp` |
| Se emite una respuesta | `./.contexto/notas/indice.md` | la memoria no se escribe y la sesión no sobrevive |
| No coincide y no toca la base | — | responde y cierra |
| No coincide y toca la base | — | `[VACÍO - SIN RUTA]`; pregunta |

**Lectura:** `Sistema: no` con petición que toca la base → `[VACÍO - SIN LECTURA]`; sin `Piso` no se abre; sin `Vista` no se decide; sin `Prueba` ni `Cierre` no se devuelve el control.
