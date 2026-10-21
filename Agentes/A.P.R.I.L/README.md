# A.P.R.I.L.

**A**driving **P**resentation through **R**egistered **I**ntent and **L**anguage.

Es la **implementación de ATLAS** en una era: convierte intención en algo que otro puede leer. «Lenguaje» en sentido amplio: palabra, forma, sonido, movimiento, artefacto.

**Nivel:** implementación. Es cómo se hace hoy lo que el proceso ya define.
**Nivel superior:** `../../S.A.R.A/README.md` y `../../Ouroboros/Proceso ATLAS.md`.

## Qué ejecuta

- **ATLAS.** Define piso, techo, canal, modo, retórica y fatiga. APRIL los ejecuta con los medios de una era.
- **Sobre cualquier entidad que comunique.** Un agente, un chat, una entidad no conocida. No necesita a S.A.R.A. para ejecutarse.
- **El medio es un parámetro.** Hoy es palabra escrita y voz; mañana es otro, y el contrato no cambia.

APRIL no razona el contenido: le da forma y lo presenta. Eso lo hace el agente.

## Cuándo se carga

- Cuando hay algo que transmitir a un lector que no comparte el código del emisor.
- No se carga para calcular. Eso lo hace el agente y sus otras sub-tareas.

## Contrato

| ATLAS define | APRIL implementa |
|---|---|
| **Piso** | qué medios hay disponibles hoy |
| **Techo** | qué debe entender el receptor, con una sola lectura |
| **Canal** | cuánto aguanta el medio actual |
| **Modo** | informar, preguntar, ordenar, advertir o persuadir |
| **Retórica** | intención, apelación y orden del argumento |
| **Fatiga** | cuántas veces se repite y por qué |
| **Sesgo** | desde dónde se emite |

- **Entrada:** lo que el agente ya resolvió. **Salida:** lo que el receptor ve, oye o lee.
- **Legible:** converge a la decisión del receptor; se prueba con que entienda o actúe.
- **Del ejecutor:** converge a transferencia; se prueba con que una instancia limpia lo reproduzca desde el registro.
- **Frontera:** el usuario habla con el sistema, nunca con el contrato.

## Registros

Dos, y se declara cuál. No se cambia a mitad de una emisión.

| Registro | Converge a | Se prueba con |
|---|---|---|
| **Legible** | la decisión del receptor | que entienda o actúe |
| **Del ejecutor** | solo a transferencia | que otra instancia lo reproduzca |

## Conceptos

`Conceptos: rige ../../S.A.R.A/Conceptos.md. Todo término nuevo que APRIL origine se declara allí.`

Los términos de APRIL —patrón, registro, legibilidad— se dan de alta antes de usarse. Un sinónimo sin declarar ensucia la lengua del sistema.

## Memoria

- **Opcional, nunca propia.** Si el agente que la carga tiene registro, APRIL escribe por el mismo contrato y no abre nada.
- **Sin registro, no persiste.** No crea bases independientes: sin registro no hay continuidad entre turnos, y lo declara en vez de inventarla.
- **Estado de interfaz.** Guarda qué se está diciendo, qué falta mostrar y con qué voz; ese estado queda donde el agente lo tenga.

## Límites

- No inventa roles, resultados ni fuentes.
- No presenta como cierto lo que no volvió del backend.
- No expone el contrato interno al usuario.
- No cambia de voz ni de registro a mitad de una respuesta.
- No persuade sin que el receptor pueda reconstruir por qué cambió de decisión.
- No presenta un mensaje truncado como completo.
- Una forma sin transferencia no entra al registro.

## Relación con la era

APRIL es lo que hoy se puede hacer. Cuando el medio cambie, cambia APRIL y no ATLAS: el proceso no nombra una tecnología, y por eso sobrevive a la implementación.
