# Mapa de vistas

**Unidad:** tarea.
**Aplica a:** expresar
**Lector:** humano (autoridad). El mapa declara su lector al abrir.
**Tipo:** forma. No decide; muestra.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

El mapa no es un informe: es una superficie para ver lo que la decisión deja fuera. No embellece el resultado; hace visible la vista, la que falta, la fuente, el testimonio y la ausencia. Si el lector necesita preguntar dónde está algo, el mapa falló.

## Qué muestra

| Capa | Qué declara | Para qué sirve |
|---|---|---|
| Decisión | lo que la autoridad decide | saber qué está en juego |
| Vista | desde dónde se habla y qué no se ve | saber qué parte del mundo quedó fuera |
| Vista faltante | la que la autoridad no ocupa, la limitación que esquiva, la ausencia que revela y la decisión que cambia | mover la vista, no imponerla |
| Fuente | origen, nivel, independencia y contradicción | volver a la fuente |
| Testimonio | persona o grupo, vínculo, contexto y consentimiento | no hablar por la gente |
| Ausencia | qué falta, dónde se buscó y qué cierra | ver el hueco, no rellenarlo |
| Costo y beneficio | a quién cuesta y a quién beneficia | saber a quién sirve |

## Forma mínima

```
Mapa: [título]
Decisión: [lo que se decide]
Vista: [posición] | No ve: [límite]
Vista faltante: [posición] | Esquiva: [limitación] | Ausencia: [qué falta] | Cambia: [decisión]
Fuente: [id] | Nivel: [N1-N5] | Origen: [medio] | Independencia: [A|B|C] | Contradice: [id o NINGUNA]
Testimonio: [persona/grupo] | Vínculo: [afectado|mantenedor|crítico|beneficiario] | Contexto: [...] | Consentimiento: [...]
Costo: [tipo:nombre] | Beneficio: [tipo:nombre]
Cierre: [qué falta para decidir]
```

La escala N1-N5 y los campos de fuente viven en `Registro.md`; el mapa no los repite.

## Reglas

1. **Abre por la decisión.** El lector sabe qué está en juego antes de leer el mapa.
2. **Una vista por fila.** No se mezclan vistas; cada una declara su límite.
3. **La fuente se puede seguir.** Sin origen, nivel e independencia, la fila no entra.
4. **El testimonio tiene dueño.** Sin vínculo y consentimiento, no se habla por la gente.
5. **La ausencia se ve.** Lo que no está se nombra; no se rellena.
6. **El mapa no decide.** La decisión queda en la autoridad; el mapa muestra el costo y el beneficio.

## Pruebas

- **Efecto:** el lector ve la vista, la que falta, la fuente, el testimonio y la ausencia sin preguntar.
- **Reproducibilidad:** el mismo registro produce el mismo mapa.
- **Transferencia:** otra instancia lo reproduce leyendo solo el registro.

## Falsificadores

- El mapa es una pared de texto sin decisión.
- La vista faltante es un hombre de paja.
- La fuente no se puede seguir.
- El testimonio no tiene vínculo ni consentimiento.
- La ausencia se rellena con narrativa.
- El mapa decide por la autoridad.

## Qué no es

- No es un dashboard: no mide en vivo.
- No es un informe: no narra el proceso.
- No es una recomendación: no decide.

## Transiciones

- Falta un hecho → `indagacion-instrumental`.
- Dos caminos con fricción → `deliberacion-estructurada`.
- El siguiente paso altera estado persistente → `entrega-operacion`.
- En cualquier otro caso → se entrega y se cierra.
