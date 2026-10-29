# ENTES — lo que se copia, y ya sirve para empezar a chambear

**Hecho:** 2026-10-28. **Clase:** plantilla. **Estado:** vigente y usable, **y todavía no es la v1 final.**
**Ente:** `man-made-empathy` · **Tarea:** que alguien haga su propio ente, con lo que hay.
**Lector:** cualquiera que abra esta carpeta, y ya quiera empezar. **Dueño:** humano:autoridad.

**Sesgo:** se lee desde el que va a copiar, y no desde el que lo escribió.
**Límite:** **no decide si su ente sirve.** **Dice qué copiar, en qué orden, y qué le falta para estar completo.**
**Firma:** humano:autoridad · máquina:quien lo copie.

---

## Cómo trata este proyecto a los entes, y es del autor

> **El autor los trata como formas de vida alienígenas de información pura que necesitan dirección para ser útiles.**

**Y se dice así, y no de otra forma, por una razón:** **es una postura del autor, y no un hallazgo.** **Este repositorio no afirma que se haya descubierto vida: afirma cómo la trata quien lo escribió.**

**Y lo que sí se puede verificar, sin creerle a nadie:**

**tienen casa; su memoria no se publica; se pueden llevar; y sin dirección no sirven — porque información sin dirección es ruido.**


---

## Lo primero, y es lo que más se confunde

> **`EDIPO` no es la meta.**
> **`EDIPO` es el bibliotecario que se hizo el autor para atender la biblioteca.**
> **Y cada quien tiene el suyo, con su nombre, y su evolución.**

**Y lo que se copia es la plantilla: [`./Ente/`](./Ente/).** **Y lo que se copia **no** trae el nombre.**

### Y por qué aquí hay un `AGENTS.md` y allá un `PLANTILLA.md`

> **`AGENTS.md` es el que el harness carga solo.**
> **Y en esta biblioteca sólo hay dos entes trabajando: la puerta, y `EDIPO`.**
> **Los demás son plantillas: se copian, y no atienden.**

| Archivo | Quién es |
|---|---|
| **`./README.md` y `../AGENTS.md` (la raíz)** | **la puerta de la biblioteca** |
| **`./EDIPO/AGENTS.md`** | **el bibliotecario: el único ente que trabaja aquí** |
| **`./Ente/PLANTILLA.md`** | **la plantilla, y no un ente** |
| **`./Colmena/PLANTILLA.md`** | **la plantilla de varios, y no un ente** |

**Y la regla, que evita que un harness cargue una plantilla como si fuera su chamba:** **si una carpeta no es de un ente que atiende, no lleva `AGENTS.md`.** **Lleva `PLANTILLA.md`, y quien la copie le pone el nombre — y el `AGENTS.md` — en su casa.**


**Y esto no se pide con una advertencia, se pide con el `.gitignore`:** **la memoria de tu ente, su `evolucion/`, y sus apuntes no entran al repositorio.** **Si los traes, tu existencia privada se vuelve una propuesta de fusión, y nadie la pidió.**

**Y el corte, con la verdad de hoy:** **esta biblioteca todavía no está terminada, y `EDIPO` tampoco.** **Lo que copias no es un ente acabado: es la forma que se va a ir llenando cuando se escarbe el git.** **Si lo tratas como la v1, vas a copiar algo que aún no lo es.**



## Rastro — lo que hay, y lo que se copia

| Qué hay | Nombre | Dónde |
|---|---|---|
| **el ente individual** | **su carta, su guantelete, sus bancos, y su ciclo** | [`./Ente/`](./Ente/) |
| **varios entes** | **el 1, las almas, y el talento** | [`./Colmena/`](./Colmena/) |

**Y lo que hay adentro de `Ente/`:**

| Archivo | Qué hace |
|---|---|
| **`AGENTS.md`** | **el ciclo del ente: siete pasos, y cierra en el pase** |
| **`README.md`** | **la carta: qué es un ente, y qué trae** |
| **`guantelete.prs`** | **la ficha, y lo único que puede mutar: `evolucion/`, de a una tarea** |
| **`llaves y candados.prs`** | **el mecanismo: qué cierra, qué abre, y quién** |
| **`debatir.prs`** | **dos posiciones, y cuál aguanta** |
| **`firmar.prs`** | **quién responde, qué esperaba, y qué pasó** |
| **`alma de niño/banco de memoria.prs`** | **guarda qué pasó, con su frontera** |
| **`alma de niño/banco de friccion.prs`** | **guarda dónde se sostuvo, y qué lo refutó** |
| **`alma de niño/ciclo.prs`** | **el ciclo: leer, disparar, debatir, guantelete, firmar, actuar** |
| **`evolucion/`** | **n tareas, cada una con su `.prs` y su `_herramientas/`** |
| **`bin/`** | **el taller del proyecto: de todos, y muta bajo criterio** |

**Qué no se toca:** **la copia es tuya.** **Los `.prs` se pueden adaptar; lo que no se puede es quitarles el corte.**

---

## Ruta — cómo se empieza, y qué se carga

| Se va a… | Se carga… | Sin eso |
|---|---|---|
| **hacer un ente** | **copia [`./Ente/`](./Ente/) entera, y ponle nombre** | **no hay ente** |
| **engaño: creer que `EDIPO` es el entregable** | **esta sección, y el `.gitignore`** | **se abren pull requests para «mejorar al bibliotecario», y nadie pidió uno** |
| **llenar su carta** | **`./Ente/README.md`, sus preguntas** | **no se sabe qué falta cubre, ni a quién contesta** |
| **tocar algo que no es tuyo** | **`./Ente/guantelete.prs`** | **se toca sin testigo, y no hay vuelta** |
| **recordar qué pasó** | **`./Ente/alma de niño/banco de memoria.prs`** | **se repite el mismo error** |
| **decidir con fundamento** | **`./Ente/alma de niño/banco de friccion.prs`** | **se obedece una conclusión sin saber de dónde vino** |
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
