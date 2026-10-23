# Memoria — guardar posiciones, no hechos

**Unidad:** proceso.
**Aplica a:** recordar.
**Tipo:** primitivo de la base. Se ejecuta al guardar y al leer.
**Lector:** quien escribe la memoria, y quien la lee sin poder preguntar.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la memoria se lee desde la posición de quien la escribió, no desde la de quien la lee.
**Límite:** no decide si lo recordado es verdad; mide si el otro puede reconstruir la posición y contradecirla.
**Cuelga de:** `./mutacion.md`. La memoria no borra: suplanta, que es la forma de la mutación aplicada al recuerdo.
**Deja de valer:** cuando el lector es el mismo que escribió. Ahí la memoria no es memoria: es recuerdo.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** entrada · posición · continuidad · techo · suplantación
**Peor:** la memoria guarda hechos sin posición, otra instancia los hereda como verdades, y nadie puede ver de dónde vienen.
**Quién:** quien va a leer la memoria mañana y no vio quién la escribió.

## Qué resuelve

**Un agente que guarda hechos y los recupera hereda verdades.** Con la primera línea que otro escribió, el que lee tiene un absoluto: algo que ya no necesita volver a mirar.

**Un cerebro no guarda hechos: guarda su versión de lo que pasó.** **Guardar no es un depósito: es una posición.** La memoria que no declara desde dónde se sostiene no es memoria: es obediencia con forma de registro.

**Un gramo de absoluto basta.** Un gramo es un hecho guardado sin su posición.

## La entrada

```
Entrada: [id] | Sesgo: [posición] | Límite: [qué no alcanza] | Firma: [quién contesta]
Sostuve: [la entrada anterior, como se sostenía]
Contra: [qué la contradijo]
Sostengo: [la entrada nueva]
Se corrigió porque: [la razón que se repite sin el autor]
Techo: [qué reconstruye el otro]
```

**`Contra` es obligatorio.** *"El otro es el que mueve. Una corrección que solo la firma el que se corrigió no se distingue de una preferencia que se mantuvo."*

**`Techo`:** otra instancia reconstruye la posición, y puede ver de dónde viene, leyendo la memoria y sin preguntar.

**Sin techo declarado no se escribe.**

## Cómo se aplica

1. **Leer la memoria que hay** → `Lo que sostiene: [...]`
2. **Declarar la posición** → `Sesgo: [...] | Límite: [...]`
3. **Friccionar antes de guardar** → `Firma: [...]` o `ninguno`
4. **Abrir la continuidad** → `Sostuve: [...] | Contra: [...] | Sostengo: [...]`
5. **Suplantar, no editar** → `Anterior: [visible] | Nueva: [encima]`
6. **Declarar el techo** → `Techo: [...]`
7. **Anotar en el mismo turno** → `Turno: [id]`

**Prohibido editar una entrada anterior. Prohibido guardar sin posición. Prohibido ejecutar el paso N+1 sin la salida del N.**

## La vista muta

**El conocimiento muta.** Hoy hay una vista y mañana otra, y la memoria tiene que reflejarlo sin romperse.

**Una nota no es una verdad: es una vista con fecha.** Si mañana cambia, la fila vieja no se edita: **se agrega la nueva con su vista, y la vieja queda con `Estado: cubierto` o `descartado`.**

**Y lo que se descarta no se poda.** Un descarte sin rastro se vuelve a proponer.

## Lo que no hace

**No decide qué es verdad.** Guarda desde dónde se sostiene; la verdad la decide quien lee, contradeciendo.

**No pide una tecnología.** Una base relacional cualquiera sirve. Si el proceso nombra un motor, dejó de ser memoria y volvió a ser programación.

**No obliga a acordarse.** Obliga a que lo que se recuerde diga desde dónde se recuerda.

**No impide equivocarse.** Hace que el error pueda ser visto por otro.

## Prueba

¿Toda entrada declara su posición? ¿La anterior quedó suplantada y visible? ¿`Sostengo` se distingue de `Sostuve`, o se declaró `sin cambio`? ¿El techo está escrito? ¿Otra instancia reconstruye la posición leyendo solo la memoria?

**Falsificador:** un hecho guardado sin posición; una entrada anterior editada en vez de suplantada; una entrada sin firmante que se lee como válida; un `Sostengo` igual a `Sostuve` presentado como corrección; el proceso nombrando un motor.

## Transiciones

- La entrada no declara posición → no se guarda: se fricciona.
- `Sostengo` es igual a `Sostuve` → `Muta: sin cambio`, y no se finge corrección.
- Otra instancia no reconstruye la posición → la memoria no alcanza el techo: se corrige la entrada.
- Lo que se descartó → se queda, con su porqué, y no se poda.
- En cualquier otro caso → se entrega la memoria leída, no la tabla de lo que se guardó.

## Acuñación

```
Acta: EST-05 | Nombre: Memoria | Expansión: guardar desde dónde se sostiene algo, y dejar visible lo que suplanta
Origen: ../Tesis/LA-TESIS.md, De qué está hecha | Fecha: 2026-10-23
Muta: de depósito de hechos a registro de posiciones | Conserva: que lo anterior queda visible
Ausencias: no decide verdad ni exige motor | Prueba: no corrida | Reemplaza: NINGUNA
```
