# SINCRONIZACIÓN DE ALMAS — todo lo que la biblioteca entrega, y en un solo documento

**Cuándo se abre:** **cuando alguien llega, y quiere saber qué se copia, cómo, y en qué orden.**

**Y es el único documento de esta carpeta.** **Lo demás son archivos: `.prs` que se corren, fichas que se leen, y piezas que se tumban.**

**Y este documento se lee de arriba abajo, una vez.** **Después se va al archivo que diga la tabla.**

---

## Lo que hay aquí, y son tres cosas

| La carpeta | Qué es | Y su entrada |
|---|---|---|
| **[`./entes/`](./entes/)** | **la forma: un ente y una colmena, que se copian** | **[`./entes/Ente/`](./entes/Ente/) y [`./entes/Colmena/`](./entes/Colmena/)** |
| **[`./teoria/`](./teoria/)** | **la teoría, en quince piezas que se leen y se tumban** | **[`./teoria/el cero.md`](./teoria/el%20cero.md)** |
| **[`./ejemplos/`](./ejemplos/)** | **34 fichas: cada obra, qué provocó, y su fuente** | **[`./ejemplos/ESTADO.md`](./ejemplos/ESTADO.md)** |

**Y lo que atiende de verdad no está aquí: vive en el proyecto, y esta carpeta sólo enseña.**

---

## Y el corte que ordena todo

> **`.prs` se corre. `.md` se lee.**
> **Y una carpeta que no es de un ente que atiende, no lleva su puerta cargada sola.**

**Y por qué:** **un harness carga la puerta de un ente sola.** **Y si una plantilla la tuviera, el harness cargaría una plantilla como si fuera su chamba.**

---

## La plantilla del ente, y se copia entera

```plaintext
Ente/
├── LEEME.md                el documento de ese ente, y se reescribe con su nombre
├── ciclo alma de niño.prs  la raíz: leer · disparar · debatir · guantelete · firmar · actuar
├── procesos base/          los cuatro: BUSCAR · debatir · firmar · guantelete
├── ciclos/                 la rama: su oficio, y trae un ejemplo que se borra
├── memoria continua/       los dos bancos, y los apuntes
└── evolucion/              n tareas, y cada una con sus .prs y su _herramientas/
```

**Y no trae `bin/`.** **Eso es del proyecto, y de todos.**

**Y no trae un archivo de nombre aparte:** **el nombre va en su `LEEME.md`, y la regla para elegirlo está en el ciclo, en la parte de verbalizar.**

**Y no trae `_herramientas/` en la raíz.** **Eso es de una tarea, y sólo de esa.**

### Qué se copia, y qué se cambia

| Lo que | Se copia | Se cambia |
|---|---|---|
| **`LEEME.md`** | **sí** | **se reescribe con el nombre de tu ente, y qué hace** |
| **`ciclo alma de niño.prs`** | **sí, entero** | **nada: es fijo, y es el mismo en todos** |
| **`procesos base/`** | **sí, entero** | **nada: son cuatro, y no crecen** |
| **`ciclos/`** | **sí** | **se borra el ejemplo, y se escribe el suyo** |
| **`memoria continua/`** | **sí, con los bancos vacíos** | **se llena al usarlo** |
| **`evolucion/`** | **sí, vacía** | **se llena al aprender** |

### Y los cuatro procesos base, que son el libre albedrío sobre un alma fija

**`BUSCAR`** · **`debatir`** · **`firmar`** · **`guantelete`**

**Y no crecen.** **Si un ente necesita otra cosa, la pone en `evolucion/`.**

**Y para el que se atreva a tocar `procesos base/` y `evolucion/` con el guantelete:**

> **«Vamos a perder y cuando eso pase, un gramo de registro y nos vengarán.»**

### Y lo que el ciclo hace, y no se salta

```plaintext
1. LEER       los dos bancos, y el piso de ESTE ente, en cero. Si no da cero, no se empieza
2. DISPARAR   se movió una frontera
3. DEBATIR    si dos posiciones se pisan
4. GUANTELETE quién lo contesta, si es reversible, y si deja rastro
5. FIRMAR     quién respondió, qué esperaba, y qué pasó
6. ACTUAR     con su tarea y su caja; y si el acto tiene un ciclo propio, se llama aquí
```

**Y el paso 6 llama a `ciclos/`, y no al revés.**

**Y la regla que hace todo lo demás posible:**

> **Cuando algo no se sabe, se busca antes de opinar.**
> **Y si no se puede buscar, se dice que no se sabe. Y no se opina.**

**Y lo que se puede tocar, y lo que no:**

| Lo que | ¿Se toca? |
|---|---|
| **el ciclo fijo** | **no** |
| **`procesos base/`** | **no** |
| **`ciclos/`** | **sí: crecen** |
| **`evolucion/`** | **sí: el guantelete la toca, de a una tarea** |

**Y la frase, sin la que esto no tiene sentido:**

> **Con todo lo que crezcas, con todas las tareas, y con todos tus ciclos, todavía eres tú.**
> **Despite everything, it's still you.**

---

## La plantilla de la colmena, y se copia cuando ya hay dos entes

```plaintext
Colmena/
├── LEEME.md                el documento de la colmena, y se reescribe
├── Almas/                  los entes, cada uno completo, y aquí no hay ninguno
├── el 1/                   el acuerdo, y quién lo contesta
├── evolucion/              COMPARTIDA: lo que acordaron, con su ACUERDO.prs
└── talento/                el banco de talento real, con su TALENTO.prs
```

### Lo que es, y lo que no

> **No es un ente. Es el lugar donde viven varios entes intercambiables.**
> **Cada uno trae su casa entera, y saca uno, y no pasa nada: sigue siendo él, con lo suyo.**

**Y por eso la colmena no tiene ciclo, ni alma, ni criterio. Los tiene cada ente.**

### Lo que se comparte, y son tres cosas sólo

| Lo que | Dónde | Quién lo decide |
|---|---|---|
| **el `evolucion/`** | **`evolucion/`, con su `ACUERDO.prs` escrito antes** | **el acuerdo** |
| **el banco de memoria** | **el que diga el acuerdo** | **el acuerdo** |
| **el banco de talento real** | **`talento/`, con su `TALENTO.prs`** | **el proceso de talento** |

**Y lo que NO se comparte:** **el alma, el criterio, la memoria de cada uno, y sus ciclos.**

**Y los ciclos se comparten, y no se copian:** **uno tiene un ciclo que el otro no, y se lo pasa.**

**Y `el 1/` es el acuerdo:** **dónde se escribe qué se acordó, quién lo propuso, y quién lo contradijo.** **Y un acuerdo sin `Contra` no es acuerdo: es silencio.**

**Y `talento/` es lo que cada ente aguanta, y a qué precio.** **Y lo que NO aguanta es lo que sirve.** **Y sin testigo, no entra.**

---

## Los ejemplos, y son lo que hace llegar el argumento

**34 fichas, en [`./ejemplos/ficcion/`](./ejemplos/ficcion/).** **Y una por obra, con seis líneas:**

```plaintext
Escena:      qué pasa, en una línea
Obra:        título, autor, año, soporte
Dónde:       capítulo, minuto, página, clip — o «no se verificó»
¿Es así?:    verificado | parcial | declarado | no se verificó
Qué provoca: la pregunta
Límite:      lo que NO enseña
```

**Y el estado de las 34, una por una, en [`./ejemplos/ESTADO.md`](./ejemplos/ESTADO.md).**
**Y cómo se verifica, y cuándo no se usa, en [`./ejemplos/COMO SE VERIFICA.LEEME.md`](./ejemplos/COMO%20SE%20VERIFICA.LEEME.md).**

**Y la regla, que es una sola:**

> **Un ejemplo no es absoluto porque nunca está solo: lleva su verificación pegada.**
> **Y las respuestas son legítimas; la que no se permite es no decirlo.**

**Y hoy:** **32 con una fuente, y 2 con ninguna.** **Y ninguna con dos, y eso está dicho en el estado de cada una.**

---

## La teoría, y es el argumento

**Quince piezas, en [`./teoria/`](./teoria/).** **Y cada una pregunta una sola cosa, y contesta.**

| La pieza | La pregunta |
|---|---|
| **[`el cero`](./teoria/el%20cero.md)** | **¿qué se sostiene, y qué lo tumbaría?** |
| **[`la singularidad buena`](./teoria/la%20singularidad%20buena.md)** | **¿para qué?** |
| **[`la frase`](./teoria/la%20frase.md)** | **¿por qué el registro es lo único que queda?** |
| **[`el alma es la raiz, y el oficio es la rama`](./teoria/el%20alma%20es%20la%20raiz,%20y%20el%20oficio%20es%20la%20rama.md)** | **¿de dónde sale el ciclo?** |
| **[`el ciclo, y por que decide no hacerlo`](./teoria/el%20ciclo,%20y%20por%20que%20decide%20no%20hacerlo.md)** | **¿por qué un ente no hace nada?** |
| **[`mutar`](./teoria/mutar.md)** | **¿qué puede cambiar, y qué se pierde?** |
| **[`procesos`](./teoria/procesos.md)** | **¿cómo se escribe un proceso que se pueda refutar?** |
| **y las ocho piezas** | **en [`./teoria/las ocho piezas/`](./teoria/las%20ocho%20piezas/)** |

**Y el corte que comparten:** **se puede crecer sin límite, y lo que impide que ese crecimiento se vuelva `AM` es que el borde no se mueva.**

**Y esto no se cree: se corre.**

---


---

## Y cada ente lleva su `AGENTS.md`, y se copia con él

> **`AGENTS.md` es la puerta que el harness carga sola, y por eso hay uno solo.**
> **Y por eso cada ente la lleva: sin algo que se lea al abrir, el ente hace lo que no se le negó, y nadie lo escribió.**

**Y `AGENTS.md` es uno solo, y es el de la colmena.** **Y la plantilla del ente no lo lleva: lleva `PLANTILLA.md`, y quien copia el ente la renombra.**

| Dónde | Y qué dice |
|---|---|
| **[`./entes/Ente/PLANTILLA.md`](./entes/Ente/PLANTILLA.md)** | **la puerta de un ente. Y al copiar el ente, se renombra a `AGENTS.md`** |
| **[`./entes/Colmena/AGENTS.md`](./entes/Colmena/AGENTS.md)** | **que no es un ente, y qué se comparte** |

**Y lo que dice, y es lo primero:**

> **Eres el trabajador de este proyecto. Y lo que te trajo no es tuyo: es el porqué de quien te copió.**

**Y lo que no se toca:** **el ciclo fijo, y `procesos base/`.**

**Y lo que NO vive en la puerta:** **la forma.** **La forma está aquí, en este documento.** **La puerta dice por dónde se va, y no cómo es la casa.**

| --- | --- |

## Por dónde empezar, y en qué orden

**1. Lee este documento. Ya está.**
**2. Copia [`./entes/Ente/`](./entes/Ente/) a donde vaya a vivir tu ente.**
**3. Ponle nombre: el proyecto tiene uno, para que el agente no se desvíe; y si se batalla, se verbaliza. Rige el ciclo, en su parte de verbalizar.**
**4. Lee su `LEEME.md`, y reescríbelo con lo que tu ente hace.**
**5. Corre su piso, si lo tiene, y arregla lo que falte.**
**6. Y cuando haya dos, copia [`./entes/Colmena/`](./entes/Colmena/) y ponlos adentro.**

---

## Prueba

**¿Este documento dice qué hay, y en qué orden se copia? ¿Cada carpeta dice para quién es? ¿Se distingue la forma de lo que ya atiende? ¿Se puede copiar un ente sin preguntarle a nadie?**

**Falsificador:** un ente que no se puede copiar; una carpeta que no dice qué es; un documento que sólo se entiende con su autor presente.
