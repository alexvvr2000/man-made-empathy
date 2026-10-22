# Deterrente de Ouroboros

**Unidad:** nivel.
**Aplica a:** sostener.
**Tipo:** deterrente de deterrentes. No produce, no ejecuta, no chequea: dice qué pasa si el nivel no se sostiene.
**Lector:** quien va a mutar Ouroboros, y quien lo audita después.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

Cada proceso tiene su `Falsificador`: quién lo refuta. **Este archivo es el de Ouroboros entero**, y no refuta procesos: refuta **que el nivel exista.**

Sin deterrente, un archivo no puede justificarse. **Es un fantasma**, y un fantasma que parece necesario es peor que uno obvio, porque nadie lo mira dos veces.

## Lo que se pierde si se viola

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| un primitivo deja de tener forma | no se puede componer con otro | cada proceso se escribe a su manera |
| dos primitivos se contradicen | no hay lenguaje: hay dos | un proceso cumple uno e incumple el otro |
| un primitivo no deriva en nada | es un fantasma | nadie lo carga, pero se mantiene por costumbre |
| una mutación no declara qué conserva | no se puede reconstruir el cambio | el proceso nuevo parece nuevo y no lo es |
| el nivel se salta hacia arriba | MANTIS edita sin nivel | se arreglan cosas que nadie puede volver a encontrar |

## Los cinco primitivos

Cinco, y no se derivan de nada:

| # | Primitivo | Qué hace |
|---|---|---|
| 1 | `manipulación de procesos` | produce, calibra, reemplaza y retira |
| 2 | `aplicar` | ejecuta un proceso sobre una entrada |
| 3 | `mutación` | transforma, declara qué conserva y deja rastro |
| 4 | `claridad` | **la fuente de la que se muta** |
| 5 | `ingeniería inversa` | deduce un proceso de lo observable |

**Ninguno es superior a otro.** `mutación` vuelve sobre los demás, pero no los gobierna: **es la arista de retorno, no la jerarquía.**

## Lo que se muta desde los primitivos

`claridad` no es el proceso pesado que todos leen. **Es el primitivo del que se muta.**

| Mutación | Nace de | Qué conserva de `claridad` |
|---|---|---|
| `fricción` | `claridad` | que el otro pueda reconstruir la decisión |
| `sesgo declarado` | `claridad` | que se vea desde dónde se mira |

**Las dos nacieron de la misma pregunta:** *¿el otro puede reconstruir esto?* Una la aplica al momento de decidir; la otra, al de mirar. **Ninguna es "derivada": son mutaciones**, y declaran qué conservan.

**Y de ahí sale lo que hace poderoso a esto:** una mutación nueva puede nacer de **n primitivos**, no de uno. `fricción` y `sesgo` nacieron las dos de `claridad`; una tercera puede nacer de `claridad` y `aplicar` a la vez. **Los primitivos son piezas, no una cadena.**

## Lo que Ouroboros declara que no es

**No es un catálogo.** Un catálogo lista; Ouroboros **compone**: la salida de uno es la entrada de otro sin traducción.

**No es una jerarquía.** Los cinco no manda uno sobre otro; cada uno se rompe de una manera distinta.

**No contiene el contenido.** Ouroboros dice **cómo se hace un proceso**, no **qué procesos hay**. Los procesos viven en las instancias —`Ouroboros/` misma, `S.A.R.A/`, `mantis/`— y en la era que los implementa.

## Prueba

¿Los cinco primitivos siguen sin derivarse de nada? ¿Cada mutación declara de qué primitivo nace y qué conserva? ¿Algún archivo de esta carpeta no deriva en nada?

**Falsificador:** un primitivo que se explica por otro; una mutación sin `Conserva:`; un archivo del nivel que nadie carga; dos primitivos que no se pueden cumplir a la vez; un sexto primitivo agregado sin quitar uno.

## Transiciones

- Un primitivo no compone → `./primitivos/aplicar.md`, `Compone:`.
- Una mutación no declara qué conserva → `./primitivos/mutacion.md`, `Sin herencia`.
- Un archivo del nivel no deriva en nada → se declara fantasma y se retira.
- En cualquier otro caso → se entrega y se cierra.
