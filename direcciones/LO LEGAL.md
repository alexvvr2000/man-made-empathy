# LO LEGAL — el ciclo, y son dos: antes de publicar, y si te llega algo

**Hecho:** 2026-10-29. **Clase:** proceso. **Estado:** vigente.
**Lector:** quien vaya a publicar algo, y quien abra un correo de un abogado.
**Dueño:** humano:autoridad.

**Sesgo:** se lee desde el que puede reclamar, y desde el que va a quedar expuesto.
**Límite:** **no sustituye a un abogado.** **Ordena lo que se puede hacer sin uno, y marca dónde hace falta.**
**Firma:** humano:autoridad · máquina:quien lo corra.

---

## Y son dos ciclos, porque son dos problemas distintos

> **Prevenir es antes de publicar: buscar, declarar, y no copiar.**
> **Defenderse es después: lo que ya está publicado, y alguien reclama.**

**Y confundirlos es lo que hace que uno se defienda con excusas.** **Lo que se previene no se defiende: no pasó.**

---

# CICLO 1 — ANTES DE PUBLICAR

**Y se corre cada vez que algo va a salir: un release, una ficha, una imagen, un chat, un nombre.**

```plaintext
1. INVENTARIO   ¿qué entra? Se nombra pieza por pieza: texto, imagen, enlace, nombre.
2. FUENTE       ¿de quién es cada pieza? Si no se sabe, no entra.
3. DERECHO      ¿se puede usar? Citar, citar con ficha, o no entrar.
4. DECLARAR     ¿quedó dicho dónde está y si se verificó? Si no, no entra.
5. ABOGADO      ¿esto necesita un abogado? Si hay duda, se pregunta.
6. PUBLICAR     y se anota qué se publicó, con fecha.
```

**Y las reglas de cada paso, que son las que ya están escritas:**

| El paso | La regla | Dónde |
|---|---|---|
| **inventario** | **lo que no se nombró, no entra** | **este archivo** |
| **fuente** | **una obra sin autor no entra; y un canal de terceros se nombra y no se enlaza** | **[`./ATTRIBUTION.md`](../ATTRIBUTION.md)** |
| **derecho** | **se cita y se remite; no se reproduce** | **[`./Sincronización de almas/ejemplos/COMO SE VERIFICA.md`](../Sincronización%20de%20almas/ejemplos/COMO%20SE%20VERIFICA.md)** |
| **declarar** | **`[SIN VERIFICAR]` es una respuesta; el silencio no** | **[`./Sincronización de almas/ejemplos/ESTADO.md`](../Sincronización%20de%20almas/ejemplos/ESTADO.md)** |
| **abogado** | **si hay duda, se pregunta; no se resuelve de memoria** | **[`./PARA EL ABOGADO.md`](../PARA%20EL%20ABOGADO.md)** |

---

# CICLO 2 — SI TE LLEGA UNA RECLAMACIÓN

**Y aquí no se improvisa. Una reclamación tiene forma, y su respuesta también.**

```plaintext
1. NO CONTESTES EN CALIENTE.   Un correo respondido con miedo es una admisión.
2. GUARDA TODO.                El correo, la fecha, y qué reclamó. Sin eso, no hay defensa.
3. MIRA QUÉ RECLAMA.           ¿Dice la obra, la pieza, y dónde está? Si no lo dice, se pide.
4. BUSCA LA PIEZA.             ¿Está en el repo? ¿Se publicó, y cuándo?
5. CONTESTA CON LO QUE HAY.    La ficha, su fuente, y qué se hizo. Sin excusas.
6. Y HAZ LO QUE TOQUE.         Si hay que quitar, se quita, y se dice que se quitó.
```

**Y lo que dice GitHub, y es lo que va a pasar si es una reclamación formal:**

> **GitHub tiene un procedimiento de ***takedown*** y otro de ***counter-notice***.** **Se quita la pieza, y se avisa; y el que la subió puede pedir que se vuelva a poner, con sus razones, y con su nombre.**
> — [DMCA Takedown Policy de GitHub](https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy) · [guía del counter-notice](https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-counter-notice)

**Y la lección de eso:** **el `counter-notice` pide tu nombre y tu consentimiento a la jurisdicción.** **O sea: defenderse no es gratis, y por eso se previene.**

---

## Y las cuatro cosas que este ciclo NO hace

**No dice que tengas razón.** **Dice qué tienes, y dónde está escrito.**

**No borra la historia.** **Si se quita algo, se declara que se quitó, y por qué.** **Y el historial de git lo tiene: borrarlo es peor.**

**No sustituye al abogado.** **Lo llama a tiempo, y le lleva [`./PARA EL ABOGADO.md`](../PARA%20EL%20ABOGADO.md).**

**Y no promete que no pase nada.** **Promete que, si pasa, hay con qué contestar.**

---

## Lo que se revisa en cada release, y son seis preguntas

1. **¿Hay alguna imagen, y es de alguien?**
2. **¿Hay algún enlace a una copia, y no a la obra?**
3. **¿Hay alguna ficha sin autor, o sin `[SIN VERIFICAR]`?**
4. **¿Hay algún nombre de obra usado como nombre propio?**
5. **¿Hay algo de terceros en lo que se publica, y se dice?**
6. **¿El abogado ya lo vio, o se declara que no?**

**Y si alguna se contesta mal, el release espera.** **No se publica y luego se arregla.**

---

## Prueba

**¿Se corrió el ciclo antes de publicar? ¿Cada pieza tiene fuente, o no entró? ¿Si llegara una reclamación, hay con qué contestarla? ¿Se sabe qué se publicó, y cuándo?**

**Falsificador:** una imagen sin declinar; un enlace a una copia; una ficha sin estado; un release sin las seis preguntas; una reclamación contestada sin guardar nada.
