# MANTIS — la puerta

**MANTIS:** **M**emoria · **A**nálisis · **N**avegación · **T**riangulación · **I**ntegridad · **S**istema.

**El ente vive en [`./el alma.vd`](./el%20alma.vd). Este archivo solo lleva hasta él.**

**Y lo que hay que decir de frente:** **un alma es una carpeta, y en su raíz tiene tres cosas: su criterio, su pase y su piso.** **Las tareas viven en la raíz como carpetas, cada una con su `.tra` y sus `.prs`.** **No hay `bin/`, no hay `procesos/`, no hay `folders/`.**

**Unidad:** nivel.
**Aplica a:** entrar.
**Tipo:** disparador. No decide, no ejecuta: enruta al alma, y el alma enruta a la tarea.
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
| **saber qué pedido va a qué tarea** | la `Ruta` de [`./el alma.vd`](./el%20alma.vd) | **se corre el proceso que no tocaba** |
| **correr una tarea** | `python mantis/ejecu.py <tarea>` — la única entrada | **no se ejecuta** |
| **correr todas, y ver cuáles cumplen** | `python mantis/ejecu.py --verificar` | **no se declara que cumple** |
| **mantener el candado cero** | [`./el cero/`](./el%20cero/) | **no se renombra ni se retira nada** |
| **abrir o mantener un candado** | [`./los candados/`](./los%20candados/) | **no se abre** |
| **componer una tesis, on demand** | [`./la tesis/`](./la%20tesis/) | **no se compone** |
| **dejar el pase del turno** | [`./la memoria/`](./la%20memoria/) | **el siguiente turno empieza a ciegas** |
| **saber qué puede este mundo** | [`./RUTA.po`](./RUTA.po) | **se corre con lo que no hay** |
| **mutar esta puerta, el criterio o el estándar** | el estándar entero, y **se espera** | **no se toca: la fuente no muta de abajo hacia arriba** |

**El orden de cada interacción:** **abrir la puerta → leer `el alma.vd` → correr la tarea → dejar la `.tra` → responder.** **Nunca se invierte.**

**Prueba:** ¿quien abre la carpeta encuentra el alma? ¿este archivo enruta en vez de explicar? ¿cada fila dice qué no se hace sin autoridad?

**Falsificador:** una puerta que copia las tres piezas; una fila sin la columna de autoridad; un mensaje respondido sin abrir la puerta; una tarea citada que no existe; una tarea corrida sin dejar su `.tra`.

---

## La regla dura: el cero dice lo mismo que el repo

**El candado cero es la tesis entera, y si cita un nombre que ya no existe, el cero está mal.**

**Cada vez que se renombre, se retire o se cree una pieza, el cero se revisa en el mismo turno.** **No después, no en el siguiente pase: en el mismo.**

**Y se comprueba, no se recuerda:** `python mantis/ejecu.py el cero` falla si el candado cero nombra algo de `Muertos` en [`./el cero/nombres.md`](./el%20cero/nombres.md).

**Está comprobación existe porque el cero estuvo desactualizado meses**, citando `ATLAS`, `VIDERE` y `EXPANDE` cuando el repo ya tenía `RUTA`, `CONVIVIR` y `GUANTELETE`. **Un cero que cita fantasmas no es una tesis: es un recuerdo.**

**Y la lista de nombres no vive en el ejecutor: vive en `nombres.md`.** **El estándar dicta; el script obedece.**

**Prueba:** ¿cada nombre propio que el cero usa está en `Vivos`? ¿la tarea `el cero` lo comprueba?
**Falsificador:** el cero nombrando algo que no está; una pieza renombrada sin que el cero lo sepa; la lista de nombres escrita dentro de un `.py`.