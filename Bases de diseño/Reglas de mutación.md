# Reglas de transformación de tareas

**Unidad:** tarea.
**Aplica a:** mutar
**Tipo:** reglas. Se aplican, no se ejecutan.
**Alcance:** toda transformación de una tarea desde un estado inicial.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

Mutar es cambiar una tarea desde un estado inicial sin borrar el origen ni al responsable. La forma se arma y se desarma; volver es otra mutación.

## 1. Origen

**Enunciado:** toda mutación declara el estado inicial y el marco de origen: qué es la tarea desde el principio. Sin origen no hay mutación: hay reemplazo.
**Prueba:** ¿se puede decir de dónde viene el cambio?
**Falsificador:** un cambio sin estado inicial ni origen.

## 2. Cambio declarado

**Enunciado:** antes de mutar, se declara qué cambia, qué se conserva y qué se elimina. Lo no declarado se conserva.
**Prueba:** ¿el registro distingue cambio, conservación y eliminación?
**Falsificador:** un cambio que no declara qué tocó.

## 3. Trazabilidad

**Enunciado:** toda mutación deja el rastro necesario para reconstruir el cambio y al responsable, no solo la tarea. Si otro no puede reconstruirlo sin el mutador, no es mutación trazable.
**Prueba:** ¿otro lee el registro y reconstruye el cambio y el responsable?
**Falsificador:** una mutación que solo el mutador puede contar.

## 4. Libertad controlada

**Enunciado:** la autoridad muta el marco; el ejecutor muta su estado de tarea dentro del perímetro. Para tocar el marco de origen, el ejecutor pregunta y declara el estado actual, el cambio y el beneficio; sin esa captura no hay autorización. La buena intención no es autorización.
**Prueba:** ¿el ejecutor preguntó antes de tocar el marco? ¿La pregunta capturó estado, cambio y beneficio?
**Falsificador:** un ejecutor que cambia el marco sin preguntar, aunque el cambio sea bueno.

## 5. Retorno

**Enunciado:** mutar de regreso no está prohibido: es otra mutación. Se declara la clase `reversible | compensable | irreversible` como información, no como prohibición. La acción persistente irreversible se rige por `./Principios para alineación de tareas/Autonomo.md`.
**Prueba:** ¿la clase y el retorno están declarados?
**Falsificador:** una mutación irreversible sin autoridad; una mutación de regreso sin registro.

## 6. Prueba

**Enunciado:** la mutación se prueba con reconstrucción independiente: otro lee el registro y reconstruye el cambio y el responsable. Sin eso, no entra.
**Prueba:** la Prueba de Rendición sobre el registro.
**Falsificador:** un registro que necesita al mutador para tener sentido.

## 7. Creación

**Enunciado:** crear un artefacto es una mutación: declara origen, acta y prueba. Si el artefacto puede actuar por su cuenta, es un subproceso: además pasa por el `Ciclo` y por la hard rule 8.

**Prueba:** ¿el artefacto tiene acta? ¿Si actúa, tiene `Ciclo` y autoridad?
**Falsificador:** se crea sin acta; actúa sin `Ciclo`; se duplica sin autoridad.

## Acta de creación

La forma del artefacto nuevo. No es implementación: es el registro que la implementación produce.

```
Acta: [id] | Nombre: [nombre] | Expansión: [significado] | Origen: [fuente|predecesor|ejecutor:<id>] | Fecha: [ISO]
Encargo: [frase exacta] | Fin: [estado observable]
Muta: [qué cambia] | Conserva: [qué no] | Ausencias: [qué no tiene] | Prueba: [corrida|no corrida|pendiente]
Autoridad: [tipo:nombre] | Cierra en: [tipo:nombre] | Reemplaza: [id o NINGUNA]
```

- **Nombre y expansión.** El nombre se lee como nombre propio; la expansión dice qué significa.
- **Origen.** Fuente, predecesor o ejecutor; sin origen no hay creación.
- **Encargo y fin.** La frase exacta y el estado observable; no se interpreta.
- **Muta y conserva.** Lo no declarado se conserva.
- **Ausencias.** Lo que no tiene se declara; no se simula.
- **Prueba.** Corrida, no corrida o pendiente; la no corrida se declara.
- **Autoridad y costo.** Quién autoriza y quién asume el costo.

El subproceso la cita en su `Crear`; no la absorbe.

**Prueba:** ¿el acta declara nombre, origen, encargo, mutado, conservado, ausencias y prueba?
**Falsificador:** se crea sin acta; el acta no declara ausencias; la prueba se declara corrida sin recibo.

## Ancla

Se emite antes de mutar; el registro se completa después.

`Origen: [...] | Antes: [...] | Cambia: [...] | Conserva: [...] | Después: [...] | Responsable: [...] | Autorización: [sí|no|no aplica] | Clase: [reversible|compensable|irreversible]`
