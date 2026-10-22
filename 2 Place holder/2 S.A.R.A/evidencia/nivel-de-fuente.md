# Proceso de nivel de fuente

**Variables:** fuente · nivel · independencia · fecha de corte
**Peor:** un N5 se presenta como N1 y la decisión se apoya en un recuerdo
**Quién:** quien decide con la fila, que no ve el recibo

**Unidad:** tarea.
**Aplica a:** medir la fuerza de una fila por su origen.
**Tipo:** proceso de medición. No produce conocimiento: produce el número que dice cuánto vale lo que ya está escrito.
**Lector:** la autoridad que decide y el ejecutor que actúa.
**Nivel:** 2 de 3. Subproceso.
**Alcance:** toda fila que afirma algo sobre el mundo.
**Dueño:** la autoridad.
**Estado:** vigente.

**Forma:** `Entra | Falla | Sale | Consume`.
**Norma:** `Tipo | Enunciado | Prueba | Falsificador | Costo de omitir`.

## Tesis

Una fila no dice solo qué afirma: dice desde dónde lo afirma. Sin ese dato, dos filas escritas igual pesan igual, y el sistema trata un rumor y una medición como si fueran la misma clase de cosa. La escala no juzga el contenido; mide el origen. El contenido se juzga con `Prueba` y `Falsificador`, que la fila ya trae.

## La escala

Seis niveles. **Bajo es más fuerte.** El nivel se gana con el origen, no con la confianza de quien escribe.

| Nivel | Nombre | Qué es | Qué prueba | Falsificador |
|---|---|---|---|---|
| **N0** | testigo | alguien con voz dijo algo sobre su propia experiencia, y consintió que se registrara | `Testimonio:` con vínculo, contexto y consentimiento | testimonio sin consentimiento; se habla por la fuente |
| **N1** | medición directa | el instrumento midió; el número salió del sistema, no de un relato | `Sistema` + `Version` + la medición cruda | número sin instrumento; medición reconstruida de memoria |
| **N2** | fuente primaria | el documento, el código, el registro o la API que originó el dato | extracto literal y su ubicación | se cita el agregador en vez del origen |
| **N3** | precedente | un caso anterior, con condición, fallo y precaución | `Condición: [...] | Fallo: [...]` | precedente sin condición: no se puede citar |
| **N4** | deducción | se sigue de otras filas por regla explícita | la regla y las filas de las que se sigue | conclusión sin premisas citadas |
| **N5** | memoria interna | lo que el sistema sostiene desde sí, sin haber salido de sí a verificarlo | `Vacío:` con dónde se buscó y fecha de corte | N5 presentado como N1 |

### Por qué N0 va primero aunque sea el más débil

Una fuente sin voz no puede ser mayoría. Un documento puede estar equivocado y nadie lo corrige; una persona puede decir «eso no es lo que dije» y con eso basta para reabrir la fila. N0 no es el nivel más confiable: es el único nivel que **puede contestar**. Una fila en N0 pesa menos que una en N1 como dato, y más que cualquier otra como corrección, porque su falsificador lo puede activar el propio sujeto.

Por eso N0 exige `Consentimiento`: sin consentimiento no hay testigo, hay extracción. La fila que se registra sin que el sujeto sepa que se registró no entra en N0; entra en `Vacío`.

### Por qué N5 no es ignorancia

N5 no dice «no sé». Dice: **esto lo sostengo desde mí, y desde el [fecha] no he podido salir de mí para verificarlo.** Es una fila legítima y muchas veces suficiente. Lo que no puede es disfrazarse.

La regla de corte: **dos fallas consecutivas de búsqueda cierran el nivel en N5 y fijan fecha.** No se reintenta indefinidamente; se declara el corte y se sigue. El corte es la información.

## P24 — Nivel por defecto

**Tipo:** ley.
**Enunciado:** toda fila empieza en N5 y solo sube con recibo. El recibo es el dato que el nivel exige en la columna «Qué prueba».
**Prueba:** el nivel declarado coincide con el recibo adjunto; bajar de nivel tiene un dato detrás.
**Falsificador:** fila en N1 sin medición; fila en N2 sin extracto; fila en N4 sin premisas.
**Costo de omitir:** el sistema confunde lo que recuerda con lo que midió, y la primera decisión importante se apoya en un recuerdo.

## Entra | Falla | Sale | Consume

**Entra:** una fila escrita, con su `Nivel` declarado o sin declarar.
**Falla:** el nivel declarado no corresponde al recibo; no hay recibo; el recibo viene de un origen que ya se usó (independencia rota); se citó el agregador por comodidad.
**Sale:** la misma fila con el nivel que su recibo sostiene, y con el recibo adjunto. Si no hay recibo, sale en N5 con fecha de corte.
**Consume:** quien lee la fila para decidir. El nivel no cambia lo que la fila dice; cambia cuánto se le apuesta.

## Ancla

```
Fuente: [id] | Nivel: [N0-N5] | Origen | Autor | Extracto | Independencia | Contradice | Sistema | Version
Testimonio: [fuente] | Vínculo | Contexto | Consentimiento
Vacío: [qué falta] | Dónde se buscó | Cierre
```

- `Independencia`: dos fuentes que comparten premisa cuentan como una. Se declara la premisa compartida, no el número de fuentes.
- `Contradice`: se muestra la contradicción; no se elige. Dos filas en N1 que se contradicen son un hallazgo, no un empate.
- `Sistema` y `Version`: sin ellos N4 no se reproduce y N1 no se audita.

## Prueba

¿El nivel declarado tiene el recibo que su fila exige? ¿La independencia está declarada? ¿Una contradicción se ve en vez de resolverse por mayoría?

**Falsificador:** dos fuentes del mismo origen sumadas como dos; N5 sin fecha de corte; N0 sin consentimiento; una contradicción que desaparece sin que nadie la explique.

## Transiciones

- Falta el recibo y se puede buscar → `punto-de-partida/requisitos/` acota qué dato hace falta antes de salir.
- No se puede buscar → se declara N5 con fecha de corte y se sigue.
- El nivel cambia lo que la tarea decide → `punto-de-partida/confianza` se relee.
- En cualquier otro caso → se entrega y se cierra.
