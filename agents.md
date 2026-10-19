# agents.md — Disparador de ruta

**Tipo:** disparador. Máquina primero. Se carga la fila que coincide; el resto no se carga.
**Alcance:** todo artefacto de este repositorio.
**Base:** `./Bases de diseño/`.
**Consecuencia:** esto no es un token; cada fila carga una norma que puede cambiar archivos, agentes o reglas. Sin ruta, la respuesta no se emite.
**Disparador:** apunta, no contiene — ver `./Bases de diseño/constitucion.md` (LEY 1 y LEY 2).

`Ruta: [fila] | Documento: [doc] | Sistema: [sí|no] | Consecuencia: [qué se rompe]`

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se escribe o edita una idea | `./Bases de diseño/README.md` | la idea queda sin mapa |
| Se agrega, revisa o admite una norma | `./Bases de diseño/constitucion.md` | la norma no entra |
| Se fusiona o retira una regla | `./Bases de diseño/constitucion.md` | el cambio queda sin dueño |
| Se crea o muta un artefacto | `./Bases de diseño/Reglas de mutación.md` | el cambio queda sin origen |
| Se crea una instrucción | `./Bases de diseño/Reglas de escritura.md` y `./Instrucciones/instruccion-de-autoridad.md` | la instrucción no se ejecuta |
| Se ejecuta SARA u opera un agente | `./Agentes/Proyecto S.A.R.A/Componentes/agents.md` | la operación no ocurre |
| Se audita cumplimiento o se evalúa rendición/utilidad | `./Bases de diseño/constitucion.md` y `./Bases de diseño/Pruebas/readme.md` | el veredicto no cuenta |
| Se revisa consistencia | `./Bases de diseño/constitucion.md` | el cambio queda sin verificación |
| No coincide y no toca la base | — | responde y cierra |
| No coincide y toca la base | — | `[VACÍO - SIN RUTA]`; pregunta |

**Lectura:** si `Sistema: no` y la petición toca la base, se emite `[VACÍO - SIN LECTURA]`; no se responde.
