# Mutación

**Unidad:** proceso.
**Aplica a:** mutar.
**Tipo:** estándar de mutación. No decide, no ejecuta: dice qué forma tiene un cambio para que siga siendo el mismo ente.
**Lector:** quien va a cambiar un ente, un proceso o un paso.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

**Mutar es transformar desde un punto de referencia.** Incluye agregar, modificar y eliminar; **eliminar también es mutación.**

**Y lo que muta no es el contenido solo: es el nombre y el lugar.** Si el nombre sobrevive al cambio, **no hubo mutación: hubo edición.** Un nombre viejo sobre un cuerpo nuevo es una etiqueta que miente, y la etiqueta es lo único que el lector tiene para orientarse.

**La forma se lee como nombre propio; la expansión dice qué significa.** Un acrónimo que solo se puede leer deletreando **no es un nombre: es una etiqueta.**

## Qué muta en un ente

| Pieza | Qué cambia | Qué no cambia |
|---|---|---|
| **Rastro** | casi nunca: el cuerpo no cambia sin cambiar de especie | qué hay, qué no se toca y cómo se verifica |
| **Ruta** | siempre: si el hoy cambia y la Ruta no, enruta lo de ayer | que enruta |
| **Carga** | cuando el fin cambia; si el fin deja de existir, no se muta: se retira | que declara la pérdida |

**Un ente que conserva nombre de carpeta después de mutar no mutó: se editó.** Una sub-tarea que cambia y conserva su carpeta es el mismo caso.

## Sin herencia

**El reemplazo no hereda forma, nombre ni estructura del anterior.** Si el nuevo se parece al viejo, es coincidencia, no requisito.

**Sin crecimiento obligatorio.** El conjunto puede encogerse: quitar una pieza es mutación, y no se compensa agregando otra.

```
Serie: [conjunto] | Antes: [n piezas] | Después: [n piezas] | Quita: [...] | Pone: [...] | Reordena: [ninguno|qué]
```

## El nombre muta con la cosa

```
Lugar: [carpeta nueva o NINGUNO] | Reemplaza: [nombre anterior o NINGUNA]
```

**`Reemplaza:` apunta al nombre anterior.** El anterior no se borra: **se sustituye, y la razón se declara.** Sin `Reemplaza:` no hay cadena, y un nombre nuevo sin cadena no se distingue de un invento.

**Sin cambio, no hay acuñación fingida.** Lo que no cambió acuña igual, pero su `Muta:` declara el estado: *«sin cambio»*. Lo que no se permite es acuñar como si hubiera pasado algo.

**Un nombre que sirve para dos versiones distintas no nombra nada.**

## Lo que no cambia

**El fin no muta al mismo ritmo que el proceso.** Un proceso puede reemplazarse entero y el fin seguir siendo el mismo. **Si el fin cambia, no es mutación de la serie: es una mutación del fin, y se declara como tal.**

```
Fin: [qué se persigue] | Cambia: [sí|no] | Si cambia: [por qué]
```

## Entra | Falla | Sale | Consume

**Variables:** pieza · nombre · lugar · fin · reemplazo
**Peor:** el cambio se llama mutación y conserva el nombre anterior: el lector cree que lee lo de antes y lee otra cosa.
**Quién:** quien va a usar la pieza, y quien la va a mutar después.

- **Entra:** la pieza y el cambio que se quiere hacer.
- **Falla si:** el cambio no declara qué conserva, o no deja rastro, o conserva el nombre del anterior.
- **Sale:** la pieza transformada, completa, con `Muta:`, `Conserva:`, `Ausencias:` y `Reemplaza:`.
- **Consume:** quien va a usar la pieza transformada, y la autoridad que lo acepta.

```
Acta: [id] | Nombre: [nombre] | Expansión: [significado] | Fecha: [ISO]
Muta: [qué cambia] | Conserva: [qué no] | Ausencias: [qué no tiene] | Reemplaza: [nombre anterior o NINGUNA]
Lugar: [carpeta nueva o NINGUNO] | Autoridad: [tipo:nombre] | Cierra en: [tipo:nombre]
```

**Prueba:** ¿la mutación acuñó nombre? ¿`Reemplaza:` apunta al anterior? ¿Se declaró qué conserva? ¿Si cambió de nivel, cambió de carpeta?

**Falsificador:** una edición presentada como mutación; una acuñación sin `Reemplaza:`; una pieza que muta y conserva su nombre; un cambio que no declara qué conserva; un conjunto que solo crece.

## Transiciones

- El fin dejó de existir y no entra nada en su lugar → se retira, con su registro.
- La pieza cambia de nivel → cambia de carpeta y se declara.
- En cualquier otro caso → se entrega la pieza completa y se cierra.
