# SINCRONIZACIÓN DE ALMAS — la guía para trabajar

**Cuándo se abre:** **cuando alguien va a copiar un ente, y quiere ponerse a trabajar hoy.**

**Y es una guía, no un libro.** **Dice qué hay, en qué orden se usa, y qué no se toca.**
**Y el porqué está en [`./teoria/`](./teoria/): se lee cuando se quiera entender, y no antes.**

---

## Lo que hay aquí, y son tres cosas

| La carpeta | Qué es | Y por dónde entrar |
|---|---|---|
| **[`./entes/`](./entes/)** | **la forma: un ente y una colmena, que se copian** | **[`./entes/Ente/`](./entes/Ente/)** |
| **[`./teoria/`](./teoria/)** | **el argumento, los ejemplos, y el porqué de todo esto** | **[`./teoria/las ocho leyes del punto cero.md`](./teoria/las%20ocho%20leyes%20del%20punto%20cero.md)** |
| **[`./teoria/ejemplos/`](./teoria/ejemplos/)** | **34 fichas: cada obra, qué provocó, y su fuente** | **[`./teoria/ejemplos/ESTADO.md`](./teoria/ejemplos/ESTADO.md)** |

**Y lo que atiende de verdad no está aquí: vive en el proyecto, y esta carpeta sólo enseña.**

---

## La regla que ordena todo, en una línea

> **`.prs` se corre. `.md` se lee.** **Y cada carpeta tiene los suyos.**

---

## Cómo se hace un ente, y son seis pasos

```plaintext
1. copiar ./entes/Ente/    a donde vaya a vivir tu ente
2. renombrar               el PLANTILLA.md a AGENTS.md
3. poner el nombre         en el LEEME.md de tu ente, y en su carpeta
4. correr el piso          si lo tiene, y arreglar lo que falte
5. llenar ciclos/          con tu oficio, y borrar el ejemplo
6. trabajar                y cada tarea nueva, en evolucion/ con su _herramientas/
```

**Y cuando haya dos entes: copiar [`./entes/Colmena/`](./entes/Colmena/), y ponerlos adentro.**

---

## La plantilla del ente, y qué trae

```plaintext
Ente/
├── LEEME.md                el documento de ese ente, y se reescribe con su nombre
├── PLANTILLA.md            la puerta. Al copiar el ente, se renombra a AGENTS.md
├── ciclo alma de niño.prs  el fijo: leer · disparar · debatir · guantelete · firmar · actuar
├── procesos base/          los cuatro: BUSCAR · debatir · firmar · guantelete
├── ciclos/                 el oficio, y trae un ejemplo que se borra
├── memoria continua/       los dos bancos, y los apuntes
└── evolucion/              n tareas, y cada una con sus .prs y su _herramientas/
```

| Lo que | Se copia | Se cambia |
|---|---|---|
| **`LEEME.md`** | **sí** | **se reescribe con el nombre de tu ente, y qué hace** |
| **`PLANTILLA.md`** | **sí** | **se renombra a `AGENTS.md`, y se pone el nombre arriba** |
| **`ciclo alma de niño.prs`** | **sí, entero** | **nada: es fijo** |
| **`procesos base/`** | **sí, entero** | **nada: son cuatro, y no crecen** |
| **`ciclos/`** | **sí** | **se borra el ejemplo, y se escribe el suyo** |
| **`memoria continua/`** | **sí, con los bancos vacíos** | **se llena al usarlo** |
| **`evolucion/`** | **sí, vacía** | **se llena al aprender** |

**Y no trae `bin/`:** **eso es del proyecto, y de todos.**
**Y no trae `_herramientas/` en la raíz:** **eso es de una tarea, y sólo de esa.**

---

## Lo que NO se toca, y se dice una vez

**· el ciclo fijo**
**· `procesos base/`**

**Y el guantelete toca `evolucion/`, y nada más.** **El porqué, en [`./teoria/por que el guantelete no toca el alma.md`](./teoria/por%20que%20el%20guantelete%20no%20toca%20el%20alma.md).**

---

## La plantilla de la colmena, y qué comparte

```plaintext
Colmena/
├── LEEME.md                el documento de la colmena, y se reescribe
├── AGENTS.md               la única puerta del producto, y es ésta
├── Almas/                  los entes, cada uno completo, y aquí no hay ninguno
├── el 1/                   el acuerdo, y quién lo contesta
├── evolucion/              COMPARTIDA: lo que acordaron, con su ACUERDO.prs
└── talento/                el banco de talento real, con su TALENTO.prs
```

**Y comparte tres cosas, y no más:** **el `evolucion/` por acuerdo · el banco de memoria · y el talento real.**
**Y no comparte:** **el alma, el criterio, la memoria de cada uno, y sus ciclos.**

---

## Los ejemplos, y para qué están

**34 fichas, en [`./teoria/ejemplos/ficcion/`](./teoria/ejemplos/ficcion/).** **Y cada una dice: la escena, la obra, dónde está, si se verificó, qué provoca, y qué NO enseña.**

**Y su estado, una por una, en [`./teoria/ejemplos/ESTADO.md`](./teoria/ejemplos/ESTADO.md).**

---

## La teoría, y cuándo se lee

**Cuando quieras el porqué, y no antes.** **Y hay dieciocho piezas, y el orden de las lecturas está en [`./teoria/LEEME.md`](./teoria/el%20orden%20de%20las%20lecturas.md).**

| La pieza | Y qué contesta |
|---|---|
| **[`las ocho leyes del punto cero`](./teoria/las%20ocho%20leyes%20del%20punto%20cero.md)** | **por qué la forma es así** |
| **[`la casa del ente`](./teoria/la%20casa%20del%20ente.md)** | **qué es lo suyo, y qué no** |
| **[`por que el guantelete no toca el alma`](./teoria/por%20que%20el%20guantelete%20no%20toca%20el%20alma.md)** | **dónde está el borde, y por qué** |
| **[`el alma es la raiz, y el oficio es la rama`](./teoria/el%20alma%20es%20la%20raiz,%20y%20el%20oficio%20es%20la%20rama.md)** | **de dónde sale el ciclo** |
| **[`el ciclo, y por que decide no hacerlo`](./teoria/el%20ciclo,%20y%20por%20que%20decide%20no%20hacerlo.md)** | **por qué un ente no hace nada** |
| **y el argumento entero** | **[`el cero`](./teoria/el%20cero.md)**, **y las ocho piezas** |

---

## Prueba

**¿Esta guía basta para copiar un ente y trabajar hoy, sin leer la teoría? ¿Dice qué no se toca? ¿Y manda a `teoria/` lo que es porqué?**

**Falsificador:** una guía que no alcanza para trabajar; una que no dice qué no se toca; y una que mete el porqué, y la vuelve un libro.