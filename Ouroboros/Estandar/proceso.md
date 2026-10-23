# Formato de proceso

**Unidad:** nivel.
**Aplica a:** dar forma.
**Tipo:** estándar de formato. No decide, no ejecuta: dice qué forma tiene lo que un ejecutor puede leer.
**Lector:** todo ejecutor —humano, modelo o programa— que tenga que leer o producir un proceso.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la forma se lee desde el ejecutor que la recorre, no desde el gusto del autor.
**Límite:** no juzga contenido. Un proceso con todos los campos puede no decir qué decide; eso lo dice `./union.md` y `./ACERO.md`.
**Cuelga de:** `./ESTANDAR.md`. Es la forma de todo lo demás: no hay proceso sin este formato.
**Deja de valer:** cuando el ejecutor deja de necesitar la forma porque ya sabe qué hacer. Ahí la forma sobra.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra él mismo.

**Variables:** proceso · campo · compuerta · ancla · acuñación
**Peor:** cada archivo inventa su forma, el ejecutor tiene que adivinar, y adivinar no es ejecutar.
**Quién:** quien hereda el proceso y no sabe qué campo le incumbe.

## Qué es

**Todo se escribe siempre igual. Si cada archivo inventa su forma, el ejecutor tiene que adivinar, y adivinar no es ejecutar.**

**Rige el formato, no el contenido.** Un proceso con los campos escritos puede no decir qué decide; eso no lo salva el formato.

## Todo es un proceso

**No hay piezas que no sean proceso.** El `Rastro`, la `Ruta`, la `Carga` y el propio formato **también se ejecutan**: verifican, enrutan, declaran pérdida o dicen la forma.

**Describir el conjunto no es un oficio distinto: es un proceso que decide sobre el conjunto.**

**Un archivo no se excluye del estándar por su nombre. Se excluye si al quitarlo nadie sabría qué hacer — y eso lo decide su propia `Prueba`.**

**El nivel no cambia el oficio: cambia la carpeta.** Un paso de `Ouroboros/` es un ente y se lee con `./ente.md`; lo que ese ente contiene son procesos y se leen aquí.

## La forma del proceso

**Un proceso lleva variables arriba, el bloque de entrada, y su reverso.**

| Campo | Qué dice | Forma literal |
|---|---|---|
| `Variables` | qué mueve el proceso, antes de escribir | `**Variables:** nombre1 · nombre2 · nombre3` |
| `Peor` | qué pasa si se mueve la que más pesa | `**Peor:** qué pasa` |
| `Quién` | quién puede decir que se movió mal, o `ninguno` | `**Quién:** tipo:nombre` |
| `Entra` | qué recibe | `- **Entra:** ...` |
| `Falla` | el caso concreto que lo incumple | `- **Falla si:** ...` |
| `Sale` | qué emite, con su forma exacta | `- **Sale:** ...` |
| `Consume` | quién decide con la salida | `- **Consume:** ...` |
| `Prueba` | cómo se comprueba que cumplió | `**Prueba:** ...` o `## Prueba` |
| `Falsificador` | qué lo refuta | `**Falsificador:** ...` o `## Falsificador` |

**Las tres variables van arriba del primer campo, como línea propia.** Sin ellas no hay contra qué chequearlo cuando falla.

## Los campos condicionales

**Todo proceso tiene nueve campos. Hay cuatro más que solo se escriben cuando la pieza es de la base.** Un campo que no cambia una decisión no se escribe: **los condicionales no son un formulario, son una prueba.**

| Campo | Cuándo se escribe | Forma literal |
|---|---|---|
| `Sesgo` | la pieza es de la base | `**Sesgo:** la posición desde la que se sostiene` |
| `Límite` | con `Sesgo` | `**Límite:** No se aplica a qué` |
| `Firma` | con `Sesgo` | `**Firma:** tipo:nombre` |
| `Continuidad` | el proceso aprende | `**Continuidad:** veces revisada | última | qué cambió | contra qué` |

**La regla del condicional.** Se escribe el `Sesgo` o se declara por qué no aplica. Un límite que no se escribió no existe: es `No se aplica a: nada que esto exija`.

**`Firma` obligatoria con `Sesgo`.** Un veredicto que se firma a sí mismo no es veredicto: es una firma. Mientras no haya firmante distinto del productor, el veredicto es `indeterminado`, no `pasa`.

**`Continuidad` obligatoria donde el proceso aprende.** Lo que no se vuelve a medir se convierte en absoluto.

**Prueba:** ¿la pieza es de la base? ¿declara su `Sesgo`, su límite y su firmante? ¿el proceso aprende y su `Continuidad` dice contra qué se revisa?
**Falsificador:** una pieza de la base sin `Sesgo`; un `Sesgo` sin `No se aplica a`; una `Firma` que nombra al productor; una `Continuidad` vacía donde el proceso aprende.

## La forma del cuerpo

**El cuerpo no cuenta lo que el proceso es: lo ejecuta.** Se escribe como compuertas numeradas, no como prosa. La prosa explica un proceso que ya se leyó; el cuerpo lo recorre.

**Compuertas secuenciales.** El artefacto del paso N es el insumo obligatorio del N+1:

```
1. [qué entra] → [el artefacto del paso]
2. [qué se calcula] → [el artefacto del paso]
Prohibido ejecutar el paso N+1 sin la salida del N.
```

**Sin verbos de sugerencia.** Toda bifurcación cierra con una rama por defecto: `Si ... → ... | Si ... → ... | En cualquier otro caso → ...`. **Queda prohibido `procura`, `idealmente`, `si es necesario`, `cuando sea apropiado`.**

**Anclas de una línea.** Toda clasificación, medición o supuesto se declara en una línea de cinco a doce palabras, antes o junto a la acción.

**Tres ángulos por obligación.** Una obligación que no puede omitirse se escribe desde tres sitios: el imperativo, el caso que la incumple y el costo de omitirla.

**El acceso implícito no ocurre.** Una consulta externa se anuncia en una línea antes de ejecutarse. Lo que no se anuncia no pasó.

**Prueba:** ¿cada tránsito exige la salida del anterior? ¿queda algún verbo de sugerencia? ¿hay rama por defecto? ¿cada acción de juicio tiene su ancla?
**Falsificador:** una lista de viñetas sin dependencia de orden; una bifurcación sin rama por defecto; una acción de juicio sin ancla; una obligación escrita una sola vez; una consulta externa sin anuncio.

## El formato sigue al lector

**El campo no se escribe para el gusto del autor: se escribe para el lector que lo va a ejecutar.**

| Lector | Forma | Qué se escribe |
|---|---|---|
| **máquina** | campos, anclas, compuertas, salida determinista | lo que el lector recorre sin preguntar |
| **humano** | contexto, razón, ejemplo, decisión posible | lo que el lector necesita para entender el porqué |

**No se mezclan en un mismo artefacto sin declararlo.** Si el mismo contenido va a los dos, se entregan dos formatos.

**Prueba:** ¿la clase está declarada? ¿la forma corresponde a su lector?
**Falsificador:** un proceso escrito como ensayo; un texto de lectura con compuertas de ejecución; una clase que no se declaró.

## La admisión de un proceso

**Un proceso entra por la forma, no por la prosa.** Cuatro condiciones, y ninguna se rellena después.

| Condición | Qué exige | Sin ella |
|---|---|---|
| **La falla nombrada** | el caso que lo incumple, señalable en un archivo | es actividad, no proceso |
| **Las variables** | qué mueve, antes de escribir | no hay contra qué chequearlo cuando falla |
| **El falsificador** | el caso que lo refuta | es una opinión con formato de norma |
| **La salida que se usa** | alguien decide algo con ella | nadie lo carga |

**Prohibido escribir un proceso sin la falla nombrada.** Una petición de mejora que no dice qué falla no se contesta con ideas: se contesta con la falla.

**La cabecera.** Un proceso abre con `Unidad`, `Aplica a`, `Tipo` y `Estado`.

**Las dos formas de `Prueba` y `Falsificador` son legítimas.** Ninguna es mejor y ninguna se convierte a la otra.

## Unidad y proceso

**Un archivo puede contener una unidad o varias normas.** Lo que no se permite: un archivo con varias unidades y un solo `Entra`. Eso son dos procesos con un nombre.

**La norma no es la unidad.** Bajo la unidad pueden vivir apartados —`Tesis`, `Cómo se aplica`, `Ancla`, `Transiciones`— y cada uno con su par.

## La acuñación

**Todo lo que se nombra, se acuña.** Un proceso sin nombre no existe; una mutación sin nombre no se puede rastrear.

```
Acta: [id] | Nombre: [nombre] | Expansión: [significado] | Origen: [fuente] | Fecha: [ISO]
Encargo: [qué se encarga] | Fin: [estado observable]
Muta: [qué cambia] | Conserva: [qué no] | Ausencias: [qué no tiene] | Prueba: [corrida|no corrida|pendiente]
Autoridad: [tipo:nombre] | Cierra en: [tipo:nombre] | Reemplaza: [nombre anterior o NINGUNA]
```

**El nombre se lee como nombre propio; la expansión dice qué significa.** Un acrónimo que solo se puede leer deletreando no es un nombre: es una etiqueta.

> **Un nombre que sirve para dos versiones distintas no nombra nada.**

**Sin cambio, no hay acuñación fingida.** Lo que no cambió acuña igual, pero su `Muta:` declara `sin cambio`.

**El nombre anterior no se borra:** se reemplaza con `Reemplaza:` y la razón.

**Prueba:** ¿la pieza acuñada tiene nombre, expansión, `Muta`, `Conserva`, `Ausencias` y `Reemplaza`? ¿El nombre se lee como nombre propio?
**Falsificador:** un nombre que sirve para dos versiones; una acuñación sin `Reemplaza:`; una expansión que deletrea el acrónimo; un proceso que redefine esta forma en vez de citarla.

## Cómo lee el ejecutor

1. **Abrir la cabecera.** `Unidad`, `Aplica a`, `Tipo`, `Estado`.
2. **¿Tiene el bloque de entrada?** `Entra | Falla | Sale | Consume`. Sin él no es proceso.
3. **¿Tiene variables?** `Variables`, `Peor`, `Quién`.
4. **¿Tiene su reverso?** `Prueba` y `Falsificador`.
5. **Si falta algo, se nombra qué.** No se adivina.
6. **Si no puede leer el archivo, se declara `indeterminado`.** Incompleto es otra cosa.

## Lo que este formato no hace

**No juzga si la pieza sirve.** Un proceso puede tener todos los campos y ser inútil. Eso lo dice `./ACERO.md`.

**No dice cuántos procesos hay.** Eso lo dice cada instancia, y muta.

## Prueba

¿Cada proceso declara variables, bloque de entrada y reverso? ¿Los niveles cambian la carpeta y no el oficio? ¿Faltar algo se nombra en vez de adivinarse?

**Falsificador:** un proceso sin variables; un proceso sin `Falsificador`; un archivo excluido del estándar por su nombre; una sola forma aceptada y la otra marcada como error; un ejecutor que completa lo que falta por su cuenta.

## Acuñación

```
Acta: EST-00 | Nombre: Formato de proceso | Expansión: nueve campos, cuatro condicionales, cuerpo en compuertas
Origen: futuro/Estandar/Ente/formato de proceso.md | Fecha: 2026-10-23
Muta: de forma suelta a forma que cuelga del estándar | Conserva: los nueve campos y los cuatro condicionales
Ausencias: no juzga contenido ni cuenta procesos | Prueba: no corrida | Reemplaza: futuro/Estandar/Ente/formato de proceso.md
```
