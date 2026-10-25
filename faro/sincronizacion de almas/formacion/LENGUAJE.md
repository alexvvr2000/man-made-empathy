# La forma del sincronizacion de almas — la era

**Unidad:** lenguaje.
**Aplica a:** escribir, abrir y sostener.
**Tipo:** especificación. Se ejecuta: lo que no la cumple no es del lenguaje.
**Lector:** quien escribe un ente, una tarea o un proceso.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** se sostiene desde lo que se puede correr sin su autor.
**Límite:** no decide qué hace un ente. Dice con qué se escribe.
**Firma:** humano:autoridad · máquina:quien la copie.

**Variables:** ente · tarea · proceso · piso
**Peor: se escribe un proceso que sabe cómo se hace por dentro, y entonces no vuelve: se queda en su autor.**
**Quién:** quien escriba un proceso que no se puede repetir.

## Las tres piezas, y su extensión

| Extensión | Qué es | Su corte | Qué lleva |
|---|---|---|---|
| **`.vd`** | **ente**: lo que sostiene | las tres piezas: **Rastro**, **Ruta**, **Carga** | qué hay, qué no se toca, cómo se verifica; qué se carga y cuándo; qué se pierde y su síntoma |
| **`.tra`** | **tarea**: lo que pasó y se abre | **es la carpeta**; su `.tra` dice qué pasó y a qué proceso entra | la frase dicha, el contra, la huella, la distancia |
| **`.prs`** | **proceso**: lo que vuelve | **`Entra | Falla | Sale | Consume`** | y nada más: **no dice cómo se hace por dentro** |

**Y el corte que los separa es uno:**

> Lo que vuelve es `.prs`. Lo que pasó una vez es `.tra`. Lo que sostiene a los dos es `.vd`.

## La tarea es la carpeta

```
no era tan fácil/              ← la tarea ES la carpeta, y su nombre es el de la tarea
├── no era tan fácil.tra       ← qué pasó, y a qué proceso entra
├── ENTRAR.prs                 ← primer proceso
├── MIRAR.prs                  ← segundo
└── …                          ← los que esa tarea necesita
```

Copiar la carpeta es copiar la tarea completa con sus procesos. Una tarea son varios procesos: nunca uno.

El nombre de la carpeta y el de su `.tra` son el mismo. Si el acto cambia, cambian juntos, o ninguno.

## El proceso solo declara cuatro cosas

```
Entra:    qué recibe
Falla si: el caso concreto que lo incumple
Sale:     qué emite, con su forma exacta
Consume:  quién decide con la salida
```

**Y lo que NO declara: cómo se logra.** Por eso un RAG, una llamada a API o una tabla nueva caben dentro de un `.prs` sin que el lenguaje cambie. **El cómo es el piso.**

## El piso

El piso es lo disponible para ejecutar: canales, formatos, herramientas, acceso a la web. **No se elige por gusto: se declara.**

```
Piso: [lo disponible] | Falta: [lo que no hay] | Se pierde: [qué no se puede hacer sin eso]
```

Y el piso es de verdad cuando crece con cada capacidad probada: una capacidad probada entra al piso, y desde ahí la usa cualquier ente.

## Los nombres

El nombre se lee de un tirón; la expansión va adentro. Es nombre cuando expone el acto; es etiqueta cuando solo se deletrea.

```
Nombre:    [el de hoy] | Expande: [el acto, citable]
Se nombró: [el instante] | Reemplaza: [el anterior, o NINGUNO] | Miente si: [qué acto no ocurrió]
```

- **Sin número.** Un número finge que el nombre nuevo es el mismo.
- **Un nombre vigente.** Los anteriores quedan con `Reemplaza:`, visibles.
- **Cambia por suceso, no por segundo.**
- En el texto con puntos; en la carpeta sin.

## Lo que la tarea guarda y no guarda

**Guarda: la frase dicha, el contra, la huella, la distancia. No guarda procesos a la vez: los carga desde su carpeta.** Si ves tres procesos corriendo dentro de un `.tra`, es un `.prs` con nombre de tarea.

## Lo que no se repetía hoy de la memoria

Y esto es la lección de la era, escrita como regla:

- **saber las limitaciones:** un `.vd` sin `Ruta` ni `Carga` es un ente que no sabe lo que no sabe, y contamina.
- lo que no cambia una decisión no se guarda.
- una sola versión viva: se reemplaza, no se copia.
- el jugo no se guarda con permiso: se guarda porque es el respaldo de lo que se destruye.

Rige `../../Libre albedrio/criterio.md`, `El rastro de la decisión`.

## Prueba

¿Cada ente es un `.vd` con las tres piezas? ¿Cada tarea es una carpeta con su `.tra` adentro? ¿Cada proceso es un `.prs` con sus cuatro campos y sin explicar el cómo? ¿El piso declara lo que falta? ¿Los nombres coinciden con sus carpetas, sin número? ¿Los nombres viejos quedaron con `Reemplaza:`?

**Falsificador:** un proceso que explica cómo se hace por dentro; una tarea con un solo proceso; una carpeta y su `.tra` con nombres distintos; un nombre con número; un nombre cambiado sin `Reemplaza:`; un piso que no declara lo que falta; una tarea que contiene procesos en vez de cargarlos.

## Transiciones

- Algo vuelve → se escribe un `.prs`, y entra al piso cuando se prueba.
- Algo pasó → se abre una carpeta, con su `.tra` y sus `.prs`.
- El acto cambió → se renombra la carpeta y su `.tra` juntos, y el viejo queda con `Reemplaza:`. **Sin número.**
- Una capacidad nueva se prueba → entra al piso, y desde ahí la usa cualquier ente.


