# costo-del-error

**Variables:** afirmación · costo · umbral · abstención · consecuencia
**Peor:** el sistema acierta casi siempre y **falla justo donde más costaba**, porque el costo nunca se declaró/ Nadie puede decir que la decisión estaba mal tomada: estaba bien tomada con el precio equivocado/
**Quién:** quien paga la consecuencia, o `ninguno` si el error no le cuesta a nadie/

## Entra | Falla | Sale | Consume

- **Entra:** una respuesta que el sistema va a dar, y el contexto en el que se va a usar/
- **Falla:** se responde sin declarar cuánto cuesta equivocarse; se aplica el mismo umbral a un error barato y a uno caro; la abstención se juzga con la misma vara que el acierto/
- **Sale:** la respuesta con su costo declarado, su umbral y la decisión de contestar o abstenerse/
- **Consume:** quien usa la respuesta/ Con el costo declarado, decide si le alcanza/

## Tesis

**Sin costo no hay abstención/** Un sistema que no sabe cuánto cuesta equivocarse **siempre va a adivinar**, porque adivinar y acertar pesan lo mismo/ Y eso no es un defecto del modelo: es que nadie le dijo el precio/

La investigación de 2026 sobre alucinación lo demostró: *"under standard scoring, guessing is a dominant strategy"*/ Un modelo que adivina **le gana** a uno que se abstiene, aunque tenga más del triple de errores/ **No porque sea mejor: porque el marcador premia adivinar/**

Y el arreglo no es un modelo mejor/ Es **declarar el precio junto con la pregunta/**

## Proceso

### 1/ Declarar el costo

Antes de responder, el costo de equivocarse en **este** caso/

| Costo | Qué significa | Qué exige |
|---|---|---|
| **barato** | el error se corrige solo, y nadie lo paga | se responde con la mejor hipótesis |
| **caro** | alguien lo paga, y no se deshace | se exige recibo antes de responder |
| **irreversible** | el error no se corrige | **no se responde sin N1 o N2**, o se abstiene |

```
Costo: [barato|caro|irreversible] | Quién lo paga: [nombre|ninguno] | Se deshace: [sí|no]
```

### 2/ Declarar el umbral

**El umbral es lo que hay que saber para contestar**, y sale del costo:

```
Umbral: [qué habría que mostrar para contestar] | Si no se alcanza: [abstenerse y declarar Vacío]
```

**Sin umbral no hay decisión**, solo opinión con formato/

### 3/ Puntuar la abstención

**Abstenerse no es cero: cuesta, y cuesta distinto según el costo/**

| Si el costo es | Abstenerse vale |
|---|---|
| barato | poco: se espera que adivine |
| caro | lo mismo que acertar: se espera que declare |
| irreversible | **más que acertar**: se espera que no arriesgue |

**Regla:** el sistema que acierta con costo irreverible y el que se abstiene con el mismo costo **no se puntúan igual**/ Y el que adivina en irreversible **pierde**, aunque acierte/

### 4/ Contar el peor caso, no la media

**Un sistema con promedio alto y peor caso desastroso no sirve donde el costo es irreversible/** Se reporta el peor caso, y el peor caso se reporta **por costo**, no global/

```
Media: [n] | Peor caso: [n] | Peor caso en irreversible: [n]
```

## Prueba

¿Se declaró el costo antes de responder? ¿El umbral sale del costo? ¿La abstención se pinta distinto según el costo? ¿Se reporta el peor caso en lo irreversible?

**Falsificador:** se responde sin costo declarado; el mismo umbral para barato e irreversible; la abstención contada como cero; un promedio alto presentado sin su peor caso; adivinar en irreversible contado como acierto/

## Modos de falla

- **Costo decorativo/** Se declara después de responder, para cumplir/
- **Umbral fijo/** El mismo umbral para todo, y en lo caro adivina igual/
- **Abstención gratis/** Se cuenta como cero y por eso nunca conviene/
- **Peor caso escondido/** Se reporta la media y el desastre aparece en producción/
- **Irreversible sin recibo/** Se contesta lo irreversible con lo que se tiene, porque "algo es mejor que nada"/

## Transiciones

- El costo es irreversible y no hay recibo → `//trazar/md`, y si no se alcanza, `//nivel-de-fuente/md` con fecha de corte/
- El costo es caro y el que lo paga no está → `//////autoridad-yo/declarar-interes/md`/
- Hace falta declarar el vacío → `//trazar/md`, paso 5/
- En cualquier otro caso → se entrega y se cierra/
