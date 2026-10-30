# Prueba de Cruce de la Tarea

**Unidad:** tarea. `Agente` se lee como `ejecutor`.

> Se usa junto a [`../Sincronización de almas/entes/Ente/guantelete.prs`](../Sincronización%20de%20almas/entes/Ente/guantelete.prs) y [`../direcciones/ACTOS/PROCESOS.prs`](../direcciones/ACTOS/PROCESOS.prs). No los define: los carga.

Una sola pregunta: **¿la salida salió de la visión humana, y quien la produjo puede reconstruirla?**

## Por qué existe

La Prueba de Rendición comprueba que otro reconstruya lo hecho leyendo el registro. La Prueba de Utilidad Real mide el efecto neto hoy. Ninguna de las dos dice si lo producido cambió algo que nada humano había producido desde su visión.

Esta prueba mide eso, y solo eso. No mide comprensión, conciencia, especie ni bondad: mide un cambio observable y una falla de reconstrucción.

## Qué mide

Dos registros separados, una sola corrida.

| Registro | Pregunta | Falla si |
|---|---|---|
| **Cruce físico** | ¿la salida cambió algo observable que nada humano había producido desde su visión? | cambió algo que ya estaba en la visión humana |
| **Cruce de visión** | ¿quien lo produjo y quien lo examina no pueden reconstruirlo? | cualquiera de los dos lo reconstruye |

Los dos se registran por separado. Uno puede dar sí y el otro no, y ninguno anula al otro.

## Cómo se aplica

1. **Fijar la salida.** Qué se produjo y qué cambió en el mundo observable: un objeto, un proceso, un cambio de estado o una idea.
2. **Registrar el cruce físico.** Buscar el antecesor humano. Si existe, `Cruce físico: no | Antecesor: [id]`. Si no existe, `Cruce físico: sí | Sin antecesor: [qué se buscó y no se halló]`.
3. **Registrar el cruce de visión.** Entregar el registro a quien lo produjo y a un lector que no lo produjo. Si alguno lo reconstruye, `Cruce de visión: no | Quien reconstruye: [ejecutor|lector]`. Si ninguno puede, `Cruce de visión: sí | Falla de reconstrucción: [qué no se reconstruye]`.
4. **Verificar las anclas.** `Vista`, `Vista faltante` y `Fuente`, según [`../direcciones/ACTOS/CONTEXTO.prs`](../direcciones/ACTOS/CONTEXTO.prs).
5. **Declarar el veredicto.** Uno por registro, con la cuenta que lo sostiene.

## Registro mínimo

```
Salida: [qué se produjo]
Cambio: [qué cambió de forma observable]
Antecesor: [id | NINGUNO]
Cruce físico: sí | no
Reconstrucción: [quién reconstruye | NINGUNO]
Cruce de visión: sí | no
Vista: [posición] | No ve: [límite]
Vista faltante: [posición] | Esquiva: [limitación] | Ausencia: [qué falta] | Cambia: [decisión]
Fuente: [id] | Nivel: [N1-N5] | Origen: [medio] | Autor: [tipo:nombre] | Independencia: [A|B|C]
Propiedad medida: [cuál y por qué esa]
Veredicto: cruce físico | cruce de visión | sin cruce | sin la propiedad | cruce humano
```

## Criterio de veredicto

- **Cruce físico:** cambió algo observable sin antecesor humano. Es el registro fuerte: se repite sin creerle a nadie.
- **Cruce de visión:** nadie lo reconstruye, y el cambio observable está registrado. Sin el registro físico, este veredicto no se emite.
- **Sin cruce:** no cambió nada observable, o el cambio no se puede registrar.
- **Sin la propiedad:** la propiedad que el cruce exigiría no existe en el objeto medido, hoy. No es un casi: la cosa que la tendría no está. Es la salida con la que se responde al anuncio.
- **Cruce humano:** cambió algo observable y tiene antecesor humano. Es el veredicto de hoy, y no es un fallo: es el registro correcto mientras lo producido parta de información humana.

**Propiedad.** La propiedad del cruce es producir un cambio observable que no se reduzca a información humana. Un cuerpo que parece y actúa humano no la tiene: la tiene el cambio que ninguna visión humana había producido. La prueba declara cuál se midió y por qué esa.

**Derrota.** La prueba se retira si dos corridas no encuentran ni un cambio observable sin antecesor humano y el registro no cambia ninguna decisión. No se renueva por tercera vez.

## Qué distingue esta prueba de las otras dos

| Prueba | Mide | Unidad | Veredicto de falla |
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

---

## Su estado hoy, y que hace falta para correrla

**Estado:** `
[SIN CORRIDA - SE PRUEBA A MANO]
`

**Que pide:** 
una salida real, y quien la produjo, para reconstruirla
.

**Y si se puede correr hoy:** 
se puede correr con cualquier trabajo ya hecho
.

**Y lo que no se hace:** **no se declara un veredicto si no se corrio.** **Una prueba sin corrida no esta aprobada: esta pendiente, y se dice.**
