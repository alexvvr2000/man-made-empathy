# TESIS AL CERRAR EL CANDADO — el método, on demand

**Nombre.** TESIS AL CERRAR EL CANDADO. **Y el nombre es el disparador: no corre sola, corre cuando alguien cierra un candado.**

**Origen.** De la autoridad: **"implementa el método on demand"**, y de la corrección: **el nombre se quita de la duración, porque se puede leer como background infinito**, y de la pregunta que lo hizo posible: **¿y si el candado, al cerrarse, se triangula y se verbaliza para que amarre?**

**Unidad:** nivel.
**Aplica a:** componer.
**Tipo:** se cumple. **No se ejecuta sola: se pide, y se pide sobre una visión.**
**Lector:** quien va a generar una tesis desde la memoria, y quien la va a leer.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** una tesis se compone desde lo que el autor sostuvo, no desde una redacción nueva que lo interprete.
**Límite:** compone con lo que hay. **Si faltan piezas, lo dice; no las inventa.**
**Firma:** humano:autoridad · máquina:quien la pida.

**Variables:** visión · piezas · probadas · crudas · candado
**Peor:** la tesis dice más de lo que el autor sostuvo, **y el que la lee no puede saber cuál pieza tenía fuente y cuál no.**
**Quién:** el que va a citar la tesis creyendo que todo lo que dice está probado.

## Entra | Falla | Sale | Consume

- **Entra:** una visión, y las piezas de la base que la sostienen.
- **Falla si:** la visión no tiene piezas; una pieza cruda se presenta como probada; la tesis se compone sin dejar su rastro; el PDF no se abre.
- **Sale:** el `.tex` y el `.pdf` en `mantis/<visión>/entregables/`, y la entrada que cierra el candado.
- **Consume:** la autoridad, que lee el PDF.

**Prueba:** ¿se compuso desde la tabla y no a mano? ¿Las crudas van marcadas? ¿El PDF abre? ¿Quedó la entrada del cierre?
**Falsificador:** una tesis escrita a mano presentada como compuesta; una cruda en la sección de probadas; un PDF que no abre; un candado cerrado sin rastro.

## El método, en cuatro pasos

```
1. se pide        → python tesis.py --vision "vision del autor"
2. se lee         → las piezas de la tabla: clase, nombre, porqué, fuente, pregunta
3. se separa      → probadas (declaran fuente) y crudas (no la declaran)
4. se compone     → .tex, se compila con Tectonic, y queda el PDF
```

**Y el paso que lo vuelve repetible:** **el candado se cierra con una entrada en la memoria, con sus números.** **La siguiente vez no se empieza de cero: se compone con lo que la anterior dejó. Y si nadie cerró un candado, no hay siguiente.**

## Las crudas no se callan

**Una tesis que presenta una pieza cruda como probada es lo que la academia hace y aquí no se hace.**

**Por eso existe el apéndice `Lo que quedó crudo`:** **las piezas están, con su nombre, y con la regla dicha:** **mientras no se citen o se triangulen, no se entregan como fuente.**

**Y eso es lo que rompe el sistema:** **la tesis no se ve más débil por declarar lo que le falta; se ve más fuerte, porque no hay nada que esconder.**

## Lo que este método no hace

**No redacta.** **Compone con lo que el autor sostuvo, en el orden en que lo sostuvo.**

**No inventa la visión que falta.** **Si una visión no tiene piezas en la base, se declara `[VACÍO - SIN TESIS]` y no se compone un título.**

**No sustituye al candado.** **El candado es la tesis corta, escrita por el autor. Esto compone su versión larga desde la memoria.**

## Transiciones

- La visión tiene piezas → se compone, y el candado cierra con su rastro.
- La visión no tiene piezas → `[VACÍO - SIN TESIS]`, y se dice qué falta.
- Hay crudas → se componen en el apéndice, marcadas.
- No hay Tectonic → `.tex` y no PDF, y se declara: sin PDF no hay entregable.


