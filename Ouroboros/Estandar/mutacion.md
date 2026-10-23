# Mutación — transformar desde un punto de referencia

**Unidad:** proceso.
**Aplica a:** mutar.
**Tipo:** primitivo de la base. Dice qué forma tiene un cambio para que siga siendo el mismo ente.
**Lector:** quien va a cambiar una pieza, y quien hereda el cambio.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el cambio se lee desde lo que conserva, no desde lo que agrega.
**Límite:** no decide qué mutar; decide si lo que se hizo es mutación o edición.
**Cuelga de:** `./sesgo.md`. Sin posición declarada, no hay desde dónde comparar el antes y el después.
**Deja de valer:** cuando el fin de la pieza dejó de existir. Ahí no se muta: se retira.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** pieza · fin · conserva · nombre · reemplazo
**Peor:** un cambio se llama mutación y conserva el nombre anterior: el lector cree que lee lo de antes y lee otra cosa.
**Quién:** quien va a usar la pieza después, y quien la va a mutar otra vez.

## Qué resuelve

**Mutar es transformar desde un punto de referencia.** Incluye agregar, modificar y eliminar; **eliminar también es mutación.**

**Y lo que muta no es el contenido solo: es el nombre y el lugar.** **Si el nombre sobrevive al cambio, no hubo mutación: hubo edición.** Un nombre viejo sobre un cuerpo nuevo es una etiqueta que miente.

**Sin herencia.** El reemplazo no hereda forma, nombre ni estructura del anterior. **Si el nuevo se parece al viejo, es coincidencia, no requisito.**

**Y sin crecimiento obligatorio.** El conjunto puede encogerse: **quitar una pieza es mutación, y no se compensa agregando otra.**

## Las tres clases de cambio

| Clase | Qué mueve | Qué se declara |
|---|---|---|
| **Edición** | el texto, sin mover nombre ni lugar | la línea que cambia, y qué conserva |
| **Mutación** | la pieza, conservando nivel y fin | `Muta:`, `Conserva:`, `Reemplaza:` |
| **Promoción de nivel** | deja de ser lo que era; otra cosa porta el mecanismo | `Lugar:`, `Reemplaza:`, qué se traslada y qué se deja |

**La tercera no hereda el nombre.** El que recibe el mecanismo **toma lo que sirve y deja lo que no**; si se pareciera entero al anterior, **sería el anterior con otro nombre.**

## Cómo se aplica

1. **Fijar el antes** → `Serie: [conjunto] | Antes: [n piezas]`
2. **Declarar el movimiento** → `Quita: [...] | Pone: [...] | Reordena: [ninguno|qué]`
3. **Declarar qué se conserva** → `Conserva: [qué no cambia]`
4. **Acuñar el nombre** → `Reemplaza: [nombre anterior o NINGUNO]`
5. **Declarar el fin** → `Fin: [qué se persigue] | Cambia: [sí|no]`
6. **Emitir** → `Después: [n piezas] | Muta: [qué cambió | sin cambio]`

**Prohibido mutar sin `Conserva:`. Prohibido ejecutar el paso N+1 sin la salida del N.**

```
Serie: [conjunto] | Antes: [n] | Después: [n] | Quita: [...] | Pone: [...] | Reordena: [ninguno|qué]
Lugar: [carpeta nueva o NINGUNO] | Reemplaza: [nombre anterior o NINGUNO]
Fin: [qué se persigue] | Cambia: [sí|no] | Conserva: [qué no] | Muta: [qué cambió | sin cambio]
```

## El nombre lo pone el sistema, no la autoridad

**Regla del nombre, y son cinco condiciones:**

1. **Una sola palabra, con expansión.** Se lee como nombre propio.
2. **Suena como un nombre de agente:** corto, pronunciable, y no tiene que explicarse.
3. **La expansión es irrefutable:** cada letra nombra algo que el proceso hace, y ninguna es de relleno.
4. **Se pronuncia igual en humano y en máquina:** si un sintetizador lo dice mal, no se dicta ni se busca.
5. **El apodo no sustituye al nombre real.** El apodo se usa entre iguales; el archivo guarda el nombre acuñado.

**Un nombre que sirve para dos versiones distintas no nombra nada.**

## La acuñación

```
Acta: [id] | Nombre: [nombre] | Expansión: [significado] | Origen: [fuente] | Fecha: [ISO]
Muta: [qué cambia] | Conserva: [qué no] | Ausencias: [qué no tiene] | Reemplaza: [nombre anterior o NINGUNA]
Lugar: [carpeta nueva o NINGUNO] | Autoridad: [tipo:nombre] | Cierra en: [tipo:nombre]
```

**Sin `Reemplaza:` no hay cadena, y un nombre nuevo sin cadena no se distingue de un invento.**

**Sin cambio no hay acuñación fingida.** Lo que no cambió acuña igual, pero su `Muta:` declara `sin cambio`.

## Lo que no hace

**No decide si el cambio sirve.** Decide si es mutación o edición. Lo demás lo dice el uso.

**No obliga a crecer.** Un conjunto que solo crece no es un conjunto: es acumulación.

**No conserva por costumbre.** "Lo que funciona ya está viejo": un proceso no se defiende por antigüedad.

## Prueba

¿La mutación acuñó nombre? ¿`Reemplaza:` apunta al anterior? ¿Se declaró qué conserva? ¿Si cambió de nivel, cambió de carpeta? ¿Si no cambió, se declaró `sin cambio`?

**Falsificador:** una edición presentada como mutación; una acuñación sin `Reemplaza:`; una pieza que muta y conserva su nombre; un cambio que no declara qué conserva; un conjunto que solo crece; un nombre que sirve para dos versiones.

## Transiciones

- El fin dejó de existir → se retira, con su registro, y no se compensa.
- La pieza cambia de nivel → cambia de carpeta y se declara como promoción.
- No hay cambio → `Muta: sin cambio`, y no se finge acuñación.
- En cualquier otro caso → se entrega la pieza transformada y se cierra.

## Acuñación

```
Acta: EST-04 | Nombre: Mutación | Expansión: transformar desde un punto de referencia, declarando qué se conserva
Origen: ../Tesis/LA-TESIS.md, De qué está hecha | Fecha: 2026-10-23
Muta: de cambio de contenido a cambio de nombre y lugar | Conserva: que se declare el antes y el después
Ausencias: no decide si el cambio sirve | Prueba: no corrida | Reemplaza: NINGUNA
```
