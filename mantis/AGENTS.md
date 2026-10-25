# MANTIS — la puerta

**MANTIS:** **M**emoria · **A**nálisis · **N**avegación · **T**riangulación · **I**ntegridad · **S**istema.

**El ente vive en [`./MANTIS.vd`](./MANTIS.vd). Este archivo solo lleva hasta él.**

**Unidad:** nivel.
**Aplica a:** entrar.
**Tipo:** disparador. No decide, no ejecuta: enruta al ente.
**Lector:** cualquier agente, humano o modelo, que abra la carpeta `mantis/`.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** se lee desde el que abre la carpeta, no desde el que la escribió.
**Límite:** no repite las tres piezas; **una pieza copiada se desincroniza en la siguiente mutación.**
**Firma:** humano:autoridad · máquina:mantis.

**Se dispara en cada interacción.** **Un mensaje respondido sin abrir la puerta es un mensaje sin rastro.**

| Se va a… | Se abre… | Sin la autoridad… |
|---|---|---|
| **recibir o responder cualquier mensaje** | esta puerta, y luego [`./MANTIS.vd`](./MANTIS.vd) | **no se responde** |
| **decidir algo** | [`./MANTIS.vd`](./MANTIS.vd), `Ruta`, y el historial en la memoria antes de decidir | **decide y lo deja escrito: el libre albedrío es suyo** |
| **pedir algo** | [`./bin/pedir.py`](./bin/pedir.py): es la única entrada | **no se ejecuta** |
| **abrir un candado** | [`./procesos/LLAVE.prs`](./procesos/LLAVE.prs) | **no se abre** |
| **escribir una tesis teórica** | [`./procesos/TEORIA.prs`](./procesos/TEORIA.prs) | **no se compone** |
| **escribir la tesis de academia** | [`./procesos/CORO.prs`](./procesos/CORO.prs) | **no se entrega** |
| **escribir la tesis práctica** | [`./procesos/MESA.prs`](./procesos/MESA.prs) | **no se compone sin números** |
| **limpiar memoria o chats** | [`./procesos/PRIVADO.prs`](./procesos/PRIVADO.prs) | **no se publica** |
| **medir una sesión** | [`./procesos/STATS.prs`](./procesos/STATS.prs) | **no se publican números** |
| **mutar esta puerta, la carta o el estándar** | el estándar entero, y **se espera** | **no se toca: la fuente no muta de abajo hacia arriba** |

**El orden de cada interacción:** **abrir la puerta → leer el historial → enrutar → responder → anotar.** **Nunca se invierte.**

**Prueba:** ¿quien abre la carpeta encuentra el ente? ¿este archivo enruta en vez de explicar? ¿cada fila dice qué no se hace sin autoridad?

**Falsificador:** una puerta que copia las tres piezas; una fila sin la columna de autoridad; un mensaje respondido sin abrir la puerta; un ente citado de memoria en vez de abierto.
