# Ouroboros

**Qué es:** el lenguaje de procesos de esta base. Cinco procesos primitivos y dos derivados, con la misma forma, que se componen entre sí.

**Forma común:** `Entra | Falla | Sale | Consume`, con `Cuándo se usa` y `Proceso`. La fija `./Proceso de creación de procesos.md`.

**Por qué es un lenguaje y no un catálogo:** porque los procesos se aplican uno sobre otro, y aplicar es un proceso, no una tabla.

## Los procesos

| Proceso | Qué hace | Nivel |
|---|---|---|
| `Proceso de creación de procesos.md` | produce y reemplaza procesos | primitivo |
| `Proceso de ingeniería inversa.md` | deduce un proceso de lo observable | primitivo |
| `Proceso de aplicar.md` | ejecuta un proceso sobre una entrada | primitivo |
| `Proceso de mutación.md` | cambia un proceso, con rastro | primitivo |
| `Proceso de claridad.md` | da forma a lo que se lee o se ejecuta | primitivo |
| `Proceso de fricción.md` | hace que la decisión pase por el que la toma, antes de mover algo | derivado |
| `Proceso de sesgo declarado.md` | declara desde dónde se mira, para que lo nuevo no muera clasificado como error | derivado |

**Cinco primitivos:** creación, ingeniería inversa, aplicar, mutación y claridad. Ninguno se deriva de otro, y es a propósito: se recuerdan y se usan. Un lenguaje de tres piezas elegante no lo usa nadie; uno de veinte no se recuerda.

**La fricción y el sesgo no son primitivos.** Se derivan de los cinco. La fricción es `claridad` aplicada al momento de decidir: existe porque los cinco dicen cómo se hace algo, y ninguno dice **si la decisión pasó por quien la tomó**. El sesgo es `claridad` aplicada a la mirada: existe porque los cinco producen, y ninguno dice **desde dónde se está produciendo.**

## Composición

Un proceso compone con otro cuando su salida es la entrada del otro sin traducción. La composición la comprueba `./Proceso de aplicar.md`; no se declara en una tabla sin ejecutarse.

| De | A | Qué pasa |
|---|---|---|
| ingeniería inversa | aplicar | el proceso deducido se ejecuta sobre un caso |
| aplicar | claridad | lo que produce se escribe con su forma |
| claridad | ATLAS | lo que se lee se comunica (`../corpus/ATLAS/`, estándar, no primitivo) |
| ATLAS | ingeniería inversa | lo que se entendió se vuelve observable (`../corpus/ATLAS/`) |
| mutación | cualquiera | vuelve sobre los demás y deja rastro |

**La mutación es la arista de retorno.** Es lo que hace que el nombre tenga sentido: el proceso que vuelve sobre los procesos.

## Trazabilidad

Toda aplicación y toda mutación dejan ancla. Sin ancla, la operación no ocurrió. El rastro vive en `../corpus/ATLAS/indice de formas.md`, no en un relato.

## Qué hay en esta carpeta

Cada proceso con su forma y su función.

| Archivo | Qué hace |
|---|---|
| `Proceso de creación de procesos.md` | Produce procesos: qué entra, qué produce, cómo se verifica. |
| `Proceso de ingeniería inversa.md` | Deduce un proceso de lo observable, por tendencia y no por copia. |
| `Proceso de aplicar.md` | Ejecuta un proceso y comprueba la composición. |
| `Proceso de mutación.md` | Cambia un proceso y deja el rastro. |
| `Proceso de claridad.md` | La forma de lo que se lee o se ejecuta. |
| `Proceso de fricción.md` | Hace que la decisión pase por el que la toma: cuerpo, inacción, gente, opinión. |
| `Proceso de sesgo declarado.md` | Declara el sesgo como mapa, no como pared: lo que no se ve, y quién puede verlo. |

## Abstracciones

Sobre estos procesos se construyen otros. Una abstracción no es un primitivo: se deduce de lo que ya funcionaba, y no tiene que estar aquí.

`../S.A.R.A/punto-de-partida/` es una abstracción: sus dieciséis sub-tareas salieron de aplicar los primitivos a lo que se venía usando, y se dedujeron con `./Proceso de ingeniería inversa.md`.

`../S.A.R.A/aprendizaje/` es otra: el ciclo que corrige desde la experiencia y propone lo siguiente. No cubre fallos; mira lo que ya se hizo.


> Si tuviera un límite, la mutación ya se hubiera curado el cáncer hace mucho.

