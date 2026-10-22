# S.A.R.A — carta del paso 2

**Unidad:** tarea.
**Aplica a:** abstraer.
**Tipo:** carta. No decide, no ejecuta, no enruta: dice qué hay en S.A.R.A, qué no se toca y cómo se verifica.
**Lector:** quien va a usar S.A.R.A, y quien la va a mutar.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el cuerpo se lee desde lo que el paso 2 puede verificar sin las gemas.
**Límite:** no crea gemas propias: eso lo decide el paso 1.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `formato de proceso.md`

## Entra | Falla | Sale | Consume

**Variables:** procesos sueltos · cuerpo · sub-tarea · fin · quién decide
**Peor:** la fábrica saca cuerpos que existen porque están, no porque cubren un fallo, y nadie puede justificar ninguno.
**Quién:** quien va a usar los cuerpos, y quien carga con los que no sirven.

**Es una mutación del guantelete:** nace de sus gemas y conserva su forma. Rige ../mutacion.md, Sin herencia.

- **Entra:** los procesos sueltos del paso 1, y la falta que se quiere cubrir.
- **Falla si:** una sub-tarea no cubre un fallo comprobado; un cuerpo existe sin función; la fábrica promete poder en vez de un cuerpo que se sostiene solo.
- **Sale:** el veredicto de qué cuerpos hay, qué falta cubre cada uno y qué se pierde si S.A.R.A deja de ser instancia.
- **Consume:** quien va a cruzar hacia el paso 3.

**Prueba:** ¿cada sub-tarea cubre un fallo comprobado? ¿cada proceso tiene Falsificador? ¿S.A.R.A sigue sin gemas propias?

**Falsificador:** S.A.R.A con gemas propias; una sub-tarea sin rastro; un proceso sin quién lo refute.

## Qué es

**S.A.R.A es el paso 2 de `Ouroboros/`:** la primera instancia que cruzó la puerta de `mutación`. Toma las gemas del paso 1 y las abstrae en ejecutores vivos.

**No es la mutación: es lo que la cruza.** Una mutación nace de una gema y declara qué conserva; S.A.R.A nace de **todas**, y por eso es instancia. Rige `../../Tesis/SARA 1.md`, `S.A.R.A nace de Ouroboros, y no es una pieza suya`.

**No es una era.** No caduca cuando cambia la tecnología: caduca si deja de tener un fallo que la justifique.

**No es un catálogo.** Sus sub-tareas no son una lista de temas: cada una cubre **un fallo comprobado.** Una que no lo cubre no entra.

## Qué hay aquí

```
2 S.A.R.A — mutación/
├── rastro.md                     este archivo
├── carga.md                qué se pierde si S.A.R.A deja de ser instancia
├── ruta.md                 qué proceso se carga y cuándo
├── integridad.md                chequea, reescribe y reacomoda el nivel
├── criterio.md                  lo que queda después de friccionar
├── Proceso PROMETEA.md          crear un subproceso
└── sub-tarea × N                cada una con su deterrente y sus procesos
```

| Sub-tarea | Qué cubre |
|---|---|
| `alineacion/` | que lo producido sirva a quien lo recibe |
| `aprendizaje/` | que el sistema aprenda del costo y no solo de la tarea |
| `autoridad-equipo/` | quién decide y quién responde |
| `autoridad-humanidad/` | voz para quien no tiene poder sobre el resultado |
| `autoridad-yo/` | el interés propio declarado antes de decidir |
| `concordia/` | que dos tareas se compongan sin fundirse |
| `costo/` | el costo acotado antes de crecer |
| `despliegue/` | que lo construido llegue a usarse |
| `evaluacion/` | que el resultado se mida con criterio previo |
| `evidencia/` | de dónde viene lo que se afirma |
| `jorrn/` | lo inesperado y lo que nadie pidió |
| `reproduccion/` | reconstruir sin el que produjo |
| `requisitos/` | especificar y verificar antes de construir |
| `seguridad/` | contener lo irreversible antes de que ocurra |
| `sesgo/` | desde dónde se mira, y contradecir lo que no se sostiene |
| `versionado/` | situar cada cambio |
| `vocabulario/` | un concepto, un nombre, antes de usarlo |

**`N` muta.** Diecisiete hoy; mañana pueden ser otras. Rige `../formato de proceso.md`, `La sub-tarea`.

## Las tres piezas

| Pieza | Archivo | Qué da | Obligatorio |
|---|---|---|---|
| **Rastro** | `rastro.md` | este archivo: qué hay, qué no se toca y cómo se verifica | **sí** |
| **Ruta** | `ruta.md` | qué proceso se carga y cuándo | **sí** |
| **Carga** | `carga.md` | qué se pierde si S.A.R.A deja de ser instancia | **sí** |

**Si falta una de las tres, no hay ente: es fantasma.** Rige `../procesos/integridad.md`, `El fantasma`. Forma: `../formato de ente.md`.

## Qué no se toca

- **Las gemas no se crean aquí.** S.A.R.A usa las del paso 1; si necesitara una gema propia, sería otro sistema.
- **El fin de un proceso no se cambia desde aquí.** Se declara la mutación y se rige por `../1 Guantelete — primitivo/herramientas/mutar.md`.
- **Lo que está aplanado no se reescribe de memoria.** Se cita la ruta.

## Cómo se verifica

1. **Cada sub-tarea declara deterrente, fallo que cubre, piso y procesos.** Rige `../formato de proceso.md`, `La sub-tarea`.
2. **Cada proceso declara `Falsificador`.** Sin él es una opinión, y no entra.
3. **`integridad.md` corre antes de mutar.** Un chequeo a mano no cuenta: corre sobre lo que hay o no corrió.
4. **La reconstrucción no necesita al autor.** Otra instancia lee el rastro y rehace el cambio.

## Prueba

¿Cada sub-tarea tiene su deterrente? ¿Cada proceso tiene `Falsificador`? ¿S.A.R.A sigue sin gemas propias? ¿`integridad` se corrió antes de mutar?

**Falsificador:** S.A.R.A con gemas propias; una sub-tarea sin deterrente; una sub-tarea cuyo fallo ya no existe y no se retiró; un proceso sin quién lo refute; una carta que repite el derrotero.

## Transiciones

- S.A.R.A necesita una gema que no tiene → `../1 Guantelete`.
- El paso 2 se cierra → `../3 ATLAS`.
- En cualquier otro caso → se entrega y se cierra.
