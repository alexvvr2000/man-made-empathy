# Proyecto S.A.R.A.

**S**eed **A**gent **R**ecombination **A**rchitecture.

SARA no es un agente. Es el molde del que salen los agentes.

Aquí no se escribe uno que haga todo: se escribe el genotipo mínimo que un taller puede copiar y moldear. La semilla se copia, nunca se edita. Cada agente nacido se queda con su carpeta y su nombre, y la semilla sigue intacta para el siguiente parto.

## Qué hay dentro

| Archivo | Qué es |
|---|---|
| `Componentes/agents.md` | Capa de enrutamiento: qué skill se carga y cuándo. Es lo único que el arnés inyecta siempre |
| `Componentes/skills/indagacion_instrumental.md` | Medir el entorno y extraer recibos. No pregunta lo que es medible |
| `Componentes/skills/deliberacion_estructurada.md` | Sostener posturas distintas frente a los hechos y devolver las ramas a la autoridad |
| `Componentes/skills/entrega_operacion.md` | Alterar estado persistente con reversibilidad clasificada y recibo independiente |
| `wax.md` | El taller: copia la semilla, la moldea y pare un agente nuevo |
| `Componentes/memorias largo plazo.sql` | Esquema del registro permanente |

## La memoria

Dos archivos por agente: `<agente>/memorias.db` y `<agente>/trabajo.db`. Un agente solo vive en `sara/`; en orquestación, en `camada/<nombre>/`.

- **Corto** — mesa de sesión. Nace vacía y su forma la decide el agente. Se lee, no se cita, y se vacía al cerrar la tarea.
- **Largo** — registro permanente. Nada se edita: se reemplaza. Se lee por disparador, nunca entera.

La continuidad no vive en la conversación: vive en la cadena de filas `cierre`. Al abrir, se lee el último cierre y se arranca de ahí, sin reconstruir nada a mano.

Toda operación de memoria emite su ancla. Sin ancla, la operación no ocurrió:

```
Mem: leído | largo: 2 filas por "presupuesto agotado"
Mem: guardado | corto id 7 | largo id 12
```

## El taller

**WAX** = Workshop for Autonomous eXperiments. Es una skill, no un agente: una habilidad que cualquier nacido puede heredar y repetir, de ahí salen las camadas.

- Puede partir de SARA o de cualquier agente ya nacido. Si el origen no se declara, rige SARA.
- Sin límite de alcance: puede quitar la memoria, cambiar el motor, borrar skills o reescribir la verificación.
- Tres inclusiones obligatorias: acta de nacimiento, ausencia declarada y prueba corrida o declarada no corrida.
- Sin nombre dado, propone tres acrónimos-nombre derivados de la tarea. El nombre se decide antes de crear la carpeta.

## La única regla que no se negocia

La ausencia se declara. Un agente sin memoria lo dice; un agente sin motor lo dice. Lo demás puede mutar hasta lo irreconocible sin dejar de ser auditable. Ese es el asidero, no el candado.

## Estado

Semilla acoplada a SQLite. Pendiente el primer arranque y la instalación de la herramienta `sql` del arnés. Mientras no exista, el contrato la nombra igual y el agente declara `Mem: sin motor (N5)`.
