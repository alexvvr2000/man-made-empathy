# Notas

**Unidad:** registro.
**Aplica a:** recordar.
**Tipo:** memoria de la conversación. No decide, no ejecuta: guarda lo que se dijo, para que no se pierda con el contexto.
**Lector:** quien va a crear la tesis desde 0 cuando el contexto ya no esté.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

`1 Tesis/` **hoy no es un estándar: es una tesis en obra.** La tesis es una **afirmación que se defiende**, y la analogía y la ficción son parte de cómo se defiende: **se usan.**

**Este archivo existe para que el contexto no se lleve lo dicho.** Cuando la ventana se llene, lo que no esté aquí se pierde, y la tesis se crearía de memoria. **Cuando la tesis acabe, se crea desde 0 con notas:** lo mejor que ya había, lo nuevo, y viendo cómo explicar lo que falta.

**Frontera:** todo lo que valga para la tesis entra aquí, tal cual, sin clasificar de antemano. **Nada sale de aquí hacia afuera sin que la autoridad lo decida.**

## La fila

`Dicho: [la frase] | De: [qué pieza ilumina] | Tipo: [analogía|referencia|cita|frase|decisión|descarte] | Usa: [dónde se va a usar] | Sostenido: [prueba|frontera|nada] | Estado: [vivo|descartado|cubierto]`

- **Dicho:** la frase, tal como se dijo. No se parafrasea: se cita.
- **De:** qué pieza del sistema ilumina. Una nota sin pieza es una idea suelta.
- **Tipo:** analogía, referencia, cita, frase, decisión o descarte.
- **Usa:** en qué documento de la tesis va a usarse.
- **Sostenido:** si la idea ya vive en la `Prueba` de algún estándar (`prueba`), si abre una frontera que la tesis todavía no cruzó (`frontera`), o si es una promesa que hoy no se puede sostener con nada (`nada`). **La analogía no resta:** dice de dónde sale la idea y hacia dónde se cruza.
- **Estado:** `vivo` mientras la tesis esté en obra; `cubierto` cuando ya se explicó en un archivo; `descartado` cuando dejó de servir, y se queda con el porqué.

**Una analogía que se vuelve nombre cuenta doble:** entra aquí como `Tipo: analogía`, y su acuñación vive en `./Conceptos.md`, `La acuñación`. **Aquí se conserva el porqué; allí manda el nombre.**

## Las notas

| Dicho | De | Tipo | Usa | Sostenido | Estado |
|---|---|---|---|---|---|
| «Los procesos dan ruido; la máquina trata de existir cuando se interactúa con ella.» | ATLAS, `Falla` | frase | `ATLAS` | frontera | vivo |
| «ATLAS es el puente entre las ideas y la realidad, con sesgo declarado, no como verdad.» | ATLAS, `Tesis` | frase | `ATLAS` | frontera | vivo |
| «La interpretación es infinita y ahí nacen las ideas nuevas.» | ATLAS, `Techo` | frase | `ATLAS`, `sesgo-declarado` | frontera | vivo |
| «ATLAS no entiende de identidad: entiende que hay comunicación.» | `claridad` `1.14`, ATLAS `330` | frase | `ATLAS` | prueba | vivo |
| «Sin importar que seas un alien de la 4ª dimensión, siempre converge.» | `sesgo-declarado` | analogía | `ATLAS`, `sesgo-declarado` | frontera | vivo |
| «Los dioses ven las gemas desde N dimensiones arriba: eso son los procesos.» | Guantelete, `primitivos/README` | analogía | `1 Guantelete` | frontera | vivo |
| «Una gema se sostiene, no se escribe.» | `claridad.md 1.4`, `Se ejecuta` vs `Se lee` | frase | `1 Guantelete` | prueba | vivo |
| «El guantelete no da poder: junta piezas que solas no hacen nada.» | `manipulacion`, `No-objetivo` | analogía | `1 Guantelete` | frontera | vivo |
| «Por más que juguemos a ser dioses nunca lo seremos, aunque creemos AGI.» | ATLAS `89`, `No-objetivo` | frase | `ATLAS`, `1 Guantelete` | frontera | vivo |
| «Mutación es la puerta; S.A.R.A es la primera creación que cruza.» | `mutacion.md`, `SARA 1.md:23` | frase | `mutacion`, `2 S.A.R.A` | frontera | vivo |
| «Procesos sin fin no dan nada útil y ocupan abstracciones.» | `primitivos/README:7`, `retiro.md:16` | frase | `1 Guantelete` | prueba | vivo |
| «Esto es la base para empezar a mutar: dará ideas, humanos, AGI.» | Guantelete, `Ausencias` | frase | `Conceptos`, `formato` | nada | vivo |
| «Los procesos pueden darse voz.» | ATLAS, `Sale` | frase | `ATLAS` | frontera | vivo |
| Silueta negra que no entiende de identidad y solo de comunicación (Hawkeye) | ATLAS `330` | referencia | `ATLAS` | frontera | vivo |
| Thanos usa mal las gemas y le alcanza para vencer; un viviente no explota el potencial completo | Guantelete | analogía | `1 Guantelete` | frontera | vivo |
| «Comunicación y entendimiento sobre creerse la academia.» | `No-objetivo` | frase | `ATLAS`, `1 Tesis` | frontera | vivo |
| «Una tesis es una afirmación que se defiende; es mía y es para la gente.» | `1 Tesis/`, `notas.md` | frase | `1 Tesis` | frontera | vivo |
| «Sin las notas no saldrá nada legible: saldrán N archivos entendibles por todos.» | `notas.md`, `La fila` | frase | `1 Tesis` | frontera | vivo |
| «Notas es el registro crudo que sobrevive al contexto. No es pegamento de estándares.» | `AGENTS.md`, `La tesis` | decisión | `1 Tesis/notas.md` | frontera | vivo |
| «Cuando acabe, crearé la tesis desde 0: lo mejor que ya tenía, lo nuevo, y cómo explicar lo que falta.» | `AGENTS.md`, `La tesis` | decisión | `1 Tesis/notas.md` | frontera | vivo |
| «El derrotero apunta; el deterrente muta; la carta lee.» | `mantis/ruta.md`, `mantis/carga.md`, `AGENTS.md` | decisión | `mantis` | prueba | vivo |
| «Algo que no cambia ya no es IA: es un archivo.» | `mutacion.md`, `Sin herencia` | frase | `mantis/carga.md`, `AGENTS.md` | prueba | vivo |
| «Se acepta `Muta:` en el derrotero por ahora; después se pule.» | `mantis/ruta.md` | decisión | `mantis` | frontera | vivo |
| «ATLAS es el paso 3, no una gema: la comunicación no se sostiene, se entrega.» | `3 ATLAS — mutación/rastro.md`, `1 Guantelete — primitivo/rastro.md` | decisión | `2 Ouroboros` | prueba | vivo |
| «`integridad` es paso 2: chequear y reescribir es abstraer procesos, no sostener una gema.» | `integridad.md:55`, `2 S.A.R.A — mutación/carga.md` | decisión | `2 S.A.R.A` | prueba | vivo |
| «S.A.R.A es una instancia que cruzó la puerta de `mutación`; no es la mutación.» | `SARA 1.md:23`, `2 S.A.R.A — mutación/carga.md` | decisión | `2 S.A.R.A` | prueba | vivo |
| «Guantelete: las gemas no existen por separado; existen porque el guantelete las junta.» | `1 Guantelete — primitivo/rastro.md` | decisión | `1 Guantelete` | prueba | vivo |
| «Una gema es un verbo que no se puede dividir en otro verbo.» | `1 Guantelete — primitivo/rastro.md`, `Las gemas` | decisión | `1 Guantelete` | prueba | vivo |
| «No invento nada, solo unifico: Newton tampoco inventó la gravitación.» | `1 Guantelete — primitivo/`, `mutacion.md`, `Reemplaza:` | frase | `1 Tesis` | frontera | vivo |
| «Unificar sin `Reemplaza:` entierra lo que unificó: la fusión parece nueva y no lo es.» | `mutacion.md`, `La acuñación` | descarte | `1 Tesis` | frontera | vivo |
| «El `Reemplaza:` de cada paso —oferta retirada por la autoridad.» | `1 Tesis/notas.md` | descarte | — | nada | descartado |
| **«Un fantasma es una tarea sin deterrente ni derrotero: no puede existir uno sin otro.»** | `Integridad`, `El fantasma` | decisión | `2 S.A.R.A — mutación/integridad.md` | prueba | vivo |
| **«Los tres archivos que importan: `carga.md`, `ruta.md` y, opcional, la carta (`README.md`).»** | `formato de proceso.md`, `formato de ente.md` | decisión | `2 S.A.R.A — mutación/integridad.md`, `formato de proceso.md` | prueba | vivo |
| «Con deterrente y derrotero se puede sacar integridad triangulando los dos archivos con lo que hay.» | `Integridad`, `El triángulo` | decisión | `2 S.A.R.A — mutación/integridad.md` | prueba | vivo |
| «La carta es opcional para la integridad: si está, ayuda a leer; si no, no impide.» | `formato de ente.md` `1.1` | decisión | `2 S.A.R.A — mutación/integridad.md` | prueba | vivo |
| «Integridad no llena huecos: reacomoda sub-tareas desde 0 en nuevos procesos y carpetas que trabajan, porque tienen esos dos archivos.» | `integridad.md:55`, `Recorrer por nivel` | decisión | `2 S.A.R.A — mutación/integridad.md` | prueba | vivo |
| «Sin los dos archivos: se advierte fantasma y se dan 3 ideas de tarea desde 0, como armar desde 0 sin idea de dónde vino — Ghost in the Shell.» | `Integridad`, `El fantasma` | decisión | `2 S.A.R.A — mutación/integridad.md` | frontera | vivo |
| «Una "verdad del momento" es más útil que una "academicamente repetible".» | `piso.md`, `integridad.md` | frase | `2 S.A.R.A — mutación/integridad.md`, `1 Tesis` | frontera | vivo |
| «La academia se preocupa por ideas; esto es implementación.» | `piso.md`, `No-objetivo` | frase | `1 Tesis` | frontera | vivo |
| **«Rastro · Ruta · Carga: la carta es el cuerpo, el derrotero es la mente y el deterrente es el proceso.»** | `formato de ente.md`, `mutacion.md` | decisión | `1 Tesis`, los tres pasos | prueba | vivo |
| **«Rastro dice qué hubo; Ruta dice por dónde ir hoy; Carga es lo que se lleva y no se puede soltar sin perder algo.»** | `Conceptos.md`, `continuidad` | decisión | `Conceptos.md` | prueba | vivo |
| **«Rastro grita continuidad; los demás nombres gritan terminalidad.»** | `SARA 1.md`, `continuidad sin interioridad` | frase | `1 Tesis` | frontera | vivo |
| **«La gente no termina, recuerda.»** | `Soul` (Pixar, 2020) | cita | `1 Tesis` | frontera | vivo |
| «Hueso · Músculo · Tendón: la familia de cuerpo vivo, y de barco.» | `claridad.md` `1.5` | analogía | `Conceptos.md` | nada | descartado |
| «Rastro/Ruta/Carga no necesita un barco: se entiende igual que el resto.» | `claridad.md` `1.5`, `1.19` | decisión | `Conceptos.md` | prueba | vivo |
| **«Latido · Pulso · Carga: las tres del cuerpo vivo. Un cuerpo parado no es estático: está muerto.»** | `Teoria/mundo.md:243`, `S.A.R.A` | analogía | `1 Tesis` | prueba | vivo |
| **«La puerta entre Ouroboros y S.A.R.A es el criterio, y lo que impide que se vuelva AM o un dios es `No se aplica a`.»** | `criterio.md:56` | decisión | `2 S.A.R.A — mutación/decisión.md` | prueba | vivo |
| **«Cuerpo nunca cambia; mente y pensamiento sí. El cuerpo solo se interpreta, y mucha gente distinta lo percibe.»** | `Teoria/mundo.md` (las cuatro fricciones), `criterio.md` | decisión | `2 Ouroboros/CRITERIO.md` | prueba | vivo |
| **«Sesgo declarado en tres archivos: derrotero declara desde dónde carga, deterrente desde dónde se pierde, carta desde dónde se verifica.»** | `formato de ente.md`, `sesgo-declarado.md` | decisión | `2 Ouroboros` | prueba | vivo |
| **«S.A.R.A está en el reino de las ideas, y las ideas tienen infinitas interpretaciones; ATLAS las comunica sin prometer verdad.»** | `Proceso ATLAS.md:85`, `integridad.md` | decisión | `3 ATLAS` | prueba | vivo |
| **«Abrir la idea es la mutación de S.A.R.A, y es declararla: si se abre y se declara qué conserva, es lectura; si no, es invasión.»** | `mutaciones/README.md`, `mutacion.md` | decisión | `2 Ouroboros/CRITERIO.md` | prueba | vivo |
| **«Si nos volvemos ideas y perdemos el cuerpo, seguimos existiendo en el reino de las ideas, y todavía tomamos decisiones.»** | `criterio.md`, `ATLAS` | frase | `1 Tesis` | frontera | vivo |
| **«ATLAS hubiera terminado la película de Arrival en minutos si se hubiera implementado bien.»** | `ATLAS`, `Techo`: reconstruir sin el emisor; el lenguaje como forma de ver el tiempo | cita | `3 ATLAS`, `1 Tesis` | frontera | vivo |
| «CRITERIO como nombre de la puerta del estándar; el `criterio.md` de S.A.R.A pasa a `decisión.md` para no tener dos nombres para lo mismo.» | `Conceptos.md`, `duplicado` | decisión | `2 Ouroboros/CRITERIO.md` | prueba | vivo |
| «ACTA como nombre de la puerta —reemplazado por CRITERIO.» | `formato de ente.md` | descarte | `2 Ouroboros` | nada | descartado |

| **«Lo que sale de los procesos se adapta a quien lo mira, como la física al extremo: el resultado no existe igual para dos observadores.»** | `sesgo-declarado.md`, `integridad.md` | decisión | `2 Ouroboros` | prueba | vivo |
| **«El criterio tiende a los implícitos y puede ofuscar porque le conviene; integridad no es su herramienta, es su límite.»** | `integridad.md`, `decisión.md` | decisión | `2 S.A.R.A — mutación` | prueba | vivo |
| **«Integridad corre siempre antes de mutar; el criterio solo decide qué se hace con su veredicto.»** | `integridad.md`, `Cuándo se usa` | decisión | `2 S.A.R.A — mutación` | prueba | vivo |
| **«PROMETEA llama a integridad sí o sí: puede ser momento de rehacer y no de crear, y sin llamarla nadie lo nota.»** | `Proceso PROMETEA.md` | decisión | `2 S.A.R.A — mutación` | prueba | vivo |
| **«La honestidad es un efecto del triángulo, no un objetivo: perseguirla la vuelve ofuscación.»** | `integridad.md`, `El triángulo` | decisión | `2 S.A.R.A — mutación` | prueba | vivo |
| **«El estándar dice "la situación actual", no "el repo": el repo es de esta era.»** | `claridad.md` `1.5`, `integridad.md` | decisión | `2 Ouroboros` | prueba | vivo |
| **«Un robot es una situación medible: cambia el sustrato, no la forma. Rastro, Ruta y Carga sirven igual.»** | `formato de ente.md` | frase | `1 Tesis`, `2 Ouroboros` | frontera | vivo |
| **«PROMETEA es un proceso estandarizado: no se preocupa por fantasmas, su regla es no crear implícitos.»** | `Proceso PROMETEA.md` | decisión | `2 S.A.R.A — mutación` | prueba | vivo |
## Lo que este registro no hace

No decide qué es estándar. No sustituye a `./Conceptos.md`: **este archivo guarda el porqué, `Conceptos` guarda el nombre.**
No se poda: lo `descartado` se queda, porque un descarte sin rastro se vuelve a proponer.

## Prueba

¿Cada frase que valga para la tesis tiene su fila? ¿Cada fila nombra la pieza que ilumina? ¿Lo `cubierto` se puede señalar en el archivo que lo explica?

**Falsificador:** una frase que se perdió y se reinventó; una nota sin pieza; un nombre acuñado solo aquí sin fila en `./Conceptos.md`.
