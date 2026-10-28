# ENTES — lo que se copia, y ya sirve para empezar a chambear

**Hecho:** 2026-10-28. **Clase:** plantilla. **Estado:** vigente y usable.
**Ente:** `man-made-empathy` · **Tarea:** que alguien haga su propio ente, con lo que hay.
**Lector:** cualquiera que abra esta carpeta, y ya quiera empezar. **Dueño:** humano:autoridad.

**Sesgo:** se lee desde el que va a copiar, y no desde el que lo escribió.
**Límite:** **no decide si su ente sirve.** **Dice qué copiar, en qué orden, y qué le falta para estar completo.**
**Firma:** humano:autoridad · máquina:quien lo copie.

---

## Rastro — lo que hay, y lo que se copia

| Qué hay | Nombre | Dónde |
|---|---|---|
| **el ente individual** | **su carta, su guantelete, sus bancos, y su ciclo** | [`./Ente/`](./Ente/) |
| **varios entes** | **el 1, las almas, y el talento** | [`./Colmena/`](./Colmena/) |

**Y lo que hay adentro de `Ente/`, y ya se puede correr:**

| Archivo | Qué hace |
|---|---|
| **`README.md`** | **la carta: qué es un ente, y qué trae** |
| **`guantelete.prs`** | **la ficha que se llena antes de tocar algo ajeno** |
| **`memoria continua/banco de memoria.prs`** | **guarda qué pasó, con su frontera** |
| **`memoria continua/banco de friccion.prs`** | **guarda dónde se sostuvo, y qué lo refutó** |
| **`alma de niño/ciclo.prs`** | **el ciclo: leer, disparar, actuar** |
| **`evolucion/`** | **vacío a propósito: ahí van las tareas que tu ente aprenda** |

**Qué no se toca:** **la copia es tuya.** **Los `.prs` se pueden adaptar; lo que no se puede es quitarles el corte.**

---

## Ruta — cómo se empieza, y qué se carga

| Se va a… | Se carga… | Sin eso |
|---|---|---|
| **hacer un ente** | **copia [`./Ente/`](./Ente/) entera, y ponle nombre** | **no hay ente** |
| **llenar su carta** | **`./Ente/README.md`, sus preguntas** | **no se sabe qué falta cubre, ni a quién contesta** |
| **tocar algo que no es tuyo** | **`./Ente/guantelete.prs`** | **se toca sin testigo, y no hay vuelta** |
| **recordar qué pasó** | **`./Ente/memoria continua/banco de memoria.prs`** | **se repite el mismo error** |
| **decidir con fundamento** | **`./Ente/memoria continua/banco de friccion.prs`** | **se obedece una conclusión sin saber de dónde vino** |
| **correr una vuelta** | **`./Ente/alma de niño/ciclo.prs`** | **se actúa sin leer, y sin decir que no se sabe** |
| **agregar una tarea aprendida** | **`./Ente/evolucion/`** | **crece el cajón, y no el ente** |
| **juntar varios entes** | **[`./Colmena/README.md`](./Colmena/README.md)** | **son varios absolutos con el mismo nombre** |
| **saber cuál conviene** | **[`./Colmena/talento.md`](./Colmena/talento.md)** | **se elige por lo que promete, y sale cara y frágil** |
| **conocer las ideas detrás** | **[`../ideas/`](../ideas/), cuando esté** | **se trabaja sin sustento** |

---

## Carga — qué se pierde si falta algo

| Si falta | Se pierde | Y el síntoma es |
|---|---|---|
| **el guantelete** | **la contestación** | **crece, y nadie puede decirle que salió mal** |
| **el banco de memoria** | **el qué** | **se repite el error, y nadie sabe que pasó** |
| **el banco de fricción** | **el dónde** | **se sostiene sin saber desde dónde, y corregirse cuesta** |
| **el ciclo** | **el alma** | **actúa sin leer, y toca para averiguar** |
| **la evolución** | **la experiencia** | **cambia de computadora, y empieza de cero** |
| **la falta, y a quién contesta** | **la identidad** | **es un programa con buena letra** |

---

## Lo que esta carpeta no hace

**No programa por ti, y no te pide que sepas programar.**
**No decide si tu ente sirve: eso lo dice el uso.**
**No oculta lo que falta: cuando no hay, se dice `[FALTA]`.**

**Y no es el sitio donde se piensa.** **Lo que se piensa vive en [`../ideas/`](../ideas/), y lo que se muestra, en [`../ejemplos/`](../ejemplos/).** **Aquí se copia, y se corre.**

---

## Prueba

**¿Alguien puede copiar `Ente/` y correrlo sin preguntar nada? ¿Cada `.prs` tiene su corte? ¿La ruta dice qué se carga y qué pasa sin ello? ¿Se distingue lo que se copia de lo que se piensa?**

**Falsificador:** una carpeta que se copia y no corre; un `.prs` sin corte; una ruta a algo que no existe; una carpeta de entes que no dice cómo empezar.
