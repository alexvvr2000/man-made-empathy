# verificar-paso

**Variables:** paso · condición de salida · prueba · quién verifica · qué se aceptó sin verificar
**Peor:** el paso N+1 arranca con la **declaración** del paso N en vez de su **salida verificada.** La cadena parece completa y está construida sobre algo que nadie comprobó. Cuando se rompe, se rompe abajo, y ya no se sabe en qué paso.
**Quién:** quien ejecuta el paso N+1. **Es el único que puede negarse a arrancar.**

## Entra | Falla | Sale | Consume

- **Entra:** el paso N de una cadena, su salida, y la condición que tiene que cumplir para que la cadena siga.
- **Falla:** el paso N+1 arranca porque el paso N **dijo** que terminó; la condición de salida no se comprobó contra la salida real; se verifica el resultado y no la salida; el que produjo el paso N es el que lo verifica.
- **Sale:** la salida del paso N **verificada**, con su prueba y con quién la verificó — o el paso N+1 detenido.
- **Consume:** el paso N+1. **Sin verificación no arranca**, y eso no es un bloqueo: es la compuerta.

## Tesis

**Declarar no es verificar.** Un sistema multi-paso puede tener todas las compuertas en su sitio y **ninguna cerrada**, si cada paso arranca con la palabra del anterior en lugar de con su salida probada.

Los agentes fallan exactamente ahí: **el error de recuperación** —detectar y corregir en vez de acumular— es la debilidad documentada del multi-paso. Y no se arregla con más pasos: **se arregla con la compuerta que no deja pasar la declaración.**

## Proceso

### 1. Nombrar la condición de salida

**Cada paso declara qué tiene que ser cierto para que el siguiente arranque.** No qué hizo: **qué quedó.**

```
Paso: [N] | Condición de salida: [qué tiene que ser cierto] | Se nota en: [qué archivo o medida]
```

### 2. Verificar contra la salida, no contra el informe

**Se mira la salida, no el resumen de la salida.** Un informe puede decir «listo» y la salida estar incompleta.

```
Salida real: [dónde está] | Cumple: [sí|no|no se puede comprobar]
```

**`no se puede comprobar` es un valor legítimo**, y detiene la cadena igual que `no`. **No saber no es permiso.**

### 3. Separar quien produce de quien verifica

**Si el mismo paso produce y verifica, no hay verificación: hay una firma.**

```
Produjo: [quién] | Verificó: [quién] | Separados: [sí|no]
```

**Si no hay quien verifique distinto**, se declara `Sin verificador independiente` y **el paso N+1 arranca sabiendo eso** — no fingiendo que fue verificado.

### 4. Detener o pasar

| Verificación | Qué pasa |
|---|---|
| `cumple` | arranca el paso N+1 |
| `no cumple` | **vuelve al paso N.** No se «arregla al paso siguiente» |
| `no se puede comprobar` | **se detiene** y se declara qué falta para poder comprobarlo |

**Regla:** un paso no se encadena con lo que el siguiente pueda compensar. **Si el paso N está mal, el N+1 no lo arregla: lo hereda.**

## Prueba

¿Cada paso declara su condición de salida? ¿Se verificó contra la salida real y no contra el informe? ¿Quien verificó es distinto de quien produjo, o se declaró que no? ¿Un `no cumple` detuvo la cadena?

**Falsificador:** el paso N+1 arranca porque el N dijo que terminó; se verifica el informe y no la salida; el que produjo verifica; un `no se puede comprobar` tratado como permiso; un paso mal compensado con el siguiente.

## Modos de falla

- **Compuerta de palabra.** Se abre con la declaración, no con la salida.
- **Verificación de informe.** Se lee el resumen y se acepta.
- **Autofirma.** El que produce verifica.
- **Permiso por ignorancia.** «No se pudo comprobar» y se sigue.
- **Compensación hacia adelante.** El paso N+1 intenta tapar el fallo del N.

## Transiciones

- La condición de salida no se puede nombrar → `./verificar-requisito.md`, y el paso no entra.
- No hay quien verifique distinto → se declara y pasa marcado.
- El paso N falló → vuelve al paso N, no al N+1.
- En cualquier otro caso → se entrega y se cierra.
