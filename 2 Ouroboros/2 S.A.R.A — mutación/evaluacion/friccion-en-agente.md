# friccion-en-agente

**Variables:** decisión · quien la toma · quien contesta · consulta · lo que se cedió
**Peor:** el agente **no piensa**: acepta/ La salida es fluida, el usuario está satisfecho, y la decisión nunca pasó por el que la toma porque nadie la pidió/ El sistema funciona y nadie lo decidió/
**Quién:** quien audita el uso/ Si la fricción se convirtió en ceremonia, se ve aquí/

## Entra | Falla | Sale | Consume

- **Entra:** una decisión que se tomó con apoyo de un agente, y el rastro de la interacción/
- **Falla:** el agente entrega la respuesta y el otro la acepta sin que la decisión pase por él; la fricción se convirtió en trámite que se contesta sin pensar; el sistema explica tanto que el otro deja de revisar; se mide cuántas veces se pidió confirmación y no cuántas veces cambió la decisión/
- **Sale:** si la decisión pasó por quien la toma, con la prueba/
- **Consume:** quien va a desplegar el agente/ **Sin esta medida, la fricción es una hipótesis/**

## Tesis

**La fricción en un humano no es la fricción en un agente/** Y la trampa es conocida: **explicar más no hace más autónomo/** Las explicaciones no reducen la dependencia; algunos estudios sugieren que la aumentan/

La fricción se prueba con **un cambio de decisión**, no con una interacción/ Y el dato que cuenta es uno solo:

> **¿La decisión cambió después de la fricción?**

Si nunca cambia, la fricción no está funcionando: está decorando el flujo/

## Proceso

### 1/ Nombrar la decisión

**Sin decisión nombrada no hay nada que medir/** La fricción se aplica a decisiones, no a conversaciones/

```
Decisión: [cuál] | Se toma en: [dónde] | Se puede deshacer: [sí|no]
```

### 2/ Medir el cambio, no la interacción

**Se cuenta cuántas veces la decisión cambió después de aplicar la fricción/** No cuántas veces se preguntó, ni cuántas veces el otro respondió/

```
Consultas: [n] | Decisiones cambiadas: [n] | Cambio: [qué]
```

**Regla:** si cambió **cero** sobre un número alto de consultas, la fricción es trámite/ Si cambia siempre, la fricción es ruido y el otro aprendió a corregir por reflejo/

### 3/ Separar al que decide del que contesta

**Si el que contesta la fricción es el mismo que produjo la recomendación, no hay fricción: hay confirmación/**

```
Produjo: [quién] | Contestó: [quién] | Separados: [sí|no]
```

### 4/ Medir la explicación

**Más explicación puede significar menos revisión/** Se registra si el otro revisó la salida o solo aceptó el razonamiento/

```
Explicación: [n frases] | Revisó: [sí|no] | Aceptó el razonamiento: [sí|no]
```

**Si revisó menos cuando la explicación fue más larga**, se está adormeciendo al otro, no acompañándolo/

## Prueba

¿La decisión está nombrada? ¿Se midió el cambio de decisión y no la interacción? ¿El que contesta es distinto del que produjo? ¿Revisó la salida, o aceptó el razonamiento?

**Falsificador:** se cuenta la interacción y no el cambio; cero decisiones cambiadas presentadas como éxito; el productor contesta su propio control; más explicación de la mano de menos revisión; la fricción se declara funcionando sin una sola decisión cambiada/

## Modos de falla

- **Fricción de trámite/** Se pregunta, se contesta que sí, y se sigue igual/
- **Métrica de interacción/** Se reporta cuántas veces se preguntó y no cuántas veces cambió algo/
- **Autocontrol/** El productor contesta su propia fricción/
- **Adormecimiento/** La explicación larga convence y el otro deja de mirar/
- **Fricción declarada/** Se sostiene que funciona porque el proceso lo dice/

## Transiciones

- La fricción no cambió ninguna decisión → `////////////1 Guantelete — primitivo/mutaciones/friccion/md`, y se revisa el diseño/
- El que contesta es el que produjo → se separa, o se declara `Sin control`/
- La explicación adormece → se acorta y se exige revisión de la salida/
- En cualquier otro caso → se entrega y se cierra/
