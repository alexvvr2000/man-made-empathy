# Ouroboros

**Qué es:** el lenguaje de procesos de esta base. Cinco primitivos y dos mutaciones, con la misma forma, que se componen entre sí.

**Deterrente:** `./deterrente.md`. Enruta subprocesos: sin él, un subproceso no sabe cuándo se carga, y una puerta abierta pierde el rastro de por qué se hizo algo.

**Piso:** `./piso.md`. Rige `../corpus/piso.md`.

**Forma común:** `Entra | Falla | Sale | Consume`, con `Cuándo se usa` y `Proceso`. La fija `./primitivos/manipulacion.md`.

**Por qué es un lenguaje y no un catálogo:** porque los procesos se aplican uno sobre otro, y aplicar es un proceso, no una tabla.

## El árbol

El nombre lo da la carpeta. **Lo que está dentro ya se sabe que es un proceso: no se repite en cada archivo.**

```
Ouroboros/
─── deterrente.md              el de este nivel
─── integridad.md              el único que no produce: chequea
─── primitivos/
│   ─── manipulacion.md        produce, calibra, reemplaza, retira
│   ─── aplicar.md             ejecuta un proceso sobre una entrada
│   ─── mutacion.md            transforma y deja rastro
│   ─── claridad.md            la fuente de la que se muta
│   └── ingenieria-inversa.md  deduce de lo observable
─── mutaciones/
│   ─── friccion.md            nace de claridad
│   └── sesgo-declarado.md     nace de claridad
└── README.md
```

**Cuatro carpetas y ninguna es una clasificación.** `primitivos/` y `mutaciones/` dicen **de dónde vino** cada proceso; `integridad.md` está suelto porque es el único que chequea. **Si mañana hay otro que chequee, va al lado: sin abrir carpeta nueva.**

## Los cinco primitivos

| Primitivo | Qué hace | Se rompe así |
|---|---|---|
| `manipulacion` | produce, calibra, reemplaza y retira | se crea sin variables |
| `aplicar` | ejecuta un proceso sobre una entrada | se aplica sin que la entrada corresponda |
| `mutacion` | transforma y declara qué conserva | se muta sin declarar qué se conserva |
| `claridad` | la fuente de la que se muta | la forma no llega al lector |
| `ingenieria-inversa` | deduce de lo observable | no reproduce el resultado |

**Cinco primitivos:** ninguno se deriva de otro, y es a propósito. Se recuerdan y se usan. Un lenguaje de tres piezas elegante no lo usa nadie; uno de veinte no se recuerda.

## Las dos mutaciones

**`friccion` y `sesgo-declarado` no son primitivos: son mutaciones de `claridad`.** Las dos nacieron de la misma pregunta —*¿el otro puede reconstruir esto?*— y declaran qué conservan de él.

Una mutación nueva puede nacer de **n primitivos**, no de uno. **Las piezas se combinan, no se escalan.**

## Composición

Un proceso compone con otro cuando su salida es la entrada del otro sin traducción. La composición la comprueba `./primitivos/aplicar.md`; no se declara en una tabla sin ejecutarse.

| De | A | Qué pasa |
|---|---|---|
| ingeniería inversa | aplicar | el proceso deducido se ejecuta sobre un caso |
| aplicar | claridad | lo que produce se escribe con su forma |
| claridad | ATLAS | lo que se lee se comunica (`../corpus/ATLAS/`, estándar) |
| mutación | cualquiera | vuelve sobre los demás y deja rastro |

**La mutación es la arista de retorno.** Es lo que hace que el nombre tenga sentido: el proceso que vuelve sobre los procesos.

## Trazabilidad

Toda aplicación y toda mutación dejan ancla. Sin ancla, la operación no ocurrió. El rastro vive en `../corpus/ATLAS/indice de formas.md`, no en un relato.

## Abstracciones

Sobre estos procesos se construyen otros. Una abstracción no es un primitivo: se deduce de lo que ya funcionaba, y no tiene que estar aquí.

`../S.A.R.A/punto-de-partida/` es una abstracción: sus dieciséis sub-tareas salieron de aplicar los primitivos a lo que se venía usando, y se dedujeron con `./primitivos/ingenieria-inversa.md`.
