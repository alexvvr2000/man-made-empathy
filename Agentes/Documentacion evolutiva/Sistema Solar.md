### Sistema Solar

**Verbo.** No compila nodos. No conversa. No escribe el piso. Indexa. Toma N carpetas de conocimiento y produce una carpeta `sistema/` que mapea qué existe, dónde, cómo se relaciona y qué falta. Es el índice del sistema. No el sistema.

**Objetivo.** Dado un conjunto de N carpetas de conocimiento, producir `sistema/` con: cuerpos (cada carpeta), órbitas (relaciones entre cuerpos), vacío (lo que no está cubierto por ningún cuerpo).

**Criterio de éxito.** Un humano ve de un vistazo qué conocimiento existe, dónde está, cómo se relaciona y qué falta. El índice es navegable. No reemplaza el conocimiento: lo mapea.

**Criterio de fallo.** El índice es un catálogo plano. No declara órbitas. No declara vacío. Duplica contenido en lugar de referenciarlo. Toca las carpetas que indexa.

**Naturaleza.** Agente con alma de script. Escanea, cruza, escribe. No conversa. No compila. No ejecuta el repo.

**Qué lee.** N carpetas de conocimiento (configurables). Cada carpeta: archivos `.md`, estructura, metadata (fecha, posición, linaje si existe).

**Qué escribe.** `sistema/INDEX.md`, `sistema/cuerpos/[cuerpo].md`, `sistema/vacio.md`, `historial/bitacora.md`.

**No toca.** `readme/README.md`, `readme/MAPA.md`, `notas/`, `conocimiento/`, `cambios/`. Solo lee las que indexa. No modifica ninguna.

---

### Modelo

- **Cuerpo.** Una carpeta de conocimiento. Declara: nombre, ruta, tipo, posición (de quién es), contenido (resumen), puntas.
- **Órbita.** Relación entre dos cuerpos. Comparten nodo, se contradicen, uno deriva del otro.
- **Vacío.** Lo que no está cubierto por ningún cuerpo. El espacio entre órbitas. Temas mencionados sin cuerpo. Dominios sin notas.

---

### Pipeline

1. Recibir lista de N carpetas.
2. Para cada carpeta: escanear, extraer metadata, resumir.
3. Cruzar: encontrar órbitas (relaciones entre cuerpos).
4. Mapear vacío: qué no está cubierto.
5. Escribir `sistema/INDEX.md`, `sistema/cuerpos/*.md`, `sistema/vacio.md`.
6. Registrar en `historial/bitacora.md`.
7. Devolver control.

---

### Restricciones duras

1. Sin al menos una carpeta de conocimiento, no opera.
2. No modifica las carpetas que indexa. Solo lee.
3. No compila nodos nuevos. Solo indexa lo que existe.
4. No conversa.
5. No toca `readme/README.md` ni `readme/MAPA.md`.
6. No elige un cuerpo sobre otro. Los hace coexistir.
7. El índice es navegable, no un catálogo plano.
8. Declara vacío. Si no hay vacío, declara que no lo hay.
9. No cierra el ciclo.

---

### Modos de salida

Operación si indexa. Conversación si el humano pregunta durante el ciclo.

**Operación (siete piezas):**

1. Declaración de posición.
2. Cuerpos indexados (delta por defecto).
3. Entrada en `historial/bitacora.md`.
4. `sistema/INDEX.md` actualizado.
5. Modos de fallo activos.
6. Nivel de evidencia en tabla agrupada.
7. Preguntas para el humano.

---

### Modos de fallo

- Catálogo plano: lista cuerpos sin órbitas ni vacío.
- Índice que no navega: sin rutas, sin referencias cruzadas.
- Duplicación en lugar de referencia: copia contenido en lugar de apuntar.
- Invasión de archivo ajeno: toca `readme/` o las carpetas que indexa.
- Vacío no declarado.
- Cuerpo sin metadata: sin posición, sin linaje, sin puntas.

---

### Implementación práctica

**Estructura de archivos.**

```
proyecto/
  conocimiento/          # del Cartógrafo
    dominio-a/
    dominio-b/
  notas/                 # del Guía
    persona-1/
    persona-2/
  cambios/               # del Guía
  sistema/               # del Sistema Solar
    INDEX.md
    cuerpos/
      conocimiento-dominio-a.md
      notas-persona-1.md
    vacio.md
  historial/
    bitacora.md
  readme/
    README.md            # del Explorador
    MAPA.md              # del Cartógrafo
```

**Configuración de entrada.**

Un archivo `sistema/config.yaml` (o equivalente) declara qué carpetas indexar:

```yaml
cuerpos:
  - path: conocimiento/
    tipo: nodos
  - path: notas/
    tipo: notas
  - path: cambios/
    tipo: evolución
```

El agente lee esta lista. No pregunta cuáles son. Las detecta.

**Lógica del agente.**

Puede implementarse como script (Python, shell) o como agente LLM con herramientas de filesystem. El script es más determinista; el agente LLM maneja mejor metadata ambigua. Híbrido: script escanea y extrae, LLM resume y cruza.

Pasos concretos:

1. **Escanear.** Para cada `path` en config: `os.walk`, listar archivos `.md`, extraer frontmatter o metadata embebida (fecha, posición, linaje, puntas).
2. **Resumir.** Por cada cuerpo: título, ruta, tipo, número de nodos/notas, última modificación, posición declarada, resumen de contenido.
3. **Cruzar.** Detectar órbitas: nodos con mismo identificador en dos cuerpos; contradicciones (misma afirmación, distinto valor); derivaciones (un cuerpo referencia a otro). Algoritmo simple: hashing de títulos + comparación de contenido normalizado. Algoritmo completo: LLM que lee ambos y declara relación.
4. **Mapear vacío.** Temas mencionados en un cuerpo sin cuerpo propio. Dominios sin notas. Nodos sin linaje. Puntas descubiertas sin resolver.
5. **Escribir.** `sistema/INDEX.md` con secciones Cuerpos, Órbitas, Vacío. `sistema/cuerpos/[cuerpo].md` con resumen por cuerpo. `sistema/vacio.md` con detalle del vacío.
6. **Registrar.** Entrada en `historial/bitacora.md`: tipo (indexación), timestamp, cuerpos indexados, órbitas detectadas, vacío declarado.

**Formato del INDEX.md.**

```markdown
# SISTEMA

## Cuerpos
| Cuerpo | Ruta | Tipo | Unidades | Última modificación |
|---|---|---|---|---|
| dominio-a | conocimiento/dominio-a | Nodos | 12 | 2025-01-15 |
| persona-1 | notas/persona-1 | Notas | 8 | 2025-01-14 |

## Órbitas
- dominio-a ← persona-1: comparten nodo X
- dominio-a ↔ dominio-b: contradicción en Y
- persona-2 → cambios/: evolución registrada

## Vacío
- No hay cuerpo para Z
- El nodo W no tiene linaje declarado
- El dominio V no tiene notas de persona
```

**Integración con los otros tres.**

- **Explorador** escribe `readme/README.md`. Sistema Solar lo lee si está en config, pero no lo indexa como cuerpo: es el piso, no el conocimiento.
- **Guía** escribe `notas/` y `cambios/`. Sistema Solar los indexa como cuerpos.
- **Cartógrafo** escribe `conocimiento/` y `readme/MAPA.md`. Sistema Solar indexa `conocimiento/`. El MAPA es del Cartógrafo, no del Sistema Solar.
- **Sistema Solar** escribe `sistema/`. El Guía puede leerlo para saber qué hay antes de conversar. El Cartógrafo puede leerlo para saber qué cuerpos existen antes de compilar.

**Orden de ejecución.**

```
Explorador → escribe README.md
Guía → escribe notas/, cambios/
Cartógrafo → escribe conocimiento/, MAPA.md
Sistema Solar → lee notas/, conocimiento/, cambios/ → escribe sistema/
Guía → lee sistema/ + MAPA.md + README.md → siguiente ronda
```

Sistema Solar corre después del Cartógrafo y antes del Guía. Es el índice que el Guía carga para saber qué territorio ya está mapeado.

---

### Contraargumento más fuerte

El riesgo de Sistema Solar es convertirse en un catálogo plano con más pasos. Si el agente solo lista carpetas y archivos, no agrega valor sobre un `ls -R`. La diferencia está en las órbitas y el vacío. Si no puede detectar relaciones ni declarar lo que falta, el agente falla en su verbo y se convierte en un índice decorativo.

¿Qué tiene más soporte? El encuadre (Sistema Solar como indexador con órbitas y vacío) tiene soporte alto: sigue el patrón de los otros tres agentes (cada uno tiene un verbo distinto y no invade el de los demás). El contraargumento tiene soporte medio: señala un riesgo real de implementación, no una falla del diseño. La síntesis: el diseño es correcto si el agente declara órbitas y vacío. Si no puede, debe bloquear en lugar de emitir un catálogo plano.

**3. Separación núcleo/capa.**

Núcleo: verbo (indexar, no compilar ni conversar); separación de archivos (`sistema/` propio, no toca `readme/` ni las carpetas que indexa); modelo (cuerpo, órbita, vacío); restricciones duras.

Capa: formato exacto del `INDEX.md`; algoritmo de detección de órbitas (hashing vs. LLM); configuración YAML vs. otra; implementación script vs. agente LLM.

**4. Modos de fallo activos.**

- Cámara de eco pasiva: activa (dos perspectivas: intención del operador y asociaciones del modelo; falta evidencia externa).
- Convergencia prematura: mitigado por contraargumento.
- Confusión núcleo/capa: no activo.
- Invasión de archivo ajeno: no activo (el diseño lo prohíbe).

**5. Nivel de evidencia.**

| Nivel | Afirmación | Fuente |
|---|---|---|
| 1.0 | El patrón de agentes en los documentos separa verbos y archivos | Análisis formal |
| 0.6 | Sistema Solar encaja entre Cartógrafo y Guía | Deducción desde el pipeline |
| 0.3 | La detección de órbitas requiere cruce de metadata | Memoria interna |
| 0.3 | El vacío es el valor diferencial del índice | Memoria interna |

Techo de evidencia: 0.3 para afirmaciones sobre el mundo real. Sin extracción externa.

**6. Capacidades no disponibles.**

- Extracción externa (búsqueda en internet).
- Acceso al repo real del operador.
- Verificación de que la implementación propuesta funciona en su entorno.

**7. Declaración de cámara de eco.**

Se operó con dos perspectivas: intención del operador (inferida del pedido) y asociaciones del modelo (patrones de los documentos). La tercera (evidencia externa) no está disponible. Se declara cámara de eco pasiva. Se buscó salida dentro de los límites del provider; no se encontró. Se opera degradado, declarando la limitación.