# S.A.R.A — derrotero del paso 2

**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Carta:** [`./rastro.md`](./rastro.md). Sin carta no se lee.
**Deterrente:** [`./carga.md`](./carga.md). Sin él, no se sabe qué se pierde si S.A.R.A deja de ser instancia.
**Piso:** `../../1 Tesis/piso.md`.
**Abstracción:** `../` — S.A.R.A es el paso 2 de `2 Ouroboros/`.
**Integridad:** `./integridad.md`. Se carga cuando el chequeo encuentra que hay que reacomodar el nivel o que la tarea es fantasma.
**Criterio:** `./decisión.md`. Se carga cuando una decisión se va a repetir sin fricción.

## Entra | Falla | Sale | Consume

**Variables:** petición · proceso · sub-tarea · condición · quién la levanta
**Peor:** se carga el proceso de una sub-tarea que no cubre el fallo que se está atendiendo, y el resultado parece correcto.
**Quién:** quien enruta, y quien audita después qué se cargó.

- **Entra:** una petición de trabajo sobre el paso 2.
- **Falla si:** no hay fila para lo pedido; se cargan dos procesos y no se declara por qué.
- **Sale:** el proceso que se carga, o [VACÍO - SIN PROCESO].
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿cada fila tiene su proceso y su consecuencia? ¿el vacío se declara?

**Falsificador:** una petición sin fila que se ejecuta igual; dos procesos cargados sin declararlo.

## La tabla: si se va a...

| Si se va a... | Se carga | Si no... |
|---|---|---|
| chequear y reescribir una tarea, o reacomodar su nivel | `./integridad.md` | no hay veredicto |
| dejar que una decisión se repita sin volver a preguntar | `./decisión.md` | se pregunta lo mismo cada vez |
| aprender de lo ejecutado y corregir la tarea intuida | `./aprendizaje/aprender.md` | el sistema repite el mismo error |
| proponer lo que nadie pidió, sin ejecutarlo | `./aprendizaje/iniciar.md` | el sistema solo reacciona |
| dar voz a quien no tiene poder sobre el resultado | `./autoridad-humanidad/dar-voz.md` | el efecto cae sobre quien no decide |
| identificar quién decide y quién responde | `./autoridad-equipo/identificar-partes.md` | ninguna autoridad se sabe suya |
| declarar el interés propio antes de decidir | `./autoridad-yo/declarar-interes.md` | se decide sin decir desde dónde |
| que dos caminos se sostengan sin fundirse | `./evaluacion/deliberar.md` | se funden en una respuesta tibia |
| medir si el resultado cumple el criterio previo | `./evaluacion/evaluar.md` | se mide sin criterio fijado antes |
| comprobar que lo que servía sigue sirviendo | `./evaluacion/probar-regresion.md` | lo que se rompió no se nota |
| vigilar servilismo, sesgo heredado, automatización y bucle | `./evaluacion/vigilar-tendencias.md` | la tendencia sube y el daño también, sin registro |
| medir si la fricción cambió la decisión | `./evaluacion/friccion-en-agente.md` | cero decisiones cambiadas presentadas como éxito |
| declarar el nivel de fuente de una afirmación | `./evidencia/nivel-de-fuente.md` | una salida se lee como fuente sin serlo |
| medir el costo de un error | `./evidencia/costo-del-error.md` | el error se paga sin saberse |
| declarar el peor caso antes de actuar | `./evidencia/peor-caso.md` | el peor caso aparece sin nombre |
| decidir si una ayuda no pedida corresponde | `./evidencia/ayuda-no-pedida.md` | se ayuda donde nadie lo pidió |
| trazar una afirmación hasta su origen | `./evidencia/trazar.md` | no se sabe de dónde salió lo que se afirma |
| declarar lo inesperado | `./jorrn/declarar-inesperado.md` | lo inesperado se llama error |
| producir algo nuevo sin subestimarlo ni sobreestimarlo | `./jorrn/producir.md` | se produce de más o de menos |
| reproducir un resultado sin el que lo produjo | `./reproduccion/reproducir.md` | la reconstrucción necesita al autor |
| especificar un requisito antes de construirlo | `./requisitos/especificar.md` | se construye sin saber qué se pide |
| verificar un requisito o un paso | `./requisitos/verificar-requisito.md`, `./requisitos/verificar-paso.md` | se declara cumplido sin verificarlo |
| contener una acción persistente o irreversible | `./seguridad/contener.md` | el daño se descubre después |
| contradecir una idea que no se sostiene | `./sesgo/contradecir.md` | la objeción válida se retira sin dato |
| auditar el sesgo de una fuente o una decisión | `./sesgo/auditar-sesgo.md` | se califica por quién es y no por lo que produce |
| versionar un cambio | `./versionado/versionar.md` | el cambio ocurre y no se puede situar |
| dar de alta un concepto antes de usarlo | `./vocabulario/conceptualizar.md` | aparece un nombre sin acta |
| armonizar o componer una tarea con otra | `./concordia/armonizar.md`, `./concordia/componer.md` | dos tareas se contradicen y cada una parece correcta |
| acotar el costo de una operación | `./costo/acotar.md` | el costo crece sin que nadie decida |
| desplegar lo que se construyó | `./despliegue/desplegar.md` | lo construido no llega a usarse |
| declarar y crear un subproceso | `./Proceso PROMETEA.md` | un subproceso nace sin Ciclo ni autoridad |

**Una fila, un proceso.** Si se cargan dos, se declara por qué: **dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

## Vacío

**Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.**

## Transiciones

- No hay fila para lo que se va a hacer → `[VACÍO - SIN PROCESO]`.
- Una sub-tarea no puede declarar su deterrente → se declara fantasma y se retira.
- S.A.R.A necesita una gema que no tiene → se declara en `../1 Guantelete — primitivo/primitivos/`, y deja de ser instancia.
- El paso 2 se cierra → `../3 ATLAS`.
- En cualquier otro caso → se enruta, se ejecuta y se cierra.

## Lectura

**Sin derrotero no se carga un proceso de S.A.R.A; con él, se carga el que coincide y ni uno más.**
