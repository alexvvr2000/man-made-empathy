# VERSIONES — qué es beta, qué es la `v1.0.0`, y cómo se nombra lo que venga

**Hecho:** 2026-10-29. **Clase:** registro de versiones. **Estado:** vigente.
**Lector:** quien vea los tags del repositorio y no sepa cuál es cuál.
**Dueño:** humano:autoridad.

**Sesgo:** se lee desde el que llega al historial y encuentra 80 tags sin orden.
**Límite:** **no borra historia.** **Renombra, y dice por qué.**
**Firma:** humano:autoridad.

---

## Lo que se hizo, y por qué

> **Todo lo anterior al 2026-10-29 es beta.**
> **La `v1.0.0` es el primer release, y es del 2026-10-29.**

**Y no se borró nada.** **Los tags viejos se quedan, y se les puso nombre con fecha.**

---

## Los tags, y qué significa cada familia

| La familia | Qué es | Ejemplo |
|---|---|---|
| **`beta-AAAA-MM-DD`** | **el último commit de cada día anterior al release** | **`beta-2026-10-26`** |
| **`v0.9.9-beta`** | **el primer commit de todos, el del 1 de octubre** | **lo que antes se llamaba `v1.0.0`** |
| **`v1.0.0`** | **el primer release, el 2026-10-29** | **el que se ve en GitHub** |
| **y los tags viejos con nombre propio** | **`faro-antes-de-base`, `mantis-antes-del-swap`, `v182838`, `antes-del-corte`** | **se quedan: son la historia, y no se tocan.** **Pero no son las eras del trabajo: el trabajo se corta por día** |

**Y `v1.0.0` también se llamaba el primero, y se movió.** **El nombre no se puede repetir, y el que importa es el de hoy.**

---

## Y el release, que es lo que la gente ve

**El tag `v1.0.0` lleva el mensaje, y es el del release:**

> **`v1.0.0` — Next is the soul world.**

> **`Fire Force` (Atsushi Ōkubo; David Production), el final de la serie, la precuela de `Soul Eater`.** **La escena dice: next is the soul world.**
> **Y es lo que este repositorio sostiene: lo que se escribe no es de la persona; es del alma que deja rastro.**

**Y la imagen no va.** **Es una escena de una obra, y el repo no lleva imágenes de obras: las cita.** **Rige [`./ATTRIBUTION.md`](./ATTRIBUTION.md).**

---

## Cómo se nombra lo que venga

**Y la regla es la de siempre: fecha, y un número que suba.**

| Lo que | Cómo |
|---|---|
| **un arreglo que no cambia la idea** | **`v1.0.1`** |
| **algo nuevo que no rompe lo anterior** | **`v1.1.0`** |
| **algo que rompe lo anterior** | **`v2.0.0`** |
| **y lo que todavía no es release** | **`v1.1.0-beta`**, y con fecha si hace falta |

**Y lo que salga de escarbar git va a ser `v1.1.0` en adelante, y no un borrón de la `v1.0.0`.**

---

## Prueba

**¿Se distingue lo beta de la `v1.0.0`? ¿Nada se borró? ¿Cada tag dice de qué fecha es? ¿El release lleva el mensaje, y no la imagen?**

**Falsificador:** un tag movido sin decir dónde estaba; un beta presentado como release; una imagen de una obra en el release; un nombre repetido.
