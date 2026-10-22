# Proceso de integridad de procesos

**Reemplaza:** `Proceso de integridad para procesos hermanos`. La 4ª pregunta chequea un proceso contra su propio implícito, no contra un par; el nombre viejo dejaba de ser exacto.

**Unidad:** tarea.
**Aplica a:** chequear.
**Tipo:** proceso de nivel 0. No produce, no ejecuta: chequea lo que otros produjeron.
**Lector:** quien está por mutar el sistema, y quien lo audita después.
**Nivel:** 0 de 3. Por encima de las tareas. No las gobierna: las **chequea**.
**Alcance:** todo proceso, solo o comparado con sus hermanos.
**Dueño:** la autoridad.
**Estado:** vigente.

**Forma:** `Entra | Falla | Sale | Consume`.
**Norma:** `Tipo | Enunciado | Prueba | Falsificador | Costo de omitir`.

## Tesis

Los procesos hermanos no se ven entre sí. Cada uno cumple su regla, y **dos reglas que se cumplen por separado pueden ser incompatibles juntas.**

Y cada proceso, solo, puede servir sin que esté escrito **qué tiene que cumplirse para que sirva.** Las dos cosas se chequean aquí.

El nivel 0 no es "un proceso de procesos": eso ya es `./Proceso de creación de procesos.md`. Es más chico y más raro: **es el chequeo que corre sobre lo que ya existe, antes de que la incompatibilidad o el implícito salgan a la superficie.**

**Niveles negativos no sirven.** Nada por debajo de esto: se pasa del chequeo al inmueble, y lo inmueble no tiene falsificador.

## Lo que impide crecer por crecer

Este proceso no solo encuentra faltas: **fija cuándo una pieza está completa.**

> Un proceso está completo cuando **todo lo que tiene que cumplirse para que sirva está escrito dentro.**
> Una sub-tarea está completa cuando **sus procesos no dependen de un implícito que viva en otra.**

Sin ese límite, el formato `tarea → sub-tarea × N → proceso × N` no tiene fondo: cada cosa entra a su caja y la caja nunca se llena. **Agregar deja de ser crecimiento y pasa a tener que justificar completitud.**

## Por qué es nivel 0, y no el nivel de arriba

El nivel de arriba (metalenguaje) **produce**. El nivel 0 **chequea**. Son opuestos:

| Nivel de arriba | Nivel 0 |
|---|---|
| produce procesos nuevos | no produce nada |
| sube cuando lo de abajo no alcanza | **baja: opera sobre lo que ya está escrito** |
| se juzga por lo que produce | se juzga por **lo que encuentra** |
| un proceso | un **chequeo**, que puede no encontrar nada y aun así haber servido |

Y por eso el chequeo no es de hijos: **no es superior a lo que chequea.** Es una pasada.

## Entra | Falla | Sale | Consume

**Entra:** uno o más procesos — solos o con sus hermanos — y sus enunciados con `Prueba` y `Falsificador`.
**Falla:** dos hermanos se contradicen y nadie lo ve; una tarea es en realidad sub-tarea de otra; un proceso no lo carga nadie; un proceso sirve solo bajo una condición que no está escrita; el chequeo se hace después de que el problema ya produjo daño.
**Sale:** la incompatibilidad, el huérfano y el implícito, o la declaración de que no hay ninguno.
**Consume:** quien iba a mutar el sistema. **Si hay incompatibilidad o un implícito que la sostiene, no muta hasta resolverlo.**

## Cuándo se usa

**Antes** de mutar, y **después** de una serie. Nunca durante: un chequeo a medias no encuentra lo que busca.

## Proceso

### 1. Agrupar por padre

Solo se comparan hermanos: los que cuelgan del mismo padre. Un proceso y su padre no se contradicen: se especializan.

**La 4ª pregunta no necesita par:** corre igual sobre un proceso solo, y por eso este paso puede dejar Hermanos: 1.

```
Padre: [cuál] | Hermanos: [n] | Se comparan: [n(n-1)/2 pares]
```

### 2. La doble barrida

Dos pasadas, y no es redundancia: es el mismo principio que un chequeo en la base y otro en la API. **Cada uno ve lo que el otro no puede ver.**

| Pasada | Qué mira | Qué encuentra | Qué no ve |
|---|---|---|---|
| **1. Del enunciado** | qué obliga cada uno | la contradicción declarada | lo que se contradice sin decirlo |
| **2. De la salida** | qué produce cada uno | lo que choca en la práctica | la contradicción que nunca se ejecutó |

**Pasada 1 — el enunciado.** Se ponen los dos `Enunciado` uno al lado del otro y se pregunta: **¿puede un mismo acto cumplir los dos?**

**Pasada 2 — la salida.** Se ponen las dos `Sale` y se pregunta: **¿lo que produce uno puede ser inservible para el otro?**

Si las dos pasadas coinciden, se cierra. Si discrepan, **la discrepancia es el hallazgo.**

### 3. Las cuatro preguntas que vale la pena verbalizar

Las tres primeras comparan **pares**. La cuarta corre sobre **un proceso solo**.

| # | Pregunta | Qué detecta | Señal de falla |
|---|---|---|---|
| **1** | ¿Un mismo acto puede cumplir los dos? | contradicción de regla | el acto que cumple a uno incumple al otro |
| **2** | ¿Este proceso pertenece a otro? | sub-tarea disfrazada | su entrada es la salida de otro y no lo declara |
| **3** | ¿Alguien carga este proceso? | huérfano | ninguna `Transición` ni `README` lo trae |
| **4** | ¿Qué tiene que cumplirse para que esto sirva, y no está escrito? | **el implícito** | lo tomado sin lo que lleva |

**La 2 es la que más pesa entre pares:** una tarea que es sub-tarea y no lo sabe **trabaja doble y contradice sin que nadie la vea.** Es el modo de falla que no se nota porque cada mitad parece correcta.

### 4. La 4ª pregunta — el implícito

Esta no compara. Corre **sobre un proceso solo**, y por eso el chequeo ya no es solo de hermanos.

**El modo de falla que detecta:** se toma una característica nueva sin los implícitos de lo que lleva tenerla. El proceso hace lo que dice y **faltan las condiciones que lo hacían servir.**

Casos reales de este repo, todos encontrados después y ninguno escrito a tiempo:

| Se tomó | Faltaba |
|---|---|
| la escala de `ayuda-no-pedida` | **el `Retiro`**: sin retiro, la ayuda se vuelve sustitución |
| que la fricción «obliga a contestar» | **que no puede imponer**: sin eso es coerción |
| `ATLAS` como primitive | **que es abstracción**: sin eso, afirma que el universo comunica |
| `N0` como nivel de fuente | **que exige consentimiento**: sin eso es extracción |

**Cómo se contesta.** No se pregunta «¿de qué proceso más grande forma parte?» — eso no tiene fondo, y lleva a inventar. Se pregunta:

> **¿Qué condición tiene que cumplirse para que este proceso sirva, y no está escrita adentro?**

**El hallazgo es el implícito, no el proceso faltante.** Un implícito se corrige con una línea; un proceso faltante inexistente se inventa. **Buscar el proceso de arriba produce ruido; buscar la condición olvidada produce el archivo.**

```
Implícito: [la condición] | Dónde falta: [sección del proceso] | Qué pasa sin ella: [el fallo]
Es de este proceso: [sí|no] | Si no: [a quién pertenece]
```

**Cuándo se descarta:** si el implícito no se puede señalar en un archivo, no es un implícito: es una tesis. Se descarta y se anota.

### 5. Declarar

```
Par: [a] × [b] | Acto común: [sí|no] | Contradice: [cuál|ninguna]
Pertenece a: [a→b|b→a|ninguno] | Carga: [quién|nadie]
Implícito: [la condición] | Falta en: [sección]
Pasada 1: [enunciado] | Pasada 2: [salida] | Coinciden: [sí|no]
```

**`Coinciden: no` se declara como hallazgo**, no se resuelve en silencio.

### 6. Resolver o declarar

- **Contradicción real** → uno de los dos se corrige, y se dice cuál y por qué.
- **Sub-tarea disfrazada** → se anida o se declara por qué quedó suelta.
- **Huérfano** → se declara; no se borra sin decidir.

**Prohibido resolver una contradicción borrando el chequeo.** Si el chequeo molesta, el que sobra es el proceso.

### 7. Acuñar el nombre de la corrida

**Todo muta: tarea, sub-tarea, subproceso y nombre.** Por eso una corrida no termina en veredicto: **termina en un nombre nuevo.**

Nombrar no es un adorno del reporte. **Es lo que obliga a verbalizar qué cambió**, y sin verbalizarlo la corrida no dejó criterio: dejó un resultado.

**Se acuña siempre, para lo que se chequeó**, sea tarea, sub-tarea o subproceso.

**La forma es la de** `./Proceso de mutación.md`, `Acta`. Se reusa, no se redefine:

```
Acta: [id] | Nombre: [nombre] | Expansión: [significado] | Origen: [hallazgo de esta corrida] | Fecha: [ISO]
Encargo: [qué se chequeó] | Fin: [estado observable del veredicto]
Muta: [qué cambió en la corrida] | Conserva: [qué no] | Ausencias: [qué no se pudo ver] | Prueba: [corrida|no corrida|pendiente]
Autoridad: [tipo:nombre] | Cierra en: [tipo:nombre] | Reemplaza: [nombre o NINGUNA]
```

**El nombre se lee como nombre propio; la expansión dice qué significa.** Un acrónimo que solo se puede leer deletreando no es un nombre: es una etiqueta.

**La regla que lo vuelve criterio:**

> **Un nombre que sirve para dos corridas distintas no nombra nada.** Si el mismo nombre sobrevive a un cambio, el cambio no se verbalizó.

**Sin hallazgo no hay acuñación.** Una corrida que no encontró nada acuña igual, pero su `Muta:` declara el estado: *«sin cambio: el piso aguantó»*. Lo que no se permite es acuñar como si hubiera habido un cambio.

**El nombre anterior no se borra:** se reemplaza con `Reemplaza:` y la razón. Rige `./Proceso de mutación.md`, `Sin herencia`.

**Prueba:** ¿la corrida acuñó nombre? ¿El nombre se lee como nombre propio? ¿`Muta:` declara el cambio real, o el estado si no hubo? ¿`Reemplaza:` apunta al anterior?

**Falsificador:** una corrida sin nombre; un nombre reusado de otra corrida; una expansión que deletrea el acrónimo; una acuñación sin `Reemplaza:`; un `Muta:` que dice «varios» sin nombrar ninguno.

## ATLAS al 100%

El chequeo no es una tabla: es una emisión. Y rige `../../corpus/ATLAS/Proceso ATLAS.md`:

| Pieza | Cómo se usa aquí |
|---|---|
| **Situación** | qué padre, cuántos hermanos, en qué momento del repo |
| **Participantes** | quiénes cargan esto, y qué autoridad tiene cada uno |
| **Atención conjunta** | los dos procesos miran el mismo acto, y el chequeo lo hace saber |
| **Piso** | qué hay escrito hoy: el texto, no la intención |
| **Techo** | el lector debe poder decir *cuál contradice a cuál* — o no se alcanzó |
| **Canal** | una tabla, no un ensayo: quien decide necesita el par, no la historia |
| **Sesgo** | desde qué versión del repo se chequeó, y qué quedó fuera |
| **Modo** | informar, no persuadir: el hallazgo no se defiende |
| **Fatiga** | se dice una vez por par; repetirlo no lo vuelve más cierto |

**El techo del chequeo es una frase:** *«este proceso incumple este otro, en este acto»*. Si el lector no puede decirla, el chequeo no llegó.

## Ancla

```
Chequeo: [id] | Padre: [cuál] | Pares: [n] | Procesos solos: [n] | Versión: [fecha del repo]
Hallazgos: [n] | Contradicciones: [n] | Disfrazadas: [n] | Huérfanos: [n] | Implícitos: [n]
Implícito: [la condición] | Falta en: [sección] | Qué pasa sin ella: [el fallo]
```

## Prueba

¿Se compararon los pares del mismo padre? ¿Las dos pasadas corrieron? ¿Cada hallazgo nombra el acto que se contradice? ¿El techo se alcanzó?

**Falsificador:** se compara un proceso con su padre como si fueran hermanos; corre una sola pasada y se llama doble; un hallazgo sin el acto que lo demuestra; un «coinciden: no» resuelto en silencio; un implícito que no se puede señalar en un archivo; se busca «el proceso más grande» en vez de la condición olvidada; se borra el chequeo porque encontró algo incómodo.

## Modos de falla

- **Barrida única.** Se corre la pasada del enunciado y se olvida la salida.
- **Contradicción declarada como opinión.** Se nombra el par, pero no el acto que lo demuestra.
- **Huérfano que se calla.** Nadie lo carga y no se dice.
- **Disfrazada que se anida sin declararlo.** Se mueve el archivo y no se dice por qué era sub-tarea.
- **Chequeo complaciente.** Corre, no encuentra nada, y nunca encuentra nada.
- **Implícito inventado.** Se declara una tesis como si fuera una condición, y se vuelve la abstracción que no vale.
- **Padre imaginario.** Se busca el proceso de arriba en vez de la condición olvidada, y se inventa un nivel que nadie pidió.

## Transiciones

- La contradicción está en un estándar → `../../mantis/mantenimiento/editar.md`, gana el estándar.
- El par no se entiende → `../Proceso de claridad.md`, `1.4`.
- Hace falta saber si una creación se sostiene → `./Proceso de creación de procesos.md`, `No-objetivo`.
- Falta el sesgo de la comparación → `../Proceso de sesgo declarado.md`.
- En cualquier otro caso → se entrega y se cierra.
