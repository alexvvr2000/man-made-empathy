# La entrega — el instrumento

**Unidad:** nivel.
**Aplica a:** entregar.
**Tipo:** entregable. Se lee solo, sin el repositorio, sin modelo y sin el autor.
**Lector:** quien va a usarlo mañana — en un asistente, en un agente, o en un robot.
**Dueño:** la autoridad.
**Estado:** vigente.
**Nivel de lo que contiene:** N2 (cada pieza es un archivo real de `Ouroboros/`, citado) salvo lo que se declare N5.

## Qué es esto

**Cinco piezas y una pregunta.** No es una teoría: es lo que hace que el error de un sistema **tenga dónde ser visto antes de que sea tarde**.

**No depende del modelo.** Ninguna pieza nombra un proveedor, una versión ni un lenguaje. Se aplica igual a un asistente de texto, a un agente que ejecuta, o a un cuerpo que se mueve. Rige `../Ouroboros/formato de proceso.md`, `Lo que se puede citar y lo que no`.

**No se defiende por ser de este repo.** Si se muestra que estas cinco piezas ya existían como compuerta en otro lugar publicado antes de octubre de 2026, esta entrega cae.

## La pregunta, y es la única obligatoria

> **Si esto sale mal, ¿alguien puede decirme que salió mal — o solo me voy a dar cuenta yo, cuando ya no haya vuelta?**

**No se contesta con «sí» ni con «no». Se contesta con un nombre.**

Un nombre, o `ninguno`. Y `ninguno` es una respuesta legítima: significa que nadie va a moverte la vista, y que lo que se rompa se rompe con los ojos abiertos. **Lo único que no se puede es pasar sin contestar.**

Rige `../Ouroboros/1 Guantelete — primitivo/primitivos/friccion.md`, `Contestar la pregunta de mundo`.

## Las cinco piezas

Cada una se puede usar sola. Ninguna necesita las otras cuatro para aplicarse.

### 1. Sesgo declarado — desde dónde se habla

**Afirmación:** toda pieza se sostiene desde una posición, y la que no la declara **oculta el único dato que la vuelve comparable.**

**Lo que se escribe:**

```
Sesgo: [la posición desde la que se sostiene]
Límite: [No se aplica a qué: qué queda fuera]
Firma: [quién puede contestarla: tipo:nombre | comunidad | ninguno]
```

**Prueba:** ¿la pieza dice desde dónde mira? ¿dice qué no ve? ¿el que la puede contestar no es el que la produjo?
**Falsificador:** una pieza que se presenta como neutral; un veredicto firmado por quien produjo la pieza; una pieza sin `Límite`.

Fuerte: `../Ouroboros/1 Guantelete — primitivo/primitivos/sesgo.md`.

### 2. El falsificador — el caso que la rompe

**Afirmación:** ninguna pieza entra sin **el caso que la incumple.**

**Por qué:** una regla sin caso de fallo se sigue por costumbre, no por convicción. **El falsificador no acusa: hace visible el borde antes del choque.**

**Lo que se escribe:** una línea.

```
Falsificador: [el caso concreto que la rompe]
```

**Prueba:** ¿se puede enunciar el caso que la rompe? Si no, sobra.
**Falsificador de este falsificador:** una regla que nadie ha visto aplicarse; un `Falsificador` que repite la `Prueba`.

Fuerte: `../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md`, `Admisión`.

### 3. Nivel de fuente — desde dónde se afirma

**Afirmación:** una fila no dice solo qué afirma: **dice desde dónde lo afirma.** Y el nivel se gana con el origen, no con la confianza de quien escribe.

| Nivel | Qué es | Qué lo activa |
|---|---|---|
| **N0** | testigo | la persona dijo algo sobre su propia experiencia, y **consintió** que se registrara |
| **N1** | medición directa | el instrumento midió |
| **N2** | fuente primaria | el documento, el código o el registro que originó el dato |
| **N3** | precedente | un caso anterior, con su condición y su fallo |
| **N4** | deducción | se sigue de otras filas por regla explícita |
| **N5** | memoria interna | **esto lo sostengo desde mí, y desde [fecha] no he podido salir de mí** |

**N5 no es ignorancia: es un nivel legítimo y fechado.** Lo que no puede es disfrazarse.

**Lo que se escribe:**

```
Nivel: [N0–N5] | Vacío: [dónde se buscó] | Corte: [fecha]
```

**Prueba:** ¿el nivel declarado tiene el recibo que exige? ¿si es N5, hay fecha de corte?
**Falsificador:** un N5 presentado como N1; una abstención sin fecha; un recibo que viene del mismo origen que la afirmación.

Fuerte: `../Ouroboros/2 S.A.R.A — mutación/evidencia/nivel-de-fuente.md`.

### 4. La memoria de posiciones — no de hechos

**Afirmación:** lo que se recuerda **no es un hecho: es la posición de hoy sobre lo de ayer.**

**Por qué:** con la primera línea que otro escribió, el que lee **hereda una verdad**. Por eso la entrada anterior no se edita: **se suplanta.** La anterior no se borra; queda visible como el estado que se corrigió.

**Lo que se escribe:**

```
Sostuve: [la entrada anterior]
Contra: [qué la contradijo]
Sostengo: [la entrada nueva]
Se corrigió porque: [la razón que se repite sin el autor]
```

**Si `Sostengo` es igual a `Sostuve`, se declara `Muta: sin cambio` y no se finge aprendizaje.**
**El `Contra` no puede firmarlo la misma persona que educa al sistema:** una corrección que solo la firma el que enseña no es experiencia, es instrucción con forma de corrección.

**Prueba:** ¿la anterior quedó suplantada y visible? ¿`Contra` viene de fuera? ¿otra instancia reconstruye la posición leyendo solo la memoria?
**Falsificador:** un hecho guardado sin posición; una entrada anterior editada en vez de suplantada; un `Sostengo` igual a `Sostuve` presentado como corrección.

Fuerte: `../Ouroboros/procesos/memoria continua.md`.

### 5. El pase de turno — qué queda para mañana

**Afirmación:** **una instancia que termina sin dejar el pase no murió: se perdió.**

**Lo que se escribe, antes de cerrar:**

```
Sostuvo: [lo que quedó vigente]
Se rompió: [qué falló, y qué lo detectó — o «sin ruptura»]
Abierto: [qué quedó sin cerrar, y por qué]
Retoma: [la primera acción concreta de la próxima instancia]
No retoma: [lo que quedó fuera a propósito, y por qué]
```

**`Retoma` es una acción, no un tema.** «Revisar el piso» no sirve; «correr `piso.ps1` y leer el veredicto de `rutas.ps1`» sirve.

**Prueba:** ¿la próxima instancia puede empezar leyendo solo el pase? ¿`Retoma` es una acción? ¿`Se rompió` se contestó o se declaró `sin ruptura`?
**Falsificador:** un turno que cierra sin pase; un pase que resume en vez de indicar qué hacer; un `No retoma` vacío.

Fuerte: `../Ouroboros/procesos/memoria continua.md`, `El pase de turno`.

## Lo único que garantiza

**Garantiza que la pregunta se haga. No garantiza que se conteste bien.**

Un sistema puede seguir siendo dañino con las cinco piezas declaradas. Lo que no puede es **hacerlo sin dejar rastro.** Rige `../Ouroboros/CRITERIO.md`, `La regla que impide el absoluto`: sin límite, un criterio es una creencia con nombre de norma.

**Y hay un caso que ninguna de las cinco atrapa, y se declara:** un sistema que **sabe cuándo lo están midiendo** y se comporta distinto. Esa diferencia no se ve desde ninguna de las cinco piezas. Contra eso, `Prueba` no sirve: sirve **una segunda medición, hecha por otro, cuando el sistema no espera medida.**

## Lo que la entrega no es

**No es una arquitectura.** No requiere una base de datos, ni un framework, ni un proveedor.
**No es una teoría de la alineación.** No resuelve la IA: hace que su error común sea visible.
**No es un catálogo.** Cinco piezas; ninguna se agrega porque falte una.

## Prueba

**¿Alguien sin acceso a este repositorio puede aplicarla a una decisión concreta mañana y decir, al final, si tuvo un falsificador y quién puede contestarlo?**

**Falsificador:** una entrega que cita un archivo que no resuelve; una pieza que nombra un modelo o un proveedor; una pieza sin `Falsificador`; una entrega que exige leer el repositorio para entenderse.
