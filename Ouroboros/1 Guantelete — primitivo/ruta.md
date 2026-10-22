# Guantelete — derrotero del paso 1

**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Carta:** [`./rastro.md`](./rastro.md). Sin carta no se lee.
**Deterrente:** [`./carga.md`](./carga.md). Sin él, no se sabe qué se pierde si el paso deja de servir.
**Piso:** `../piso.md` — `Ouroboros/piso.md`.
**Abstracción:** `../` — el guantelete es el paso 1 de `Ouroboros/`.

**Sesgo:** la ruta se lee desde la petición que llega, no desde el catálogo.
**Límite:** no decide si la pieza cargada sirve; eso es integridad.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `formato de proceso.md`

## Entra | Falla | Sale | Consume

**Variables:** petición · pieza · firma · herramienta · quién la levanta
**Peor:** se carga una herramienta sin la pieza que la sostiene, y el resultado parece correcto porque no declara desde dónde se tomó.
**Quién:** quien enruta, y quien audita después qué se cargó.

- **Entra:** una petición de trabajo sobre el paso 1.
- **Falla si:** no hay fila para lo pedido; se cargan dos piezas y no se declara por qué; una herramienta se carga sin la pieza de base.
- **Sale:** la pieza o la herramienta que se carga, con su firma, o `[VACÍO - SIN PIEZA]`.
- **Consume:** quien ejecuta lo cargado.

**Prueba:** ¿cada fila tiene su pieza y su consecuencia? ¿el vacío se declara? ¿toda herramienta cargada tiene sesgo declarado?

**Falsificador:** una petición sin fila que se ejecuta igual; dos piezas cargadas sin declararlo; una herramienta aplicada sobre una decisión sin posición declarada; un vacío implícito.

## La tabla: si se va a...

### Las piezas

| Si se va a... | Se carga | Si no... |
|---|---|---|
| sostener una regla nueva y saber quién puede contestarla | `./primitivos/sesgo.md` | la regla se sostiene sin saber desde dónde |
| mirar desde otra mirada y declarar la propia, de forma extendida | `./extensiones/sesgo-declarado.md` | se descarta sin nombrar la regla que rompe |
| decidir algo que afecta a otro | `./primitivos/friccion.md` | no se decide: se ejecuta |

### Las herramientas

| Si se va a... | Se carga | Si no... |
|---|---|---|
| crear, calibrar, reemplazar o retirar un proceso | `./herramientas/manipulacion.md` | no se toca un proceso |
| ejecutar un proceso sobre una entrada | `./herramientas/aplicar.md` | no se ejecuta |
| cambiar un proceso y dejar rastro | `./herramientas/mutar.md` | no se muta |
| retirar un proceso cuyo fin dejó de existir | `./herramientas/retiro.md` | se queda ocupando el lugar |
| deducir un proceso de lo observable | `./herramientas/ingenieria-inversa.md` | no se deduce |
| escribir o emitir cualquier archivo | `./herramientas/claridad.md` | no se emite |

**Una fila, un destino.** Si se cargan dos, se declara por qué: **dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

## Las puertas que no se abren solas

| Puerta | Cuándo se cierra | Quién la levanta |
|---|---|---|
| **sesgar** | si la pieza no declara posición, límite y firma | quien produce la pieza |
| **friccionar** | si la decisión se ejecuta sin pasar por quien la toma | quien decide |
| **sostener** | si no se nombran las variables antes de crear | la autoridad |
| **aplicar** | si la entrada no le corresponde al proceso | quien aplica |
| **mutar** | si no se declara qué conserva y qué reemplaza | quien muta |
| **retirar** | si no se declara el fin que queda descubierto | quien retira |
| **deducir** | si el deducido no reproduce nada observable | quien deduce |
| **decir** | si la forma no llega al lector | quien emite |

**Cerrar una puerta no es bloquear: es no dejar pasar algo que iba a fallar después, más lejos y más caro.**

## Vacío

**Lo que no entra en una fila se declara `[VACÍO - SIN PIEZA]` y se pregunta; no se improvisa.**

## Transiciones

- No hay fila para lo que se va a hacer → `[VACÍO - SIN PIEZA]`.
- Una pieza no puede declarar su firma → su veredicto es `indeterminado`.
- El paso 1 se cierra → `../2 S.A.R.A — mutación`.
- En cualquier otro caso → se enruta, se ejecuta y se cierra.

## Lectura

**Sin derrotero no se carga una pieza; con él, se carga la que coincide y ni una más.**
