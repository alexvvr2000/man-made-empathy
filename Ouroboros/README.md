# Ouroboros

**Qué es:** el lenguaje de procesos de esta base. Seis procesos con la misma forma, que se componen entre sí.

**Forma común:** `Entra | Falla | Sale | Consume`, con `Cuándo se usa` y `Proceso`. La fija `./Proceso de creación de procesos.md`.

**Por qué es un lenguaje y no un catálogo:** porque los procesos se aplican uno sobre otro, y aplicar es un proceso, no una tabla.

## Los seis

| Proceso | Qué hace | Nivel |
|---|---|---|
| `Proceso de creación de procesos.md` | produce y reemplaza procesos | primitivo |
| `Proceso de ingeniería inversa.md` | deduce un proceso de lo observable | primitivo |
| `Proceso de aplicar.md` | ejecuta un proceso sobre una entrada | primitivo |
| `Proceso de mutación.md` | cambia un proceso, con rastro | primitivo |
| `Proceso de claridad.md` | da forma a lo que se lee o se ejecuta | primitivo |
| `Proceso ATLAS.md` | comunica con piso, techo y sesgo | primitivo |

Seis procesos, todos primitivos: ninguno se deriva de otro. Es más piezas que el mínimo teórico, y es a propósito: se recuerdan y se usan. Un lenguaje de tres piezas elegante no lo usa nadie.

## Composición

Un proceso compone con otro cuando su salida es la entrada del otro sin traducción. La composición la comprueba `./Proceso de aplicar.md`; no se declara en una tabla sin ejecutarse.

| De | A | Qué pasa |
|---|---|---|
| ingeniería inversa | aplicar | el proceso deducido se ejecuta sobre un caso |
| aplicar | claridad | lo que produce se escribe con su forma |
| claridad | ATLAS | lo que se lee se comunica |
| ATLAS | ingeniería inversa | lo que se entendió se vuelve observable |
| mutación | cualquiera | vuelve sobre los otros cinco y deja rastro |

**La mutación es la arista de retorno.** Es lo que hace que el nombre tenga sentido: el proceso que vuelve sobre los procesos.

## Trazabilidad

Toda aplicación y toda mutación dejan ancla. Sin ancla, la operación no ocurrió. El rastro vive en `./indice de formas.md`, no en un relato.

## Qué hay en esta carpeta

| Archivo | Qué es |
|---|---|
| `Proceso de creación de procesos.md` | Produce procesos: qué entra, qué produce, cómo se verifica. |
| `Proceso de ingeniería inversa.md` | Deduce un proceso de lo observable, por tendencia y no por copia. |
| `Proceso de aplicar.md` | Ejecuta un proceso y comprueba la composición. |
| `Proceso de mutación.md` | Cambia un proceso y deja el rastro. |
| `Proceso de claridad.md` | La forma de lo que se lee o se ejecuta. |
| `Proceso ATLAS.md` | Comunicación efectiva: piso, techo y sesgo declarado. |
| `indice de formas.md` | Las formas que pasaron su prueba, por intención. |

## Abstracciones

Sobre estos seis se construyen otros procesos. Una abstracción no es un primitivo: se deduce de lo que ya funcionaba, y no tiene que estar aquí.

`Procesos no humanos/` es una abstracción: sus tres subprocesos salieron de aplicar los primitivos a lo que se venía usando, y se dedujeron con `./Proceso de ingeniería inversa.md`.

## Lo que absorbió

`A.R.E.S` eran cuatro archivos revueltos: `idea`, `protocolo`, `mapa`, `atlas`. Ahora es el proceso `ATLAS` y su índice. `teoria.md` se retiró: era la tesis explicativa, y el `README` de la base la cubre.

`Escritura` eran dos archivos: claridad y creación de procesos. Ahora están aquí.

`Reglas de mutación` hablaba de tareas. Ahora es el primitivo de mutación, y mutar tareas es una abstracción.
