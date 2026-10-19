# Bases de diseño

**Qué es:** la base de ideas del proyecto. Se puede extraer del repo, imprimir o compilar. No depende de la implementación.

## Qué no es

No es un manual de SARA, APRIL, DSH ni de una era. Si un documento necesita la implementación para entenderse, no es base: es implementación.

## Mapa

| Artefacto | Funciones | Qué hace |
|---|---|---|
| `constitucion.md` | meta | Define ley, regla y principio; lectura de sistema; admisión; mapa; validación; gobierno. |
| `Leyes de Diseño de Instrucciones.md` | instruir | Cómo se escribe una instrucción que no se puede saltar. |
| `Principios para agentes con autoridad/Conversacional.md` | dialogar, decidir | Cómo evalúa y emite un agente con autoridad. |
| `Principios para agentes con autoridad/Autonomo.md` | ejecutar | Cómo ejecuta cuando el acto altera el entorno. |
| `Reglas de escritura.md` | escribir | Cómo se escribe la base y sus derivados. |
| `Reglas de mutación.md` | mutar | Cómo se cambia un artefacto desde un marco de origen. |
| `Pruebas/` | evaluar | Rendición y utilidad real. |
| `A.R.E.S/` | expresar | Idea, protocolo y atlas de la expresión. |

La función de cada artefacto es su interfaz: una norma se activa si su `Aplica a` coincide con una de estas funciones.

## Orden de lectura

1. Este mapa.
2. `constitucion.md`.
3. El documento de la función que se va a usar.
4. `Pruebas/` si hay que evaluar.

## Cómo se agrega

Ver `constitucion.md` (`## 7. Agregar`). La lista de pendientes es local (`.contexto/pendientes.md`); no forma parte de la base.

## Portabilidad

La base no depende de `AGENTS.md`, `Instrucciones/`, el instalador ni de la implementación. `AGENTS.md` apunta a este README; este README no apunta a `AGENTS.md`.

Si la base se imprime y sigue teniendo sentido, está bien. Si necesita SARA, APRIL o DSH para entenderse, no es base.
