# requisitos

**Deterrente:** si un requisito entra sin poder medirse, nadie puede decir después si se cumplió y la cadena entera queda sin piso. **Un requisito que no se distingue de su ausencia no es un requisito: es un deseo con formato.**

**Fallo que cubre:** la cadena multi-paso que arranca con la **declaración** del paso anterior en vez de su salida verificada. Es la debilidad documentada de los agentes: acumulan el error en vez de corregirlo. `../../corpus/problemas-abiertos.md`, filas de agentes multi-paso y razonamiento fiable.

**Piso:** `../../corpus/piso.md`. La verificación de un paso corre igual en dos ejecutores; si uno la da por buena y el otro no, no se verificó: se opinó.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `especificar.md` | si una intención se puede escribir como requisito observable | el requisito no distingue cumplido de incumplido |
| `verificar-requisito.md` | si el requisito se puede medir antes de aceptarlo | dos lectores entienden cosas distintas |
| `verificar-paso.md` | si el paso N+1 arranca con la salida verificada del N | la cadena sigue con la declaración, no con la prueba |

**X muta.** Tres hoy; mañana pueden ser otros.

> **Declarar no es verificar.** Si el paso N está mal, el N+1 no lo arregla: lo hereda.
