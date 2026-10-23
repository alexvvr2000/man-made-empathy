**Autor:** [nombre del autor]
**Afiliación:** [institución]
**Contacto:** [correo]
**Fecha:** 2026-10
**Versión:** 1
**Licencia:** CC-BY-4.0

# Cómo se publica esta carpeta

**Tipo:** entregable. Las condiciones de depósito de los seis documentos de esta carpeta. **Lector:** el autor que va a depositar, y quien va a revisar antes de que salga.

## 1. Qué hay aquí

**Seis documentos, y ninguno necesita otro para leerse.** El artículo principal es autónomo; los demás lo acompañan y se citan entre sí por enlace relativo.

| Documento | Qué es | Se publica |
|---|---|---|
| [El protocolo de admisión](./paper.md) | el artículo principal: problema, hueco, siete condiciones, instrumento, límites | solo |
| [Fuentes](./fuentes.md) | el mapa de fuentes: cada afirmación atada a quién la sostiene, con año y nivel | con el artículo |
| [La fricción](./friccion.md) | qué impide que un sistema actúe sin volver a mirar, y qué lo degrada en coerción | solo |
| [Casos de ficción](./casos.md) | qué pieza faltó en cada caso conocido, y qué síntoma avisa antes | solo |
| [El mapa del campo](./campo.md) | los problemas abiertos, qué pieza los toca y qué le falta a cada una | solo |
| [El instrumento sobre el repositorio](./aplicacion.md) | la corrida: comando, resultado con números, fallas y vacío | solo |

## 2. Los seis campos del autor

**Cinco se completan antes de depositar.** El sexto es una fecha y ya está.

| Campo | Está | Si falta |
|---|---|---|
| nombre y afiliación | **no** | el depósito no se acepta sin autor |
| contacto | **no** | el arbitraje no puede contestar |
| licencia | sí: CC-BY-4.0 | — |
| versión y fecha | sí: 1, 2026-10 | — |
| conflicto de interés | **no** | se declara, aunque sea «ninguno» |
| financiación | **no** | se declara, aunque sea «ninguna» |

**Los seis están escritos en este mismo archivo como `Autor:`, `Afiliación:`, `Contacto:`, `Conflicto de interés:` y `Financiación:`.** Se completan aquí y se repiten en cada documento que se deposite por separado.

## 3. Qué falta para el depósito

| Faltante | Por qué bloquea | Quién lo resuelve |
|---|---|---|
| autor y afiliación | es la firma del artículo | la autoridad |
| contacto | el arbitraje no puede contestar | la autoridad |
| conflicto de interés y financiación | es obligatorio declararlos | la autoridad |
| PDF | la carpeta emite LaTeX y, con motor instalado, PDF; sin motor no hay PDF | quien deposite instala un motor LaTeX y corre el comando del apartado 4 |
| identificadores de las fuentes | dos fuentes están solo con nombre y año; sin DOI ni URL no se verifican | la autoridad: se buscan y se completan |

**Dos fuentes con título y año, y sin identificador:** el estudio de *Nature* de 2026 y *Artificial Emotion* (arXiv 2508.10286, este sí con identificador). El primero se localiza por título y año; el segundo ya trae el suyo.

## 4. Cómo se emite el documento

```
pwsh -File mantis/compilar.ps1 -Solo Tesis/publicable
```

**Produce**, en `dist/publicable/`, un `.tex` por documento del manifiesto (`manifiesto.txt`, una fila por archivo con su título). **Si hay un motor LaTeX instalado** (`xelatex`, `lualatex`, `pdflatex` o `tectonic`), produce además el PDF; si no, lo declara y **no lo finge**.

## 5. Las cinco condiciones de una publicación

**La carpeta no se publica si una de las cinco falla.** Cada una es comprobable sin leer la prosa.

| Condición | Cómo se comprueba |
|---|---|
| **1. Cada afirmación tiene fuente o falsificador** | en `fuentes.md`, una fila por afirmación, propia o heredada |
| **2. Lo heredado no se presenta como propio** | la tabla de la sección 2 del artículo y la declaración de aporte |
| **3. Los casos están marcados como casos** | `casos.md`, encabezado; y el artículo, declaración de aporte |
| **4. Los límites están escritos** | sección 6 del artículo; vacío en `aplicacion.md`; límites en `friccion.md` |
| **5. La corrida se puede repetir** | el comando del apartado anterior, con su resultado |

**Y una sexta, que es la que hace creíble a las otras cinco:** el artículo declara **su propio falsificador**. Si se muestra que la compuerta ya existe en un lenguaje de procesos publicado antes de octubre de 2026, la contribución cae.

## 6. Falsificador

**Falsificador de esta carpeta:** un documento que cita un archivo que no resuelve; una cifra que no coincide con lo que hay; un caso presentado como evidencia; una fuente sin año o sin nivel; un límite suavizado para que la carpeta se vea completa.

## Prueba

¿Cada enlace de esta carpeta resuelve a un archivo real? ¿Cada documento se lee sin los demás? ¿Las cinco condiciones se pueden comprobar sin leer la prosa? ¿Lo que falta para depositar está escrito, y no se presenta como si estuviera?

```
Autor: [nombre del autor]
Afiliación: [institución]
Contacto: [correo]
Conflicto de interés: [ninguno | el que sea]
Financiación: [ninguna | la que sea]
```
