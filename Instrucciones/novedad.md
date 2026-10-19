# Novedad

**Tipo:** instrucción.
**Disparador:** un cambio aprobado en un meta-repo, o el llamado de la autoridad máxima.
**Carga:** bajo demanda. No se carga en cada turno.
**Lector:** máquina (arnés).

## Alcance

Solo meta-repos, o cuando la autoridad máxima lo manda a llamar. Fuera de eso: `[VACÍO - NO META]` y se cierra.

## Permisos

- **`reporte`** — lee, captura y registra; no toca leyes, principios ni reglas.
- **`meta-cambios`** — con `Autorización: sí`, puede editar el documento dueño; test, evidencia externa y registro. Sin autorización, cae a `reporte`.

## Operaciones

| Operación | Qué hace | Alcance | Triangulación |
|---|---|---|---|
| `normal` | captura y triangula un candidato nuevo | el candidato | internet + usuario |
| `meta comprobación` | audita normas existentes (manual) | subconjunto indicado | internet + consistencia; sin usuario |
| `meta-corroborar` | corrobora un candidato de cualquier lado | el candidato | internet solo; sin usuario; una corrida |
| `derivar` | envía el ejecutable a las Reglas de mutación | el derivado | internet + usuario |

`meta comprobación` no usa experiencia ni aprobación del usuario: si las aporta, es `normal`. `meta-corroborar` no usa usuario: es una corrida de internet. `derivar` no etiqueta: la etiqueta vuelve de las Reglas.

## Almacén

- **`auto`** — por defecto. El agente decide: global si el candidato es un patrón entre repos o personal; repo si es de este repo.
- **`global`** — `~/.dsh/Novedad/candidatos.md` (ruta del instalador). Fuera de todo repo; personal; no se versiona.
- **`repo`** — `./Novedad/candidatos.md`. Local; va en `.gitignore`; no se versiona.

`global|repo` es un modo oculto: solo la autoridad lo fuerza. No se expone en `agents.md`.

## Seguridad

La seguridad se rige por `./Bases de diseño/Principios para agentes con autoridad/Conversacional.md` (`Modelo de seguridad`); no se copia.

## Compuertas

Prohibido ejecutar la compuerta N+1 sin la salida de la N.

1. **Fijar permiso, operación y alcance.** `Permiso: [reporte|meta-cambios] | Operación: [normal|meta comprobación|meta-corroborar|derivar] | Meta-repo: [sí|no] | Llamado: [autoridad|no] | Almacén: [auto|global|repo]`. Si `Meta-repo: no` y `Llamado: no`, `[VACÍO - NO META]` y se cierra. Si `meta-cambios` no tiene `Autorización: sí`, se declara `Permiso: reporte`. Si `Almacén` es `global|repo` sin `Autorización: sí`, se declara `Almacén: auto`.
2. **Capturar.** `Novedad: cambio="[qué cambió]" | fuente=[repo|conversación|análisis] | aprobación=[sí|no]`. Sin aprobación, se cierra.
3. **Filtrar.** `Capa: [norma|mutación] | Test: [la línea que lo incumple] | Duplica: [sí|no] | Fallo conocido: [sí|no]`. Sin test no se captura; si duplica, se referencia la fila y se cierra; si es fallo conocido, se rechaza.
4. **Registrar.** En el `Almacén` elegido, agregar o actualizar una fila de `Novedad/candidatos.md`: `Fecha | Fuente | Cambio | Aprobación | Capa | Tipo | Test | A favor | En contra | Externo | Conclusión | Experiencia | Estado`. `Estado: [candidato|hipotesis|patron|promovido|rechazado]`.
5. **Entregar.** `Novedad: capa=[norma|mutación] | test=[...] | almacén=[auto|global|repo] | estado=[candidato|rechazado]`. No se crea ley ni se muta.
6. **Cerrar.**

## Anclas

`Permiso: [reporte|meta-cambios] | Operación: [normal|meta comprobación|meta-corroborar|derivar] | Almacén: [auto|global|repo]`
`Novedad: capa=[norma|mutación] | test=[...] | estado=[...]`

## Falsificadores

- Se ejecuta fuera de un meta-repo sin llamado de la autoridad.
- Se captura sin aprobación.
- Se captura sin test.
- Se duplica sin referenciar.
- Se promueve a ley o se muta: esta instrucción solo captura.
- Se aplica sin autorización o en segundo plano; el `Modelo de seguridad` lo prohíbe.
- Se fuerza `global|repo` sin autoridad.

## Transiciones

- `norma` → `./Bases de diseño/Leyes de Diseño de Instrucciones.md` o `./Bases de diseño/Principios para agentes con autoridad/Conversacional.md`; la autoridad promueve.
- `mutación` → `./Bases de diseño/Reglas de mutación.md`; la autoridad decide.
- `En cualquier otro caso` → cerrar.

## Salida

`Novedad: capa=[norma|mutación] | test=[...] | almacén=[auto|global|repo] | estado=[candidato|rechazado]`

## Test

`Meta-repo o llamado → captura | Sin ambos → no | Sin test → no | Promueve → falla | Aplica → falla`.
