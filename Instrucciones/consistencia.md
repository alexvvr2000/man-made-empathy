# Consistencia

**Tipo:** instrucción.
**Origen:** ./Instrucciones/instruccion_de_autoridad.md.
**Disparador:** cambia un documento, una ley, una regla, una referencia o una instrucción.
**Lector:** máquina (arnés). El plan declara su lector: humano para decisión, máquina para transferencia.
**Leyes:** por defecto, las del skill (`./Instrucciones/instruccion_de_autoridad.md`); la autoridad puede pasar otras o crear nuevas.

## Mandato

Quien ejecuta esta instrucción revisa que el cambio se refleje en sus dependientes. No reescribe los documentos: detecta, marca y enruta. La regla de consistencia vive en `./Bases de diseño/Principios para agentes con autoridad/Conversacional.md` (`Consistencia cruzada`); esta instrucción la aplica.

## Compuertas

Prohibido ejecutar la compuerta N+1 sin la salida de la N.

1. **Detectar el cambio.** `Cambio: [documento] | Tipo: [semántico|formal] | Alcance: [ley|regla|referencia|instrucción|README]`. Si el tipo es `formal` (typo, formato, sin cambio de sentido), se declara `Cambio: formal | Sin revisión` y se cierra.
2. **Consultar dependencias.** Leer la tabla de `## Dependencias` y listar los dependientes del tipo de cambio. `Dependientes: [N] | [documentos]`.
3. **Revisar dependientes.** Por cada uno: `Revisión: [documento] | Qué: [sección] | Resultado: [sin cambio|requiere cambio|pendiente]`.
4. **Registrar.** `Consistencia: [pasa|falla en N] | Pendientes: [...]`.
5. **Cerrar.** Si falta una ley, una instrucción o una regla, se enruta; si no, se cierra.

## Anclas

`Cambio: [documento] | Tipo: [semántico|formal] | Alcance: [...]`
`Revisión: [documento] | Qué: [sección] | Resultado: [...]`
`Consistencia: [pasa|falla en N]`

## Dependencias

La tabla se lee por **tipo de cambio**, no por nombre de archivo. Si el cambio es semántico, se revisan los dependientes; si es formal, no.

| Cambia | Dependientes | Qué se revisa |
|---|---|---|
| Una ley de diseño | `Reglas de escritura`, `instruccion_de_autoridad`, tests | criterios de validación, referencias, lector |
| La tabla de validación de `instruccion_de_autoridad` | `Leyes`, tests | fila nueva, fila que no está en `Leyes`, divergencia de criterio |
| Una regla de escritura | `agents.md`, `Leyes` (lector), derivados | forma, `Lector`, referencias |
| Un principio | `Autonomo`, SARA `agents.md`, tests | leyes duras, principios, consistencia |
| Una ley dura | `Conversacional`/`Autonomo`, SARA skills, tests | consistencia, ejecución |
| Un disparador o ruta | skills, `Instrucciones/README` | trigger, ruta |
| Una instrucción | `agents.md` (router), README de la carpeta | ruta, trigger |

**Test:** `Cambio semántico → dependientes revisados | Cambio formal → sin revisión | Dependiente omitido → falla`.

## Excepciones

Cada excepción se define por el tipo de cambio, no por el nombre del documento.

- **Cambio formal:** typo, formato o comentario sin cambio de sentido. Se declara y no se revisa.
- **Copia:** si el documento no es el dueño, se corrige la copia; no se revisa el dueño.
- **README human-first:** solo se revisa si cambia el sentido; no tiene compuertas.
- **Test:** se revisan los criterios, no los pasos.
- **Referencia:** se resuelve la ruta; no se revisa el contenido.

## Casos específicos

Cada caso se define por el tipo de cambio, no por el nombre del documento.

- **Ley nueva:** se agrega a `Leyes` y se copia a la tabla de validación de `instruccion_de_autoridad` (copia marcada); se revisa `Reglas de escritura` y el lector.
- **Cambio en la tabla de validación:** si la tabla cambia, se revisa `Leyes`; si la ley es la fuente, la tabla se corrige; si la tabla descubre una ley que falta, se agrega a `Leyes` y se vuelve a copiar.
- **Regla de escritura nueva:** se agrega a `Reglas de escritura`, se revisa `agents.md` y los derivados.
- **Cambio en agnosticismo:** se revisan `Leyes` (`Contratos por Propiedades`), `Conversacional` (`Agnosticismo de medios`) y las instrucciones; un ejemplo marcado con tecnología no se toca.
- **Cambio en SARA:** se revisan `Conversacional`/`Autonomo` y el `agents.md` de SARA; y al revés.
- **Instrucción nueva:** se genera con `instruccion_de_autoridad` y se agrega al router de `agents.md`; el README de `Instrucciones` solo se toca si cambia el mapa.

## Falsificadores

- Se cambia el sentido y no se revisan los dependientes; la consistencia no se probó.
- Se declara `formal` un cambio que cambia el sentido; se salteó la revisión.
- Se corrige una copia sin tocar el original; el dueño sigue mal.
- Una referencia no resuelve; la instrucción está rota.

## Transiciones

- Falta una ley → `./Bases de diseño/Leyes de Diseño de Instrucciones.md`.
- Falta una instrucción → `./Instrucciones/instruccion_de_autoridad.md`.
- Cambio en SARA → `./Agentes/Proyecto S.A.R.A/Componentes/agents.md`.
- En cualquier otro caso → cerrar y declarar.

## Salida

`Plan: [documentos revisados] | Consistencia: [pasa|falla en N] | Pendientes: [...]`.

## Test

`Cambio semántico → plan con dependientes | Cambio formal → sin revisión | Copia sin original → falla | Referencia rota → falla`.
