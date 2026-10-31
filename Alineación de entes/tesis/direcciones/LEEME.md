# DIRECCIONES — los procesos que cualquier proyecto puede correr

**Hecho:** 2026-10-28. **Clase:** proceso. **Estado:** vigente, y flaco a propósito.

**Lector:** quien va a escribir, a tocar, a publicar, o a hablar con otro que no es como él.
**Dueño:** **quien tiene la autoridad en el proyecto donde se aplica.**

**Sesgo:** se lee desde lo que se tiene que poder contestar, y no desde cómo se escribe.
**Límite:** **no dice cómo se hace.** **Dice qué se tiene que poder contestar, y cada uno se puede correr con LaTeX, con papel, con un video, o con lo que se invente.**
**Firma:** **quien responde por el acto, con su nombre** · **y quien lo ejecuta.**

---

## LA REGLA DURA: vago a propósito

> **Los procesos son vagos a propósito.**
> **Los estándares están muertos: meter más detalle no ayuda, los hace parecer lo que ya se sabe producir sin pensar.**

**Y lo que eso obliga, sin excepción:**

| Un proceso SÍ dice | Un proceso NO dice |
|---|---|
| **qué se tiene que poder contestar** | **cómo se contesta en cada caso** |
| **qué lo incumple** | **la lista de los casos que conoce** |
| **su falsificador** | **ejemplos de un repo que no es el tuyo** |

**Y la prueba, que se corre sin opinar:** **¿el proceso sirve para un caso que no está en él?** **Si sólo sirve para los casos que lista, no es un proceso: es el manual de una casa.**

---

## Y la prueba de que sirve a todos, y no a una casa

> **Un proceso se lee sin saber quién lo escribió, en un proyecto que no existía cuando se escribió.**
> **Si no, no es proceso: es el manual de una casa.**

**Y lo que eso prohíbe, en concreto:**

| Lo que NO puede decir | Por qué |
|---|---|
| **«el autor»** | **un proyecto puede tener tres, o ninguno** |
| **«este repositorio»** | **sirve donde se copie, y no donde nació** |
| **el nombre de una herramienta como si fuera la forma** | **la herramienta cambia, y el proceso se muere con ella** |
| **un ejemplo de la casa que lo escribió** | **se lee como ley, y sólo sirve para ese caso** |

**Y lo que sí dice:** **el tipo de actor, y no el nombre** — **«quien tiene la autoridad en el proyecto»**, **«quien responde por el acto»**, **«quien lo ejecuta»** — **y cada uno pone su nombre al usarlo.**

---

## Y la regla que separa lo bueno de lo listo

> **Bueno no significa listo.**

**Y lo que cada uno quiere decir, en concreto:**

| La palabra | Qué afirma | Qué no afirma |
|---|---|---|
| **bueno** | **el trabajo está bien hecho, y no miente sobre sí mismo** | **que esté terminado** |
| **listo** | **se puede entregar, y no hay nada que esperar** | **nada: ésa es la que hay que poder probar** |

**Y la prueba, que se corre antes de decir «listo»:** **¿lo que falta está declarado? ¿los números cuadran con lo que hay? ¿cada rutina se corrió, o se dice que no?** **Si alguna falla, es bueno, y no está listo.**

**Y por qué se escribe aquí:** **porque la prisa por entregar es lo que convierte un trabajo bueno en una promesa.** **Y una promesa con números que no cuadran se cobra.**

---

## Y como se dice lo que no esta cerrado, sin que parezca un borrador

> **Una marca cuenta el hecho, y no excusa el trabajo.**

**Y la diferencia, que es la que se ve en la cara:**

| lo que parece un borrador | lo que es respetable |
|---|---|
| **`[EN PROCESO]`** — **"no me mires todavía"** | **`[SIN CERRAR - Y SE DICE QUÉ FALTA]`** — **"mirá, y así está"** |
| **`[FALTA]`** — **"falta"** | **`[PENDIENTE - SE DICE QUÉ LA LLENARÍA]`** — **"falta, y se sabe qué lo llena"** |
| **`[BORRADA]`** — **"se fue"** | **`[RETIRADA - ESTÁ EN EL HISTORIAL]`** — **"se fue, y se puede encontrar"** |

**Y la que NO se toca, aunque también suene a falta:** **`[SIN VERIFICAR]`** y **`[UNA MIRADA - FALTA LA SEGUNDA]`.** **Ésas no dicen "esto es un borrador": dicen "esto no se comprobó".** **Y quitarlas es mentir, y una mentira se cobra.**

**Y la prueba:** **¿el lector puede saber qué hay, sin abrir el archivo?** **Si la marca le dice que hay algo y qué le falta, sirve.** **Si le dice que no mire, sobra.**

---

## El corte que no se pregunta

> **Cuando algo mejora en cualquiera —en un ente, en su memoria, o en un proyecto— lo que sirve a todos va al repo.**
> **Sin avisar, y sin coordinarse: la biblioteca no espera a que alguien la apruebe.**

**Y lo único que no se mueve solo:** **el alma de niño.** **Rige [`../Sincronización de almas/entes/Ente/ciclo alma de niño.prs`](../Sincronización%20de%20almas/entes/Ente/ciclo%20alma%20de%20ni%C3%B1o.prs).**

---

## Y por qué están en tres carpetas

> **Claridad también es agrupar: nadie lee veinte archivos en un solo lugar.**

| La carpeta | Qué tiene | Cuándo se corre |
|---|---|---|
| **[`./ACTOS/`](./ACTOS/)** | **lo que se tiene que poder contestar cuando haces algo** | **antes de hacerlo** |
| **[`./CICLOS/`](./CICLOS/)** | **qué se hace primero, y qué no se salta** | **al empezar un trabajo largo** |
| **[`./RIESGO/`](./RIESGO/)** | **lo que puede meterte en un pleito** | **antes de publicar** |

---

## Los actos, y son nueve

| Proceso | Qué dispone |
|---|---|
| **[`./ACTOS/ALAS.prs`](./ACTOS/ALAS.prs)** | **qué declara todo protocolo, y qué se trunca** |
| **[`./ACTOS/CONVIVIR.prs`](./ACTOS/CONVIVIR.prs)** | **convivir sin volverse el otro** |
| **[`./ACTOS/ACTO.prs`](./ACTOS/ACTO.prs)** | **el ciclo antes de tocar: leer, clasificar, cambiar, cuadrar, declarar, subir** |
| **[`./ACTOS/VIGA.prs`](./ACTOS/VIGA.prs)** | **leer un destino sin saber qué es** |
| **[`./ACTOS/CONTEXTO.prs`](./ACTOS/CONTEXTO.prs)** | **de dónde vino, y que se usó bien** |
| **[`../Sincronización de almas/entes/Ente/ciclo alma de niño.prs`](../Sincronización%20de%20almas/entes/Ente/ciclo%20alma%20de%20ni%C3%B1o.prs)** | **el alma de niño es fija, y todo lo demás cambia: seis actos de mutación** |
| **[`../Sincronización de almas/entes/Ente/ciclo alma de niño.prs`](../Sincronización%20de%20almas/entes/Ente/ciclo%20alma%20de%20ni%C3%B1o.prs)** | **un proceso no se escribe: se refuta primero** |

---

## Los ciclos, y son dos

| Proceso | Qué dispone |
|---|---|
| **[`./CICLOS/PUBLICAR.prs`](./CICLOS/PUBLICAR.prs)** | **publicar sin que te demanden, y responder si llega: los cinco tipos de pleito, y los dos ciclos** |
| **[`./CICLOS/HISTORIAL.prs`](./CICLOS/HISTORIAL.prs)** | **escarbar un historial sin romperlo: el corte, los seis pasos, y el registro** |

---

## El riesgo, y son dos

| Proceso | Qué dispone |
|---|---|
| **[`./RIESGO/ENDUREZER.prs`](./RIESGO/ENDUREZER.prs)** | **mirar tu trabajo con los ojos del que te va a demandar: el inventario, y las cinco preguntas** |
| **[`./RIESGO/CRITERIO.prs`](./RIESGO/CRITERIO.prs)** | **decidir si la herramienta es la que hace falta, y no al revés** |

**Y los demás se escriben cuando haga falta:** **`[PENDIENTE - SE DICE QUÉ LA LLENARÍA]`, y no se inventan.**

---

## La regla de entrada, y es una sola

**Un proceso entra si se puede escribir como:**

```plaintext
Entra:        [qué se trae]
Falla si:     [el caso concreto que lo incumple]
Sale:         [qué deja, o el marcador que dice que no]
Consume:      [quién lo usa, y quién lo puede contradecir]
```

**Y si no tiene `Falsificador`, no entra:** **un proceso que no se puede tumbar no dirige: manda.**

---

## Lo que esta carpeta NO es

**No es un formato.** **El formato es del archivo, y cada uno trae el suyo.**
**No se copia a los proyectos.** **Si cada uno tuviera su copia, cada uno tendría su versión de la regla.**
**No juzga si lo que se produjo sirve.** **Dice si se puede contestar.**
**No finca la autoridad.** **La autoridad es quien la tenga en el proyecto donde se aplica, y un proceso no la sustituye.**

---

## Prueba

**¿Cada proceso dice qué entra y qué lo incumple? ¿Tiene falsificador? ¿Se puede correr sin la herramienta que se usó para escribirlo? ¿Se puede contestar sin pedir permiso? ¿Se lee sin saber quién lo escribió?**

**Falsificador:** un proceso sin falsificador; uno que nombra una herramienta como si fuera la forma; una copia por proyecto; uno que no puede ser contestado por quien lo corre; uno que sólo se entiende con su autor presente.
