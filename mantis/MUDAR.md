# MUDAR de mantis — las cuatro pieles, nacidas en regla

**Nombre.** MUDAR de MANTIS.
**Origen.** **De la decisión de la autoridad: retroceder y nacer en regla.** **Las cuatro tareas existían porque yo las juzgué necesarias; no porque una falta las pidiera.** **Se borraron, y se vuelven a crear por `MUDAR`, con su falta nombrada, su término y su autoridad.**

**Unidad:** registro.
**Aplica a:** crecer.
**Tipo:** se ejecuta. **Se lee antes de crear una tarea; se escribe al crearla.**
**Lector:** quien va a hacer que `MANTIS` haga algo que hoy no hace.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** la tarea se lee desde la falta que cubre, no desde la costumbre de que exista.
**Límite:** **no decide si la tarea sirve; eso lo dice el uso.** **No muda el criterio.**
**Firma:** humano:autoridad · máquina:quien la cree.

**Variables:** falta · piel · término · autoridad · criterio
**Peor:** se crea una tarea porque parece que debe existir, **y el alma se llena de lo que nadie pidió.**
**Quién:** quien use un alma que hace mucho y sostiene poco.

---

## La regla que se aplica aquí

**Rige [`./base/alma en blanco/MUDAR.vd`](../base/alma%20en%20blanco/MUDAR.vd).**

**Y el borde, que es el mismo:** **mudar es cubrir una falta; nacer es cambiar lo que se sostiene.** **`Criterio: igual` en las cuatro, o no son mudas.**

---

## Las cuatro pieles

| Tarea | Falta que cubre | Termina cuando | Cierra en | Criterio |
|---|---|---|---|---|
| **`el cero/`** | **nada comprueba que el candado cero diga lo mismo que el repo, y ya citó fantasmas durante meses** | **cuando `estandar/` traiga su propia comprobación** | `el cero/el cero.tra` | **igual** |
| **`los candados/`** | **nada dice cuántos candados están incompletos, y hoy son 52 de 94** | **cuando la cifra llegue a cero, o cuando la autoridad decida que los que quedan no se completan** | `los candados/los candados.tra` | **igual** |
| **`la tesis/`** | **las tres clases de tesis existen en el estándar y nadie las compone cuando se piden** | **nunca: se compone on demand, y su término es por pedido** | `la tesis/la tesis.tra` | **igual** |
| **`la memoria/`** | **el turno cierra sin pase, y el siguiente empieza a ciegas** | **nunca: es el pase de cada turno; su término es el turno** | `la memoria/la memoria.tra` | **igual** |

**Y lo que esas dos «nunca» significan, porque no son una fuga:** **`Terminar: por pedido` y `Terminar: por turno` son términos declarados, no ausencia de término.** **Lo que `MUDAR` prohíbe es no saber cuándo se funde; aquí sí se sabe: cada vez que se pide, o cada vez que cierra el turno.**

---

## Lo que se declara al crear cada una

```plaintext
Muda:        mantis | Falta: [la de la tabla] | Piel nueva: [la tarea]
Nombre:      [el de la tarea] | Termino: [Crear | Terminar | Cierra en]
Conserva:    [el corte del .prs, y su .paso]
Funde:       ninguna — es la primera piel
Autoridad:   humano:autoridad
Criterio:    igual
```

---

## Prueba

**¿Cada tarea declara la falta que cubre, y se puede señalar? ¿Cada una declara su término, aunque sea por pedido o por turno? ¿Cada una dice dónde cierra? ¿Se puede escribir `Criterio: igual` en todas?**

**Falsificador:** una tarea sin falta nombrada; una sin término; una que cambió el criterio y se llama muda; una creada sin autoridad; una que existe porque «ya estaba».

## Transiciones

- Aparece una falta que se puede nombrar → **se crea la tarea, y entra en esta tabla.**
- Una tarea deja de cubrir su falta → **se funde con `RETIRAR`, y queda su `Vacío:`.**
- La falta no se puede nombrar en una línea → **no falta una tarea: falta un nivel; se rehace.**
- En cualquier otro caso → **se declara, y se cierra.**
