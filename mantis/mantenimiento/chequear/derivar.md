# derivar — la ley de la deriva

**Unidad:** proceso.
**Aplica a:** verificar.
**Tipo:** proceso de mantenimiento. Se ejecuta cuando cambia una idea de la base.
**Lector:** quien va a cambiar una idea, y quien carga con lo que quedó desfilado.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** idea · artefactos que la declaran · test · falsificador · deriva
**Peor:** una idea cambia y los artefactos que la citaban siguen diciendo lo viejo, y nadie lo nota porque cada uno sigue siendo coherente consigo mismo.
**Quién:** quien usa los artefactos viejos, que no vio el cambio.

**Sesgo:** la deriva se lee desde los artefactos, no desde la idea: la idea puede estar mejor y el repo haber quedado peor.
**Límite:** no decide si la idea nueva es buena; solo si lo que la cita quedó viejo.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `../../../Ouroboros/procesos/integridad.md`

**Reemplaza:** NINGUNA.

## Qué resuelve

**Una idea cambió y sus artefactos no.** Cada uno sigue siendo coherente consigo mismo, y el conjunto ya no dice lo mismo. Nadie lo nota porque cada archivo, leído solo, está bien.

No es un duplicado ni un fantasma: **es una deriva.** El texto quedó apuntando a una versión del mundo que ya no existe.

**El reporte no edita:** nombra artefacto, ruta y línea, y la corrección la aplica la autoridad. Una unidad que corrige sola se vuelve la autoridad.

## Entra | Falla | Sale | Consume

- **Entra:** la idea que cambió, y el mapa de artefactos que la declaran.
- **Falla si:** se cambia la idea y no se deriva; la deriva se reporta sin ruta ni línea; el reporte corrige en vez de señalar; se derivan artefactos que no declaran esa tarea.
- **Sale:** la lista de derivas, cada una con artefacto, ruta, línea, el test que se cumplió y el falsificador que se activó.
- **Consume:** la autoridad, que decide qué se corrige y qué se declara cubierto.

## Cómo se aplica

1. **Nombrar la idea que cambió.** Su `Test` y su `Falsificador`, tal como están escritos hoy.
2. **Listar los artefactos que la declaran.** Se busca por la tarea que gobierna, no por la palabra: **un artefacto puede citar la idea sin nombrarla.**
3. **Aplicar el `Test` a cada uno.** ¿El artefacto sigue cumpliendo lo que la idea nueva exige?
4. **Activar el `Falsificador`.** Si el falsificador se cumple en el artefacto, **hay deriva**. Si no se cumple y el test pasa, no hay nada que hacer.
5. **Reportar sin editar.** Una fila por deriva.
6. **Declarar el vacío.** Lo que no se pudo derivar se declara `Sin derivar: [qué]`, con su porqué.

```
Idea: [cuál cambió] | Test: [el vigente] | Falsificador: [el vigente]
Deriva: [artefacto] | Ruta: [ruta] | Línea: [n] | Dice: [qué dice hoy] | Debería: [qué exige la idea]
Sin derivar: [qué] | Porqué: [por qué no se pudo]
Corrige: [la autoridad] | No edita este reporte: [sí]
```

**Prohibido** ejecutar el paso N+1 sin la salida del N.

## Lo que no hace

**No decide si la idea nueva es mejor.** Solo si lo que la cita quedó viejo.

**No corrige.** Reporta: quien cambia el artefacto es la autoridad.

**No es una búsqueda de texto.** Buscar la palabra encuentra las citas; **encontrar la deriva exige aplicar el test**, y eso no lo hace un `grep`.

**No reemplaza a `integridad`.** Integridad mira si un ente se sostiene; la deriva mira si lo que lo cita se quedó atrás.

## Prueba

¿Cada deriva trae artefacto, ruta, línea, qué dice y qué debería decir? ¿El reporte editó algo, o solo señaló? ¿Lo que no se pudo derivar está declarado?

**Falsificador:** una idea que cambió y nadie derivó; una deriva sin ruta ni línea; un reporte que corrige el artefacto; un `grep` presentado como derivación; un `Sin derivar` que no se declara.

## Transiciones

- Una deriva se corrige → `../editar/editar.md`, y el artefacto se entrega completo.
- Un artefacto citaba la idea y ya no la declara → no es deriva: es `retiro`, y se declara el fin que queda descubierto.
- La deriva se repite en el mismo artefacto → la idea no está escrita con un `Test` que se pueda aplicar: se corrige el `Test`.
- En cualquier otro caso → se entrega el reporte y se cierra.
