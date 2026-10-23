# README

**Unidad:** nivel.
**Aplica a:** publicar.
**Tipo:** puerta de la carpeta publicable. No decide ni ejecuta: dice qué hay aquí, cómo se lee y qué la vuelve publicable.
**Lector:** quien va a depositar, y quien va a arbitrar sin conocer el repositorio.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

**Los seis documentos que se publican, y nada más.** No es un resumen de `../`: es el corte que se lee solo. Cada documento es un entregable: se entiende sin abrir otro archivo del repositorio, y ningún nombre interno se usa sin glosa.

| Documento | Qué es |
|---|---|
| [`paper.md`](./paper.md) | el artículo principal: qué falla, qué ya existía, qué hueco queda, siete condiciones con su falsificador, el instrumento, los límites |
| [`fuentes.md`](./fuentes.md) | el mapa de fuentes: cada afirmación atada a quién la sostiene, con año y nivel |
| [`friccion.md`](./friccion.md) | la fricción: qué impide que un sistema actúe sin volver a mirar, y qué la degrada en coerción |
| [`casos.md`](./casos.md) | la ficción y la historia como factura ya cobrada: qué pieza faltó en cada caso, y los cinco futuros con su síntoma temprano |
| [`campo.md`](./campo.md) | los diez problemas abiertos del campo, qué pieza toca cada uno y qué le falta |
| [`aplicacion.md`](./aplicacion.md) | la corrida del instrumento sobre el repositorio: comando, resultado, fallas y vacío |
| [`LEEME-publicacion.md`](./LEEME-publicacion.md) | las condiciones de depósito: qué falta, quién lo completa y cómo se emite el documento |

**`manifiesto.txt` no se publica:** dice qué documentos se emiten y con qué título. Lo lee el conversor.

## Cómo se lee

1. **[`paper.md`](./paper.md), secciones 1 a 3.** Qué falla, qué ya existía, qué hueco queda.
2. **[`paper.md`](./paper.md), sección 4.** Las siete condiciones, cada una con su `Falsificador`.
3. **[`paper.md`](./paper.md), sección 6.** Los límites. **Es la sección que hace creíble el resto.**
4. **[`fuentes.md`](./fuentes.md).** El mapa. **Es lo que se cita, más que la prosa.**
5. **[`LEEME-publicacion.md`](./LEEME-publicacion.md).** Qué falta para depositar.

**Quien arbitra** lee el artículo y el mapa, y comprueba una de las cinco condiciones del `LEEME`. **Quien decide en qué gastar el tiempo** lee `campo.md`. **Quien va a replicar** lee `aplicacion.md`.

## Qué la vuelve publicable

| Condición | Dónde se comprueba |
|---|---|
| cada afirmación trae su fuente o su falsificador | `fuentes.md`, una fila por afirmación |
| lo heredado está declarado como heredado | `paper.md`, sección 2 y declaración de aporte |
| los casos están marcados como casos | `casos.md`, encabezado |
| los límites están escritos | `paper.md`, sección 6; `aplicacion.md`, vacío |
| la corrida se puede repetir | `aplicacion.md`, el comando y su resultado |
| el artículo declara su propio falsificador | `paper.md`, declaración de aporte |

**Un documento no entra aquí porque esté terminado: entra porque se sostiene sin el resto del repositorio.**

## Qué no es esta carpeta

**No es la fuente.** Lo que se dijo antes de compilar vive en la memoria del repositorio; esta carpeta es un corte de esa memoria, con su fecha. Si el documento cambia, cambia aquí y en la fuente en el mismo acto.

**No es una promesa de inteligencia general.** El artículo no la hace y los documentos no la necesitan.

**No es un catálogo de ficción.** Los casos están marcados como casos: **una factura ya cobrada no es una medición.**

## Cómo se emite

```
pwsh -File mantis/compilar.ps1 -Solo Tesis/publicable
```

Emite un `.tex` por fila de [`manifiesto.txt`](./manifiesto.txt) en `dist/publicable/`, y el PDF si hay motor LaTeX. **Sin motor, lo declara y no lo finge.**

## Prueba

¿Cada enlace de esta carpeta resuelve a un archivo real? ¿Cada documento se lee solo? ¿Cada documento está en el manifiesto, o se declara por qué no? ¿Lo que falta para depositar está escrito?

**Falsificador:** un enlace que no resuelve; un documento que necesita el repositorio para entenderse; un caso presentado como evidencia; una condición de publicación que no se puede comprobar; lo que falta para depositar escondido en vez de escrito.
