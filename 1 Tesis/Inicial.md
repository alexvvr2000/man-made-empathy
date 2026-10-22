# Corpus

**Unidad:** nivel.
**Aplica a:** estandarizar.
**Tipo:** estándar de estándares. No decide, no ejecuta, no enruta.
**Lector:** quien va a construir sobre este repo, y quien lo construyó hace seis meses.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es este nivel

Aquí viven las **formas**. No lo que hoy se hace — eso muta — sino **cómo tiene que ser algo para estar completo.**

Este nivel no existía, y su ausencia costaba caro: el estándar del derrotero vivía dentro de la instancia, y el de la comunicación vivía como si fuera un primitivo. **Un estándar guardado dentro de lo que estandariza no se puede ver como estándar.** Por eso cada lector nuevo tardaba en entender qué se le pedía.

## Los tres niveles

| Nivel | Responde | Qué contiene | Cambia cuando | Si desaparece |
|---|---|---|---|---|
| **Estándar** | ¿cómo tiene que ser? | este nivel: `corpus/` | casi nunca | no se sabe cuándo algo está bien hecho |
| **Instancia** | ¿qué se hace hoy? | `Ouroboros/`, `S.A.R.A/`, `mantis/` — **instancias de este corpus** | siempre | el estándar queda sin efecto |
| **Era** | ¿con qué se hace? | `Agentes/` | cuando cambia la era | el estándar sigue intacto |

**Las tres carpetas de instancia no son hermanas de `corpus/`: son instancias suyas.** Aplican la forma; no la definen.

| Instancia | Qué aplica |
|---|---|
| `Ouroboros/` | el lenguaje: primitivos, mutaciones e integridad |
| `S.A.R.A/` | las abstracciones: la tarea, sus sub-tareas y sus procesos |
| `mantis/` | la operación: edita, audita y **hace cumplir el formato**. Su piso corre en `piso/` |

**`Agentes/` es la era, no una instancia.** Una instancia se corrige; una era se reemplaza. Un estándar que caduca con la era deja de ser estándar, y por eso la era no puede vivir dentro de `corpus/`.

**El piso vive en la instancia, no en el estándar.** `corpus/piso.md` dice **qué** tiene que decidir una unidad y **qué forma** tiene un proceso. El archivo que corre —un `.ps1`, un `.py`, lo que sea— vive en `mantis/piso/`, porque el lenguaje es de la era. **Si ese lenguaje cambia, el estándar no se toca.**

**La prueba entre estándar e instancia:** un estándar sin instancia **no hace nada**. Una instancia sin estándar **está a la deriva**: no hay forma de saber si está completa.

**La prueba entre instancia y era:** si la era muere y la instancia sigue teniendo sentido, no era era.

**No hay jerarquía de mando entre niveles.** El estándar no obedece a la instancia ni la instancia al estándar: cada uno se rompe de una manera distinta. La era existe para probar el estándar, no al revés.

## Qué hay aquí

| Archivo | Qué estandariza | Estado |
|---|---|---|
| `ruta.md` | la forma de enrutar: qué necesita un derrotero para estar completo | **obligatorio** |
| `Conceptos.md` | la forma de nombrar: un concepto, un nombre preferido, con origen | **obligatorio** |
| `esquema-de-fila.md` | la forma de dejar rastro: qué escribe todo proceso al actuar | **obligatorio** |
| `formato de proceso.md` | la forma de los tres niveles: tarea, sub-tarea y proceso | **obligatorio** |
| `indice.md` | qué hay en el repo y dónde: se regenera cuando algo muta | **obligatorio** |
| `piso/` | qué hace un ejecutor para que dos lleguen al mismo sitio | **opcional** |
| `problemas-abiertos.md` | el mapa: qué problema del campo toca qué pieza, y qué le falta | **opcional** |
| `ATLAS/` | la forma de comunicar: piso, techo, canal, sesgo, cuerpo | **opcional** |

**`piso/` es lo primero que ve alguien que abre este repo desde afuera.** No porque sea lo más importante, sino porque es **lo que la industria no tiene**: herramientas que corren igual en cualquier ejecutor. Levanta más cejas que veintiocho procesos, y por eso va aquí y no enterrado en una carpeta de abstracciones.

**Obligatorio** quiere decir que sin eso **no hay sistema**: se puede tener un derrotero sin ATLAS, y se puede funcionar; no se puede funcionar sin saber qué se nombra ni qué se deja escrito.

**Opcional** no quiere decir descartable: quiere decir que se puede empezar sin él, y que llegará un punto donde haga falta.

## El camino mínimo

Un lector que quiera construir esto y no quiera leerlo todo necesita **tres archivos**:

1. `ruta.md` — para saber qué cargar y cuándo.
2. `Conceptos.md` — para no inventar nombres.
3. `esquema-de-fila.md` — para dejar rastro.

Con esos tres hay un sistema que corre. **ATLAS llega cuando algo no llega al otro lado.** Esto se declara aquí porque un estándar que exige todo para empezar no se empieza: se abandona.

## La carta de cada era

Un **derrotero** enruta. Una **carta** dice cómo se lee el derrotero, y es lo que cada era carga por obligación.

- **Estándar de la carta:** el derrotero dice *qué ruta se toma*; la carta dice *qué hay, qué no se toca y cómo se verifica*. Las dos reglas viven aquí: `ruta.md`, `La carta y el derrotero son dos piezas`.
- **Carta de esta era:** `../AGENTS.md`, en la raíz, porque así lo leen las herramientas de hoy.
- **Su nombre no es suyo:** la carta es de cada era y cambia con ella. Su contenido, no.

## Qué no entra aquí

**Los casos no son estándares.** Un catálogo no dice cómo debe ser algo: dice qué le pasó a otros.

| Se queda fuera | Por qué |
|---|---|
| `S.A.R.A/futuros.md` | catálogo de futuros y síntomas: es un caso, no una forma |
| `S.A.R.A/individuos.md` | catálogo de robots: es un caso, no una forma |
| `S.A.R.A/mundo.md` | es el pegamento de este repo, y depende de sus tres piezas |
| `S.A.R.A/estado-del-arte.md` | es una medida con fecha, no una forma |
| `Ouroboros/primitivos/` y `Ouroboros/mutaciones/` | son procesos del lenguaje, no formas |

**La regla:** si el archivo dice **cómo tiene que ser**, es estándar. Si dice **qué pasó una vez**, es caso. Un estándar que se llena de casos deja de servir para juzgar: solo sirve para recordar.

## Prueba

¿Cada estándar puede aplicarse a más de una instancia? ¿Ninguno depende de un caso concreto? ¿El camino mínimo corre sin el resto?

**Falsificador:** un estándar que solo sirve para este repo; un caso presentado como forma; un lector obligado a leerlo todo para empezar; un estándar guardado dentro de lo que estandariza.

## Transiciones

- El estándar no tiene instancia → se declara como hipótesis, no como obligatorio.
- Un archivo nuevo no se sabe si es forma o caso → `ruta.md`, `Conformidad`.
- Una instancia contradice su estándar → `../mantis/mantenimiento/editar.md`, y gana el estándar.
- En cualquier otro caso → se entrega y se cierra.
