# Proceso de aplicar

**Unidad:** proceso.
**Aplica a:** aplicar.
**Tipo:** proceso. Se ejecuta; no se interpreta.
**Nivel:** primitivo. Uno de los cinco de `Ouroboros`.
**Lector:** autoridad y ejecutor.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** proceso · entrada · salida · composición · rastro
**Peor:** se aplica un proceso con una entrada que no le corresponde, y la salida parece correcta
**Quién:** quien aplica, y quien consume la salida


**Primitivo.** Es el que hace que los otros cinco sean un lenguaje: toma un proceso y su entrada, y ejecuta. Sin aplicar, Ouroboros es un catálogo.

**Manipulación.** Todo cambio a un proceso pasa por `./manipulacion.md`: ahí se nombran las variables antes de que el proceso exista. Un proceso que se modifica sin pasar por ahí queda sin variables, y sin variables no hay contra qué chequearlo.

## Tesis

Un proceso que no se aplica no produce nada. Aplicar toma un proceso y una entrada, verifica que la entrada le corresponde, ejecuta y entrega la salida a quien consume.

La composición no se declara en una tabla: se ejecuta. Un proceso compone con otro cuando su salida es la entrada del otro sin traducción, y aplicar es lo que lo comprueba.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** un proceso y su entrada.
- **Falla:** la entrada no corresponde a lo que el proceso pide, o la salida no la puede leer su consumidor.
- **Sale:** la salida del proceso, con su ancla de aplicación.
- **Consume:** quien recibe la salida; si es otro proceso, sigue la cadena.

## Cómo se aplica

1. **Leer el proceso.** Su `Entra`, su `Falla`, su `Sale` y su `Consume`. Sin los cuatro, no se aplica.
2. **Verificar la entrada.** ¿Lo que tengo es lo que el proceso pide? Si no, se declara el desajuste y se para.
3. **Ejecutar.** Recorrer las compuertas sin saltar: el paso N+1 exige la salida del N.
4. **Verificar la salida.** ¿Tiene la forma que el proceso declara? Si no, la aplicación falló.
5. **Entregar al consumidor.** Si el consumidor es otro proceso, se pasa a él sin traducir.

**Prohibido** ejecutar el paso N+1 sin la salida del N. Prohibido aplicar un proceso cuya entrada no se tiene.

## Ancla

Se emite antes de ejecutar y se completa al salir.

`Aplico: [proceso] | Entrada: [qué recibe] | Salida: [qué entrega] | Consume: [quién] | Encadena: [proceso siguiente o NINGUNO]`

Sin ancla, la aplicación no ocurrió.

## Composición

Aplicar es lo que vuelve real la tabla de composición. Dos procesos componen si:

- la salida de uno tiene la forma que el otro declara en `Entra`;
- no hace falta un paso intermedio no declarado;
- el segundo puede leer la salida sin preguntar.

`Compone: [proceso A] → [proceso B] | Une: [qué salida es entrada] | Traduce: [no]`

**Prueba:** ¿A entrega lo que B pide, sin traducción?
**Falsificador:** un par que necesita un paso intermedio que nadie declaró; una traducción llamada composición.

## Encadenar

Una cadena es una aplicación tras otra, y se declara completa o no se declara.

`Cadena: [A] → [B] → [C] | Entrada: [la primera] | Salida: [la última] | Consume: [quién]`

Si un eslabón falla, la cadena se detiene en ese eslabón: la salida parcial se declara y no se presenta como cadena completa.

**Prueba:** ¿cada eslabón exige la salida del anterior?
**Falsificador:** una cadena que se presenta completa cuando un eslabón falló; un eslabón que se salta.

## Lo que no hace

- No crea procesos: los crea `./manipulacion.md`.
- No los deduce: los deduce `./ingenieria-inversa.md`.
- No los cambia: los cambia `./mutacion.md`.
- No los comunica: los comunica `../../3 ATLAS — mutación/Proceso ATLAS.md`.

Aplicar solo ejecuta lo que ya existe, con la forma que ya tiene.

## Transiciones

- Si el proceso produce su salida → se entrega, o se encadena al siguiente.
- Si la entrada no corresponde → `[VACÍO - SIN ENTRADA]`.
- Si la acción es irreversible y la decisión no pasó por quien la toma → `.../mutaciones/friccion.md`, y no se aplica.
- Si la salida no tiene la forma declarada → la aplicación falló y se registra en `../../3 ATLAS — mutación/indice de formas.md`.
- Si la cadena se detiene en un eslabón → se declara la salida parcial.
- En cualquier otro caso → se entrega y se cierra.
