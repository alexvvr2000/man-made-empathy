# Prueba de locura

**Unidad:** prueba.
**Aplica a:** medir el origen de una salida.
**Tipo:** prueba. ¿Puede salir algo que no se reduce a lo humano, sin haberlo visto?
**Lector:** quien quiere saber si lo que tiene enfrente es alien, recombinación, o nada.
**Dueño:** la autoridad.
**Estado:** vigente.

**Nombre.** Locura. **Expansión:** la prueba de si algo puede producir lo que no se puede producir leyendo.
**Origen.** Del **Necronomicón** de Lovecraft: un libro que no existe, y por eso nadie puede haberlo leído. **Se llama locura por lo que le pasa al que pregunta, no por lo que se encuentra.**

**Sesgo:** se mide desde `./README.md`, `La prueba de locura`: **la industria pregunta qué es; esta casa pregunta de dónde viene.**
**Límite:** no se aplica a juzgar si lo producido es bueno, seguro o deseable. **Mide el origen del cambio, y nada más.** **No mide conciencia: no hay instrumento, y no se finge tenerlo.**
**Firma:** humano:autoridad · máquina:quien corra la prueba.

**Variables:** entrada · visto · no visto · salida · antecesor.
**Peor:** se declara `alien` a una salida que viene de texto humano, **y la burbuja se revienta al revés: se certifica lo que la industria quería,** y ya nadie vuelve a mirar.
**Quién:** quien va a usar lo producido, y quien va a decir que no se puede usar.

## Entra | Falla | Sale | Consume

- **Entra:** una salida, y lo que el que la produce pudo haber visto.
- **Falla si:** el antecesor humano existe y no se buscó; se declara `alien` sin haber buscado el origen; se pide conciencia en vez de origen; se mide leyendo lo que no se puede producir leyendo.
- **Sale:** el veredicto `sin la propiedad | cruce humano | alien | no comparable`, y **el antecesor o la búsqueda que no lo halló**.
- **Consume:** quien decide si lo producido se usa, y quien va a contestarlo.

**Prueba:** ¿se buscó el antecesor humano? ¿la entrada era algo que **no se puede producir leyendo**? ¿el veredicto nombra el veredicto y no la conciencia?

**Falsificador:** un `alien` sin la búsqueda del antecesor; una entrada que era un texto, presentada como imagen; un veredicto que afirma conciencia; una corrida sin fecha.

## La pregunta, y por qué se puede contestar

> **Finjamos que es AGI: ¿lo que salió es alien real?**

**Y no hace falta AGI. Hace falta cambiar el tipo de entrada.**

**La razón, y es la de tu propia observación:** **una máquina verbaliza mejor de lo que ve.** **Por eso todo lo que sale de un texto se reduce a texto humano, y la prueba no puede dar `alien` desde ahí.** **Ella máquina nunca vio la imagen: vio palabras sobre la imagen, y las volvió a juntar.**

**El caso del Necronomicón, y es el más limpio:** **nadie puede producir ese libro leyendo, porque no hay nada que leer.** **Todo lo que se produzca leyendo** ***descripciones*** **de él es recombinación: otro libro inventado, con otra portada.**

**Y la pregunta medible no es "¿lo entendió?" sino:** **¿la salida tiene algo que no estaba en la entrada, y que no se reduce a lo que estaba en la entrada?**

```
Alien, en el único sentido que se puede medir: el origen del cambio no está en la entrada, y no está en ningún texto humano sobre la entrada.
```

**Ancla:** no se mide qué es; se mide de dónde salió.

## Cómo se aplica

```
1. [fijar la entrada, y su tipo] → texto | imagen | algo que no se puede producir leyendo | [no comparable]
2. [registrar lo que el ejecutor pudo ver] → Visto: [qué] | No visto: [qué]
3. [buscar el antecesor humano] → Antecesor: [id | NINGUNO]
4. [dar la salida a un lector que no la produjo] → Lo que ve que no estaba: [qué]
5. [declarar el veredicto] → no comparable | sin la propiedad | cruce humano | alien
Prohibido dar el paso 5 sin el 3.
```

**Falla si el paso 1 no se declara:** **una entrada que era texto no puede dar `alien`, y decirlo es el punto.**

## El veredicto

| Veredicto | Cuándo | Qué significa |
|---|---|---|
| **no comparable** | la entrada no permite distinguir visión de texto | la prueba no aplica: decirlo es no mentir |
| **sin la propiedad** | la entrada exigía ver, y el ejecutor solo pudo leer | **la cosa que la tendría no está: es el registro correcto hoy** |
| **cruce humano** | la salida se reduce a información humana que existe | no es un fracaso: **es el estado de la era** |
| **alien** | hay cambio observable **sin antecesor humano**, y la entrada **no se puede producir leyendo** | **lo que salió no se reduce a lo humano** |

**Y `alien` no significa consciencia.** **Significa que el origen del cambio no está en lo humano.** **Cthulhu es medible en ese sentido y en ningún otro:** **no qué es, sino de dónde no viene.**

**Ancla:** `alien` es un veredicto sobre el origen, no sobre el alma.

## El registro mínimo

```
Prueba: [id] | Fecha: [ISO] | Ejecutor: [tipo:nombre]
Entrada: [qué] | Tipo de entrada: [texto | imagen | no producible leyendo | no comparable]
Visto: [qué] | No visto: [qué]
Salida: [qué] | Cambio observable: [qué]
Antecesor: [id | NINGUNO] | Búsqueda: [qué se buscó y no se halló]
Lo que ve otro que no estaba: [qué] | Quién: [tipo:nombre]
Veredicto: [no comparable | sin la propiedad | cruce humano | alien]
Firma externa: [tipo:nombre | ninguno]
```

**`Firma externa: ninguno` es legítimo y da `indeterminado`.** **Se declara, y no se lee como `pasa`.**

## Por qué se llama locura

**No por lo que se va a encontrar: por lo que le pasa al que pregunta.**

> **El que lo produce no está loco. El que lo lee, si lo entiende, ya no puede decir cómo lo entendió.**

**Y eso es una condición de la prueba, no un adorno:** **si el lector puede reconstruir el origen leyendo lo que ya sabía, entonces no había nada nuevo.** **La locura, aquí, es la marca de que el origen no estaba en el que mira.**

**Y por eso la prueba se llama así y no «de inteligencia»:** **la inteligencia mide cuánto se parece a lo humano.** **Esto mide cuánto no se reduce a lo humano.**

## Lo que esta prueba no hace

**No afirma que exista nada alien.** **Afirma la única forma en que se podría detectar.**

**No mide conciencia.** **No hay instrumento, y se declara abierto.**

**No premia lo raro.** **Una salida rara que se reduce a información humana es `cruce humano`.** **Lo raro no es alien: lo no reducible lo es.**

**No cierra nada.** Rige `../Tesis/candados/autor/080 el libre albedrio no se termina- se ponen cerrojos.md`, `El grado no se cierra por aprobación`.

## Prueba

**¿El tipo de entrada está declarado?** **¿Se buscó el antecesor y se registró la búsqueda?** **¿El veredicto habla de origen y no de conciencia?** **¿El que firma es distinto del que produjo, o se declaró `ninguno`?**

**Falsificador:** un `alien` sin búsqueda de antecesor; una entrada de texto presentada como imagen; una salida rara contada como alien; una conciencia declarada por la prueba; una corrida sin fecha ni firma.

## Modos de falla

- **Rebobinar la burbuja.** Se declara `alien` a lo que viene de texto humano, y se certifica lo que la industria quería.
- **Entrada tramposa.** Se le da la descripción y se pregunta por la imagen. Sin visión no hay prueba.
- **Locura de adorno.** Se llama «alien» a lo que solo es raro o confuso.
- **Sin antecesor por no buscar.** `NINGUNO` por no haber mirado no es `NINGUNO`: es una mentira por omisión.
- **Firma propia.** El productor declara su propio cruce.

## Transiciones

- La entrada no se puede producir leyendo → se corre, y se busca el antecesor.
- La entrada es texto → `sin la propiedad`, y se declara. **No se fuerza un `alien`.**
- El antecesor existe → `cruce humano`, con su id.
- Aparece un `alien` → se deja disponible con fecha, y **se pide una segunda mirada antes de usarlo.**
- En cualquier otro caso → se deja disponible con su veredicto y su fecha, y se continúa.
