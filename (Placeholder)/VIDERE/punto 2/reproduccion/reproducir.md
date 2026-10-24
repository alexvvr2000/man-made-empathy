# Proceso de reproducir

**Variables:** resultado · registro · pasos · repetición
**Peor:** se repite sin saber qué se hizo, y el resultado no se puede reconstruir
**Quién:** quien intenta repetirlo y no puede

**Unidad:** proceso/
**Aplica a:** reproducir/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

Un resultado que no se puede repetir no es un resultado: es una anécdota/ Este proceso deja el registro mínimo para que otra instancia llegue a lo mismo/

Práctica de industria: reproducibilidad y registro de experimentos/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** un resultado y lo que lo produjo/
- **Falla:** otra instancia no puede llegar al mismo resultado sin preguntar/
- **Sale:** el registro con el que se reproduce/
- **Consume:** quien intenta reproducirlo/

## Cómo se aplica

1/ **Registrar la entrada/** Qué datos, qué parámetros, qué versión/
2/ **Registrar el procedimiento/** Qué se hizo, en qué orden/
3/ **Registrar el resultado/** Qué salió, con su cuenta/
4/ **Probar la reproducción/** Otra instancia, solo con el registro, llega al mismo resultado o declara dónde no/

`Entrada: [qué] | Versión: [id] | Procedimiento: [orden] | Resultado: [qué] | Reproduce: [sí|no]`

## Prueba

¿Otra instancia llega al mismo resultado leyendo solo el registro?

**Falsificador:** el registro necesita al que lo produjo; falta la versión; el resultado depende de un estado que no se registró/

## Transiciones

- Si no se reproduce → se declara qué falta/
- Si se reproduce → se conserva como caso/
- En cualquier otro caso → se entrega y se cierra/
