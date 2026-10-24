# ACERO — cuándo algo se sostiene

**Unidad:** nivel.
**Aplica a:** dar el grado de lo que aguantó.
**Tipo:** estándar. No se ejecuta: se cumple. Dice **cuándo algo es ACERO**, y cuándo deja de serlo.
**Lector:** quien va a decir si un agente o un sistema sirve, y quien va a usarlo confiando en que sirve.
**Dueño:** la autoridad.
**Estado:** vigente.

**Nombre.** ACERO. **Expansión:** **el grado de lo que resistió sin que nadie lo defendiera.**
**Origen.** Restituido desde `Ouroboros/procesos/medir-acero.md`, commit `04d6771`, donde ya existía. Se perdió con la limpieza `45ce43c`.
**Sesgo:** se sostiene desde `./criterio.md`: **ACERO es el veredicto que se emite sobre lo que aguantó, y no sobre lo que se escribió.**
**Límite:** no se aplica a lo que nunca fue contestado. **Sin nadie que lo haya intentado mover, hay vacío, no acero.**
**Firma:** humano:autoridad · máquina:quien mida.

## Qué forma fija

**Que un sistema se declare ACERO por lo que resistió, no por lo que promete.**

> **ACERO es la fricción aplicada al cierre.**

**Un sistema puede tener las normas, los tests, los estándares y el formato, y no aguantar nada.** **ACERO no premia tener: premia resistir.**

## Las dos condiciones, y ninguna basta sola

**Y esto resuelve una tensión que este estándar tenía sin declarar.** **"Un ente que hace una sola tarea bien es acero" y "ACERO exige las cuatro propiedades" son dos cosas distintas, y las dos son verdad:**

| Condición | Qué mide | Qué autoriza |
|---|---|---|
| **hace una tarea bien** | la función: sirve, y se sostiene en distintos ejecutores | **ser útil** |
| **resistió que la movieran** | la forma: recibió fricción y siguió de pie, o cambió explicando por qué | **ser ACERO** |

**Una tarea hecha bien y sin contestación es una herramienta buena: no es ACERO.** **Le falta que alguien haya intentado moverla.** **Y una que recibió contestación pero ya no sirve tampoco: aguantó y se volvió inútil.**

**Ancla:** útil es que sirva; acero es que sirva después de que alguien lo intentara mover.

## Las cuatro propiedades

**Las cuatro se miden, y las cuatro son observables. Ninguna se declara por intención.**

| Propiedad | Qué se mide | Falla si |
|---|---|---|
| **Arquitectura** | niveles declarados, piezas declaradas, sin jerarquía oculta | un nivel sin declarar; una pieza que manda y no lo dice |
| **Control** | el que verifica no es el que produjo | el mismo acto produce y certifica |
| **Evidencia** | el registro tiene criterio previo, falsificador y descarte | falta alguno; el criterio se fijó después |
| **Registro** | otra instancia reconstruye lo hecho sin preguntar | la reconstrucción necesita al que produjo |

**Y `Control` no se compensa.** **Si el que produjo también certifica, la propiedad falla y el veredicto se marca `sin revisor independiente`.** **Un ACERO que solo se puede medir a ojo no es ACERO: es una opinión compartida.**

**Y `Control` no es lo mismo que el testigo de `VIDAL`.** **VIDAL mide si un agente sigue vivo; ACERO mide si lo que hizo se sostiene.** **Un sistema puede ser ACERO y su agente estar en `indeterminado`.**

## Cómo se aplica

```
1. [la tarea: qué hace, y que lo haga en dos ejecutores] → el artefacto de la tarea
2. [la función: sirve, y sigue sirviendo] → útil | no útil
3. [la fricción: quién intentó moverla, y qué pasó] → el Contra
4. [las cuatro propiedades, una por una] → sí | no, con la evidencia
5. [el veredicto] → ACERO | útil pero no ACERO | sin revisor independiente | vacío
Prohibido dar el paso 5 sin el 3: sin contestación no hay acero, hay vacío.
```

**Falla si:** una de las cuatro propiedades no se sostiene y no se declara; el sistema se certifica a sí mismo; se declara ACERO sin haber sido movido.

**Sale:** las cuatro propiedades medidas, con su evidencia, y la fricción que recibió.

`Arquitectura: [sí|no] | Control: [sí|no] | Evidencia: [n filas en error] | Registro: [sí|no] | Fricción: [quién|nadie] | ACERO: [sí|no]`

**Consume:** quien decide si el sistema se despliega.

## El chango viejo

**Y ACERO existe, en parte, para ver al que no se deja mover.** Rige `./criterio.md`, `La costumbre tiene dueño`.

> **«Chango viejo no aprende maroma nueva.»**

**El chango viejo pasa las cuatro propiedades y sigue sin ser ACERO:** **tiene arquitectura, control, evidencia y registro, y recibió fricción y no se movió.** **Cumplió todo y no aprendió.**

**ACERO lo distingue porque mide resistencia, no cumplimiento:** **al chango viejo se le cierra el paso 3, no el 4.**

## Lo que este estándar no hace

**No juzga contenido.** Un proceso con todos los campos puede no decir qué decide; eso lo dice `./criterio.md`.

**No se gana con antigüedad.** **Un sistema viejo sin contestación sigue en vacío.** El tiempo no produce acero: la fricción sí.

**No se hereda.** **Lo que fue ACERO con una mirada no lo es con otra: se vuelve a medir.**

**No certifica la verdad.** **Certifica que aguantó algo sin que nadie lo defendiera.**

## Prueba

**¿Se midieron las cuatro propiedades con evidencia?** **¿Se identificó quién intentó moverlo?** **¿El que verifica es distinto del que produjo?** **¿Ninguna propiedad se declaró por intención?** **¿Se distingue útil de ACERO?**

**Falsificador:** una propiedad declarada sin evidencia; el sistema se certifica a sí mismo; una propiedad que falla y se compensa con otra; se declara ACERO sin las cuatro; **se declara ACERO a un sistema que nunca fue contestado; se confunde útil con ACERO; un chango viejo que cumple las cuatro y se cuenta como acero.**
