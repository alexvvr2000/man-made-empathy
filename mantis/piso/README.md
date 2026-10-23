# Piso — las unidades de esta instancia

**Unidad:** nivel.
**Aplica a:** trabajar.
**Tipo:** puerta del piso de esta instancia. No decide ni ejecuta: dice qué unidades hay, qué decide cada una y cuándo dejan de usarse.
**Lector:** quien va a usar MANTIS.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

**El piso no es MANTIS.** El piso es el instrumento, y MANTIS es su tarea.

**La diferencia, y es la que hay que ver:** MANTIS **decide** qué se carga, cuándo se edita y qué se pierde. El piso **mira y emite veredicto.** **Una herramienta no decide: mide.**

**Y el piso ya no mide forma: mide existencia.** Cada unidad tiene que declarar antes de correr **qué se le resiste, quién puede contestarla, qué se pierde si deja de correr y cuándo deja de valer.** Sin las cuatro, **no corre: aparece.** Rige `../../Ouroboros/procesos/friccion como fundamento del piso.md`, `Las cuatro pruebas de existencia`.

**Y por eso el piso no cambia de nombre cuando VIDERE se separa:** lo que se separa es **el ente que llega desde el Guantelete**, no la herramienta que lo mide. **Una regla que se muda de carpeta no se lleva el metro que la mide.** Rige `../../futuro/DIFERENCIA.md`.

**El flujo, y es el mismo desde el principio:** ente (Guantelete → VIDERE) → **la realidad** → y si se quiere comunicar, **ATLAS**. **El piso mide en cada tramo, y no es ninguno de los tres.**

**El piso corre aquí y ahora.** Cada unidad decide una cosa, emite un veredicto y se lee sola: `pasa`, `falla` o `indeterminado`, con el porqué.

**La forma de cada unidad la dice `../../Ouroboros/piso.md`.** Aquí solo se declara cuáles hay, qué decide cada una, **y dónde deja de valer.**

**Estas ocho no son las únicas posibles: son las que ganaron su lugar.** Una tarea que no vuelve es un tiro, y no se guarda. Rige `../../Ouroboros/CRITERIO.md`, `Unidad y tiro`.

## Las unidades

**Cada una declara qué decide, qué no puede ver, y su `No se aplica a`** — la cuarta condición del estándar. **Un límite es el que dice cuándo dejar de usarla**, y por eso no se omite.

| Unidad | Qué decide | Qué no puede ver | `No se aplica a` |
|---|---|---|---|
| `inventario.ps1` | qué procesos hay y qué campo les falta | si lo que tienen sirve | lo que no es proceso: un índice, un borrador, una nota |
| `rutas.ps1` | qué ruta relativa no resuelve a un archivo real | si el destino dice lo que debe | rutas externas, plantillas con `[corchete]` y enlaces de era |
| `fantasmas.ps1` | qué ente no tiene `rastro.md`, `ruta.md` o `carga.md` | si el fallo que cubre sigue existiendo | carpetas sin ninguna de las tres: no son entes |
| `notas.ps1` | si la memoria se escribe como manda la carta, y si cada archivo cambiado tiene nota | si lo anotado es válido; qué archivo cambió por trabajo y qué por otra persona | el contenido de la fila: eso lo decide el aplanado |
| `turno.ps1` | si el turno cerró con su entrada en la memoria | si lo anotado sirve | abrir el turno: eso lo decide quien lo empieza |
| `quien.ps1` | de quién es cada zona y cuáles zonas cambió este turno | si el cambio le pertenece a quien lo escribió | la intención; se declara en el pase |
| `privacidad.ps1` | si un archivo versionado o nuevo/no ignorado expone la máquina de una persona | si un ejemplo didáctico expone a alguien: eso lo decide quien lo publica | archivos ignorados por git y la firma de autor de `CITATION.cff`, que la autoridad declaró pública |

| `trazabilidad.ps1` | si lo que `Tesis/referencias` nombra tiene su archivo, y si cada archivo tiene sus cuatro campos | si una referencia vale, o si provoca algo: eso lo decide quien lee | los momentos, que son prosa sin forma fija; y los archivos que empiezan con `_`, que son plantilla |

**`trazabilidad.ps1` mide lo que se pierde sin que nadie lo note:** una referencia discutida en conversación y no guardada **desaparece cuando el contexto se llena.** Un nombre sin archivo y sin `[SIN ENTRADA]` en el índice es falla; **ese es el error que no detectaba ninguna unidad.**

**`privacidad.ps1` corre sobre lo versionado y lo nuevo que Git no ignora, no sobre el disco entero:** una ruta personal en un archivo ignorado no sale del repo y no se declara. **Y no mira commits anteriores:** lo que ya se subió al historial no lo detecta. Ese caso se resuelve sobre Git, y Git es de la autoridad.

## El tren

```
pwsh -File mantis/piso/piso.ps1
```

Corre las ocho y emite **un solo veredicto**. **Cada una también se corre sola**: un tren no es una tubería.

## Reglas del piso

1. **No usa modelo.** Si un `if` resuelve, un modelo introduce ruido.
2. **Su salida ya es veredicto.** Nunca materia prima.
3. **Se puede correr sola.** No necesita las otras siete.
4. **Se rige por el criterio, y lo declara.** Cada unidad dice su `No se aplica a`, y **el veredicto lo escribe quien lo va a usar.**

**Y lo que descarta no se tira: se anota.** Rige `../../Ouroboros/procesos/memoria continua.md`, `Purga`.

## Prueba

¿Cada unidad se corre sola? ¿Cada una emite veredicto y por qué? ¿Cada una declara su `No se aplica a`? ¿El tren da un solo veredicto?

**Falsificador:** una unidad que necesita que otra corra antes; una que emite datos sin veredicto; una que cambia de resultado entre dos corridas del mismo estado; **una unidad sin `No se aplica a`.**
