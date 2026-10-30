# bin/ — lo mínimo de EDIPO, y se publica

**Cuándo se abre:** **cuando EDIPO atiende, y se necesita saber qué puede correr.**

**Hecho:** 2026-10-29. **Clase:** el taller del bibliotecario. **Estado:** cuatro herramientas, y crece cuando haga falta.

**Sesgo:** se lee desde el que va a correrlo, y no desde el que lo escribió.
**Límite:** **no mantiene versiones, ni publica nada.** **Atiende, dice qué hay, y dice qué no.**

---

## Las cuatro herramientas, y qué hace cada una

| Lo que | Qué hace |
|---|---|
| **`ver-tesis`** | **lista los días con commits de la biblioteca, y sus commits** |
| **`decir-quien`** | **dada una pieza, dice de quién es, y en qué estado está** |
| **`que-falta`** | **dice qué está pendiente, qué está sin cerrar, y qué está sin verificar** |
| **`buscar`** | **busca en el catálogo antes de decir que no hay: un bibliotecario no contesta de memoria** |
| **`no-se`** | **anota la pregunta que no pudo contestar, y la deja como pieza que falta** |

**Y las cuatro son de un bibliotecario, y no de un ingeniero:** **dónde está, de quién es, qué falta, y qué no sé.**

---

## Por qué `no-se` es la más importante

> **Un bibliotecario que no sabe algo, y no lo dice, va a inventar.**
> **Y las preguntas que nadie puede contestar son el índice de lo que falta escribir.**

**Cada pregunta anotada es una pieza que la biblioteca no tiene.** **Y se lee antes de escribir nada nuevo: lo que falta, primero.**

---

## Por qué esto se publica, y su memoria no

> **`bin/` es la forma de trabajarlo. Quien copie a `EDIPO` necesita saber qué corre, y cómo.**
> **Su memoria es su vida privada, y se la lleva él.**

---

## Cómo se corre

```powershell
# desde la carpeta del ente, y no desde el repo
cd "Sincronización de almas\entes\EDIPO"
.\bin\ver-tesis --dias 10
.\bin\decir-quien BUSCAR
.\bin\que-falta
.\bin\no-se "¿cuándo se escribió la primera dirección?"
```

**Y tiene que correr sin pedirle nada al repo.** **Si depende del repo, no es un trabajador: es una pieza del inmueble.**

---

## Prueba

**¿Corren solas? ¿Dicen lo que hay, y lo que falta? ¿Lo que no pueden, lo dicen?**

**Falsificador:** un `bin/` que declara cosas que no hace; uno que no corre sin el repo; un `[NO SÉ]` que no aparece.
