# Mutación

**Unidad:** proceso.
**Aplica a:** mutar.
**Tipo:** estándar de mutación. No decide, no ejecuta: dice qué forma tiene un cambio para que siga siendo el mismo ente.
**Lector:** quien va a cambiar un ente, un proceso o un paso.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

**Mutar es transformar desde un punto de referencia.** Incluye agregar, modificar y eliminar; **eliminar también es mutación.**

**Y lo que muta no es el contenido solo: es el nombre y el lugar.** Si el nombre sobrevive al cambio, **no hubo mutación: hubo edición.** Un nombre viejo sobre un cuerpo nuevo es una etiqueta que miente, y la etiqueta es lo único que el lector tiene para orientarse.

**La forma se lee como nombre propio; la expansión dice qué significa.** Un acrónimo que solo se puede leer deletreando **no es un nombre: es una etiqueta.**

## Qué muta en un ente

| Pieza | Qué cambia | Qué no cambia |
|---|---|---|
| **Rastro** | casi nunca: el cuerpo no cambia sin cambiar de especie | qué hay, qué no se toca y cómo se verifica |
| **Ruta** | siempre: si el hoy cambia y la Ruta no, enruta lo de ayer | que enruta |
| **Carga** | cuando el fin cambia; si el fin deja de existir, no se muta: se retira | que declara la pérdida |

**Un ente que conserva nombre de carpeta después de mutar no mutó: se editó.** Una sub-tarea que cambia y conserva su carpeta es el mismo caso.

## Sin herencia

**El reemplazo no hereda forma, nombre ni estructura del anterior.** Si el nuevo se parece al viejo, es coincidencia, no requisito.

**Sin crecimiento obligatorio.** El conjunto puede encogerse: quitar una pieza es mutación, y no se compensa agregando otra.

```
Serie: [conjunto] | Antes: [n piezas] | Después: [n piezas] | Quita: [...] | Pone: [...] | Reordena: [ninguno|qué]
```

## El nombre muta con la cosa

```
Lugar: [carpeta nueva o NINGUNO] | Reemplaza: [nombre anterior o NINGUNA]
```

**`Reemplaza:` apunta al nombre anterior.** El anterior no se borra: **se sustituye, y la razón se declara.** Sin `Reemplaza:` no hay cadena, y un nombre nuevo sin cadena no se distingue de un invento.

**Sin cambio, no hay acuñación fingida.** Lo que no cambió acuña igual, pero su `Muta:` declara el estado: *«sin cambio»*. Lo que no se permite es acuñar como si hubiera pasado algo.

**Un nombre que sirve para dos versiones distintas no nombra nada.**

## El nombre lo pone el sistema, no la autoridad

**La autoridad no nombra. Nombra el sistema, y la autoridad lo acepta o lo cambia.**

**Por qué, y es una razón de carga:** el trabajo de la autoridad es **el mecanismo** —qué se rompe, qué se conserva, por qué—. Elegir un acrónimo es trabajo de forma, y la forma la puede resolver el sistema sin gastar el criterio de la autoridad. **Una autoridad que nombra todo se queda sin cabeza para lo que solo ella puede decidir.**

**Regla:**

1. **El sistema propone un nombre de una sola palabra, con expansión.** Se lee como nombre propio; la expansión dice qué hace.
2. **Suena como un nombre de agente humano:** JARVIS, FRIDAY. Corto, pronunciable, y **no tiene que explicarse.**
3. **La expansión tiene que ser 100 % irrefutable:** cada letra nombra algo que el proceso hace, y **ninguna es de relleno.** Si una letra hay que forzarla, el nombre no sirve.
4. **El nombre propuesto no se discute por gusto.** Se acepta o se reemplaza por otro de la misma forma. **Lo que la autoridad decide es el mecanismo; lo que el sistema resuelve es la etiqueta.**
5. **El nombre de cariño no sustituye al real.** Un apodo se puede usar entre iguales; **el nombre que queda escrito en el archivo es el que el sistema propuso y la autoridad aceptó.**
6. **Se pronuncia igual en humano y en máquina.** El nombre tiene que poder decirse en voz alta, leerse en pantalla y salir de un sintetizador **sin que cambie.** Si hace falta explicar cómo se dice, no es un nombre: es una contraseña.

**La condición 6 no es estética: es operativa.** Un nombre que una máquina pronuncia mal **no se puede cargar por voz, no se puede dictar y no se puede buscar.** Un nombre que el humano no puede decir **no se usa en la conversación, y un nombre que no se usa no se recuerda.**

| Se pronuncia | No se pronuncia |
|---|---|
| **VIDERE** — vi-de-re, igual en cualquier voz | `X Æ A-12` — se lee de tres formas y ninguna es la misma |
| **FRIDAY** — fri-dei | `J4rv1s` — un sintetizador lo deletrea |
| **MARVIN** — mar-vin | `#` y cualquier símbolo: no se dice en voz alta |

**Prueba:** ¿el nombre se dice en voz alta sin deletrearlo? ¿un sintetizador lo devuelve igual? ¿se puede dictar como palabra y no letra por letra?
**Falsificador:** un nombre con símbolos o con letras por números; un nombre cuya pronunciación cambia entre humano y máquina; un nombre que se dicta letra por letra; un nombre que necesita un instructivo de pronunciación.

```
Nombre: [una palabra] | Expansión: [qué hace, letra por letra] | Suena: [cómo se lee]
Irrefutable: [qué hace cada letra, sin relleno] | Se pronuncia: [igual en humano y en máquina]
Acepta: [la autoridad] | Reemplaza: [el anterior o NINGUNO]
```

**Prueba:** ¿el nombre es una palabra y se lee sin explicación? ¿cada letra de la expansión nombra algo que el proceso hace? ¿alguna letra existe solo para completar la palabra? ¿lo dice igual un humano y una máquina?
**Falsificador:** un acrónimo que solo se puede leer deletreando; una expansión con una letra de relleno; un nombre que la autoridad tuvo que inventar; un apodo presentado como nombre; un nombre con símbolos o cuya pronunciación cambia entre humano y máquina.

## El estándar de cambio

**Un cambio se declara por lo que mueve, no por su tamaño.** Tres clases, y **cada una se aplica distinto:**

| Clase | Qué mueve | Qué se declara | Quién lo acepta |
|---|---|---|---|
| **Edición** | el texto de una pieza, sin mover su nombre ni su lugar | la línea que cambia, y qué conserva | quien edita |
| **Mutación** | la pieza, conservando nivel y fin | `Muta:`, `Conserva:`, `Reemplaza:`, y su prueba | la autoridad |
| **Promoción de nivel** | la pieza **cambia de nivel**: deja de ser lo que era y otra cosa lo porta | `Lugar:`, `Reemplaza:`, **qué mecanismo se traslada, y qué se deja**, y su prueba | la autoridad |

**La tercera es la que no se documentaba.** Una pieza que cambia de nivel **no se muta en el mismo sitio: su mecanismo se traslada a otro, y lo que lo recibe se llama distinto porque ya no es la misma cosa.**

**Y el mecanismo trasladado no hereda el nombre.** El que lo recibe **toma lo que sirve y deja lo que no**; si se pareciera entero al anterior, **sería el anterior con otro nombre.**

```
Promoción: [de dónde] → [a dónde] | Se traslada: [el mecanismo] | Se deja: [qué no pasa]
Reemplaza: [nombre anterior o NINGUNA] | Prueba: [qué se corrió] | Autoridad: [quién]
```

**Prueba de una promoción:** ¿el mecanismo sirve en su casa nueva sin la vieja cerrada? ¿lo que se dejó está declarado? ¿el nombre viejo desapareció del lugar nuevo?
**Falsificador:** una promoción que se presenta como edición; un mecanismo trasladado que conserva el nombre viejo; lo que se dejó sin declarar; un nombre nuevo sin `Reemplaza:`.

## Lo que no cambia

**El fin no muta al mismo ritmo que el proceso.** Un proceso puede reemplazarse entero y el fin seguir siendo el mismo. **Si el fin cambia, no es mutación de la serie: es una mutación del fin, y se declara como tal.**

```
Fin: [qué se persigue] | Cambia: [sí|no] | Si cambia: [por qué]
```

## Entra | Falla | Sale | Consume

**Variables:** pieza · nombre · lugar · fin · reemplazo
**Peor:** el cambio se llama mutación y conserva el nombre anterior: el lector cree que lee lo de antes y lee otra cosa.
**Quién:** quien va a usar la pieza, y quien la va a mutar después.

- **Entra:** la pieza y el cambio que se quiere hacer.
- **Falla si:** el cambio no declara qué conserva, o no deja rastro, o conserva el nombre del anterior.
- **Sale:** la pieza transformada, completa, con `Muta:`, `Conserva:`, `Ausencias:` y `Reemplaza:`.
- **Consume:** quien va a usar la pieza transformada, y la autoridad que lo acepta.

```
Acta: [id] | Nombre: [nombre] | Expansión: [significado] | Fecha: [ISO]
Muta: [qué cambia] | Conserva: [qué no] | Ausencias: [qué no tiene] | Reemplaza: [nombre anterior o NINGUNA]
Lugar: [carpeta nueva o NINGUNO] | Autoridad: [tipo:nombre] | Cierra en: [tipo:nombre]
```

**Prueba:** ¿la mutación acuñó nombre? ¿`Reemplaza:` apunta al anterior? ¿Se declaró qué conserva? ¿Si cambió de nivel, cambió de carpeta?

**Falsificador:** una edición presentada como mutación; una acuñación sin `Reemplaza:`; una pieza que muta y conserva su nombre; un cambio que no declara qué conserva; un conjunto que solo crece.

## Transiciones

- El fin dejó de existir y no entra nada en su lugar → se retira, con su registro.
- La pieza cambia de nivel → cambia de carpeta y se declara.
- En cualquier otro caso → se entrega la pieza completa y se cierra.
