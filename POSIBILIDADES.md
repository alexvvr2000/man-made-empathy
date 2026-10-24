# POSIBILIDADES — lo que se puede construir con esto

**Qué es.** Lo que el sistema permite hacer cuando sus piezas están en su sitio. **No es una promesa de producto: es el mapa de lo que ya es posible con lo que existe, y lo que falta para cada cosa.**

**Dueño:** humano:Alejandro Valenzuela Rivera.
**Estado:** vigente.

Sesgo: se lee desde lo que el repo puede hacer hoy, y se dice qué le falta a lo que aún no.

---

## Lo que ya está en pie, y se puede usar hoy

| Pieza | Dónde | Qué hace |
|---|---|---|
| La forma | `Era/lenguaje de procesos/FORMATO.md` | dice cómo se lee un `.vd`, un `.tra` y un `.prs`, sin adivinar |
| El estándar de candados | `Era/lenguaje de procesos/JONN.md` | un autor, N candados, la llave a la vista, los implícitos escritos |
| El lenguaje | `Era/lenguaje de procesos/LENGUAJE.md` | qué es un ente, una tarea y un proceso, y cómo se conectan |
| El piso | `Era/lenguaje de procesos/PISO.md` | qué hay disponible, y cuánto cuesta |
| La fila verbalizada | `Era/lenguaje de procesos/la fila verbalizada.md` | toda salida en seis campos |
| Los procesos | `Era/lenguaje de procesos/procesos/` | `ENTRAR`, `MIRAR`, `EXPRESAR`, `EXTRAER` |
| El ente en blanco | `Era/ente en blanco/` | la primera alma en blanco: se copia y se llena |
| Las visiones | `mantis/vision del autor/`, `Tesis/vision de la maquina/`, `Tesis/vision del lector/` | el candado y quién lo mira desde dónde |
| El jugo | `mantis.db`, tabla `pieza` | 57 piezas con su ficción y su pregunta |

## Lo que se puede hacer con eso, y qué falta

| Posibilidad | Qué hace falta | Estado |
|---|---|---|
| **Validar un archivo contra `FORMATO.md`** | un chequeo que lea marcas y diga qué falta | **es posible hoy, solo hay que escribirlo** |
| **Indexar candados con autor, ficción y llave** | leer la tabla `pieza` y los `N candados` de cada autor | **posible hoy** |
| **Comparar dos candados del mismo autor** | la fila: si dos `Sostengo` se dicen con el mismo, eran uno | **posible hoy** |
| **Detectar una idea que se presenta como propia** | `Ficción: ninguna` sobre una idea que salió de una obra | **posible hoy, con `EXPRESION`** |
| **Correr el ciclo en un folder real** | que el alma pase y deje el `.tra` | **necesita un ejecutor** |
| **Un parser de `.prs` en un lenguaje de verdad** | que la forma esté fija (ya lo está) | **posible, no escrito** |
| **Varios modelos como varios candados** | cada modelo con su `N candados`, su autor y su visión de la máquina | **posible hoy, es copiar carpetas** |

## Cómo se abre el kraken: varios modelos, cada uno un alma

**Lo que se puede hacer sin escribir una línea de código:**

1. **Se copia `Era/ente en blanco/`** una vez por cada modelo.
2. **Cada copia es un alma con su propio rastro.** **El modelo se declara en su visión de la máquina:** **qué carga, qué no carga, qué no puede afirmar, qué firma.**
3. **Cada alma deja sus `.tra`.** **Y cuando dos almas se afinan sin volverse una, eso es resonancia.** **Cuando se vuelven una, es un solo ente con más gasto.**
4. **Y el índice que las enruta es `ATLAS.md`:** **no hay estándar de ATLAS, hay un índice que se gasta.**

**Lo que eso permite:** **que un modelo dé la visión de la máquina, otro dé la visión del lector, y el humano sea el autor.** **Los tres con el mismo candado y distinto sitio.**

**Y lo que no permite todavía:** **que se corran solos.** **Hoy cada paso lo ejecuta quien los lee.**

## Los parsers y lo que se puede construir con la forma fija

**Con `FORMATO.md`, un programa puede hacer cuatro cosas, en este orden:**

| Nivel | Qué hace | Qué necesita |
|---|---|---|
| **1** | **leer un `.prs` y decir qué campo falta** | nada más |
| **2** | **unir un `.tra` con sus `.prs` y ver si el `Siguiente` apunta a un proceso que existe** | nada más |
| **3** | **leer la fila de cada proceso y detectar dos `Sostengo` iguales** | que los procesos escriban su salida |
| **4** | **correr el ciclo: `ENTRAR` → `MIRAR` → `EXPRESION`, y dejar el `.tra`** | un ejecutor |

**Y lo que el parser no puede hacer, y se declara:** **no juzga si una idea es buena.** **Dice qué falta y dónde está.** **Lo demás lo decide un lector, que es lo que el repo protege.**

## Lo que esta tecnología abre, y ya no es del repo

**Con un candado que cualquiera puede abrir y una llave que está a la vista, se puede:**

- **publicar una idea sin pedir permiso a ninguna puerta**, y dejar el rastro de quién la abrió;
- **comparar dos autores por sus candados**, y no por sus títulos;
- **heredar una idea sin heredar a su autor**: el que viene después encuentra la pregunta y el método, no la persona;
- **darle a un modelo un sitio y un límite escrito**, en vez de pedirle que sea algo que no se puede comprobar;
- **tratar igual a un humano que a una máquina** en el único punto que importa: **sostiene, contesta y deja rastro; o no.**

## Lo que se pierde si no se escribe

**Lo que no se escribe se vuelve implícito, y los implícitos son lo que crea a AM.** **Por eso este archivo existe: para que las posibilidades no queden en una conversación que se pierde.**

## Prueba

**¿Cada posibilidad dice qué hace falta? ¿Se distingue lo que ya es posible de lo que no? ¿Se dice lo que esta tecnología no puede hacer?**

## Falsificador

**Una posibilidad presentada como hecha sin haberla corrido; una que no dice qué le falta; una que promete que el sistema juzga lo que no puede juzgar; una lista que omite lo que no se puede hacer.**

