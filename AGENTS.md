# AGENTS.md — la puerta del repositorio

**Ente:** `man-made-empathy` · **Tarea:** sostener que la dirección se puede contestar, y que lo que corre se puede repetir.
**Clase:** se ejecuta. **Lector:** cualquier agente, humano o modelo, que abra este repositorio.
**Dueño:** humano:autoridad. **Estado:** vigente.

**Sesgo:** se lee desde el que llega sin saber nada de esto, y desde lo que ya corre.
**Límite:** **no juzga si la tesis es cierta.** **Dice qué hay, dónde, qué se toca, y qué no.**
**Firma:** humano:autoridad · máquina:agente-de-turno.

---

## Rastro — el cuerpo

| Qué hay | Nombre | Dónde |
|---|---|---|
| **El producto: lo que se copia y corre** | **el ente, y la colmena** | [`./Sincronización de almas/entes/`](./Sincronización%20de%20almas/entes/) |
| **La puerta del producto** | **qué copiar, en qué orden, y qué pasa si falta** | [`./Sincronización de almas/entes/README.md`](./Sincronización%20de%20almas/entes/README.md) |
| **La dirección: lo que se tiene que poder contestar** | **nueve, cada una con su falsificador** | [`./direcciones/`](./direcciones/) |
| **El taller: el ciclo mínimo** | **`bin/ciclo.py` y su esquema** | [`./bin/`](./bin/) |
| **La lectura para la gente** | **qué es esto, y qué no** | [`./README.md`](./README.md) |
| **Los agradecimientos, y la regla de los nombres** | **las personas, y los nombres del repo** | [`./FUENTES.md`](./FUENTES.md) |
| **De dónde vino lo que se usó** | **la máquina, los nombres vivos, y los muertos con su reemplazo** | [`./contexto.md`](./contexto.md) |
| **Lo legal** | **la licencia CC BY 4.0, el DOI de Zenodo, y lo que se hace con lo ajeno** | [`./ATTRIBUTION.md`](./ATTRIBUTION.md) |
| **Lo que se piensa** | **el cero sin sus ejemplos, y la tesis vieja con su índice** | [`./Sincronización de almas/ideas/`](./Sincronización%20de%20almas/ideas/) |
| **Lo que se muestra** | **26 fichas: cada obra, su lugar, y si se verificó** | [`./Sincronización de almas/ejemplos/`](./Sincronización%20de%20almas/ejemplos/) |
| **Lo que se dijo y se descartó** | **en `notas/`, en el repo** | **`.memoria continua/notas/`** |
| **El histórico del método** | **el esquema viejo y el rastro crudo de MANTIS, para ver la evolución** | **[`.memoria continua/historico/`](.memoria%20continua/historico/)** |

**Qué no se toca:** **la dirección, y lo que entrega el producto.** **Se leen, se citan, y lo que las cambia se espera a la autoridad.**

---

## Ruta — la mente

| Se va a… | Se carga… | Sin la autoridad… |
|---|---|---|
| **hacer un ente** | `./Sincronización de almas/entes/README.md`, y se copia `Ente/` | **no se inventa la forma** |
| **tocar algo que otro sostiene** | [`./Sincronización de almas/entes/Ente/guantelete.prs`](./Sincronización%20de%20almas/entes/Ente/guantelete.prs) | **no se toca** |
| **recordar qué pasó** | [`./Sincronización de almas/entes/Ente/memoria continua/banco de memoria.prs`](./Sincronización%20de%20almas/entes/Ente/memoria%20continua/banco%20de%20memoria.prs) | **se repite el mismo error** |
| **sostener una posición** | [`./Sincronización de almas/entes/Ente/memoria continua/banco de friccion.prs`](./Sincronización%20de%20almas/entes/Ente/memoria%20continua/banco%20de%20friccion.prs) | **se obedece una conclusión sin saber de dónde vino** |
| **correr el ciclo** | [`./Sincronización de almas/entes/Ente/alma de niño/ciclo.prs`](./Sincronización%20de%20almas/entes/Ente/alma%20de%20niño/ciclo.prs) | **se actúa sin leer, y sin decir que no se sabe** |
| **juntar varios** | [`./Sincronización de almas/entes/Colmena/`](./Sincronización%20de%20almas/entes/Colmena/) | **son varios absolutos con el mismo nombre** |
| **escribir un proceso** | [`./direcciones/PROCESOS.md`](./direcciones/PROCESOS.md) | **se escribe un deseo con pasos** |
| **nombrar algo** | [`./direcciones/VERBALIZAR.md`](./direcciones/VERBALIZAR.md) | **se pone una etiqueta, y lo que se deletrea no se corre** |
| **hablar con otro que no es como uno** | [`./direcciones/ALAS.md`](./direcciones/ALAS.md) | **se trunca, y se lee como completo** |
| **declarar de dónde vino algo** | [`./direcciones/CONTEXTO.md`](./direcciones/CONTEXTO.md) | **lo heredado se presenta como propio** |
| **citar un ejemplo** | [`./Sincronización de almas/ejemplos/ESTADO.md`](./Sincronización%20de%20almas/ejemplos/ESTADO.md), y su regla en [`./Sincronización de almas/ejemplos/COMO SE VERIFICA.md`](./Sincronización%20de%20almas/ejemplos/COMO%20SE%20VERIFICA.md) | **se cita la primera cosa que salió** |
| **correr el ciclo mínimo** | [`./bin/`](./bin/), y su README | **no se corre: se supone** |
| **leer lo que se dijo y se descartó** | **`.memoria continua/notas/`** | **se repite una discusión cerrada** |
| **mutar la dirección o el producto** | todo lo anterior, **y se espera** | **no se toca: la fuente no muta de abajo hacia arriba** |

**La fila que no puede faltar:** **lo que muta `direcciones/` o `entes/` se espera.** **Sin autoridad, no se toca.**

**Y la que se ejecuta en cada turno, sin que nadie la pida:**

```plaintext
al abrir    → python bin/ciclo.py ver         qué pasó, y qué se sostiene
al cerrar   → python bin/ciclo.py disparar    si movió una frontera
              python bin/ciclo.py sostener    si cambió una posición
              python bin/ciclo.py pase        lo que quedó abierto, y lo que se retoma
```

**Y si un turno se cierra sin `pase`, el siguiente empieza a ciegas.** **Eso ya pasó: la memoria se usó una vez para probarla, y se dejó de usar.** **El banco no sirve si se consulta cuando alguien lo pide: sirve si se consulta antes de decidir.**

---

## Carga — el pensamiento

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| **se abre el repo sin esta puerta** | el rumbo | el agente adivina qué existe, y trabaja sobre lo que no hay |
| **se copia `Ente/` sin su carta** | la falta | el ente no sabe qué cubre, ni a quién contesta |
| **una dirección trae casos** | la dirección | se vuelve un manual de una casa, y sólo sirve para esos casos |
| **un proceso no tiene el caso que lo rompe** | el corte | se escribe para que se lea, no para que se corra |
| **el banco guarda lo que no movió frontera** | el criterio | se llena de ruido, y lo que importa se pierde |
| **la fricción edita en vez de suplantar** | la historia | hay una sola fecha, y ninguna prueba de qué cambió |
| **el proceso se entrega junto al borrador** | la entrega | se lee como final algo que todavía se estaba pensando |
| **se nombra una era como regla** | la vigencia | la regla muere cuando cambia la era |
| **una ruta apunta a algo que no existe** | la confianza | se promete un método y no está |

---

## Lo que este repositorio no hace, y se declara

**No certifica originalidad ni prioridad.** Ver [`./ATTRIBUTION.md`](./ATTRIBUTION.md): la licencia es CC BY 4.0, y el DOI es de Zenodo desde el segundo cero.

**No usa el nombre de una obra como nombre propio.** Ver [`./contexto.md`](./contexto.md), y los nombres muertos.

**No promete que un modelo local dé lo mismo que uno remoto.** Ver la sección de la máquina, en [`./contexto.md`](./contexto.md).

**No entrega el proceso: lo entrega en la historia.** Ver `.memoria continua/notas/lo que se entrega.md`.

**No esconde lo que falta.** Cuando no hay, se dice `[FALTA]`; cuando hay y no está listo, `[EN PROCESO]`; cuando se fue, `[BORRADA]`.

**Y la tesis escrita se borró:** **`[BORRADA - SE ESCRIBE OTRA VEZ]`.** **Lo que hoy la sostiene es `direcciones/` y `entes/`, y se puede usar sin ella.**

---

## Prueba

**¿Alguien que abre este archivo encuentra Rastro, Ruta y Carga? ¿La ruta tiene la columna de autoridad? ¿La carga dice el síntoma? ¿Cada ruta que cita existe? ¿Se declara lo que no se hace?**

**Falsificador:** una de las tres piezas ausente; una ruta sin autoridad; una carga sin síntoma; una cita a un archivo que no está; un apartado vacío que parece contenido.
