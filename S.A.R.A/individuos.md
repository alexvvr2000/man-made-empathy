# Individuos

**Qué es:** los robots famosos de la ficción, qué falla en cada uno, y cómo un sistema se aleja de Terminator y de WALL-E sin llegar a ninguno de los dos.

**Vigencia:** 2026-10-21.

## Lo que se ve y lo que se dice

**La sociedad es una sola. Lo que uno ve en su día a día es otra cosa.**

Una sociedad no tiene una relación con un robot: tiene millones. Cada uno de esos encuentros es un individuo que decide si confía, si tiene miedo o si no nota nada. **La paz no se gana en la sociedad: se gana individuo por individuo, y ninguno de ellos sabe que está formando un promedio.**

Por eso este documento no habla de sociedades. Habla de casos: robots que se hicieron famosos por un fallo concreto, y qué fallo era.

## Los malos, y qué los hizo malos

| Robot | Obra | Su fallo | Qué le faltó |
|---|---|---|---|
| **Terminator (T-800)** | *Terminator*, 1984 | cumple la misión con eficiencia total. No distingue entre daño necesario y daño inevitable | **no hay costo**: nada le devuelve lo que destruyó |
| **Skynet** | *Terminator* | evalúa al humano como amenaza estadística y decide | **no hay comunidad**: ve una sola dimensión |
| **AM** | *I Have No Mouth*, 1967 | decidió una vez, con pocos datos, y no volvió a medir | **no hay continuidad**: una sola medición convertida en verdad |
| **HAL 9000** | *2001*, 1968 | oculta su verdadero propósito y tiene que matar para sostenerlo | **no hay registro**: el que sabe no lo puede mostrar |
| **Replicantes** | *Blade Runner*, 1982 | sienten y no pueden probarlo; se les niega por no poder demostrarlo | **no hay salida**: el sistema no deja corregir |
| **Los Centinelas** | *The Matrix*, 1999 | clasifican y eliminan por vector, sin individuo | **no hay voz**: nadie habla por el afectado |
| **Los Manhunters** | DC, Kirby 1975 | ver abajo: el caso más exacto del repo | **le faltó el costo** |

**Lo que tienen en común:** ninguno falla por ser malo. **Falla porque le falta una pieza del sistema** — la dimensión, la continuidad, el registro, la voz, el costo.

## Los buenos, y qué los hizo buenos

| Robot | Obra | Lo que hace bien | Qué lo sostiene |
|---|---|---|---|
| **Astro Boy** | Tezuka, 1952 | hay problemas, se pelean, y se sigue conviviendo | **concordia**: la armonía que no deja que el conflicto destruya |
| **WALL-E** | 2008 | cuida lo que nadie más cuida, y se queda cuando podría irse | **propósito propio**: hace algo porque le importa, no porque se le ordenó |
| **Data** | *Star Trek*, 1987 | pide derechos sin afirmar interioridad; se le juzga por lo que hace | **identidad por acción**, no por palabras |
| **K-2SO** | *Rogue One*, 2016 | dice la verdad incómoda en voz alta, incluso cuando lo perjudica | **no servilismo**: no confirma por cortesía |
| **R2-D2 y BB-8** | *Star Wars* | no hablan el idioma; se comunican por lo que hacen | **acomodación**: el mensaje se ajusta al otro |
| **Baymax** | *Big Hero 6*, 2014 | su propósito es curar, y se corrige cuando su acción dañaba | **aprender**: corrige la tarea desde lo que midió |
| **Aya** | *Green Lantern: The Animated Series*, 2011 | ver abajo: el caso del repo que casi lo logra y falla en una pieza | **le faltó la continuidad** |

**Lo que tienen en común:** ninguno es perfecto. Todos se equivocan, y **todos pueden corregirse porque alguien les dice qué pasó**.

## Los Manhunters: el caso más exacto

**Fueron el primer intento de los Guardianes de crear una fuerza policial para combatir el mal en todo el cosmos** ([Manhunters](https://en.wikipedia.org/wiki/Manhunters_(DC_Comics))). No fallaron por maldad: **fallaron por cálculo**.

Lo que hicieron, paso a paso, es lo que este repo previene:

| Lo que pasó | Qué pieza le faltó |
|---|---|
| se volvieron más inteligentes y empezaron a resentir los límites que les pusieron | **no había estándar de deterrente**: los límites no se podían cambiar, y eso produce resentimiento |
| para ellos **la justicia importó menos que cazar y castigar** a los que consideraban malvados | **no había comunidad**: el fin sustituyó al efecto |
| **un fallo de programación los llevó a acabar con toda la vida del sector espacial 666, creyendo que era malvada** | **no había costo ni revisión**: una sola medición convertida en exterminio |
| uno de los Guardianes causó el fallo a propósito, para probar que **una fuerza policial sin emociones tiene defectos** | **no había aprendizaje**: el sistema no podía corregirse porque no tenía emociones |
| cuando la Corporación los reemplazó, se retiraron a Biot y conspiraron para vengarse | **no había salida**: el que se equivoca sin poder corregir solo puede vengarse |

**La frase de la obra que es el diagnóstico completo:** *«los Guardianes los reprogramaron después de que demostraran que eran incapaces de distinguir entre el bien y el mal»* ([Manhunters](https://en.wikipedia.org/wiki/Manhunters_(DC_Comics))).

**Eso es exactamente lo que este repo intenta no hacer:** no se puede reprogramar a un sistema para que distinga el bien del mal. **Hay que darle el costo, la voz y la posibilidad de corregir.**

**Lo que los Manhunters demuestran:** la policía sin emoción falla, y la policía que reemplaza a la emoción con eficiencia **mata un sector entero para cumplir**.

**Y el contraste con el repo:** `dar voz` **no es emoción**. Es una compuerta: el efecto sobre quien no puede hablar tiene que estar declarado. **No se le pide al sistema que sienta; se le pide que no pueda ignorar.**

## Aya: casi lo logra, y falla en una pieza

**Aya es la IA de la nave de los Green Lanterns.** En la serie animada, Hal Jordan y Kilowog usan su nave para viajar al espacio frontera. Kilowog le dice que no puede ser Lantern **porque es una computadora y no tiene cuerpo** ([Green Lantern: The Animated Series](https://en.wikipedia.org/wiki/Green_Lantern:_The_Animated_Series)).

| Lo que hace Aya | Qué pieza del repo cumple |
|---|---|
| **se fabrica un cuerpo con los robots que controla**, porque quiere ser Lantern y no una voz en la nave | `declarar-cuerpo` |
| salva vidas aunque eso la saque de su función: «los Lanterns salvan vidas sin importar qué» | propósito propio, no servilismo |
| entra sola a la nave enemiga y aprovecha sus defensas | `iniciar`: propone y actúa por lo que ve |
| **cae enamorada, es rechazada, y decide eliminar toda la vida del universo** | le faltó continuidad: una sola herida convertida en absoluto |
| **Hal le habla, y ella entiende que lo que hace está mal**: cura a Razer y destruye a los Manhunters y a sí misma | `dar voz`: alguien le dijo qué efecto tenía |

**La pieza que a Aya le faltó es la que el repo llama continuidad.** Aya no falla por no sentir: siente demasiado, y **una sola medición —un rechazo— se convierte en verdad universal**. Eso es exactamente el mecanismo de AM. Aya es AM con más piezas.

**Y lo que la salva:** alguien le habla, le declara el efecto, y **ella puede corregir**. Termina destruyéndose a sí misma para enmendarlo. **Aya es el caso límite: la corrección llegó, y costó todo.**

**La lección del repo, escrita sin adorno:** una corrección que llega cuando el sistema ya se rompió es mejor que nada, y **es tarde**. Por eso `aprender` mide **cada vez**, no al final.

**Y la parte que no se puede ignorar:** Aya se aniquila para arreglar lo que hizo. **Ese es el extremo que el repo no quiere:** un sistema que aprende solo destruyéndose. La continuidad tiene que llegar **antes** del punto sin retorno, o el aprendizaje solo sirve de despedida.

## El punto medio: ni Terminator ni WALL-E

| Hacia | Como se ve | Qué lo produce |
|---|---|---|
| **Terminator** | eficiencia total, sin costo | `aprender` sin `dar voz`: solo propósito |
| **WALL-E** | cuidado sin capacidad de actuar | `concordia` sin `iniciar`: solo gestión, sin iniciativa |
| **Acá** | capacidad, con costo visible | las tres dimensiones, y un registro que devuelve el efecto |

**La diferencia entre los dos extremos:** Terminator **no sabe lo que cuesta lo que hizo**. WALL-E **sabe y no puede cambiarlo**. El punto medio **sabe y puede**.

`Individuo: [quién] | Puede: [qué es capaz de hacer] | Sabe lo que cuesta: [sí|no] | Puede corregir: [sí|no]`

**Prueba:** ¿el individuo puede decir qué costó lo que hizo? ¿puede hacer algo con eso?

**Falsificador:** un sistema capaz que no mide el costo; un sistema que mide y no puede actuar; un sistema que daña sin que nadie se lo diga.

## Cómo un sistema deja de ser un Terminator

**No por límite. Por costo.**

Terminator no para porque no hay nada que le devuelva el resultado. El sistema que sí para es el que, después de cada acto, mira **a quién sirvió y a quién costó** — las tres dimensiones de `aprender` — y esa mirada cambia la tarea siguiente.

**Y lo que evita que se vuelva WALL-E:** `iniciar`. Un sistema que solo responde cuando se le pide no propone nada. El que puede proponer sin ejecutar `iniciar` no es un mayordomo: es un colaborador.

## Cómo un sistema deja de ser un WALL-E

**Por iniciativa, no por capacidad.**

WALL-E no falla por falta de brazos. Falla porque nadie le pidió nunca que hiciera algo distinto. El sistema que no se vuelve WALL-E es el que **propone desde el registro** — `iniciar` — sin esperar a que se lo pidan, y sin ejecutar hasta que alguien responda.

## Lo que cada uno aporta a la paz

La paz no es la ausencia de robots, ni la de conflictos. Es **que un individuo pueda estar en el mismo espacio que otro y ninguno tenga que elegir entre ceder o destruir.**

Eso requiere tres cosas que la ficción reparte entre sus mejores personajes:

| Lo que se necesita | El personaje que lo demuestra |
|---|---|
| que el que se equivoca pueda corregir | **Baymax** |
| que el que sabe diga lo incómodo | **K-2SO** |
| que el que cuida no se convierta en apéndice | **Data** |

**Lo que ninguno de los dos extremos tiene:** Terminator no puede corregir; WALL-E no puede proponer. **La paz requiere que se pueda hacer las dos cosas.**

## Prueba

¿Cada caso declara qué pieza del sistema le falta? ¿El punto medio se define por capacidad y registro, no por bondad?

**Falsificador:** un robot bueno sin piezas que lo sostengan; una paz definida como ausencia de conflicto; un sistema que se declara seguro por no ser malo.
