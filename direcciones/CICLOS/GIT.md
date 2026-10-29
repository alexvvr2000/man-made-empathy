# GIT — el ciclo de un turno de git, y lo legal no se salta

**Hecho:** 2026-10-29. **Clase:** ciclo. **Estado:** vigente.
**Lector:** quien vaya a trabajar el historial, y quien tenga que defender lo publicado.
**Dueño:** **quien tiene la autoridad en el proyecto donde se aplica.**

**Sesgo:** se lee desde el pleito que puede llegar, y no desde el commit que se quiere hacer.
**Límite:** **no decide qué se rescata.** **Decide el orden, y qué no se puede saltar.**
**Firma:** **quien responde por el acto, con su nombre** · **y quien lo ejecuta.**

**Peor:** se escarba el historial durante semanas, **y un día se publica algo sin preguntar, y lo que se ganó en un mes se pierde en una demanda.**

---

## La regla de arriba, y no se salta nunca

> **Lo legal no es un paso al final: es la puerta de cada paso.**

**Y en cada turno de git se corren los tres ciclos de [`./LO LEGAL.md`](./LO%20LEGAL.md):**

| El ciclo | Cuándo | Qué pregunta |
|---|---|---|
| **CICLO 0 — antes del commit 1** | **antes de tocar el historial** | **cuadrar, rutas, copyright, fuente, nombres, datos, abogado** |
| **CICLO 1 — antes de publicar** | **en cada commit que sale** | **qué entra, de quién es, y si se puede usar** |
| **CICLO 2 — si llega una reclamación** | **cuando llegue** | **no contestar en caliente, guardar todo, y mirar qué reclama** |

**Y el sexto tipo de pleito, que no es pleito pero se lleva el proyecto igual:** **afirmar que algo está probado cuando no se corrió.**

---

## El turno de git, y son seis pasos

**Uno por día, del más nuevo al `2026-10-01`.** **Y el día es el corte: no hay eras que nombrar.**

```plaintext
1. LEE        ese día: sus commits, sus mensajes, y qué cambió
2. JUZGA      qué de eso aguanta hoy, y qué se cayó
3. SUBE       lo que aguanta va a la biblioteca, y a los entes si les toca
4. CUADRA     los números, las rutas, y el inventario
5. DECLARA    lo que se cayó, y por qué; y lo que no se puede juzgar, con qué falta
6. COMMIT     uno por día, con su rango de hashes, si lo legal pasó
```

**Y los pasos 3 y 4 no se pueden saltar entre sí:** **lo que sube sin cuadrar deja el repo mintiendo.** **Y lo que cuadra sin subir es un día perdido.**

---

## Y el freno, que es lo que impide que se olvide

> **Antes del commit, se corre el ciclo legal.**
> **Si algo no pasó —una fuente, un nombre, un dato, un número—, el commit espera, y se dice qué falta.**

**No es una advertencia: es la puerta.** **Y si el commit sale sin eso, el turno no se cerró, y se anota como fallo.**

---

## Lo que sube, y a dónde

| Lo que se rescató | A dónde va |
|---|---|
| **lo que sirve a cualquier ente** | **la biblioteca: `entes/Ente/`** |
| **lo que sirve a la gente, y no a un ente** | **la biblioteca: `direcciones/`, `ideas/`, `ejemplos/`** |
| **lo que es la experiencia de un ente** | **su `evolucion/`, y no se publica** |
| **lo que es la caja de una tarea** | **esa tarea, y no se publica** |

**Y la regla que no se pregunta:** **lo que sirve a todos, va al repo.** **Sin avisar, y sin coordinarse.** **Rige [`../README.md`](../README.md).**

---

## Lo que queda en manos de la autoridad, y no se delega

**Y se dice aquí para que nadie lo confunda:**

| Lo que | Por qué no se delega |
|---|---|
| **dar el push** | **un commit empujado sin que se mire es un riesgo legal, no una comodidad** |
| **decidir que se publica** | **es el criterio, y el criterio no se terceriza** |
| **la reunión con el abogado** | **una vez, y no la puede hacer una máquina** |
| **el dictamen de lo legal** | **lo da un abogado, y no este repositorio** |

**Y lo que sí se delega, porque es mecánico:** **leer el día, juzgar lo que aguanta, subir lo que sirve, cuadrar los números, declarar lo que se cayó, y hacer el commit.**

---

## El registro del turno, y es la prueba

**Cada turno deja un archivo, y sin él no se cerró:**

```plaintext
Día:            [la fecha, y su rango de hashes]
Commits:        [cuántos]
Se sostiene:    [qué subió, y a dónde]
Se cayó:        [qué no, y por qué]
No se juzga:    [qué falta]
Legal:          [qué se buscó, y qué se declaró; o [NO SE BUSCÓ - EL COMMIT ESPERA]]
Inventario:     [los números, antes y después]
Rutas:          [cero rotas, o cuántas quedan]
```

---

## Prueba

**¿Se corrieron los tres ciclos legales, o se declaró por qué no? ¿Cada día tiene su registro? ¿Lo que subió sirve a alguien más? ¿El inventario cuadra? ¿Las rutas dan cero? ¿El commit lleva su rango de hashes?**

**Falsificador:** un turno sin el ciclo legal; un commit sin registro del día; algo publicado sin fuente ni estado; un inventario que no cuadra; una ruta rota; un push dado sin que se mirara.
