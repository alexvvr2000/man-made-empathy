# Notas

**Unidad:** nivel.
**Aplica a:** recordar.
**Tipo:** memoria de la conversación. No decide, no ejecuta: guarda lo que se dijo, para que no se pierda con el contexto.
**Lector:** quien va a compilar la tesis, y quien va a defenderla mañana.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué hay aquí

**Una sola memoria, en dos capas:**

```
2 notas/
├── actuales.md            lo vivo: la conversación de hoy
└── generaciones/          los cortes: cada compilación, con fecha
```

**`actuales.md` es lo que se está diciendo.** **`generaciones/` es lo que ya se compiló**, y no se borra: **es la vista que el autor tenía ese día.**

**Compilar no vacía notas: las gradúa.** Lo que entra en la tesis **sale de `actuales.md` y queda en `generaciones/` como corte**; lo que no entra **se queda vivo**; **lo que se descartó se queda siempre.** Rige `../mantis/mantenimiento/escribir-notas.md`, `Compilar`.

**Y un corte no es la verdad:** es **desde qué vista se compiló**. La tesis de mañana puede compilar otra cosa de las mismas notas, y **ninguna de las dos miente.**

## La generación

Cada corte vive en `generaciones/[AAAAMMDD]-[nombre]/` y lleva su registro:

```
Generación: [id] | Fecha: [ISO] | Vista: [la de ese día]
Compilado en: [N archivos de la tesis] | Dejó vivo: [n filas] | Descartó: [n]
Reemplaza: [generación anterior o NINGUNA]
```

## Prueba

¿Existe `actuales.md`? ¿Cada generación tiene su registro y su fecha? ¿Lo que se compiló se puede rastrear hasta la fila que lo originó?

**Falsificador:** un corte sin registro; una generación que se borra; un `actuales.md` vaciado sin corte; una fila compilada sin `Compilado en:`.