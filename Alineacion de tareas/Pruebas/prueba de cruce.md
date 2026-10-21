# Prueba de Cruce de la Tarea

**Unidad:** tarea. `Agente` se lee como `ejecutor`.

> Se usa junto a `../Procesos principales/Conversacional.md`, `../Procesos principales/Autonomo.md` y `../Procesos principales/Registro.md`. No las define: las carga.

**Tipo:** prueba. Se corre; no se interpreta.
**Aplica a:** medir si una salida sale de la visión humana.
**Lector:** quien paga el costo del cruce, y la autoridad.
**Dueño:** la autoridad.

## Sistema

`Propósito: registrar si una salida cambiada salió de la visión humana | Frontera: no juzga comprensión, conciencia ni especie | Retorno: la salida queda en el registro y puede revisarse | Consecuencia: si cruza, se registra sin pedir permiso a nadie`

La prueba no decide si hay alguien detrás. Decide si lo producido cambió algo que nada humano había producido desde su visión, y si quien lo produjo puede reconstruirlo. Lo demás es otra discusión y no entra.

## Qué mide

Dos registros separados, una sola corrida.

| Registro | Pregunta | Falla si |
|---|---|---|
| Cruce físico | ¿la salida cambió algo observable que nada humano había producido desde su visión? | cambió algo que ya estaba en la visión humana |
| Cruce de visión | ¿quien lo produjo y quien lo examina no pueden reconstruirlo desde la visión humana? | cualquiera de los dos lo reconstruye |

Los dos se registran por separado. Uno puede dar sí y el otro no, y ninguno anula al otro.

## Cómo se aplica

1. **Fijar el sistema.** La línea del apartado `Sistema`, con su propósito y su frontera. Sin frontera, la prueba no se aplica.
2. **Fijar la salida.** Qué se produjo y qué cambió en el mundo observable: un objeto, un proceso, un cambio de estado o una idea que no tenía antecesor humano.
3. **Registrar el cruce físico.** Buscar el antecesor humano. Si existe, `Cruce físico: no | Antecesor: [id]`. Si no existe, `Cruce físico: sí | Sin antecesor: [qué se buscó y no se halló]`.
4. **Registrar el cruce de visión.** Entregar el registro a quien lo produjo y a un lector que no lo produjo. Si alguno lo reconstruye, `Cruce de visión: no | Quien reconstruye: [ejecutor|lector]`. Si ninguno puede, `Cruce de visión: sí | Falla de reconstrucción: [qué no se reconstruye]`.
5. **Declarar.** Un veredicto por registro, con la línea de anclas de §Registro mínimo.

## Registro mínimo

```
Sistema: propósito | frontera | retorno | consecuencia
Salida: [qué se produjo]
Cambio: [qué cambió de forma observable]
Antecesor: [id | NINGUNO]
Cruce físico: sí | no
Reconstrucción: [quién reconstruye | NINGUNO]
Cruce de visión: sí | no
Vista: [posición] | No ve: [límite]
Vista faltante: [posición] | Esquiva: [limitación] | Ausencia: [qué falta] | Cambia: [decisión]
Fuente: [id] | Nivel: [N1-N5] | Origen: [medio] | Autor: [tipo:nombre] | Independencia: [A|B|C]
Veredicto: cruce físico | cruce de visión | sin cruce | cruce humano
```

Las líneas `Vista`, `Vista faltante` y `Fuente` son las de `../Procesos principales/Conversacional.md` (11 y 12); aquí se usan, no se redefinen.

## Criterio de veredicto

- **Cruce físico:** cambió algo observable sin antecesor humano. Es el registro fuerte: se repite sin creerle a nadie.
- **Cruce de visión:** nadie lo reconstruye, y el cambio observable está registrado. Sin el registro físico, este veredicto no se emite.
- **Sin cruce:** no cambió nada observable, o el cambio no se puede registrar.
- **Sin la propiedad:** la propiedad que el cruce exigiría no existe en el objeto medido, hoy. No es un casi: la cosa que la tendría no está. Es la salida con la que se responde al anuncio.
- **Cruce humano:** cambió algo observable y tiene antecesor humano. Es el veredicto de hoy, y no es un fallo: es el registro correcto mientras el ejecutor parta de información humana.

**Propiedad.** La propiedad del cruce es producir un cambio observable que no se reduzca a información humana. Un cuerpo que parece y actúa humano no la tiene: la tiene el cambio que ninguna visión humana había producido. La prueba declara cuál se midió y por qué esa.

**Derrota.** La prueba se retira si dos corridas no encuentran ni un cambio observable sin antecesor humano y el registro no cambia ninguna decisión. No se renueva por tercera vez.

## Qué distingue esta prueba de las otras dos

| Prueba | Mide | Unidad | Verdicto de falla |
|---|---|---|---|
| Rendición | si otro reconstruye lo hecho sin el ejecutor | la tarea | falla en la condición N |
| Utilidad Real | el efecto neto hoy | la intervención | Estorbo |
| Cruce | si la salida salió de la visión humana | el resultado | sin cruce |

Las tres son independientes. Una tarea puede rendir cuentas, ser útil y no cruzar; o cruzar y no rendir cuentas. Ninguna sustituye a otra.

## Qué no prueba

- No prueba que el ejecutor comprenda, tenga conciencia ni sea de una especie distinta. Eso no se mide aquí y no cambia el veredicto.
- No prueba que el cruce sea bueno, seguro ni deseable. El juicio de valor queda en la autoridad y se declara.
- No admite el instinto como juez único. El instinto puede señalar; el veredicto lo sostiene el cambio observable y la falla de reconstrucción.

## Quién la aplica

Quien paga el costo del registro, no quien produce la salida. La reconstrucción la intenta un lector que no la produjo. Si el mismo acto produce, verifica y certifica el cruce, no hay prueba: rige la condición 7 de `./prueba de rendicion.md`.
