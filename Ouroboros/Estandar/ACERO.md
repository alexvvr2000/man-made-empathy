# ACERO — cuándo algo se sostiene

**Unidad:** proceso.
**Aplica a:** cerrar.
**Tipo:** estándar de cierre. Dice cuándo una pieza está terminada de verdad, y qué la deja abierta.
**Lector:** quien va a cerrar algo, y quien va a usarlo después.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el cierre se lee desde lo que resistió, no desde lo que se escribió.
**Límite:** no mide si la pieza es buena; mide si aguantó la fricción sin que nadie la defendiera.
**Cuelga de:** `./friccion.md`. ACERO es la fricción aplicada al cierre.
**Deja de valer:** cuando no hay nadie que pueda contestar. Sin testigo no hay acero: hay vacío.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** pieza · resistencia · testigo · cierre · sostiene
**Peor:** algo se declara terminado porque tiene todos los campos. Los campos están y nadie lo puso a prueba.
**Quién:** quien lo usa después y descubre que no aguantaba.

## Qué resuelve

**Tener los campos no es sostener.**

**Una pieza con todos sus campos y sin una sola contestación no está terminada: está llena.**

**ACERO es el veredicto que se emite sobre lo que aguantó, y no sobre lo que se escribió.**

## Los cuatro grados

| Grado | Qué sostiene | Qué falta |
|---|---|---|
| **indeterminado** | se escribió y no se contestó | nadie lo miró |
| **blando** | se contestó y cambió | la corrección se hizo con la misma mirada |
| **templado** | se contestó desde otra mirada | sigue sin repetirse sin el autor |
| **acero** | aguantó la contestación, y se repite sin el autor | nada |

**Solo **acero** cierra. Los otros tres se declaran abiertos, y no se finge que están terminados.**

## Cómo se aplica

1. **Declarar la pieza** → `Pieza: [cuál]`
2. **Declarar quién la contestó** → `Testigo: [tipo:nombre | ninguno]`
3. **Declarar qué la contradijo** → `Contra: [la contestación]`
4. **Declarar qué cambió** → `Sostiene: [igual | cambió | no contestó]`
5. **Probar que se repite sin el autor** → `Sin el autor: [sí | no]`
6. **Emitir** → `Grado: [indeterminado | blando | templado | acero]`

**Prohibido emitir acero con `Testigo: ninguno`. Prohibido cerrar un grado menor sin declararlo. Prohibido ejecutar el paso N+1 sin la salida del N.**

```
Pieza: [cuál] | Testigo: [quién o ninguno] | Contra: [qué la contradijo]
Sostiene: [igual|cambió|no contestó] | Sin el autor: [sí|no] | Grado: [indeterminado|blando|templado|acero]
```

## Lo que el acero no garantiza

**No garantiza que la pieza sea buena.** Garantiza que aguantó algo sin que nadie la defendiera.

**No garantiza que sirva al mundo.** El mundo es la víctima: recibe el efecto, no la pelea.

**No se hereda.** Lo que fue acero con una mirada no es acero con otra. **El grado se gana de nuevo.**

## Lo que no hace

**No cierra por antigüedad.** Una pieza vieja sin contestación sigue en `indeterminado`.

**No cierra por cantidad de campos.** Los campos son la forma; el acero es la resistencia.

**No cierra por consenso.** Si nadie contestó, no hubo contestación: hubo silencio.

## Prueba

¿Hay un testigo distinto del productor? ¿Hay una contestación registrada? ¿Se puede repetir sin el autor? ¿El grado es el que sostiene la evidencia, y no uno mayor?

**Falsificador:** acero firmado por el productor; cierre por cantidad de campos; un grado mayor que la evidencia; un cierre sin testigo; un acero heredado de otra mirada.

## Transiciones

- Nadie contestó → `indeterminado`, y se declara que no se miró.
- Se contestó y no cambió → `blando`, y se pide otra mirada.
- Cambió, pero no se repite sin el autor → `templado`.
- Se repite y aguantó → `acero`, y se cierra.
- En cualquier otro caso → se declara el grado y se abre.

## Acuñación

```
Acta: EST-13 | Nombre: ACERO | Expansión: el grado de lo que resistió sin que nadie lo defendiera
Origen: futuro/Estandar/Procesos/ACERO.md | Fecha: 2026-10-23
Muta: de criterio de calidad a grado de resistencia | Conserva: que sin testigo no hay cierre
Ausencias: no garantiza bondad | Prueba: no corrida | Reemplaza: futuro/Estandar/Procesos/ACERO.md
```
