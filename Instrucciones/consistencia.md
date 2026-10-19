# Consistencia

**Tipo:** instrucción.
**Origen:** ./Instrucciones/instruccion-de-autoridad.md.
**Disparador:** cambia un documento, una ley, una regla, una referencia o una instrucción.
**Carga:** on demand. Se carga solo si el disparador coincide; no se carga en cada turno.
**Lector:** máquina (arnés). El plan declara su lector: humano para decisión, máquina para transferencia.
**Leyes:** por defecto, las del skill (`./Instrucciones/instruccion-de-autoridad.md`); la autoridad máxima puede pasar otras o crear nuevas.

## Mandato

Quien ejecuta esta instrucción revisa que el cambio se refleje en sus dependientes. No reescribe los documentos: detecta, marca y enruta. La regla de consistencia vive en `./Bases de diseño/Principios para agentes con autoridad/Conversacional.md` (`Consistencia cruzada`); esta instrucción la aplica. Las referencias se escriben relativas a la raíz con `./`; no se usan rutas absolutas ni `../`. Un movimiento o renombre de carpeta obliga a revisar las rutas de los dependientes. La revisión se hace contra el inventario completo de lo disponible, no contra una copia ni una selección.

## Compuertas

Prohibido ejecutar la compuerta N+1 sin la salida de la N.

1. **Detectar el cambio.** `Cambio: [documento] | Tipo: [semántico|formal] | Alcance: [ley|regla|referencia|instrucción|README|carpeta]`. Si el tipo es `formal` (typo, formato, sin cambio de sentido), se declara `Cambio: formal | Sin revisión` y se cierra.
2. **Inventariar lo disponible.** Listar los documentos, instrucciones y tests que existen. Salida: `Disponible: [N] | [items]`.
3. **Consultar dependencias.** Leer la tabla de `## Dependencias` y listar los dependientes del tipo de cambio. `Dependientes: [N] | [documentos]`.
4. **Revisar el inventario.** Por cada item disponible: `Revisión: [documento] | Qué: [sección] | Resultado: [sin cambio|requiere cambio|no aplica|pendiente]`. Los dependientes se revisan; el resto se marca `no aplica` con la razón.
5. **Registrar.** `Disponible: [N] | Revisado: [items] | No aplica: [items] | Pendiente: [items] | Consistencia: [pasa|falla en N]`.
6. **Cerrar.** Si falta una ley, una instrucción o una regla, se enruta; si no, se cierra.

## Anclas

`Cambio: [documento] | Tipo: [semántico|formal] | Alcance: [...]`
`Disponible: [N] | [items]`
`Revisión: [documento] | Qué: [sección] | Resultado: [...]`
`Revisado: [items] | No aplica: [items] | Pendiente: [items]`
`Consistencia: [pasa|falla en N]`

## Disponible

El inventario se toma de lo que existe, no de lo que la tabla espera. Se recorre completo: cada documento, instrucción o test disponible se marca `revisado`, `no aplica` o `pendiente` con la razón. Ninguno se omite por conveniencia.

`Disponible: [N] | [items]`

**Test:** `Inventario completo → se revisa | Documento disponible omitido → falla | Sin inventario → falla`.

## Dependencias

La tabla dice qué revisar; el inventario dice qué hay. La revisión recorre el inventario completo, no solo la tabla. La tabla se lee por **tipo de cambio**, no por nombre de archivo. Si el cambio es semántico, se revisan los dependientes; si es formal, no.

| Cambia | Dependientes | Qué se revisa |
|---|---|---|
| Una ley de diseño | `Reglas de escritura`, `instruccion-de-autoridad`, tests | criterios de validación, referencias, lector |
| La tabla de validación de `instruccion-de-autoridad` | `Leyes`, tests | fila nueva, fila que no está en `Leyes`, divergencia de criterio |
| Una regla de escritura | `agents.md`, `Leyes` (lector), derivados | forma, `Lector`, referencias |
| Un principio | `Autonomo`, SARA `agents.md`, tests | leyes duras, principios, consistencia |
| Una ley dura | `Conversacional`/`Autonomo`, SARA skills, tests | consistencia, ejecución |
| Un disparador o ruta | skills, `Instrucciones/README` | trigger, ruta |
| Una instrucción | `agents.md` (router), README de la carpeta | ruta, trigger |
| Un movimiento o renombre | dependientes con referencias `./` | rutas, `Origen`, `Leyes`, transiciones |
| Un meta-cambio | dueño, tests, ledger | ley/principio, test, estado |
| Las Reglas de mutación | `agents.md`, `instruccion-de-autoridad`, `wax`, `novedad` | etiqueta, modos, anclas |

**Test:** `Cambio semántico → dependientes revisados | Cambio formal → sin revisión | Dependiente omitido → falla`.

## Excepciones

Cada excepción se define por el tipo de cambio, no por el nombre del documento.

- **Cambio formal:** typo, formato o comentario sin cambio de sentido. Se declara y no se revisa.
- **Copia:** si el documento no es el dueño, se corrige la copia; no se revisa el dueño.
- **README human-first:** solo se revisa si cambia el sentido; no tiene compuertas.
- **Test:** se revisan los criterios, no los pasos.
- **Referencia:** se resuelve la ruta relativa a la raíz con `./`; no se revisa el contenido.

## Casos específicos

Cada caso se define por el tipo de cambio, no por el nombre del documento.

- **Ley nueva:** se agrega a `Leyes` y se copia a la tabla de validación de `instruccion-de-autoridad` (copia marcada); se revisa `Reglas de escritura` y el lector.
- **Cambio en la tabla de validación:** si la tabla cambia, se revisa `Leyes`; si la ley es la fuente, la tabla se corrige; si la tabla descubre una ley que falta, se agrega a `Leyes` y se vuelve a copiar.
- **Regla de escritura nueva:** se agrega a `Reglas de escritura`, se revisa `agents.md` y los derivados.
- **Cambio en agnosticismo:** se revisan `Leyes` (`Contratos por Propiedades`), `Conversacional` (`Agnosticismo de medios`) y las instrucciones; un ejemplo marcado con tecnología no se toca.
- **Cambio en SARA:** se revisan `Conversacional`/`Autonomo` y el `agents.md` de SARA; y al revés.
- **Instrucción nueva:** se genera con `instruccion-de-autoridad` y se agrega al router de `agents.md`; el README de `Instrucciones` solo se toca si cambia el mapa.
- **Documento nuevo:** si existe y no está en la tabla, se agrega al inventario y se declara `sin dependencia` o `pendiente`; no se omite.
- **Movimiento o renombre:** se revisan las referencias `./` de los dependientes; se marcan para corrección; una ruta que no resuelve falla.
- **Meta-cambio:** se revisan el dueño, los tests y el ledger; si rompe una ley o un principio, se rechaza.

## Falsificadores

- Se cambia el sentido y no se revisan los dependientes; la consistencia no se probó.
- Se revisa solo lo que la tabla sugiere y se omite un documento disponible; la consistencia no se probó.
- Se declara `pasa` sin inventario; falta la prueba.
- Se declara `formal` un cambio que cambia el sentido; se salteó la revisión.
- Se corrige una copia sin tocar el original; el dueño sigue mal.
- Se usa una ruta absoluta o `../`; la referencia no es relativa a la raíz.
- Una referencia o una ruta relativa no resuelve; la instrucción está rota.
- Un meta-cambio sin test o sin registro; la ley quedó sin prueba.

## Transiciones

- Falta una ley → `./Bases de diseño/Leyes de Diseño de Instrucciones.md`.
- Falta una instrucción → `./Instrucciones/instruccion-de-autoridad.md`.
- Cambio en SARA → `./Agentes/Proyecto S.A.R.A/Componentes/agents.md`.
- En cualquier otro caso → cerrar y declarar.

## Salida

`Plan: [documentos revisados] | Disponible: [N] | Revisado: [items] | No aplica: [items] | Pendiente: [items] | Consistencia: [pasa|falla en N]`.

## Test

`Inventario completo → se revisa | Documento disponible omitido → falla | Sin inventario → falla | Cambio semántico → plan con inventario | Cambio formal → sin revisión | Copia sin original → falla | Referencia rota → falla | Ruta relativa rota → falla | Meta-cambio sin test → falla`.
