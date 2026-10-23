# Idea — el protocolo, formalizado

**Unidad:** nivel.
**Aplica a:** formalizar.
**Tipo:** puerta de la primera de las dos partes de la tesis. No decide ni ejecuta: dice qué hay aquí y cómo se lee.
**Lector:** quien va a publicar, y quien va a leer para decidir si la idea se sostiene.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué hay aquí

**La idea lista para publicar.** No la implementación, no el relato de cómo se llegó a ella: el protocolo, sus fuentes y su declaración de aporte.

| Archivo | Qué es |
|---|---|
| `paper.md` | el artículo: problema, estado del arte, hueco, protocolo, instrumento, límites |
| `fuentes.md` | el mapa de fuentes: cada afirmación atada a quién la sostiene, con año y nivel |

## Cómo se lee

1. **`paper.md`, secciones 1 a 3.** Qué falla, qué ya existía, y qué hueco queda.
2. **`paper.md`, sección 4.** El protocolo: siete piezas, cada una con su `Prueba` y su `Falsificador`.
3. **`paper.md`, sección 6.** Los límites. Es la sección que hace creíble el resto.
4. **`fuentes.md`.** El mapa. **Es lo que se cita, más que la prosa.**

## Cómo se compila

**Un comando, y no depende de pandoc:** el conversor vive en el repo.

```
pwsh -File mantis/compilar.ps1
pwsh -File mantis/compilar.ps1 -Solo Tesis/idea
```

**Produce**, en `dist/<parte>/`:

| Salida | Cuándo |
|---|---|
| `paper.tex` y `fuentes.tex` | **siempre**. El conversor trata el subconjunto de Markdown que usa la tesis |
| `paper.pdf` y `fuentes.pdf` | solo si hay un motor LaTeX en el sistema |

**Si no hay motor**, el comando lo declara y **no lo finge**: emite el `.tex` y el PDF queda `sin motor`. Para tener PDF, instalar uno de `xelatex`, `lualatex`, `pdflatex` o `tectonic`, y volver a correr.

**Lo que el conversor no hace:** no traduce LaTeX escrito a mano dentro del Markdown, y no arma bibliografía con BibTeX. El mapa de fuentes es una tabla, no un `\cite`.

## El material de la idea

**Los casos no están aquí: están en `../Teoria/`.** Este folder no los copia.

| Archivo | Qué aporta a la idea |
|---|---|
| `../Teoria/mundo.md` | la pregunta, los cinco casos con factura ya cobrada, las cuatro fricciones |
| `../Teoria/futuros.md` | nueve futuros, cada uno con su síntoma temprano |
| `../Teoria/individuos.md` | catorce robots, y la pieza que a cada uno le faltó |
| `../Teoria/estado-del-arte.md` | doce piezas heredadas con nivel, seis huecos del campo, cuatro aportes |

## Qué no es

**No es una promesa de AGI.** El paper no la hace y la idea no la necesita.

**No es la implementación.** `../../Implementaciones de la era/` es la era; aquí está lo que no caduca cuando la era cambia.

**No es un catálogo de ficción.** La ficción está marcada como caso, y un caso no es evidencia: es una factura ya cobrada.

## Prueba

¿El paper declara qué es heredado y qué es propio? ¿Cada afirmación de `fuentes.md` tiene año y nivel? ¿Los límites están escritos, o se escondieron?

**Falsificador:** una pieza heredada presentada como propia; una afirmación sin nivel; un índice de fuentes que no dice qué sostiene cada una; un límite suavizado para que el paper se vea completo.
