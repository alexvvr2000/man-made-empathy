# FORMATO — la forma de un ente, una tarea y un proceso

**Qué es.** La forma que se lee, no la que se explica. Si un programa no puede leer un `.vd`, un `.tra` o un `.prs` sin adivinar, la forma no está fijada.

**Unidad:** formato.
**Aplica a:** escribir y leer.
**Tipo:** estándar. Se cumple; no se interpreta.
**Lector:** quien escribe un ente, una tarea o un proceso, y quien lo va a leer con un parser.
**Dueño:** humano:Alejandro Valenzuela Rivera.
**Estado:** vigente.

**Sesgo:** la forma se lee desde el que la va a recorrer, no desde el que la escribió.
**Límite:** no dice qué va en cada campo. Dice cómo se reconoce un campo.
**Firma:** humano:autoridad · máquina:quien lo lea.

## La regla que hace legible un archivo

> Todo campo es una línea que empieza por `**Campo:**` y una palabra en negrita, y sigue con un valor. Una tabla es una línea que empieza por `|`. Un bloque es lo que está entre dos ```.

**Y nada más.** Un archivo que no cabe en esas tres marcas no es legible por parser: se lee a mano, y se declara.

## La forma del ente: `.vd`

```
# <EL NOMBRE> — <lo que es>

**Nombre.** <el nombre>. <la expansión del acto, citable>.
**Unidad:** ente.
**Aplica a:** <verbo>.
**Tipo:** <base | raíz | tarea>.
**Lector:** <quién lo abre>.
**Dueño:** humano:autoridad.
**Estado:** <vigente | primitivo | esqueleto>.

**Sesgo:** <desde dónde mira>.
**Límite:** <a qué no alcanza>
**Firma:** humano:autoridad · máquina:<quien>.

**Variables:** <a> · <b> · <c>
**Peor:** <qué se pierde si falla>
**Quién:** <quién lo paga>

## Rastro — el cuerpo
## Ruta — la mente
## Carga — el pensamiento
## Prueba
## Falsificador
## Transiciones
```

**Las tres secciones de Rastro, Ruta y Carga son obligatorias.** Si falta una, es fantasma, y el parser lo dice: `[FANTASMA - FALTA CARGA]`.

## La forma de la tarea: `.tra`

```
**Nombre:** <el de hoy>
**Expande:** <el acto que ocurrió>
**Se nombró:** <el instante>
**Reemplaza:** <el anterior, o NINGUNO>
**Miente si:** <qué acto no ocurrió>

**Qué pasó:** <la frase dicha>
**Contra:** <qué la contradijo, o ninguno>
**Huella:** <dónde quedó>
**Distancia:** <qué cambió>

**Procesos:** <a.prs> · <b.prs>
**Ficción:** <de dónde viene, o ninguna>
**Falta:** <qué no se pudo hacer>
```

**Las tres primeras son el nombre.** **Sin `Nombre`, la tarea no tiene rastro: el parser no la puede cifrar.**

## La forma del proceso: `.prs`

```
# <NOMBRE>.prs — <lo que hace>

**Nombre.** <NOMBRE> — <A> <B> <C>. Se lee de un tirón.

**Unidad:** proceso.
**Aplica a:** <verbo>.
**Tipo:** se ejecuta.
**Lector:** <quién lo corre>.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** <desde dónde mira>.
**Límite:** <a qué no alcanza>
**Firma:** humano:autoridad · máquina:quien lo corra.

**Variables:** <a> · <b> · <c>
**Peor:** <qué se pierde>
**Quién:** <quién lo paga>

## Entra | Falla | Sale | Consume

- **Entra:** <qué recibe>
- **Falla si:** <el caso que lo incumple>
- **Sale:** <qué emite>
- **Consume:** <quién decide con la salida>
```

**Y lo que la salida del proceso debe cumplir:** **la fila verbalizada, con sus seis campos:** `Sostengo`, `Ficción`, `Contra`, `Rastro`, `Siguiente`, `Borde`. **Ese formato lo hace `EXPRESION.prs`.**

**Y lo que un `.prs` no lleva:** el cómo. **Un `.prs` declara qué entra y qué sale; cómo se logra es el piso.**

## Lo que el parser hace con cada campo

| Marca | Qué es | Qué hace el parser si falta |
|---|---|---|
| `**Nombre.**` o `**Nombre:**` | la identidad del archivo | `[SIN NOMBRE]`, y no lo indexa |
| `**Unidad:**` | ente, proceso o tarea | `[SIN UNIDAD]` |
| `**Sesgo:**` | desde dónde mira | `[IMPLÍCITO - SIN SESGO]` |
| `**Límite:**` | a qué no alcanza | `[IMPLÍCITO - SIN LÍMITE]` |
| `**Firma:**` | quién responde | `[SIN FIRMA - NO SE ABRE]` |
| `## Rastro` · `## Ruta` · `## Carga` | las tres piezas | `[FANTASMA - FALTA <X>]` |
| `- **Entra:**` y sus hermanos | el corte del proceso | `[ACTIVIDAD - SIN CORTE]` |

**Ninguno se completa por defecto.** Un campo que falta **se declara ausente**, y un archivo que declara una ausencia es más útil que uno que la esconde.

## Por qué esta forma, y no otra

Sin forma, hay tres problemas que ya ocurrieron en este repo: preguntarle al autor qué quiso decir; dos archivos que dicen lo mismo con nombres distintos; y una carpeta que no sabe qué proceso corre.

Una forma fija resuelve los tres, y hay un cuarto problem que resuelve: permite que un programa diga qué falta, sin que nadie lo revise a mano.

## Lo que este formato no hace

No dice si el ente sirve. No dice si el proceso es bueno. No dice si la tarea fue correcta.

Dice que el archivo se puede leer sin adivinar.

## Prueba

¿El archivo se puede recorrer campo por campo? ¿Las tres piezas son secciones? ¿La firma y el sesgo están? ¿El corte del proceso está completo? ¿Un programa lo lee sin adivinar?

## Falsificador

Un archivo que se explica en prosa; dos campos con el mismo nombre; una sección de Rastro sin Ruta; un proceso sin `Falla si`; un campo que se completa por defecto.

## Transiciones

- Un archivo nuevo no cabe en la forma → se declara `[FUERA DE FORMA]`, y se nombra qué marca falta.
- La forma cambia → se suplanta este formato, y todos los archivos se revisan en la siguiente pasada.
- Un parser no puede leer un archivo que sí sigue la forma → el error es del parser, no del archivo.
