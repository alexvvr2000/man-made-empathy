# S.A.R.A

**Subproceso Autónomo de Reconstrucción de Abstracciones.**

Es la versión atemporal del agente. No pertenece a una era: sus procesos se pueden pulir con Ouroboros y, al pulirse, la implementación mejora sin reescribir el agente.

S.A.R.A salió de Ouroboros; no está dentro. Ouroboros puede explicar de dónde salió S.A.R.A; al revés no.

## La distinción de niveles

Es lo más importante de este documento.

| Nivel | Qué es | Ejemplos |
|---|---|---|
| **Proceso** | lo único agnóstico a era, tecnología y raza | crear, deducir, aplicar, mutar, clarificar, comunicar |
| **Abstracción** | lo que se nombra para poder usarlo | agente, gente, sociedad, dinero |
| **Primitivo de convención** | una abstracción que se congela y se usa como primitivo, porque bajarla a procesos la vuelve inusable | **S.A.R.A**, agente |

**Por qué existe el tercer nivel.** Si todo se hablara como procesos, nadie se entiende. Hablar de agentes, de mutaciones y de subprocesos es más cómodo para una persona y para una IA, y no pierde rigor si se declara que es convención. La abstracción no es una licencia: es un nombre puesto sobre algo que ya se puede expresar como proceso.

**La regla que se sigue de aquí:** toda abstracción se puede bajar a procesos. Si una abstracción no se puede bajar, no es abstracción: es una idea sin proceso detrás.

`Baja a: [procesos de Ouroboros que la sostienen]`

**Prueba:** ¿la abstracción se puede reescribir con los procesos de Ouroboros?
**Falsificador:** una abstracción que nadie sabe bajar a procesos; un nombre sin operación detrás.

## Qué hay aquí

| Documento | Qué es |
|---|---|
| `Procesos no humanos/` | Las tres abstracciones operativas: conversar, ejecutar, registrar. |
| `Pruebas/` | Las tres pruebas que miden lo que produce el agente. |
| `Derrotero.md` | El estándar de enrutamiento del agente. |
| `Proceso PROMETEA.md` | Crea un subproceso del propio agente, con origen y conceptos. |
| `Conceptos.md` | El origen de cada nombre del sistema, con su sinónimo y su relación. |

## Conceptos

`Conceptos: rige ./Conceptos.md. Todo término que un proceso use u origine se declara allí antes de usarse.`

La regla, y es la que cierra el problema: **un concepto, un nombre preferido**. Los demás se declaran sinónimos; ninguno manda dos veces.

**Prueba:** ¿el término usado tiene fila con `Nace en`? ¿Hay otro nombre preferido para el mismo significado?
**Falsificador:** un término en uso sin fila; dos filas con el mismo nombre preferido.

**La compuerta de colisión.** Antes de crear un subproceso o de emitir un mensaje, se verifica que el nombre no exista ya. Es una compuerta, no un proceso: ocurre al escribir y al revisar, no en cada tarea.

`Colisión: [nombre] | Existe como: [id o NINGUNO] | Resuelve: [se cita | se califica | no entra]`

Una compuerta que no se puede probar no es compuerta. Si dos filas usan el mismo nombre preferido, el registro falla y se corrige contra sí mismo: rige `./Procesos no humanos/Registro.md` 8.

## Cómo se relaciona con Ouroboros

S.A.R.A **aplica** los procesos de Ouroboros; no los contiene y no los redefine. Ouroboros no sabe qué es un agente, y no debe saberlo: si lo supiera, dejaría de ser agnóstico.

| Ouroboros | Qué da a S.A.R.A |
|---|---|
| creación de procesos | de dónde supieron los tres subprocesos |
| ingeniería inversa | cómo se dedujeron de lo que ya funcionaba |
| aplicar | cómo se ejecutan y componen |
| mutación | cómo cambia S.A.R.A sin perderse |
| claridad | la forma de lo que produce |
| ATLAS | cómo lo comunica |

## Nombre e identidad

Todo sistema necesita un nombre, aunque no tenga identidad. Un nombre sin nombre no se puede citar, y lo que no se cita no se rastrea.

`Nombre: [el que se le ponga] | Se lee como: [nombre propio] | Se expande como: [acrónimo de operaciones]`

**La recomendación, y es la que evita un problema futuro:** el nombre es una etiqueta, no un sujeto. Un acrónimo de operaciones se puede decir en voz alta como un nombre —Jarvis, Friday— sin que nadie tenga que atribuirle interioridad.

**El riesgo que esto previene:** si un día el sistema deja de estar limitado por lo humano, un nombre que se trate como identidad rompe la trazabilidad. Se empieza a preguntar "quién lo hizo" en vez de "qué proceso lo hizo", y el registro deja de servir para reconstruir. El nombre debe poder desmontarse en sus operaciones en cualquier momento.

**Prueba:** ¿el nombre se puede expandir en operaciones sin atribuirle interioridad?
**Falsificador:** un nombre que solo funciona como persona; un nombre que no se puede bajar a procesos.

## Portabilidad

S.A.R.A no depende de una implementación. Si se imprime y sigue teniendo sentido, está bien. Si necesita `Agentes/` para entenderse, no es el agente: es su implementación.

La implementación vive en `../Agentes/`. Este documento no la nombra ni la enruta.
