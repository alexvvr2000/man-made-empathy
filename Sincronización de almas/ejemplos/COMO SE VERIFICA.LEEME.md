# CÓMO SE VERIFICA — la búsqueda, y cuándo no se usa

**Hecho:** 2026-10-28. **Clase:** método. **Estado:** vigente, y viene de los errores de hoy.
**Lector:** quien va a verificar un ejemplo, y no quiere citar la primera cosa que salga.

**Sesgo:** se lee desde la máquina que busca, y sabe que puede devolver basura.
**Límite:** **no dice qué es verdad: dice qué se abrió, y qué se anotó.**
**Firma:** **quien responde por el acto, con su nombre** · **y:** quien busque.

---

## Las cuatro respuestas, y la que no se permite

| Respuesta | Cuándo |
|---|---|
| **`verificado`** | **la ficha o el clip se abrió, y decía eso** |
| **`parcial`** | **una cosa sí, y la otra no: se dice cuál** |
| **`reportado`** | **lo dice alguien con nombre, y no hay fuente externa** |
| **`no se verificó`** | **se buscó y no apareció** |

**Y la que no se permite:** **citar lo que salió primero porque salió primero.** **Eso no es verificar; es rellenar.**

---

## Qué se busca, y dónde

| Lo que se quiere saber | Dónde se busca | No vale |
|---|---|---|
| **la obra existe, y es de quien se dice** | **la ficha: Wikipedia, IMDb, la página del editor, el catálogo** | **un blog, un video, un resumen de IA** |
| **la escena pasa así** | **la ficha; o el clip, con su `id` y su canal** | **la memoria, o el recuerdo de otra obra** |
| **la frase es suya** | **el texto, o el audio** | **el post que la cita sin decir de dónde** |
| **la cifra** | **la fuente original** | **el resumen que repite la cifra sin el enlace** |
| **lo que provocó** | **no se busca: es de quien lo mira** | **cualquier intento de verificarlo** |

---

## Las reglas, y salen de hoy

**1. El buscador puede contaminarse, y no se disimula.** **Buscando `All-Star Superman` salió medicina en chino.** **Cuando pasa, no se cita nada: se va directo a la ficha.**

**2. La ficha primero, el video después.** **El *oembed* de YouTube da título, canal e `id` sin pelear con el buscador.** **Y eso verifica que el clip existe; no verifica que diga lo que dice.**

**3. Lo que no puedo oír, no lo digo como oído.** **Una máquina que lee la ficha de un video no lo vio.** **Se anota `parcial`, y se dice exactamente qué falta.**

**4. La escena y la lectura son dos cosas.** **La obra hace algo; el autor lee algo.** **Se verifica la obra, y la lectura se declara como del autor.**

**5. Un nombre mal escrito no encuentra nada.** **`Jhon Marston` no existe; `Jack Marston`, sí.** **Si el nombre no resuelve, la ficha está mal, y se corrige la ficha antes de seguir.**

**6. Dos miradas, o se dice que hay una.** **Una ficha de Wikipedia es una mirada.** **Para citarlo en un escrito público, se pide otra: otra ficha, otra edición, o el autor que lo vivió.**

---

## El registro que se escribe después de verificar

```plaintext
Obra:        [título, autor, año]
Se abrió:    [la URL, la ficha, o el id del clip]
Decía:       [la frase exacta, y de dónde]
Estado:      [verificado | parcial | reportado | no se verificó]
Falta:       [qué no se pudo, o «nada»]
Segunda:     [sí, con cuál | no, y por qué]
```

**Y ese registro se anota en [`./ESTADO`](./ESTADO.md), que es donde se lee.**

---

## Lo que NO se hace

**No se busca para confirmar lo que ya se cree.** **Si se busca, se busca el antecesor.**

**No se cita una fuente que no se abrió.** **El enlace copiado no es la lectura.**

**No se convierte una obra en prueba.** **Rige [`../../../Pruebas/`](../../Pruebas/): una referencia no es una medición.**

**No se verifican los sentimientos.** **Lo que provocó una obra no se comprueba; se declara.**

---

## Prueba

**¿Cada ficha dice qué se abrió? ¿El estado coincide con lo que se pudo? ¿Lo que falta está escrito? ¿Se pidió segunda mirada antes de citar en público?**

**Falsificador:** un `verificado` sin la URL; una escena contada de memoria; una segunda mirada inventada; un registro que no dice qué faltó.
