# El origen — de dónde sale cada línea

**Unidad:** nivel.
**Aplica a:** rastrear.
**Tipo:** registro. No decide ni ejecuta: dice de dónde viene lo que hay en `futuro/`, y qué de la memoria no se copia.
**Lector:** quien va a leer `futuro/` y quiere saber si le miente.
**Dueño:** la autoridad.
**Estado:** vigente.
**Sesgo:** el origen se lee desde quien hereda el archivo, no desde quien lo escribió.
**Límite:** no decide si lo escrito vale; dice de dónde viene.
**Cuelga de:** `./UNION.md`, condición de trazabilidad.
**Deja de valer:** cuando la fuente original ya no existe en ningún sitio. Ahí el origen es leyenda, y se declara.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `<../Ouroboros/formato de proceso.md>`

## La regla

> **La memoria dice qué se decidió y por qué. El archivo dice qué hay. Cuando difieren, gana el archivo — y se anota que difieren.**

`mantis.db` tiene 223 filas y algunas apuntan a archivos que hoy no existen o cambiaron de forma. **Leerla como verdad alucina.** Esta regla no la inventa este archivo: la dice `Ouroboros/procesos/memoria continua.md`, `Qué resuelve`: *un cerebro guarda su versión de lo que pasó, no el hecho*.

## La segunda regla: nada del autor sale de aquí

> **En ningún archivo versionado de este repo se escribe una ruta absoluta de una máquina personal, un nombre de cuenta, un correo, ni la ubicación de un almacenamiento privado.**

**La fuente se nombra por su lugar en el mundo, no por la ruta de un disco.** `MEGA/mme` es una fuente: dice qué es y que vive fuera del repo. Una ruta absoluta dice además **dónde vive el autor, cómo se llama su cuenta y qué carpetas tiene** — y eso no tiene por qué estar escrito en algo que se puede publicar.

**Cómo se nombra en su lugar:**

```
Fuente: MEGA/mme — la idea. Vive fuera del repo, con su propio versionado.
```

**Prueba:** ¿algún archivo versionado contiene una ruta de usuario, un directorio temporal, o un nombre de cuenta? Si sí, no se publica.
**Falsificador:** una ruta absoluta de una máquina personal en un archivo versionado; un nombre de cuenta en un ejemplo; un correo en una constante.


## Los cuatro orígenes

| Origen | Qué aporta | Qué se copia de ahí | Qué no |
|---|---|---|---|
| **MEGA** (`MEGA/mme`) | la idea, la teoría, las fuentes | el fin, la pregunta, los límites | la implementación: no vive ahí |
| **`mantis.db`** | el porqué de cada decisión y cada descarte | por qué se descartó algo, y cuándo vuelve | rutas y conteos: pueden estar viejos |
| **`Ouroboros/`** | el cómo, con falsificador | las cinco piezas de `ENTREGA.md` | — |
| **`git`** | qué se intentó y falló | la cadena de deriva | — |

## De dónde sale cada pieza de `futuro/`

| Archivo de `futuro/` | Nivel | De dónde sale | Quién lo puede contestar |
|---|---|---|---|
| `CAMINO.md` — la meta | **N4** | se sigue de `MEGA/mme/Teoria/futuros.md` (`La utopía que se busca`) y de `MEGA/mme/Teoria/mundo.md` (`Por qué la pregunta no se puede saltar`) | el autor, con una lectura del mundo que las tumbe |
| `CAMINO.md` — los cuatro tramos | **N2** | `Ouroboros/CRITERIO.md` (niveles), `mantis/Derrotero.md` (registro), `formato de ente.md` | integridad |
| `CAMINO.md` — el tramo en curso | **N1** | medición del 2026-10-23 con `mantis/piso/` | `piso.ps1`, que se puede volver a correr |
| `ENTREGA.md` — pieza 1 (sesgo) | **N2** | `Ouroboros/1 Guantelete — primitivo/primitivos/sesgo.md` | quien use la pieza |
| `ENTREGA.md` — pieza 2 (falsificador) | **N2** | `Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md`, `Admisión` | quien use la pieza |
| `ENTREGA.md` — pieza 3 (nivel de fuente) | **N2** | `Ouroboros/2 S.A.R.A — mutación/evidencia/nivel-de-fuente.md` | quien use la pieza |
| `ENTREGA.md` — pieza 4 (memoria de posiciones) | **N2** | `Ouroboros/procesos/memoria continua.md` | quien use la pieza |
| `ENTREGA.md` — pieza 5 (pase de turno) | **N2** | `Ouroboros/procesos/memoria continua.md`, `El pase de turno` | quien use la pieza |
| `ENTREGA.md` — la pregunta | **N2** | `Ouroboros/1 Guantelete — primitivo/primitivos/friccion.md` y `MEGA/mme/Teoria/mundo.md` | el autor |
| `ENTREGA.md` — "garantiza la pregunta, no la respuesta" | **N2** | `MEGA/mme/publicable/paper.md`, §6 `Límites` | quien revise el paper |
| `ENTREGA.md` — "sabe cuándo lo miden" | **N5** | se sostuvo desde la conversación; se buscó y se encontró el reporte internacional de 2026 como mención de segundo orden, **sin leerlo entero** | quien lea la fuente primaria |
| `APLICADA.md` — el cero | **N1** | medido el 2026-10-23 | cualquiera, mirando este repo |

**Lo que está en N5, y se declara:** que "un sistema que sabe cuándo lo miden" sea un modo de falla distinto de los cinco que la entrega atrapa. **Es una deducción de lecturas de segunda mano, no una medición.** Se deja adentro porque **separa lo que la entrega no cubre**, y eso es útil; y se deja marcado porque **no se verificó.**

## Lo que la memoria dice y el archivo contradice

| La memoria dice | El archivo dice | Gana |
|---|---|---|
| filas 81, 131, 92, 132: `duplicados.ps1` está rojo y el piso es 6 de 7 | `duplicados.ps1` **no existe**; el piso es de 5 unidades y es **4 de 5** | **el archivo** |
| fila 180 y 208: hay backup en `MEGA/mme/backup-2026-10-22_2314` | **esa carpeta no está** en MEGA hoy | **el archivo** |
| filas 206 y 205: el pegamento va en `Tesis/pegamento/` | **`Tesis/` no está en el repo**; vive en MEGA | **el archivo** |
| fila 199 y 200: MANTIS no aprende por interacción y falta el candado | **`turno.ps1` ya existe** y la unidad pasa | **el archivo** |
| el paper afirma "7 de 7" y "73 de 73" | hoy son **4 de 5** y **73 de 73** | el segundo coincide; **el primero no** |

**Ninguna de estas contradicciones se corrige aquí.** Se declaran: una memoria sin contradicciones declaradas es una memoria que finge estar al día.

## Lo que `futuro/` no copia, y por qué

| Qué | De dónde | Por qué no se copia |
|---|---|---|
| los 68 procesos de `Ouroboros/` | `Ouroboros/` | **se citan, no se copian:** una copia envejece y miente |
| el paper y las fuentes | `MEGA/mme/publicable/` | viven en la idea; `futuro/` es la entrega |
| las 217 filas | `mantis.db` | la memoria se lee en su sitio: no se mueve a un documento |
| las 5 rutas rotas | `Ouroboros/` | se declaran como faltante en `CAMINO.md`; reparar es trabajo del tramo 4, no de la entrega |

## Prueba

**¿Cada línea de `futuro/` tiene origen y nivel? ¿Lo que está en N5 se declara? ¿Las contradicciones entre la memoria y el archivo están escritas? ¿Alguna pieza de `futuro/` cita un archivo que no resuelve?**

**Falsificador:** una línea sin origen; un N5 presentado como N2; una memoria copiada como verdad; una copia de `Ouroboros/` que va a envejecer; una contradicción conocida y no declarada.
