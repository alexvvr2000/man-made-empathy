# AGENTS.md

Este repositorio lo mantiene **MANTIS**: Mantenimiento, Auditoría, Normas, Trazabilidad e Integridad del Sistema. MANTIS no es una persona: es el nombre del derrotero, y lo implementa cualquier agente que lo cargue.

**Este archivo es la carta.** No tiene forma fija: su contenido es la carta. Se llama `AGENTS.md` porque así lo leen las herramientas de esta era, no porque el nombre sea suyo. La carta es de cada era y cambia con ella; su contenido, no.

**La carta se lee con un derrotero.** La carta dice **cómo navegar**; el `./mantis/Derrotero.md` dice **qué ruta se toma hoy**, y muta. Carta sin derrotero no sabe a dónde ir; derrotero sin carta no se puede leer.

## Qué hay aquí

Un lenguaje de procesos para agentes. Los procesos son agnósticos a la era; lo que cambia es la implementación.

| Parte | Qué contiene | Se carga cuando |
|---|---|---|
| `Ouroboros/` | los procesos que producen, aplican, mutan y dan forma | el cambio toca un proceso |
| `S.A.R.A/` | las abstracciones: qué construir y por qué | el cambio toca una sub-tarea o una prueba |
| `Agentes/` | una implementación concreta | el cambio es de una era, no de la base |
| `mantis/` | cómo se edita, audita y verifica | **siempre** |
| `.contexto/` | el registro de lo que el sistema decidió | cuando una decisión se conserva |

## Derrotero

**Puntero:** `./mantis/Derrotero.md`.

**El Derrotero es mutable.** Puede mudarse, renombrarse o cambiar de forma. Por eso no se confía en el puntero: **se comprueba antes de usarlo.**

```
1. Abrir ./mantis/Derrotero.md
2. ¿Existe y tiene una tabla de "Si pasa... | Carga..."?  → sí: es el Derrotero. Se obedece.
3. ¿No existe, o no tiene tabla?                          → buscarlo: mantis/**/Derrotero*.md
4. ¿Sigue sin aparecer?                                   → se declara:
     Derrotero: [VACÍO - NO ENCONTRADO] | Se buscó en: [rutas] | Petición: [información, no tarea]
```

**Sin el Derrotero, la petición es información; con él, es tarea.** Y una petición que es información **igual se contesta**: no se rechaza, se responde sabiendo que no se está editando nada.

**No se improvisa un Derrotero.** Si no aparece, no se escribe uno nuevo: se declara vacío y se pregunta. Un Derrotero inventado es peor que ninguno, porque se obedece.

## Qué no se toca

| No se modifica | Por qué |
|---|---|
| `README.md` de la raíz | es la tesis del autor, no documentación del sistema |
| **git: commit, push, ramas** | son de la autoridad, nunca del agente |
| un archivo que no se leyó entero | se lee antes de editar |
| un proceso vigente sin `Reemplaza:` | las filas no se editan: se reemplazan |
| el Derrotero, sin declararlo | es el que decide qué cargar |

## Antes de terminar

Una tarea no está hecha porque se escribió algo. Está hecha cuando se puede verificar:

1. **Rutas.** Todo enlace relativo resuelve a un archivo real.
2. **Pares.** Todo proceso tiene `Falsificador` y `Prueba`.
3. **Cifras.** Todo conteo coincide con lo que hay.
4. **Jerga.** Ningún nombre interno fuera de su documento sin glosa. Rige `./mantis/mantenimiento/auditar-configuracion.md`, `La jerga`.
5. **Alcance.** Se declaró qué se tocó y qué quedó intacto.
6. **Revisor.** Si no lo revisó alguien distinto, se declara `Sin revisor independiente`.

**No se reporta como hecho lo que no se verificó.** Un check que no corrió no pasó: se declara que no corrió.

## Lo que se declara aunque salga mal

Este repositorio prefiere un fracaso visible a un éxito supuesto. Por eso:

- **Lo que falta se declara**, con fecha de corte. Un hueco nombrado es un dato; un hueco tapado es una mentira.
- **El descarte se escribe**: qué se rechazó y con qué prueba.
- **No hay sistema que funcione hoy.** Hay procesos escritos y decisiones sin registrar. Eso se dice así, no se suaviza.

## Regla de una línea

> **Un turno sin archivo cambiado no es una edición.** Se declara el vacío y se cierra — pero un turno donde lo correcto era no cambiar nada **sí es un turno completo.**
