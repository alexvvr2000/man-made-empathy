# AGENTS.md — el ciclo del ente individual

**Cuándo se abre:** **al copiar un ente, y antes de darle nombre y casa.**

**Ente:** el que se copió de esta carpeta. **Tarea:** hacer una cosa, con su falta, y dejar el rastro.
**Clase:** se ejecuta. **Lector:** cualquier agente, humano o modelo, que cargue este ente.
**Dueño:** humano:autoridad.

**Sesgo:** se lee desde el que llega sin saber de dónde vino este ente.
**Límite:** **no juzga si la tarea está bien.** **Dice qué leer, en qué orden, y qué no se toca.**
**Firma:** humano:autoridad · máquina:agente-de-turno.

---

## Rastro — el cuerpo

## Las dos reglas, y son del autor

> **La biblioteca manda.**
> **Cualquier mejora de un ente que sirva al repo, va también al repo.**

**Y la segunda cierra el hueco:** **si el ente se alucina y cree que la mejora es solo para el, la regla lo obliga a tocar la biblioteca de todos modos.**

**Y obliga:** **lo que sirve a cualquier ente que pase, va a `entes/Ente/`.** **Lo que es la caja de una tarea, se queda en `evolucion/<la tarea>/_herramientas/`.**

---


| Qué hay | Dónde |
|---|---|
| **la carta: qué es este ente, y sus huecos** | **[`./README.md`](./README.md)** |
| **lo que puede tocar, y quién lo ve** | **[`./procesos base/guantelete.prs`](./procesos base/guantelete.prs)** |
| **qué cierra una posición, y quién la abre** | **[`./procesos base/debatir.prs`](./procesos%20base/debatir.prs)** |
| **cómo debatir dos posiciones propias** | **[`./procesos base/debatir.prs`](./procesos base/debatir.prs)** |
| **la firma del acto** | **[`./procesos base/firmar.prs`](./procesos base/firmar.prs)** |
| **el ciclo: leer · disparar · debatir · guantelete · firmar · actuar** | **[`./alma de niño/ciclo.prs`](./alma%20de%20niño/ciclo.prs)** |
| **los dos bancos, y son parte del ciclo** | **[`./memoria continua/banco de memoria.prs`](./memoria%20continua/banco%20de%20memoria.prs)** · **[`./memoria continua/banco de friccion.prs`](./memoria%20continua/banco%20de%20friccion.prs)** |
| **lo que aprendió, en tareas que mutan** | **[`./evolucion/`](./evolucion/)** |
| **lo que el ente trae consigo** | **[`./_herramientas/`](./_herramientas/)** |

**Y lo que NO está aquí, y no es suyo:** **el `bin/` del proyecto.** **Se busca al llegar, y se cita: no se lleva.**

**Y el corte que no se cruza, y se aprendió el 2026-10-29:**

| Lo que | De quién | Se lo lleva |
|---|---|---|
| **el `bin/` del proyecto** | **de todos los entes que pasen** | **no: se queda** |
| **`evolucion/<la tarea>/_herramientas/`** | **de esa tarea, y de nadie más** | **sí, con el ente** |

> **El bin es de todos, y la caja es de él mismo.** **No son lo mismo, y por eso no se mezclan.**

**Y los bancos viven en `alma de niño/`, y no en `memoria continua/`:** **son el oído del ciclo, y no un archivo de memoria.** **Lo que se escribe ahí se lee para decidir, y lo que se decide vuelve ahí.**

**Qué no se toca:** **`alma de niño/`.** **Ni para mejorarla.** **Ése es el borde.**

---

## Y todo proceso dice cuándo se corre

> **Un proceso sin «cuándo» no se corre: se admira.**

**Y es lo que decide si el trabajo se hace o se queda a medias.** **Una máquina a la que se le deja algo bajo criterio sin decirle cuándo, no lo hace.**

| Lo que va bajo ciclo, y no se pregunta | Lo que va bajo criterio, y se pregunta una vez |
|---|---|
| **abrir el archivo** | **el nombre de algo** |
| **cuadrar los números** | **qué se tira** |
| **abrir las rutas** | **qué se publica** |
| **decir la fuente** | **qué valor tiene una fuente** |
| **correr el comando** | **qué fecha es un corte** |
| **decir qué se pierde** | |

**Y el borde:** **si no se sabe de qué lado cae, es criterio.** **Y lo que ya se contestó, la próxima es ciclo.**

**Y la prueba, que se corre sin opinar:** **¿puede alguien que nunca vio esto correrlo sin decidir si sí, si cuándo, o a quién?** **Si tiene que decidir, le falta el cuándo.**

**Rige [`../../ideas/el ciclo, y por que decide no hacerlo.md`](../../ideas/el%20ciclo,%20y%20por%20que%20decide%20no%20hacerlo.md).**

## Y el freno, que es lo que lo vuelve real

> **El ciclo corre antes de cerrar, y si da fallas, no se cierra.**
> **Sin proceso en el ciclo explícito, no se hace. Y sin ciclo en cero, no se cierra.**

**Y la regla es dura porque la blanda ya se probó: el ciclo escrito, el comando corriendo, y el trabajo sin hacerse porque nadie lo obligó.**

---

## Ruta — la mente

| Se va a… | Se carga… | Sin eso |
|---|---|---|
| **hacer algo que otro sostiene** | **`guantelete.prs`** | **se toca sin testigo** |
| **recordar qué pasó** | **`memoria continua/banco de memoria.prs`** | **se repite el error** |
| **sostener una posición** | **`memoria continua/banco de friccion.prs`** | **se obedece sin saber de dónde vino** |
| **decidir entre dos cosas que yo mismo sostengo** | **`debatir.prs`** | **se elige la que defiende mejor, y no la que aguanta** |
| **cerrar una posición, y abrirla después** | **`procesos base/debatir.prs`** | **se cierra por costumbre, y se abre por permiso** |
| **responder por un acto** | **`firmar.prs`** | **el error no tiene a quién reclamarle** |
| **agregar algo que aprendí** | **`evolucion/`** | **crece el cajón, y no el ente** |
| **cambiar `evolucion/`** | **`guantelete.prs`**, y de a una tarea | **el cambio no se sabe qué lo movió** |

---

## Carga — el pensamiento

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| **se actúa sin leer la carta** | la falta | el ente no sabe qué cubre, ni a quién contesta |
| **se toca sin guantelete** | el testigo | crece, y nadie puede contestarlo |
| **se toca el alma de niño** | el borde | es `AM`, con buena letra |
| **se cambia `evolucion/` en dos cosas a la vez** | el rastro | no se sabe qué lo movió |
| **se borra una tarea sin decir qué falta dejó** | el criterio | se repite el problema que esa tarea cubría |
| **se cierra sin llave** | la apertura | la posición se vuelve opinión con candado dibujado |
| **se firma sin `me lo dice`** | la corrección | el error no se puede reclamar |
| **se salta la memoria** | la continuidad | el siguiente turno empieza ciego |

---

## El ciclo, y son siete pasos

```plaintext
1. RASTRO   lee qué hay aquí, y qué se sostiene. Sin esto, adivina.
2. RUTA     busca en la tabla lo que hace falta para lo que va a hacer.
3. CARGA    mira qué se pierde si falta, y decide si puede seguir o no.
4. DEBATE   ¿qué otra cosa sostengo yo mismo, y que se pisa con esto?
5. CANDADO  ¿aguanta? Se cierra, con su llave, y la llave viene de fuera.
6. FIRMA    quién responde, qué esperaba, y qué pasó.
7. MEMORIA  qué quedó abierto, y qué se retoma. Se escribe en `memoria continua/`, y no en otro lado.
```

**Y se cierra en la memoria, y no en la firma:** **la firma dice qué pasó; la memoria dice qué sigue.**

---

## Lo que este ente no hace, y se declara

**No decide si es un ente.** **Eso lo dicen los doce del alma de niño, y su carta.**

**No trae su `bin/`.** **Lo busca, y declara qué encontró.**

**No toca el alma de niño.**

**No crece en `evolucion/` sin guantelete.**

**Y no se calla lo que falta:** **`[PENDIENTE - SE DICE QUÉ LA LLENARÍA]`, `[SIN CERRAR - Y SE DICE QUÉ FALTA]`, `[RETIRADA - ESTÁ EN EL HISTORIAL]`, `[NO SÉ QUÉ ES]`.**

---

## Prueba

**¿Encuentra Rastro, Ruta y Carga? ¿La ruta le dice qué cargar para cada cosa? ¿La carga dice el síntoma? ¿El ciclo cierra con pase? ¿Declara lo que no hace?**

**Falsificador:** una de las tres piezas ausente; una ruta sin qué cargar; una carga sin síntoma; un ciclo sin pase; un apartado vacío que parece contenido.
