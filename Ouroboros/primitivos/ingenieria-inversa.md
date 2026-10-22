# Proceso de ingeniería inversa

**Unidad:** tarea.
**Aplica a:** deducir.
**Tipo:** proceso. Se ejecuta; no se interpreta.
**Nivel:** primitivo. Uno de los cinco de `Ouroboros`. Produce procesos a partir de lo observable.
**Lector:** autoridad y ejecutor.
**Dueño:** la autoridad.
**Estado:** vigente.

**Manipulación.** Todo cambio a un proceso pasa por `./primitivos/manipulacion.md`: ahí se nombran las variables antes de que el proceso exista. Un proceso que se modifica sin pasar por ahí queda sin variables, y sin variables no hay contra qué chequearlo.

## Tesis

Un proceso se puede sacar de lo que se observa, sin conocer cómo se produjo. No hace falta que el resultado sea idéntico al original: hace falta que sirva, y que seguir el proceso tienda a algo real.

Es el proceso que produce procesos por prueba y error, en vez de por diseño. Sirve para lo que no tiene dueño visible: una emoción que un humano no puede explicar, una identidad, un patrón de conducta.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** lo observable: conducta, resultado, efecto, registro, o el borde de un sistema.
- **Falla:** el proceso deducido no reproduce nada observable, o no sirve para nada.
- **Sale:** un proceso nuevo, con su Prueba y su Falsificador, o la declaración de que no se pudo deducir.
- **Consume:** quien va a repetir el proceso, y la autoridad que decide aceptarlo.

**Prueba:** ¿el proceso deducido reproduce el resultado observable, y su desvío está declarado?

**Falsificador:** un proceso deducido que no reproduce nada observable; uno que se protege por parecerse al original en vez de por tender al mismo resultado; un desvío que se calla.

## Piso y techo

**Piso:** todo lo observable en el borde del sistema: qué entra, qué sale, qué cambia, qué se repite. No se toca el interior.

**Techo:** un proceso que, al seguirlo, tiende al mismo resultado observable. No es copia; es tendencia.

`Piso: [lo observable] | Techo: [qué resultado debe tender a repetir] | Idéntico: [no]`

Un proceso deducido que no tiende a nada no es ingeniería inversa: es una descripción del borde.

## Cómo se aplica

1. **Extraer.** Reunir lo observable: entrada, salida, cambio, repetición. Se declara qué quedó fuera de lo observable.
2. **Modelar.** Escribir un proceso que produzca esa salida desde esa entrada. Se escribe como proceso completo, no como explicación.
3. **Revisar.** Correr el proceso sobre un caso que no se usó para extraerlo. Si tiende al mismo resultado observable, el proceso sirve; si no, se ajusta el modelo, no la observación.
4. **Medir la tendencia.** Cuánto se acerca y dónde se desvía. El desvío se declara; no se esconde.
5. **Entregar.** El proceso con su `Entra | Falla | Sale | Consume`, su `Piso` y su `Techo`, y el registro de dónde se desvía.

**Prohibido** ejecutar el paso N+1 sin la salida del N. Prohibido modelar antes de extraer.

## Lo que hace útil a un proceso incompleto

Un proceso deducido puede no dar el mismo resultado al 100%. Sigue siendo útil si su desvío está declarado y si seguir el proceso tiende al resultado. Lo académico no decide: decide el uso.

`Tendencia: [qué tan cerca queda] | Desvío: [dónde se aparta] | Sirve: [sí|no]`

## Cerca

Este proceso no afirma un estado interno. Deduce un proceso que produce un efecto; no deduce que el original lo sienta. Lo que se puede mostrar es la conducta y el resultado.

Un proceso deducido que produce un efecto que el otro lado no puede reconstruir es manipulación, y no entra. Rige `../S.A.R.A/punto-de-partida/evaluacion/vigilar-tendencias.md` 7 y `../Pruebas/prueba de rendicion.md`, condición 6.

## Admisión

El proceso deducido entra si su salida cambia una decisión en el uso vigente, o si declara `Plazo` y `Criterio`. Rige `./primitivos/claridad.md` `1.12`.

Sin Falsificador no entra: un proceso sin el caso que lo incumple es una opinión.

## Transiciones

- Si el proceso reproduce el resultado observable → se entrega con su `Tendencia` y su `Desvío`.
- Si tiende pero se desvía → se entrega igual, y el desvío queda declarado.
- Si no tiende a nada → `[VACÍO - SIN PROCESO DEDUCIDO]`.
- Si la tarea necesita comunicar el proceso deducido → `../corpus/ATLAS/Proceso ATLAS.md`.
- En cualquier otro caso → se entrega y se cierra.
