# Proceso de auditar configuración

**Unidad:** proceso.
**Aplica a:** auditar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el repo tal como está ahora.
- **Falla:** una cifra, una ruta o un nombre no coincide con lo que hay; no se declara la diferencia.
- **Sale:** la lista de desviaciones, cada una con su ubicación y su corrección.
- **Consume:** quien edita.

## Cómo se aplica

1. **Contar lo que hay.** Cuántas sub-tareas, cuántos procesos, cuántos documentos, en cada parte.
2. **Comparar con lo que se dice.** Buscar cifras y nombres en los documentos.
3. **Verificar las rutas.** Que cada ruta relativa resuelva a un archivo real.
4. **Verificar los nombres.** Que ningún documento cite una pieza que ya no existe con ese nombre.
5. **Verificar la jerga.** Que ningún documento use un nombre interno como si el lector supiera qué es.
6. **Verificar el nivel.** Que cada documento declare si es estándar, instancia, implementación o caso, y que esté donde le toca.
7. **Declarar la desviación.** Dónde está, qué dice y qué hay. Sin corregir todavía.

`Sub-tareas: [n real | n dicho] | Procesos: [n real | n dicho] | Rutas rotas: [n] | Nombres muertos: [n] | Jerga sin glosa: [n] | Nivel sin declarar: [n]`

## El nivel

Un archivo está en el nivel correcto si dice **cómo tiene que ser** (estándar, va en `2 Ouroboros/`), **qué se hace hoy** (instancia, va en su parte), **con qué** (implementación, va en `Era/`), o **qué pasó una vez** (caso, no va en `1 Tesis/`).

| Señal | Nivel | Si está mal ubicado |
|---|---|---|
| se aplica a más de una instancia | estándar | le falta `2 Ouroboros/` |
| cambia cuando cambia el interior | instancia | no puede vivir en `2 Ouroboros/` |
| depende de una tecnología, lenguaje o modelo | implementación | no puede vivir fuera de `Era/` |
| describe un caso, una obra o un hecho con fecha | caso | no entra en `2 Ouroboros/` |

**Un estándar en el nivel equivocado es invisible como estándar:** se lee como un hermano de lo que estandariza, y nadie sabe cuál manda. Rige `../../2 Ouroboros/formato de proceso.md`.

**Prueba del nivel:** ¿el documento se aplica a más de una instancia? ¿puede sobrevivir a que cambie el interior?

**Falsificador del nivel:** un estándar dentro de una instancia; un caso dentro de `2 Ouroboros/`; un documento sin nivel declarado; una implementación fuera de `Era/`.

## La jerga

Un nombre interno es válido en el documento que lo gobierna. En cualquier otro aparece **solo con glosa**, o no aparece.

| Nombre interno | Dónde es legítimo | Qué se escribe fuera de ahí |
|---|---|---|
| `notas.md` | `README` de MANTIS, `AGENTS.md` | «lo que se anotó», sin nombrar el archivo |
| `Ouroboros`, `S.A.R.A`, `MANTIS`, `ARDOR`, `ACERO` | su `README` y su `Derrotero` | se nombra y se glosa la primera vez en el documento |
| una ruta (`./x/y.md`) | como enlace o como cita de fuente | el lector es una persona: se nombra la pieza, no el archivo |
| un campo del esquema (`Vacío:`, `Retiene`) | el proceso que lo define | se explica en palabras antes de usarlo como argumento |

**La prueba de la suciedad, y es una sola pregunta:**

> **¿Esta frase le sirve a alguien que no conoce el repo?**

Si la frase pierde sentido al quitarle el nombre interno, **el argumento no era el argumento: era el nombre.** Y un nombre interno no convence a nadie que no lo conozca.

**Falsificador de la jerga:** un nombre interno usado como remate de un argumento; un nombre interno sin glosa fuera de su documento; una frase cuyo sentido desaparece al quitarle la ruta.

## Prueba

¿Cada cifra del repo coincide con la cuenta real? ¿Cada ruta resuelve? ¿Cada nombre interno fuera de su documento tiene glosa, y la frase se sostiene sin él?

**Falsificador:** una cifra sin verificar; una ruta que no resuelve y no se declara; un nombre citado que ya no existe; un nombre interno usado como argumento sin glosa.

## Transiciones

- Si hay desviaciones → `editar.md` las corrige.
- Si el conteo cambió → se actualiza la vigencia.
- En cualquier otro caso → se entrega y se cierra.
