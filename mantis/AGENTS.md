# MANTIS — la puerta

**MANTIS:** **M**emoria · **A**nálisis · **N**avegación · **T**riangulación · **I**ntegridad · **S**istema.

**El ente vive en [`./el alma.vd`](./el%20alma.vd). Este archivo solo lleva hasta él.**

**Y una cosa que hay que decir de frente: `mantis` ya no es un cuerpo con scripts.** **Nació de `sincronizacion de almas/primitivos/alma en blanco/`: pasa por folders, y cada folder deja su `.tra`.** **Lo único que no es estándar en toda esta carpeta es [`./ejecu.py`](./ejecu.py), y lo declara.**

**Unidad:** nivel.
**Aplica a:** entrar.
**Tipo:** disparador. No decide, no ejecuta: enruta al ente, y el ente enruta al folder.
**Lector:** cualquier agente, humano o modelo, que abra la carpeta `mantis/`.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** se lee desde el que abre la carpeta, no desde el que la escribió.
**Límite:** no repite las tres piezas; **una pieza copiada se desincroniza en la siguiente mutación.**
**Firma:** humano:autoridad · máquina:mantis.

**Se dispara en cada interacción.** **Un mensaje respondido sin abrir la puerta es un mensaje sin rastro.**

| Se va a… | Se abre… | Sin la autoridad… |
|---|---|---|
| **recibir o responder cualquier mensaje** | esta puerta, y luego [`./el alma.vd`](./el%20alma.vd) | **no se responde** |
| **saber qué folder corre qué** | [`./IMA.md`](./IMA.md) | **se corre el proceso que no tocaba** |
| **correr un folder** | [`./ejecu.py`](./ejecu.py) — la única entrada | **no se ejecuta** |
| **correr todos, y ver cuáles cumplen** | `python ejecu.py --verificar` | **no se declara que cumple** |
| **mantener el candado cero** | [`./folders/el cero/`](./folders/el%20cero/) | **no se renombra ni se retira nada** |
| **abrir o mantener un candado** | [`./folders/los candados/`](./folders/los%20candados/) | **no se abre** |
| **componer una tesis, on demand** | [`./folders/la tesis/`](./folders/la%20tesis/) | **no se compone** |
| **dejar el pase del turno** | [`./folders/la memoria/`](./folders/la%20memoria/) | **el siguiente turno empieza a ciegas** |
| **mutar esta puerta, la carta o el estándar** | el estándar entero, y **se espera** | **no se toca: la fuente no muta de abajo hacia arriba** |

**El orden de cada interacción:** **abrir la puerta → leer el `IMA.md` → correr el folder → dejar la `.tra` → responder.** **Nunca se invierte.**

**Prueba:** ¿quien abre la carpeta encuentra el ente? ¿este archivo enruta en vez de explicar? ¿cada fila dice qué no se hace sin autoridad?

**Falsificador:** una puerta que copia las tres piezas; una fila sin la columna de autoridad; un mensaje respondido sin abrir la puerta; un folder citado que no existe; un folder corrido sin dejar su `.tra`.

---

## La regla dura: el cero dice lo mismo que el repo

**El candado cero es la tesis entera, y si cita un nombre que ya no existe, el cero está mal.**

**Cada vez que se renombre, se retire o se cree una pieza, el cero se revisa en el mismo turno.** **No después, no en el siguiente pase: en el mismo.**

**Y se comprueba, no se recuerda:** `python mantis/ejecu.py el cero` falla si el candado cero nombra algo de `Muertos` en [`./folders/el cero/nombres.md`](./folders/el%20cero/nombres.md).

**Está comprobación existe porque el cero estuvo desactualizado meses**, citando `ATLAS`, `VIDERE` y `EXPANDE` cuando el repo ya tenía `RUTA`, `CONVIVIR` y `GUANTELETE`. **Un cero que cita fantasmas no es una tesis: es un recuerdo.**

**Y la lista de nombres no vive en el ejecutor: vive en `nombres.md`.** **El estándar dicta; el script obedece.**

**Prueba:** ¿cada nombre propio que el cero usa está en `Vivos`? ¿el folder `el cero` lo comprueba?
**Falsificador:** el cero nombrando algo que no está; una pieza renombrada sin que el cero lo sepa; la lista de nombres escrita dentro de un `.py`.
