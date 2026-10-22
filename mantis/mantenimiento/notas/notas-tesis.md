# Notas de tesis — el proceso

**Unidad:** proceso.
**Aplica a:** recordar.
**Tipo:** proceso de mantenimiento. Lo que se dice vale para la tesis: se anota en el mismo turno o el turno no está entregado.
**Lector:** quien escribe notas, y quien va a reconstruir la tesis desde ellas.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** dicho · pieza · tipo · sostenido · vista · contexto
**Peor:** el contexto se llena y lo dicho se pierde: la tesis se reconstruye de memoria, y lo que se recuerda es lo último dicho, no lo que se pensó.
**Quién:** quien escribe, y quien va a defender la tesis mañana con menos contexto del que había hoy.

## Entra | Falla | Sale | Consume

- **Entra:** lo que se dijo —una analogía, una cita, una decisión, un descarte— y la pieza del sistema que ilumina.
- **Falla si:** la decisión se tomó y no se anotó; la fila no nombra su pieza; la nota se toma como verdad sin declarar desde qué vista se escribió.
- **Sale:** la fila en `notas/actuales.md`, con su pieza, su tipo y su vista, más lo que se purgó de `.contexto/`.
- **Consume:** quien va a reconstruir la tesis, y quien va a defenderla.

## La vista muta

**El conocimiento muta.** Hoy hay una vista y mañana hay otra, y **la tesis tiene que poder reflejar eso sin romperse.** Por eso **cada fila declara desde qué vista se escribió.**

**Una nota no es una verdad: es una vista con fecha.** Lo que hoy se cree se anota como se cree; **si mañana cambia, la fila vieja no se edita: se agrega la nueva con su `Vista` y la vieja queda con `Estado: cubierto` o `descartado`.** Rige `../../../Ouroboros/procesos/integridad.md`, `El triángulo`: el sesgo se declara, no se corrige.

**La ficción y la analogía son material, no ruido.** Se usan para hacer la tesis digerible, y la nota guarda **de dónde sale la idea y hacia dónde se cruza.** Rige `../../../AGENTS.md`, `La tesis`.

## La base

**La memoria vive en una base SQLite, y el .md es su export.** La base es el acelerador; lo publicado es la fuente.

`
.db/notas.db          la base, oculta y en gitignore
notas/esquema.sql     el esquema compartido: fila, sesion, generacion, prueba, seccion
notas/actuales.md     el export, publicado
`

**Las cuatro tablas, y qué guarda cada una:**

| Tabla | Qué guarda |
|---|---|
| ila | lo que se dijo: sección, dicho, pieza, tipo, sostenido, estado, vista, compilado |
| sesion | un solo bloque vivo; se sustituye en el sitio |
| generacion | cada compilación, con su vista y qué dejó vivo |
| prueba | las cuatro pruebas y su corrida |
| seccion | el orden en que se leen las secciones |

**No se escribe con INSERT a mano: se anota con notar.ps1, que valida contra el esquema.**

`
pwsh -File mantis/piso/anotar.ps1 -Seccion "La vista" -Dicho "..." -Pieza "..." -Tipo frase -Sostenido frontera
pwsh -File mantis/piso/anotar.ps1 -Sesion -Estado "piso.ps1 pasa"
pwsh -File mantis/piso/exportar.ps1
`

**Y 
otas.ps1 verifica que la base y el export digan lo mismo.** Sin la base, el export es una copia a mano; sin el export, la base es un binario que nadie lee.

## La fila

```
Dicho: [la frase, citada] | De: [qué pieza ilumina] | Tipo: [analogía|referencia|cita|frase|decisión|descarte] | Usa: [dónde se va a usar] | Sostenido: [prueba|frontera|nada] | Estado: [vivo|descartado|cubierto] | Vista: [la de hoy, con fecha o nombre]
```

**Prueba:** ¿cada frase que vale tiene su fila? ¿cada fila nombra su pieza? ¿cada fila declara su vista? ¿lo que se tomó de verdad está marcado como `Sostenido: prueba` y no como `frontera`?

**Falsificador:** una decisión sin fila; una nota sin pieza; una nota presentada como verdad sin vista; una analogía que se vuelve prueba; una vista nueva que borra la vieja en vez de declararla.

## Purga

**`.contexto/` no es la memoria.** Lo que está ahí **no se toma como verdad:** es lo que se creía con otra vista. Se lee, se anota lo que sirve en `notas/actuales.md` con su vista, y **se purga del repo.**

`Purgado: [qué] | De: [ruta] | Por qué: [qué vista lo hacía verdad] | Se anotó en: [fila de notas|nada]`

**Un bloque que se purga y no se anota, se pierde.** Rige `../../../notas/actuales.md`, `Las tesis del estándar` y `Lo que se purgó de .contexto/`.

## Compilar

**Compilar es graduar, no vaciar.** Lo que entra en la tesis **sale de notas/actuales.md y queda en notas/generaciones/ como corte**; lo que no entra **se queda vivo**; **lo que se descartó se queda siempre.**

**Y compilar usa claridad:** lo que se compila se escribe con la forma de ../../Ouroboros/1 Guantelete — primitivo/primitivos/claridad.md, y **lo que no se puede escribir con ella no se compila.** Es el filtro, no el formato.

| Al compilar | Qué pasa con la fila |
|---|---|
| entró en un archivo de la tesis | Estado: cubierto + Compilado en: [archivo] |
| no entró pero sirve | Estado: vivo, se queda |
| se descartó | se queda, siempre, con su porqué |

**Cada corte es una generación, y una generación no es la verdad:** es **desde qué vista se compiló**. La tesis de mañana puede compilar otra cosa de las mismas notas, **y ninguna de las dos miente.**

`
notas/generaciones/[AAAAMMDD]-[nombre]/
├── registro.md            la generación: fecha, vista, qué se compiló
└── …                      el corte, tal como quedó
`

`
Generación: [id] | Fecha: [ISO] | Vista: [la de ese día]
Compilado en: [N archivos de la tesis] | Dejó vivo: [n filas] | Descartó: [n]
Reemplaza: [generación anterior o NINGUNA]
`

**Compilado en: declara desde qué vista se compiló.** Sin eso, la tesis compilada se toma como definitiva y deja de ser una vista.

**Prueba:** ¿la generación tiene su registro? ¿cada fila compilada tiene Compilado en:? ¿lo que no entró sigue vivo en ctuales.md? ¿lo descartado sigue?

**Falsificador:** un corte sin registro; una generación borrada; un ctuales.md vaciado sin corte; una fila compilada sin Compilado en:; una tesis compilada sin declarar la vista.
## Pruebas: se toma en cuenta

**Lo que se prueba no va dentro de la tesis: vive en ../../Pruebas/, y se toma en cuenta cuando la tesis final se escriba.** Cada prueba mide una cosa distinta, y su resultado es material de la tesis:

| Prueba | Qué mide |
|---|---|
| prueba de rendicion.md | que el otro pueda reconstruir lo producido sin el que lo produjo |
| prueba de utilidad real.md | que lo producido sirva en el uso, no en el papel |
| prueba de talento utilizable.md | que el sistema produzca algo que alguien pueda usar |
| prueba de cruce.md | que dos miradas se crucen sin fundirse |

**Al compilar, una prueba no se cita por su nombre: se cita su resultado.** Una prueba sin corrida se declara [NO CORRIDA], y no se escribe como si hubiera pasado.

**Prueba:** ¿la tesis final toma en cuenta las cuatro? ¿cada una tiene su corrida o su [NO CORRIDA]?

**Falsificador:** una prueba citada sin corrida; una prueba que se nombra y no se lee; una tesis que ignora lo que las pruebas midieron.

## Las dos referencias

**No se copian: se citan.**

- **claridad** — ../../Ouroboros/1 Guantelete — primitivo/primitivos/claridad.md. **Cada fila se lee igual en cualquier IA:** sin ambigüedad, sin glosario.
- **sesgo declarado** — ../../Ouroboros/1 Guantelete — primitivo/mutaciones/sesgo-declarado.md. **Cada fila declara su Vista:** lo que hoy se cree no se presenta como lo que siempre fue.

**Y lo que vale solo para esta sesión no va aquí: va a 
otas continuas.** Rige ./notas-continuas.md.
## Transiciones

- Un bloque de `.contexto/` sirve para la tesis → se anota en `notas.md` con su vista, y se purga.
- Un bloque de `.contexto/` ya no sirve → se purga y se anota el descarte.
- La vista cambió → fila nueva; la vieja no se edita.
- En cualquier otro caso → se entrega y se cierra.
