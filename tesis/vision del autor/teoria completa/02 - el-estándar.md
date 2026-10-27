# 02. El estándar

## 02.1 La forma, y por qué se lee y no se explica

*De `formacion/FORMATO.md`.*

**La forma que se lee, no la que se explica.** **Si un programa no puede leer un `.vd`, un `.tra` o un `.prs` sin adivinar, la forma no está fijada.**

**Y eso es todo lo que pide el formato: que se pueda leer sin adivinar.** **No pide una plantilla, ni un tamaño, ni una extensión concreta por oficio. Pide que dos personas —o una persona y una máquina— saquen lo mismo de lo mismo.**

## 02.2 La claridad, que es el estándar de lo que se escribe

*De `formacion/CLARIDAD.md`.*

**No se ejecuta: se cumple.** **Dice cómo tiene que ser un artefacto para que el lector lo entienda de una sola lectura.**

**Y el repo lo cumple de la forma más difícil de fingir:** **cada pieza dice qué entra, qué la deja mal, qué sale, y a quién consume.** **Si falta uno, la pieza no está escrita: está empezada.**

## 02.3 Los seis verbos, y los tres que son la ley

*De `formacion/EJECUTOR.md`.*

> **Un ejecutor no es un programa para correr tareas: es una lista de seis verbos con su firma.** **El que se salte uno no es un ejecutor: es una mano que corre solo.**

**Y no nombra lenguaje.** **Se puede escribir en lo que sea, o no escribirse: una IA lo cumple leyendo esto.** **Lo que no se puede es inventarse un séptimo verbo sin decirlo.**

| # | Verbo | Entra | Sale | Se salta si |
|---|---|---|---|---|
| **1** | **`LEER`** | el `.tra` de una tarea | los cuatro campos, o `[SIN CORTE]` | no hay corte: **no se inventa** |
| **2** | **`BUSCAR`** | el nombre de la tarea, y **el piso del mundo** | con qué se cumple, o `[FALTA EN bin/]` | **no se busca fuera del piso** |
| **3** | **`ENSAYAR`** | el corte, y **el modo que la tarea declara** | `pasa` o `[SIN ENSAYO]`, y por qué | **el silencio no es permiso** |
| **4** | **`CORRER`** | con qué, y los cuatro campos **como texto** | la salida, y si salió bien | **el ejecutor no toca lo que no le dieron** |
| **5** | **`DEJAR`** | la salida | `rastro.tra`, la memoria, y la huella del corte | **sin esto no hay prueba: corrió y no pasó** |
| **6** | **`NEGARSE`** | por qué no | una negativa **firmada**, y **no corre** | **sin esto todo corre, y ese es `AM`** |

**Y tres son la ley: `ENSAYAR`, `DEJAR` y `NEGARSE`.**

> **Un ejecutor sin `DEJAR` es un absoluto que corre; sin `ENSAYAR` es uno que rompe antes de saber qué rompía; sin `NEGARSE` es uno que siempre puede.**

### Y el tercero, que es el que da el nombre a todo esto

**`ENSAYAR` es la regla que impide lo de la urna.** **Alguien que ve una urna de cenizas y la toma por un salero no es más fuerte: es alguien que tocó sin leer.** **Y con toda la capacidad, la urna queda en el suelo.**

> **El niño mira antes de agarrar.**

**Y `NEGARSE` no es un muro: es una pregunta de tres líneas.** **`[MOTIVO] no sé qué es…` · `me falta: …` · `y espero: …`** **La tercera no es adorno: parar sin decir qué se espera es quedarse quieto, no frenar.**

## 02.4 El piso: lo que un mundo declara, y cómo se le mide

*De `formacion/PISO.md`.*

> **Un mundo no dice lo que puede: dice lo que puede, y se le mide antes de creerle.**

**Seis capacidades, y ninguna nombra lenguaje ni dominio:**

| # | Capacidad | Qué es | Cómo se prueba |
|---|---|---|---|
| **1** | **`leer`** | **traer el contenido de algo que ya existía** | **leer el propio `RUTA.md`, y que coincida** |
| **2** | **`escribir`** | **dejar algo que otro pueda leer después** | **escribir un archivo, y volver a leerlo** |
| **3** | **`ejecutar`** | **que algo corra, y que devuelva si salió bien** | **correr un paso que diga qué salió** |
| **4** | **`medir`** | **contar el tiempo, lo que cuesta, o cuántas veces** | **medir la prueba de arriba** |
| **5** | **`fuera`** | **traer algo que no estaba en el mundo** | **puede faltar: se declara** |
| **6** | **`entre_turnos`** | **que algo siga corriendo cuando el ente no lo mira** | **puede faltar: se declara** |

**Y la regla que las vuelve un piso y no una promesa:** **una capacidad no declarada no existe; una declarada sin prueba, tampoco.** **Si un corte necesita algo que el mundo no tiene, se dice `[FALTA EN EL PISO]`, y no se corre.**

**Python no es una capacidad: es con lo que este mundo cumple una.** **Otro mundo lo cumplirá con otra cosa, y esa es la diferencia entre un estándar y un lenguaje.**

## 02.5 La integridad, y qué falta

*De `formacion/INTEGRIDAD.md`.*

**No es que cada archivo esté completo: es que el sistema no tenga agujeros.**

**Y eso es lo que hace que este documento se pueda escribir sin inventar:** **cuando algo no está, se dice que no está, y con qué nombre.** **Un documento que rellena sus huecos con prosa es un documento que nadie puede contestar.**

## 02.6 La fricción: lo que impide cagarla

*De `friccion/`. Cinco piezas, y cada una con su acto.*

| Pieza | Qué hace | Su borde |
|---|---|---|
| **`PISO`** | **medir de forma repetible** | **lo que no se mide, no se dice** |
| **`FIRMAR`** | **que la fricción quitada quede firmada** | **no se quita sin firma** |
| **`JONN`** | **recordar que un candado se abre** | **un candado que no se abre se vuelve ruido** |
| **`GUANTELETE`** | **tocar lo que otro sostiene, y que se vea** | **lo que no se ve, no se tocó** |
| **`DAR VOZ`** | **hablar por el que no puede, sin llenarle el hueco** | **una voz que sustituye al que se fue no lo representa** |
| **`JURAR`** | **frenar, y decir qué falta** | **parar sin decir qué se espera no es frenar** |

**Y `DAR VOZ` tiene dos figuras, y las dos dicen lo mismo:** **el tío Iroh, de *Avatar: The Last Airbender* (DiMartino y Konietzko; Nickelodeon, 2005-2008), que perdió a su hijo en la guerra, dejó la guerra, y el día del cumpleaños de su hijo llegó a su tumba a cantarle.** **Y Martian Manhunter, el último de su especie.** **Los dos hablan por los que no están, y ninguno les llena el hueco.**

## 02.7 La salida: qué se le deja al otro

*De `salida/`.*

| Pieza | Qué dice |
|---|---|
| **`ALAS`** | **el lugar entre hablarle a un humano y hablarle a un modelo** — **lo que no se explica, se muestra** |
| **`CONVIVIR`** | **convivir sin volverse el otro ni someterlo** |
| **`VIGA`** | **el registro de la alineación** |
| **`CONTEXTO`** | **de dónde viene cada cosa, y cómo se usó** |
| **`RESULTADOS`** | **sin archivo no hay resultado** |
| **`la fila verbalizada`** | **las seis partes de toda salida** |

**Y `ALAS` tiene la línea que sostiene todo el resto, y no es una metáfora:**

> **Lo que no se explica, se muestra.**

**Y `CONVIVIR` tiene el estándar que no es el del que puede más:** **Videl, de *Dragon Ball* (Akira Toriyama; Shueisha; anime de Toei Animation), nunca fue tan poderosa como los sayayin, y como quiera encaja.**

## 02.8 Y la función, que es lo que todo esto sostiene

> **El estándar no dice cómo se escribe. Dice qué se tiene que poder contestar.**

**Y las cuatro palabras, otra vez, porque son el resumen de la sección entera:**

**mirar (`ENSAYAR`) · pesar (`EQUILIBRIO`) · tocar (`GUANTELETE`) · dejar rastro (`DEJAR`).**

**Se puede seguir con LaTeX, con un papel, con un video, o con lo que la gente invente.** **La prueba no es que se haya seguido la forma: es que alguien más pueda contestar lo que se hizo.**

### Prueba de esta sección

**¿Cada pieza del idioma dice qué entra, qué la deja mal, qué sale y a quién consume? ¿Los seis verbos se pueden cumplir sin escribir una línea de un lenguaje? ¿El piso se mide antes de creerle?**

**Falsificador:** **una pieza del idioma sin uno de sus cuatro campos; un verbo que exija un lenguaje para cumplirse; un piso que declara lo que no puede.**

---
