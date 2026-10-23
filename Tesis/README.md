# Tesis

**Unidad:** nivel.
**Aplica a:** sostener.
**Tipo:** puerta de la tesis. No decide ni ejecuta: dice qué hay en sus partes y cómo se leen.
**Lector:** quien va a publicar, y quien va a decidir si la idea se sostiene.
**Dueño:** la autoridad.
**Estado:** vigente.

## La tesis y su corte

**La tesis tiene dos partes, y la diferencia entre ellas es una sola: la corrida.**

| Parte | Qué contiene | Qué la vuelve publicable |
|---|---|---|
| **`idea/`** | el protocolo formalizado y el mapa de sus fuentes | que cada afirmación traiga el caso que la tumba |
| **`aplicacion/`** | los casos donde el protocolo se corrió, con su medición | que cada caso traiga su corrida, su falla y su vacío |

**La idea se publica sola.** La aplicación se publica con su corrida: sin ella es una ilustración, y una ilustración se lee como evidencia sin serlo.

## La carpeta publicable

**`publicable/` es el corte que se publica: los documentos que se leen solos, sin el repositorio.** No es una tercera parte de la tesis: es la forma en que las dos se emiten para un lector que no va a abrir otra carpeta.

| Qué tiene | Cómo se usa |
|---|---|
| siete documentos, cada uno con su versión, su fecha y su licencia | se depositan como están, o se emiten a PDF con el manifiesto |
| `README.md` | la puerta: qué hay, cómo se lee y qué la vuelve publicable |
| `LEEME-publicacion.md` | las condiciones de depósito: qué falta, quién lo completa |
| `manifiesto.txt` | qué documentos se emiten y con qué título; **no se publica** |

**Un corte no es una copia.** `idea/` es la fuente de la tesis; `publicable/` es su lectura para afuera. Lo que el corte reescribe se declara allí, y lo que la fuente todavía cita con un nombre histórico queda en la fuente, no en el corte.

**Los dos dicen lo mismo, y lo dicen distinto porque el lector no es el mismo.** Quien lee `idea/` conoce el repositorio; quien lee `publicable/` no lo va a abrir.

## Cómo se lee

1. **`publicable/paper.md`**, secciones 1 a 3: qué falla, qué ya existía, qué hueco queda.
2. **`publicable/paper.md`**, sección 4: las siete condiciones, cada una con su `Falsificador`.
3. **`publicable/paper.md`**, sección 6: los límites. **Es la sección que hace creíble el resto.**
4. **`publicable/fuentes.md`**: cada afirmación atada a su fuente, con año y nivel.
5. **`publicable/aplicacion.md`**: la corrida, con su comando y su resultado.
6. **`publicable/LEEME-publicacion.md`**: qué falta para depositar.

## El material

**Los casos no se copian en la fuente: viven en `Teoria/`, y el paper los cita.** El corte sí los reescribe, porque quien lee `publicable/` no abre otra carpeta.

| Archivo | Qué aporta |
|---|---|
| `Teoria/mundo.md` | la pregunta, los casos con factura ya cobrada, las cuatro fricciones |
| `Teoria/futuros.md` | los futuros de la ficción, cada uno con su síntoma temprano |
| `Teoria/individuos.md` | los robots de la ficción, y la pieza que a cada uno le faltó |
| `Teoria/estado-del-arte.md` | lo heredado con nivel, lo que falta en el campo, lo que se agrega |
| `Conceptos.md` | el registro de nombres del sistema |
| `SARA 1.md`, `SARA 2.md` | la instancia que aplica el lenguaje, y su forma |

## Qué no es esta carpeta

**No es ejecución.** Este repo es el reino de las ideas: lo que se ejecuta sale de aquí ya con formato de ente y vive fuera. Aquí está lo que no caduca.

**No es un catálogo de ficción.** Los casos están marcados como casos: **una factura ya cobrada no es una medición.**

**No es una promesa de AGI.** La idea no la necesita, y el paper no la hace.

## Prueba

¿Cada parte declara qué la vuelve publicable? ¿El corte se lee sin el repositorio? ¿Todo documento del corte está en el manifiesto? ¿Lo que falta para depositar está escrito?

**Falsificador:** una idea presentada como conclusión y no como hipótesis con falsificador; una aplicación sin corrida; un caso de ficción presentado como evidencia; una parte que promete lo que la otra no puede sostener; un corte que necesita al repositorio para entenderse.
