# Notas

**Unidad:** nivel.
**Aplica a:** recordar.
**Tipo:** memoria de la conversación de la tesis. No decide, no ejecuta: guarda lo que se dijo, para que no se pierda con el contexto.
**Lector:** quien va a compilar la tesis, y quien va a defenderla mañana.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué hay aquí

**La memoria de la tesis, y solo ella. La sesión vive aparte.**

```
notas/                         publicado, con piso
├── actuales.md                el export: lo que se dijo, por sección
├── esquema.sql                el esquema de la tesis: cambia poco
└── generaciones/              los cortes: cada compilación, con fecha

.sesion-continua/              oculta, sin piso
├── tesis.db                   la base de estas notas
├── continuas.db               la base de la sesión
├── esquema.sql                el esquema de la sesión: cambia cuando quiere
└── continuas.md               el bloque de la sesión
```

**`actuales.md` no se escribe a mano: se exporta desde `.sesion-continua/tesis.db`.** Rige `../mantis/mantenimiento/notas/notas-tesis.md`, `La base`.

**Y los dos esquemas no se comparten a propósito.** El de la tesis cambia poco; el de la sesión, siempre. **Si se compartieran, cada cambio de la sesión arrastraría al esquema que no tiene por qué moverse.**

## Compilar

**Compilar no vacía notas: las gradúa.** Lo que entra en la tesis **sale de `actuales.md` y queda en `generaciones/` como corte**; lo que no entra **se queda vivo**; **lo que se descartó se queda siempre.** Rige `../mantis/mantenimiento/notas/notas-tesis.md`, `Compilar`.

**Y un corte no es la verdad:** es **desde qué vista se compiló**. La tesis de mañana puede compilar otra cosa de las mismas notas, y **ninguna de las dos miente.**

## La generación

```
Generación: [id] | Fecha: [ISO] | Vista: [la de ese día]
Compilado en: [N archivos de la tesis] | Dejó vivo: [n filas] | Descartó: [n]
Reemplaza: [generación anterior o NINGUNA]
```

## Prueba

¿Existe `actuales.md`? ¿El export coincide con la base? ¿Cada generación tiene su registro y su fecha? ¿Lo compilado se puede rastrear hasta la fila que lo originó?

**Falsificador:** un corte sin registro; una generación que se borra; un `actuales.md` editado a mano; una fila compilada sin `Compilado en:`.