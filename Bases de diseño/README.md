# Bases de diseño

**Unidad:** tarea. El agente es el ejecutor; la autoridad es la dueña.

**Qué es:** la base de ideas del proyecto. Se puede extraer del repo, imprimir o compilar. No depende de la implementación.

## Qué no es

No es un manual de SARA, APRIL, DSH ni de una era. Si un documento necesita la implementación para entenderse, no es base: es implementación.

## Qué es una tarea

Una tarea recibe, calcula, emite y responde. Una tarea puede pensar si declara:

`Sistema: propósito | actores | frontera | flujo | feedback | consecuencia`

más su ruta, su cálculo, su consecuencia, su test y su responsable. Sin eso, es ejecución a ciegas.

## Mapa

| Documento | Tareas | Qué hace |
|---|---|---|
| `constitucion.md` | meta | Unidad, lectura, tipos, admisión, mapa y gobierno. |
| `Leyes de Diseño de Instrucciones.md` | instruir | Cómo se escribe una tarea de instrucción. |
| `Principios para alineación de tareas/Conversacional.md` | dialogar, decidir | Cómo se conduce una tarea de diálogo. |
| `Principios para alineación de tareas/Autonomo.md` | ejecutar | Cómo se ejecuta una tarea persistente. |
| `Reglas de escritura.md` | escribir | Cómo se escribe una tarea. |
| `Reglas de mutación.md` | mutar | Cómo se transforma una tarea. |
| `Pruebas/` | evaluar | Rendición y utilidad de una tarea. |
| `A.R.E.S/` | expresar | Cómo se da forma a una tarea de expresión. |
| `Registro.md` | registrar | Cómo se conserva la tarea: memoria, fuentes y testimonio. |
| `Tesis.md` | pensar | Qué es humano y qué no en la base. |

La tarea de cada documento es su interfaz: una norma se activa si su `Aplica a` coincide con una de estas tareas.

## Orden de lectura

1. Este mapa.
2. `constitucion.md`.
3. El documento de la tarea que se va a usar.
4. `Pruebas/` si hay que evaluar.

## Cómo se agrega

Ver `constitucion.md` (`## 7. Agregar`). La lista de pendientes es local (`.contexto/pendientes.md`); no forma parte de la base.

## Portabilidad

La base no depende de `AGENTS.md`, `Instrucciones/`, el instalador ni de la implementación. `AGENTS.md` apunta a este README; este README no apunta a `AGENTS.md`.

Si la base se imprime y sigue teniendo sentido, está bien. Si necesita SARA, APRIL o DSH para entenderse, no es base.
