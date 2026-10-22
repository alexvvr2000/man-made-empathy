# chequear

**Deterrente:** si esta sub-tarea deja de cubrir su oficio —verificar que lo cambiado se sostiene— deja de justificarse. **Sus procesos quedan sin puerta, y se cargan por costumbre.**

**Fallo que cubre:** un cambio se entrega sin que nadie verifique que se sostiene.

**Piso:** ../../../Ouroboros/piso.md. Dos ejecutores que corren estos procesos tienen que llegar al mismo veredicto; si no, no eran procesos: eran costumbre.

## Entra | Falla | Sale | Consume

**Variables:** proceso · oficio · condición · rastro · quién lo carga
**Peor:** el oficio se cubre a medias y nadie lo nota: un cambio pasa sin veredicto y se descubre tres mutaciones después.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se perdió.

- **Entra:** un trabajo que cae en el oficio de chequear.
- **Falla si:** no hay proceso que cubra el trabajo; el proceso se salta; el rastro no queda.
- **Sale:** el proceso que se carga y su rastro, o [VACÍO - SIN PROCESO].
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el oficio tiene su proceso? ¿el rastro quedó? ¿el vacío se declara?
**Falsificador:** un trabajo sin proceso; un proceso saltado; un rastro que no queda.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|| `auditar-configuracion.md` | si las cifras, las rutas, la jerga y el nivel coinciden con lo que hay | una cifra que no cuadra y no se declara |
| `medir-acero.md` | si un sistema se puede reemplazar sin perder lo que servía | se certifica sin las cuatro propiedades |
