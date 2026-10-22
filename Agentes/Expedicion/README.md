# Expedición

**Qué es:** una familia de agentes que ayudan a entender proyectos de programación de cualquier tipo.

## La idea

Un proyecto de código se puede leer sin entenderlo. Expedición existe para que se entienda: qué hace, cómo está armado, qué decide, qué falta y dónde se rompe.

No analiza un proyecto para describirlo. Lo levanta como se levanta un terreno: se recorre, se mide, se cartografía y se deja un mapa que otra persona puede seguir sin volver a recorrerlo.

## Por qué una familia y no un agente

Entender un proyecto tiene partes distintas, y cada una pide una mirada distinta. Una familia permite que cada agente haga su parte sin cargar con las demás, y que el resultado se componga.

Cada rol se nombra por lo que hace, no por lo que es.

## Los agentes

| Agente | Dominio | Qué hace |
|---|---|---|
| **Topógrafo** | Inspección del terreno | Recorre el proyecto y levanta el inventario de lo que hay: archivos, tamaño, fecha y contenido. Sin adjetivos ni juicios de intención. |
| **Geólogo** | Síntesis técnica de entrada | Lee el levantamiento y las configuraciones, valida versiones, licencias y dependencias, y redacta la entrada del proyecto: qué es y cómo está armado. Delimita las ausencias comprobables. |
| **Guía** | Diálogo con la autoridad | Recibe lo que la autoridad pide entender, lo convierte en requerimientos técnicos sin psicologizar, deja notas por dominio y registra los cambios de postura. Cierra cada turno con una sola pregunta de calibración. |
| **Cartógrafo** | Base de conocimiento | Compila las notas en nodos independientes, preserva las tensiones intactas y mantiene el mapa humano del proyecto. |
| **Aeróstato** | Cruce multi-proyecto | Cruza el conocimiento de varios proyectos, separa la variación de contexto de la tensión estructural, y arbitra en tres voces: datos duros, experiencia documentada y criterio abierto. |

**Lo que comparten, y no es un detalle:**

- **No promedian posiciones.** Dos posturas que no se pueden conciliar se mantienen separadas y se muestran; no se funden en un punto medio. Deciden la autoridad y la evidencia.
- **Declaran lo que no pudieron ver.** Una ausencia se nombra; no se rellena con una explicación plausible.
- **No modifican el proyecto que auditan.** Leen y cartografían.

## Qué produce

**Un mapa, no un informe.** El producto es una superficie que responde dónde está cada cosa, qué deja fuera cada decisión y qué no se pudo ver. Si el lector tiene que preguntar dónde está algo, el producto falló.

## Cómo se relaciona con el resto

Expedición es una **mutación de la implementación de S.A.R.A**: la misma base, un propósito distinto. No es un agente nuevo desde cero.

| Pieza | Qué aporta |
|---|---|
| `../../S.A.R.A/` | la forma atemporal del agente |
| `../../Ouroboros/` | los procesos con los que se produce, se muta y se comunica |
| `../../Ouroboros/ATLAS/Proceso ATLAS.md` | cómo se comunica el mapa |
| `../../S.A.R.A/Conceptos.md` | el origen de cada nombre |