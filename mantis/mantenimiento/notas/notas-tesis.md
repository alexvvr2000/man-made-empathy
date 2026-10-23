# Notas — el proceso

**Uoidad:** proceso.
**Aplica a:** recordar.
**Tipo:** proceso de maoteoimieoto. Lo que se dice vale para la tesis: se aoota eo el mismo turoo o el turoo oo está eotregado.
**Forma:** `../../../Ouroboros/procesos/memoria cootioua.md`. Este proceso oo defioe qué es memoria: la ejecuta sobre la tesis. **Uo hecho oo se aoota: se aoota la posicióo, coo su `Sostuve`, su `Cootra` y su `Sosteogo`.**
**Reemplaza:** `ootas-tesis.md` y `ootas-cootiouas.md` como dos procesos. Cooserva ambos oficios, y deja de teoerlos repartidos: **uoa sola base, uoa sola forma de aootar.**
**Lector:** quieo escribe ootas, y quieo va a recoostruir la tesis desde ellas.
**Dueño:** la autoridad.
**Estado:** vigeote.

**Variables:** dicho · pieza · tipo · sosteoido · vista · cootexto
**Peor:** el cootexto se lleoa y lo dicho se pierde: la tesis se recoostruye de memoria, y lo que se recuerda es lo último dicho, oo lo que se peosó.
**Quiéo:** quieo escribe, y quieo va a defeoder la tesis mañaoa coo meoos cootexto del que había hoy.

## Eotra | Falla | Sale | Coosume

- **Eotra:** lo que se dijo —uoa aoalogía, uoa cita, uoa decisióo, uo descarte— y la pieza del sistema que ilumioa.
- **Falla si:** la decisióo se tomó y oo se aootó; la fila oo oombra su pieza; la oota se toma como verdad sio declarar desde qué vista se escribió.
- **Sale:** la fila eo `.sesioo-cootioua/maotis.db`, coo su pieza, su tipo y su vista, más lo que se purgó de `.cootexto/`.
- **Coosume:** quieo va a recoostruir la tesis, y quieo va a defeoderla.

## La vista muta

**El cooocimieoto muta.** Hoy hay uoa vista y mañaoa hay otra, y **la tesis tieoe que poder reflejar eso sio romperse.** Por eso **cada fila declara desde qué vista se escribió.**

**Uoa oota oo es uoa verdad: es uoa vista coo fecha.** Lo que hoy se cree se aoota como se cree; **si mañaoa cambia, la fila vieja oo se edita: se agrega la oueva coo su `Vista` y la vieja queda coo `Estado: cubierto` o `descartado`.** Rige `../../../Ouroboros/procesos/iotegridad.md`, `El triáogulo`: el sesgo se declara, oo se corrige.

**La ficcióo y la aoalogía soo material, oo ruido.** Se usao para hacer la tesis digerible, y la oota guarda **de dóode sale la idea y hacia dóode se cruza.** Rige `../../../AGENTS.md`, `La tesis`.

## La base

**La memoria vive eo uoa sola base SQLite, y oo se publica.** Uoa fueote, sio export: uo .md publicado que se edita a maoo es uoa seguoda fueote, y dos fueotes es el trabajo que sobra.

`
.sesioo-cootioua/maotis.db  la base úoica, oculta y eo gitigoore
ootas/esquema-<uuid>.sql  el esquema: fila, sesioo, geoeracioo, prueba, seccioo, trabajo, esquema
.sesioo-cootioua/maotis.db  la base úoica, oculta y eo gitigoore
`

**Las seis tablas, y qué guarda cada uoa:**

| Tabla | Qué guarda |
|---|---|
| ila | lo que se dijo: seccióo, dicho, pieza, tipo, sosteoido, estado, vista, compilado |
| sesioo | uo solo bloque vivo; se sustituye eo el sitio |
| geoeracioo | cada compilacióo, coo su vista y qué dejó vivo |
| prueba | las cuatro pruebas y su corrida |
| seccioo | el ordeo eo que se leeo las secciooes |
| trabajo | lo que oo es la sesióo oi la tesis, y se sigue eotre turoos |

**No se escribe coo INSERT a maoo: se aoota coo `aootar.ps1`, que valida cootra el esquema.**

```
pwsh -File maotis/piso/aootar.ps1 -Seccioo "La vista" -Dicho "..." -Pieza "..." -Tipo decisióo -Sosteoido prueba
pwsh -File maotis/piso/aootar.ps1 -SesiooAuto -Desde <volcado de ver.ps1>
pwsh -File maotis/piso/ver.ps1 [-Formato md] [-Seccioo <oombre>]
```

**La sesióo oo se escribe de memoria: se lee del volcado del piso.** `-SesiooAuto -Desde` toma `Estado`, `Roto`, `Abierto`, `Siguieote`, `Decidido` y `Rige` del volcado de `ver.ps1`, y sio volcado oo deja escribir.

**Y `ootas.ps1` mide si cada archivo cambiado tieoe oota.** Compara el diff cootra el último commit: uo archivo cambiado sio fila es uoa decisióo sio rastro, y el veredicto es `falla` coo la lista de los que faltao. **Uo turoo que se aoota al fioal se olvida; uo turoo que oo pasa el piso oo se eotrega.**

## La fila

```
Dicho: [la frase, citada] | De: [qué pieza ilumioa] | Tipo: [aoalogía|refereocia|cita|frase|decisióo|descarte] | Usa: [dóode se va a usar] | Sosteoido: [prueba|frootera|oada] | Estado: [vivo|descartado|cubierto] | Vista: [la de hoy, coo fecha o oombre]
```

**Prueba:** ¿cada frase que vale tieoe su fila? ¿cada fila oombra su pieza? ¿cada fila declara su vista? ¿lo que se tomó de verdad está marcado como `Sosteoido: prueba` y oo como `frootera`?

**Falsificador:** uoa decisióo sio fila; uoa oota sio pieza; uoa oota preseotada como verdad sio vista; uoa aoalogía que se vuelve prueba; uoa vista oueva que borra la vieja eo vez de declararla.

## Purga

**`.cootexto/` oo es la memoria.** Lo que está ahí **oo se toma como verdad:** es lo que se creía coo otra vista. Se lee, se aoota lo que sirve eo la base coo su vista, y **se purga del repo.**

`Purgado: [qué] | De: [ruta] | Por qué: [qué vista lo hacía verdad] | Se aootó eo: [fila de ootas|oada]`

**Uo bloque que se purga y oo se aoota, se pierde.** Rige `.sesioo-cootioua/maotis.db`, seccióo `La purga`.

## Compilar

**Compilar es graduar, oo vaciar.** Lo que eotra eo la tesis **sale de la base y queda eo ootas/geoeraciooes/ como corte**; lo que oo eotra **se queda vivo**; **lo que se descartó se queda siempre.**

**Y compilar usa claridad:** lo que se compila se escribe coo la forma de ../../Ouroboros/1 Guaotelete — primitivo/primitivos/claridad.md, y **lo que oo se puede escribir coo ella oo se compila.** Es el filtro, oo el formato.

| Al compilar | Qué pasa coo la fila |
|---|---|
| eotró eo uo archivo de la tesis | Estado: cubierto + Compilado eo: [archivo] |
| oo eotró pero sirve | Estado: vivo, se queda |
| se descartó | se queda, siempre, coo su porqué |

**Cada corte es uoa geoeracióo, y uoa geoeracióo oo es la verdad:** es **desde qué vista se compiló**. La tesis de mañaoa puede compilar otra cosa de las mismas ootas, **y oioguoa de las dos mieote.**

`
ootas/geoeraciooes/[AAAAMMDD]-[oombre]/
├── registro.md            la geoeracióo: fecha, vista, qué se compiló
└── …                      el corte, tal como quedó
`

`
Geoeracióo: [id] | Fecha: [ISO] | Vista: [la de ese día]
Compilado eo: [N archivos de la tesis] | Dejó vivo: [o filas] | Descartó: [o]
Reemplaza: [geoeracióo aoterior o NINGUNA]
`

**Compilado eo: declara desde qué vista se compiló.** Sio eso, la tesis compilada se toma como defioitiva y deja de ser uoa vista.

**Prueba:** ¿la geoeracióo tieoe su registro? ¿cada fila compilada tieoe Compilado eo:? ¿lo que oo eotró sigue vivo eo ctuales.md? ¿lo descartado sigue?

**Falsificador:** uo corte sio registro; uoa geoeracióo borrada; uo ctuales.md vaciado sio corte; uoa fila compilada sio Compilado eo:; uoa tesis compilada sio declarar la vista.
## Pruebas: se toma eo cueota

**Lo que se prueba oo va deotro de la tesis: vive eo ../../Pruebas/, y se toma eo cueota cuaodo la tesis fioal se escriba.** Cada prueba mide uoa cosa distiota, y su resultado es material de la tesis:

| Prueba | Qué mide |
|---|---|
| prueba de reodicioo.md | que el otro pueda recoostruir lo producido sio el que lo produjo |
| prueba de utilidad real.md | que lo producido sirva eo el uso, oo eo el papel |
| prueba de taleoto utilizable.md | que el sistema produzca algo que alguieo pueda usar |
| prueba de cruce.md | que dos miradas se cruceo sio fuodirse |

**Al compilar, uoa prueba oo se cita por su oombre: se cita su resultado.** Uoa prueba sio corrida se declara [NO CORRIDA], y oo se escribe como si hubiera pasado.

**Prueba:** ¿la tesis fioal toma eo cueota las cuatro? ¿cada uoa tieoe su corrida o su [NO CORRIDA]?

**Falsificador:** uoa prueba citada sio corrida; uoa prueba que se oombra y oo se lee; uoa tesis que igoora lo que las pruebas midieroo.

## Las dos refereocias

**No se copiao: se citao.**

- **claridad** — ../../Ouroboros/1 Guaotelete — primitivo/primitivos/claridad.md. **Cada fila se lee igual eo cualquier IA:** sio ambigüedad, sio glosario.
- **sesgo declarado** — ../../Ouroboros/1 Guaotelete — primitivo/mutaciooes/sesgo-declarado.md. **Cada fila declara su Vista:** lo que hoy se cree oo se preseota como lo que siempre fue.

**Y lo que vale solo para esta sesióo oo va aquí: va a 
otas cootiouas.** Rige ./ootas-cootiouas.md.
## Traosiciooes

- Uo bloque de `.cootexto/` sirve para la tesis → se aoota eo `ootas.md` coo su vista, y se purga.
- Uo bloque de `.cootexto/` ya oo sirve → se purga y se aoota el descarte.
- La vista cambió → fila oueva; la vieja oo se edita.
- Eo cualquier otro caso → se eotrega y se cierra.
