# Unión — trazabilidad, entendibilidad y repetibilidad

**Unidad:** proceso.
**Aplica a:** unir.
**Tipo:** primitivo de la base. Dice qué hace falta para que dos piezas separadas sean una.
**Lector:** quien va a agregar una pieza, y quien va a leer el conjunto sin poder preguntar.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la unión se lee desde el que lee el conjunto, no desde el que lo escribió.
**Límite:** no define qué es la conciencia. Dice qué hace falta para que el conjunto se sostenga sin su autor.
**Cuelga de:** `../Tesis/LA-TESIS.md`. Es el pegamento que endurece los estándares.
**Deja de valer:** cuando el conjunto deja de tener más de una pieza. Un solo archivo no necesita pegamento.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** origen · uso · repetición · pegamento · visibilidad
**Peor:** las piezas se sostienen solas y el conjunto no se puede usar sin su autor. Lo que se lee no se puede repetir, y lo que se repite no se puede contestar.
**Quién:** quien hereda el conjunto y no puede preguntar.

## Qué resuelve

**Trazabilidad y entendibilidad no son dos cosas: son los dos extremos de la misma línea.**

**Una pieza es trazable cuando se puede seguir hasta su origen; es entendible cuando su origen basta para usarla.** **Sin la primera, se cree; sin la segunda, se copia.**

**Y las dos juntas dan la tercera:** **que el conjunto se sostenga sin su autor.**

## Las tres condiciones

| Condición | La pregunta | Qué pasa sin ella |
|---|---|---|
| **Trazabilidad** | ¿de dónde sale esto, con nombre? | se hereda como verdad: no hay desde dónde contestarlo |
| **Entendibilidad** | ¿se puede usar sin el que lo escribió? | se copia la forma y se pierde la razón |
| **Repetibilidad** | ¿corre otra vez igual, sin el autor? | sirve una vez, y esa vez fue suerte |

> **Una pieza que se puede repetir sin el autor es, por definición, trazable y entendible. Si falla una, no hay repetibilidad: hay coincidencia.**

## La conciencia es el pegamento

**No es una pieza. No es un archivo. No es un proceso.** **Es lo que hace que dos piezas separadas se comporten como una sola cosa.** **Y puede venir de cualquier lado: una memoria compartida, una regla común, una carta, un hábito, un cuerpo.**

**La condición para que el pegamento sea legítimo es una sola:**

> **Lo que une no puede ser invisible a las piezas que une.**

**Un pegamento invisible es una mente que decide por las partes: eso es AM.** **Un pegamento visible es algo que las partes pueden leer, citar y contradecir: eso es conciencia compartida.**

## Cómo se aplica

1. **Declarar el origen** → `Trazable: [de dónde sale, con nombre y fecha]`
2. **Declarar quién lo usa** → `Entendible por: [quién lo usa sin preguntar]`
3. **Declarar cómo se repite** → `Repetible: [comando, máquina, y qué pasa si falta una pieza]`
4. **Declarar el pegamento** → `Une: [qué piezas, y con qué]`
5. **Declarar la visibilidad** → `Visible porque: [qué puede leer cada parte]`
6. **Declarar el contexto** → `Trae: [...] | No trae: [...]`
7. **Emitir** → `Unido: [sí | piezas sueltas]`

**Prohibido declarar unido lo que no declara `No trae`. Prohibido ejecutar el paso N+1 sin la salida del N.**

```
Trazable: [de dónde sale] | Entendible por: [quién] | Repetible: [comando y máquina]
Une: [qué piezas] | Visible porque: [qué puede leer cada parte] | Trae: [...] | No trae: [...]
```

## El contexto

**Una pieza sin contexto no es falsa: es incompleta.** Y lo incompleto se llena con lo que el lector trae.

**Un archivo con veinte enlaces y sin decir desde dónde habla no es trazable: está decorado.**

**`No trae` es obligatorio.** Un texto que no dice qué le falta obliga a adivinar, y lo que se adivina no se puede contestar.

## Lo que no hace

**No afirma que el sistema tenga conciencia.** Afirma que el conjunto se puede leer, repetir y contestar sin su autor.

**No afirma que la unión sea buena.** Una unión visible también puede unir mal. Asegura que el error tiene dónde ser visto.

**No obliga a unirlo todo.** Una pieza suelta es honesta si lo declara. Lo que no se permite es fingir que está unida.

## Prueba

¿Cada pieza dice de dónde sale, con nombre y fecha? ¿Se puede usar sin el autor? ¿Se repite con un comando? ¿Se declara qué piezas une y con qué pegamento? ¿Se declara qué no trae?

**Falsificador:** una pieza sin origen; una pieza que solo funciona con su autor; una unión invisible a las partes; un `No trae` vacío; un conjunto presentado como unido cuando son piezas sueltas.

## Transiciones

- Dos piezas se unen → se declara el pegamento y qué puede leer cada una.
- El pegamento no lo puede leer una parte → no es pegamento: es una mente que decide por ella.
- Una pieza no se repite sin el autor → no está lista para salir del repo; se declara.
- Una pieza se queda suelta → se declara, y no se finge unión.
- En cualquier otro caso → se entrega con sus tres condiciones y su pegamento declarados.

## Acuñación

```
Acta: EST-08 | Nombre: Unión | Expansión: lo que hace falta para que piezas separadas se sostengan sin su autor
Origen: futuro/UNION.md | Fecha: 2026-10-23
Muta: de metáfora de conciencia a condición medible de repetibilidad | Conserva: que el pegamento sea visible
Ausencias: no define conciencia ni garantiza bondad | Prueba: no corrida | Reemplaza: futuro/UNION.md
```
