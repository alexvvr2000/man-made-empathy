**Variables:** instancia · origen · conserva · esquema · ciclo
**Peor:** MANTIS opera procesos que nadie sabe de dónde salieron, y su forma parece original cuando solo es la de S.A.R.A heredada; y el esquema que guarda su memoria se pierde en el nombre, y con él la única prueba de que el sistema converge a algo legible
**Quién:** quien carga MANTIS mañana y no vio nacer la instancia, y quien va a juzgar si el sistema es un invento o una mutación

# MANTIS — acta de la instancia

**Unidad:** tarea.
**Aplica a:** declarar.
**Tipo:** acta. No decide, no ejecuta: dice de dónde viene MANTIS, qué conserva y qué acuñó.
**Lector:** la autoridad, y quien vaya a mutar MANTIS.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la instancia se lee desde lo que heredó, no desde lo que se cree haber inventado.
**Límite:** no decide si MANTIS sirve; eso lo dice quien lo usa sobre su repo.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `../Ouroboros/procesos/integridad.md`

## El acta

```
Acta: MANTIS
Nombre: MANTIS — Memoria, Análisis, Navegación, Triangulación, Integridad y Sistema
Expansión: opera sobre un repositorio real la fábrica de abstracciones del paso 2
Origen: las diecisiete sub-tareas de ../Ouroboros/2 S.A.R.A — mutación/
Fecha: 2026-10-22
Muta: de una fábrica de abstracciones nace el sistema que las ejecuta sobre un repo
Conserva: la forma de proceso, Rastro/Ruta/Carga, integridad antes de mutar, y el piso como veredicto
Ausencias: no crea sub-tareas propias; no produce procesos, los ejecuta; no sustituye a la autoridad
Prueba: corrida — el piso emite veredicto sobre este repo
Autoridad: la autoridad | Cierra en: quien publica
Reemplaza: NINGUNA — primera instancia operativa
```

## Por qué es mutación y no un cuarto paso

**`mutacion.md` pide dos cosas, y MANTIS las cumple:**

| Requisito | Cómo se cumple |
|---|---|
| **Nace de una pieza y declara qué conserva** | nace de S.A.R.A, y conserva su forma entera |
| **Acuña nombre y lugar nuevos** | `mantis/` no existe en el paso 2: es un lugar nuevo con otro nombre |

**Y no es un cuarto paso: es la misma relación que S.A.R.A tiene con el guantelete.**

| Paso 1 | Paso 2 | Instancia |
|---|---|---|
| **guantelete** sostiene las dos piezas | **S.A.R.A** abstrae en diecisiete sub-tareas | **MANTIS** las opera sobre un repo |

**Una instancia no está dentro del paso que la origina.** S.A.R.A no está en el guantelete. **MANTIS no está en S.A.R.A.**

## Las seis letras, y dónde aterriza cada una

| Letra | Oficio | Dónde vive | Lo que conserva de S.A.R.A |
|---|---|---|---|
| **M**emoria | la base única y sus instrumentos | `piso/anotar.ps1`, `piso/ver.ps1`, `piso/notas.ps1` | `reproduccion`, `versionado` |
| **A**nálisis | las unidades que miden, sin modelo | `piso/` | `evaluacion`, `evidencia` |
| **N**avegación | qué se carga y cuándo | `Derrotero.md` | `ruta.md` del ente |
| **T**riangulación | los tres vértices del veredicto | `chequear/` | `sesgo`, `integridad` |
| **I**ntegridad | chequea y reescribe antes de mutar | `../Ouroboros/procesos/integridad.md` | `integridad` del paso 2 |
| **S**istema | lo que sostiene las cinco anteriores | `carga.md` | `carga.md` del ente |

**Ninguna letra es relleno: cada una nombra una carpeta que existe.**

## El esquema con UUID — el séptimo oficio

**La memoria de MANTIS tiene un esquema, y su nombre es un UUID.**

```
notas/
├── esquema-<uuid>.sql      la forma vigente: cada cambio acuña un UUID nuevo
├── esquema anterior        no se edita: se sucede
└── .sesion-continua/mantis.db
```

**Por qué UUID y no versión:** una versión (`v1`, `v2`) es un orden que alguien cree recordar. **Un UUID no ordena: identifica.** Dos esquemas distintos no se confunden, y una base abierta dice con qué esquema se escribió sin que nadie tenga que consultar una tabla.

**Regla dura:** el esquema no se edita en el lugar. **Se acuña otro UUID y el anterior se declara sucedido.** Una base que no dice con qué esquema se escribió no se abre: se declara.

`Esquema: esquema-<uuid>.sql | Sucede a: esquema-<uuid anterior> | Base: .sesion-continua/mantis.db | Se abre con: [el uuid que la base declara]`

**Lo que este esquema no resuelve, y se declara:** que la memoria converja a algo parecido a un cerebro humano **no está establecido**. Lo que sí se puede sostener es más chico y verificable: **una memoria que guarda posiciones, se puede releer sin el autor, y dice con qué forma se escribió.** Eso sirve para curar un sistema de sus propios errores. **No cura nada que esté fuera de él.**

## Cómo evoluciona, igual que Ouroboros

**Las dos mutan con el mismo mecanismo, y ninguna muta por opinión.**

| | Qué muta | Con qué se confirma | Qué produce |
|---|---|---|---|
| **Ouroboros** | las reglas de base: guantelete, S.A.R.A, ATLAS | el **estado del arte**, con cerrojo | ejecutables con formato de ente |
| **MANTIS** | los instrumentos que operan: piso, derrotero, memoria | **su propia corrida**: el piso se corre sobre sí | veredictos |

**La regla compartida:** una pieza muta cuando **el cerrojo la sostiene** o **la corrida la rompe**. Nunca porque suene mejor.

## Entra | Falla | Sale | Consume

- **Entra:** el sistema en uso, y el rastro de su origen.
- **Falla si:** MANTIS no declara de qué nace; su forma parece original; el esquema de su memoria no tiene UUID; el esquema se editó en el lugar en vez de sucederse.
- **Sale:** el acta, y el veredicto de si MANTIS sigue siendo la instancia de S.A.R.A o se volvió otro sistema.
- **Consume:** quien va a mutar MANTIS, y quien va a juzgar si es un invento.

**Prueba:** ¿el acta nombra el origen y lo que conserva? ¿cada letra del acrónimo aterriza en una carpeta? ¿el esquema de la memoria tiene UUID y sucesor declarado?

**Falsificador:** una instancia que no declara su origen; una pieza que conserva el nombre de lo que reemplaza; un esquema editado en el lugar; un acrónimo con una letra que no nombra ninguna carpeta.

## Transiciones

- MANTIS necesita una pieza que S.A.R.A no tiene → **deja de ser instancia**: se declara en `../Ouroboros/2 S.A.R.A — mutación/`.
- El esquema cambia → se acuña otro UUID, y el anterior se declara sucedido.
- MANTIS deja de operar sobre un repo → se retira, con el fin que cubría declarado.
- En cualquier otro caso → se entrega y se cierra.
