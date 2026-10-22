# Estándar de Derrotero

**Tipo:** estándar. No decide ni ejecuta; describe qué es un Derrotero completo.
**Aplica a:** enrutar cualquier tarea.
**Nivel:** 3 de 3. Se lee; no se ejecuta.
**Nivel de corpus:** estándar. Obligatorio: sin él no hay enrutamiento.
**Lector:** autoridad y ejecutor.
**Alcance:** todo enrutamiento. La tarea se describe por su entrada, su falla, su salida y su consumidor; no por quién la ejecuta.
**Dueño:** la autoridad.
**Estado:** vigente.

## 1. Qué es

Un Derrotero es la función de entrada de un agente. Recibe una petición y la convierte en una lectura de sistema con su proceso, o declara que la petición es información o vacío. No ejecuta, no decide, no contiene el proceso: enruta y obliga a leer el sistema.

Un Derrotero completo declara: identidad, campos de enrutamiento, sistema, rutas, vacío y lectura. Sin una de esas partes, no está completo.

## 1.1 La carta y el derrotero son dos piezas

Un **derrotero** dice qué ruta se toma hoy, y muta. Una **carta** dice qué hay, qué no se toca y cómo se verifica, y es lo que cada era carga por obligación.

`AGENTS.md` es la carta de esta era: se llama así porque lo leen las herramientas de hoy, no porque el nombre sea suyo.

El estándar de las dos es este documento. Un derrotero sin carta no se puede leer; una carta sin derrotero no sabe a dónde ir. **La carta no es un derrotero con otro nombre:** el derrotero enruta una petición; la carta dice cómo se lee el derrotero.

**Prueba:** ¿la era declara cuál es su carta y dónde vive? **Falsificador:** una carta que no dice cómo se lee el derrotero; una era sin carta declarada.

## 2. Identidad

El Derrotero declara quién es el agente y cuál es su tarea. La identidad es funcional: un nombre y una tarea, no una persona. Sin identidad, el Derrotero no tiene sujeto; sin tarea, no tiene fin.

**Prueba:** ¿dice quién y para qué? **Falsificador:** un Derrotero sin agente o sin tarea.

## 3. Declaración

El Derrotero declara los campos que necesita para enrutar:

- **Tipo:** disparador. Máquina primero. Solo las filas que coinciden se cargan; el resto no.
- **Alcance:** qué artefactos cubre.
- **Base:** el repo o biblioteca que referencia; no lo copia.
- **Forma:** el estándar que implementa.
- **Cuerpo:** los procesos principales que referencia, en cualquier nivel.
- **Nivel:** en cuál de los tres niveles enruta: produce, ejecuta o lee.
- **Ley:** la ley del agente, sus tareas.
- **Consecuencia:** qué pasa cuando una fila coincide y cuando no.
- **Disparador:** apunta, no contiene; declara los invariantes que prohíben la copia.

Cada campo declara una relación; ninguno contiene el proceso. Sin los campos, la ruta no se puede seguir.

**Prueba:** ¿cada campo nombra una relación? ¿Falta alguno? **Falsificador:** un campo que contiene el proceso; un campo ausente.

## 4. Sistema

Antes de resolver, el Derrotero exige la lectura de sistema: `Sistema: [propósito | frontera | retorno | consecuencia]`. Sin ella, la petición es información; no se ejecuta. La forma completa y sus dueños viven en `punto-de-partida/evaluacion/vigilar-tendencias.md`; el Derrotero la exige, no la define.

**Prueba:** ¿la resolución declara el sistema? **Falsificador:** una tarea resuelta sin sistema.

## 5. Rutas

Cada ruta declara cuatro cosas:

- **Condición:** cuándo se carga (la tarea o el caso).
- **Proceso:** a dónde se carga (documento, archivo, registro).
- **Nivel:** en cuál de los tres niveles cae el proceso cargado: produce, ejecuta o lee.
- **Consecuencia:** qué pasa si no se cumple.

La ruta apunta al proceso vivo; no lo copia. Si el proceso cambia, la ruta sigue. Una ruta que no cambia lo que se carga sobra.

**Prueba:** ¿declara condición, proceso, nivel y consecuencia? ¿El proceso existe? **Falsificador:** una ruta sin proceso; una ruta sin nivel; una ruta que copia el proceso; una ruta que no cambia la carga.

## 6. Vacío

La tarea sin ruta se declara `[VACÍO - SIN RUTA]`; la tarea sin proceso, `[VACÍO - SIN PROCESO]`. El vacío no se rellena con narrativa ni se improvisa.

**Prueba:** ¿el vacío se declara? **Falsificador:** un proceso inventado; un vacío implícito.

## 7. Lectura

El Derrotero cierra con su regla de lectura: una petición que toca la base sin `Sistema` se declara `[VACÍO - SIN LECTURA]`; sin `Piso` no se abre; sin `Vista` no se decide; sin `Prueba` ni `Cierre` no se devuelve el control.

**Prueba:** ¿la regla está declarada? **Falsificador:** una resolución sin la regla.

## 8. Invariantes

1. **Sistema, no información.** Una petición que toca el sistema no se responde como dato: se lee como sistema antes de resolver. Si no se puede leer, es información o vacío; no se ejecuta.
2. **Sin ruta no hay ejecución.** La petición que no resuelve a una tarea es información; no se ejecuta.
3. **Toda tarea tiene proceso o vacío.** No se improvisa un proceso; la ausencia se declara.
4. **La ruta apunta, no copia.** El proceso es uno y vivo; si cambia, la ruta sigue. Una copia del proceso no es ruta.
5. **El Derrotero no contiene el proceso.** No contiene reglas, ejemplos, manuales ni el cuerpo del proceso; solo la ruta y la consecuencia.
6. **Una entrada vigente por ámbito.** Lo anidado no enruta salvo que se cargue por una ruta de la entrada vigente.
7. **La ruta es observable.** Se puede seguir y produce el proceso; si no se puede seguir, no es ruta.
8. **El Derrotero pertenece a su ámbito.** El repo no depende del agente; el agente referencia al repo; la puerta es la única referencia del repo al agente.
9. **La ruta que no cambia la carga sobra.** La que no se puede probar no entra.

## 9. Conformidad

Una instancia es conforme si:

- declara identidad y tarea;
- declara los campos de enrutamiento;
- exige la lectura de sistema;
- cada ruta declara condición, proceso, nivel y consecuencia;
- una tarea sin ruta produce `[VACÍO - SIN RUTA]`;
- una tarea sin proceso produce `[VACÍO - SIN PROCESO]`;
- declara su regla de lectura;
- la instancia se lee sin el agente y sin la implementación.

## 10. Falsificadores

- Una instancia sin identidad o sin tarea.
- Un campo de enrutamiento ausente.
- Una tarea resuelta sin lectura de sistema.
- Una ruta sin proceso, sin nivel, o que copia el proceso.
- Una tarea sin ruta que se ejecuta.
- Un proceso improvisado.
- Una ruta que no cambia lo que se carga.
- Una entrada que necesita al agente para leerse.
- Una tarea que no puede declarar su vacío.
- Una instancia sin regla de lectura.

## 11. Implementación

No es normativa. Un Derrotero puede ser una tabla, un archivo, un registro o un mapa. La tabla `Si pasa | Carga | Si no` es una forma; la `Tarea | Proceso` es otra. Cada instancia declara sus valores.

**Prueba:** una instancia limpia sigue una petición por su ruta y produce el proceso, o declara el vacío.
