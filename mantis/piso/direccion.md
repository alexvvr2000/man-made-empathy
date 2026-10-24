# direccion.ps1 — la unidad que mide si MANTIS está enrutado

**Unidad:** direccion.
**Aplica a:** medir la dirección estándar → ente.
**Tipo:** unidad del piso. Se ejecuta y da veredicto. No decide qué hacer con él.
**Lector:** quien va a desplegar MANTIS, y quien va a decir si sirve.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** se mide desde `../../Libre albedrio/piso.md`, `La dirección`: **`Ouroboros/` es la fuente; el estándar muta a MANTIS; nadie muta hacia arriba.**
**Límite:** no se aplica a juzgar si MANTIS decide bien. Mide si está enrutado contra el estándar vigente, y nada más.
**Firma:** humano:autoridad · máquina:quien corra la unidad.

**Variables:** estándar · carta · menciones · vacío.
**Peor:** la unidad pasa y MANTIS sigue citando un estándar que ya mutó, porque la unidad mide menciones y no contenido. **Se declara abajo, y es el límite real.**
**Quién:** quien despliega MANTIS y lee el veredicto.

## Entra | Falla | Sale | Consume

- **Entra:** `Libre albedrio/` y `mantis/`, tal como están ahora.
- **Falla si:** hay archivos de `Ouroboros/` modificados después de la última corrida, o MANTIS cita un estándar que ya cambió.
- **Sale:** `pasa | falla | indeterminado`, con el porqué por archivo.
- **Consume:** quien decide si MANTIS se despliega.

**Qué mutación del estándar detecta, y es el quinto requisito del piso:** **detecta que un ente de `Ouroboros/` mutó y que la carta de MANTIS no lo refleja.** **Si el estándar muta y MANTIS no, esta unidad lo dice.**

**Prueba:** ¿corre sola? ¿da veredicto con porqué? ¿declara su límite? ¿dice qué mutación detecta?

**Falsificador:** una unidad que edita `Ouroboros/` o a MANTIS; una que emite datos sin veredicto; una que pasa sin haber leído el estándar.

## Qué mide, y en este orden

```
1. ¿Ouroboros/ está limpio en git?
   Limpio    → se sigue.
   Sucia     → se declara `indeterminado`: hay una mutación sin commitear y no se sabe contra qué se compara.
   Sin git   → se declara `indeterminado`: no hay con qué comparar.

2. ¿Cada estándar que MANTIS cita, existe?
   Existe    → se sigue.
   No existe → `falla`: MANTIS cita un estándar que ya no está.

3. ¿La carta cubre las secciones del estándar?
   Cubre     → se sigue.
   No cubre  → `falla`: MANTIS está atrasado respecto del estándar.

4. ¿Nadie de abajo mutó hacia arriba?
   No mutó   → `pasa`.
   Mutó      → `falla`, y se nombra el archivo de Ouroboros con fecha posterior al último cambio de MANTIS.
Prohibido dar `pasa` sin haber recorrido las cuatro.
```

**Ancla:** la unidad mide; el criterio decide; MANTIS obedece.

## Cómo se corre

```powershell
pwsh -NoProfile -File mantis/piso/direccion.ps1
```

**Sale código `0` si `pasa`, `1` si `falla`, `2` si `indeterminado`.** **Y siempre imprime el porqué, línea por línea.**

## Lo que no verifica, y se declara

**No verifica el contenido: verifica las citas y las fechas.** **Si el estándar muta el sentido de una sección sin cambiar su nombre, esta unidad no lo ve.** **Para eso hace falta leer, y leer no lo hace una unidad.**

**Ancla:** mide el atraso, no la interpretación.

**Prueba:** ¿el veredicto cambia si cambia el estado? ¿se puede correr en otro ejecutor igual? ¿dice su límite?

**Falsificador:** declarar `pasa` con `Ouroboros/` sucio; medir MANTIS contra sí mismo; reportar `pasa` sin imprimir el porqué.

## Transiciones

- Da `falla` por citas rotas → se realinea MANTIS, y se vuelve a correr.
- Da `falla` por mutación hacia arriba → se revierte en `Ouroboros/`, y se anota con su `contra`.
- Da `indeterminado` → se declara así, y no se finge que pasó.
- En cualquier otro caso → se anota la corrida y se continúa.
