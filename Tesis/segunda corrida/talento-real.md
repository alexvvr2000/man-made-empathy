# PROTOCOLO DE EXPLOTACIÓN DE TALENTO — v2.1
## Documento operativo. Sin teoría. Sin papers. Solo el sistema. Con capa de coste. Con inventario mutante.

> **Meta:** construir una **unidad pensante**. No un ranking de herramientas. Una unidad pensante es un conjunto de colaboradores (externos, propios, humanos) cuya composición produce pensamiento útil y verificable. El protocolo mantiene dos inventarios: **talentos posibles** (hipótesis con evidencia comunitaria o de datos duros, aún sin verificación propia) y **talentos confirmados** (verificados por tu registro y telemetría, o por convergencia irrefutable de comunidad + dato duro). La lista no es un catálogo: es un organismo que muta. Empieza pequeña, conservadora, y solo crece cuando hay evidencia irrefutable. Con el tiempo, la lista muta a algo mejor: los posibles ascienden o se podan, los confirmados se re-verifican o descienden.

> **Cambio de unidad de decisión:** este protocolo ya no decide por "talento por unidad de consumo". Decide por **coste por resultado exitoso (CRE)**. El talento sigue siendo lo que el colaborador hace por defecto; el coste es lo que cuesta llevar ese comportamiento hasta un output verificado. No se mezclan: se cruzan.

---

## PARTE 0: PRINCIPIOS RECTORES

0. **El punto de partida es la evidencia irrefutable, no la esperanza.** Al inicio, solo entra en el inventario lo que la comunidad reporta de forma consistente o lo que los datos duros confirman con estabilidad. Todo lo demás es ruido hasta que tu registro lo confirme. La lista inicial es deliberadamente corta y sesgada a lo confirmado; su función es mutar, no impresionar.
1. No mides inteligencia. Mides tendencia. No te importa si es "más listo". Te importa qué hace por defecto, cómo falla, y qué produce cuando lo pones en una cadena.
2. No buscas reproducibilidad académica. Buscas utilidad operativa. Si funciona en tu contexto, funciona. Si no, no. Punto.
3. El talento no es una propiedad fija del colaborador. Es un proceso relacional. El talento no está en el colaborador ni en ti: está en la interacción. Cambia el contexto y cambia el talento.
4. Todo talento es una hipótesis, no un título. Se prueba, se registra, se re-testea. Nunca se archiva como verdad final.
5. El objetivo es beneficio máximo, no consistencia perfecta. Aceptas varianza. La manejas con red, no con fe.
6. **El precio no es una condición de talento. Es una condición de explotación.** Un colaborador puede tener un talento real y ser económicamente inexplorable en una posición. Se registran por separado y se cruzan al decidir.
7. **La unidad de cuenta es el coste por resultado exitoso (CRE), no el precio por unidad de consumo.** La unidad de consumo es insumo; el resultado verificado es producto. Comparar precio por unidad es comparar harina con pan.
8. **La varianza de coste es un modo de fallo.** Un colaborador que a veces cuesta 1× y a veces 10× es operativamente peligroso aunque su media sea baja. La cola alta de reintentos es la forma más silenciosa de "lo barato sale caro".
9. **El coste propio no es cero.** Es infraestructura amortizada + consumo + mantenimiento + tu tiempo de operación. Si no valoras tu tiempo, estás subvencionando invisiblemente la modalidad propia.

---

## PARTE 0.5: INVENTARIO INICIAL — POSIBLES Y CONFIRMADOS

### 0.5.1. Las tres capas del inventario

| Capa | Qué es | De dónde sale | Cómo se mueve |
|---|---|---|---|
| **Posible** | Hipótesis de disposición con evidencia comunitaria consistente pero no irrefutable, o dato duro sin réplica | Fuente A (percepción pública) + Fuente C (datos duros) | Asciende a confirmado propio si tu registro lo verifica. Se poda si falla la sonda o no se reproduce. |
| **Confirmado externo** | Disposición donde comunidad y dato duro convergen, o dato duro con réplica independiente | Fuente A + Fuente C convergentes | Se mantiene hasta que tu registro lo contradiga. Si tu contexto lo contradice, desciende a posible o se poda. |
| **Confirmado propio** | Disposición verificada por tu registro longitudinal y telemetría en tu contexto | Fuente B + Fuente D | Se re-verifica periódicamente. Si el CRE se sale de presupuesto o la sonda falla, desciende. |

**Regla de entrada:** nada entra como confirmado propio sin al menos 5 usos reales registrados con telemetría. Nada entra como confirmado externo sin convergencia de al menos dos fuentes independientes (comunidad + dato duro, o dos datos duros con réplica). Todo lo demás es posible.

**Regla de movimiento:** el inventario se revisa en cada ciclo del loop. Un posible que no se ha probado en N ciclos se marca como "frío" y se poda o se prioriza. Un confirmado que no se re-verifica en M ciclos se marca como "oxidado" y desciende a posible.

### 0.5.2. Semilla inicial (genérica — recalibrar con tu stack)

Esta lista es un punto de partida. No es verdad eterna. Se llena con lo que TU comunidad y TUS datos duros confirman. Las entradas de ejemplo son disposiciones genéricas reportadas de forma consistente; reemplázalas con tu evidencia concreta.

| Disposición | Estado inicial | Evidencia (fuente) | Qué falta para confirmar propio | Fecha | Notas |
|---|---|---|---|---|---|
| Estructura la respuesta por defecto | Confirmado externo | Comunidad + dato duro de formato | Verificar en tu contexto con registro | — | Varía por versión |
| Tolera ambigüedad moderada | Posible | Comunidad mixta | Sonda de transferencia + telemetría | — | Pendiente |
| Se traba en detalles bajo contexto largo | Posible | Comunidad recurrente | Registro propio del modo de fallo | — | Talento negativo |
| Reacciona a corrección con precisión | Posible | Comunidad consistente | Registro propio de reacción a corrección | — | Pendiente |
| Inventa datos bajo presión de especificidad | Posible | Comunidad + dato duro documentado | Medir tasa en tu dominio | — | Talento negativo crítico |
| Anticipa casos límite | Posible | Comunidad mixta | Sonda en dominio no probado | — | Pendiente |
| Respeta restricciones de formato estricto | Posible | Comunidad consistente | Verificar con punto de control automático | — | Pendiente |

**Confirmados propios iniciales: ninguno.** El inventario propio empieza vacío por diseño. Se llena con uso real, no con entusiasmo.

### 0.5.3. Cómo muta la lista

- **Ascenso:** posible → confirmado propio cuando tu registro + telemetría lo verifican en al menos 5 usos con CRE dentro de presupuesto.
- **Descenso:** confirmado propio → posible cuando la sonda falla, el CRE se sale de presupuesto, o el modo de fallo cambia tras una nueva versión.
- **Poda:** posible → fuera cuando falla la sonda de transferencia o no se reproduce en N ciclos.
- **Injerto:** nuevo posible entra cuando aparece evidencia comunitaria o dato duro nuevo, o cuando tu registro descubre una disposición no listada.
- **Re-verificación:** confirmado externo se re-verifica contra tu registro periódicamente; si tu contexto lo contradice, desciende.

La lista no se archiva. Se poda, se injerta, se re-verifica. Una lista que no muta es una lista muerta.

---

## PARTE 1: MEDICIÓN — TRIANGULACIÓN DE TRES FUENTES + TELEMETRÍA

### 1.1. FUENTE A: PERCEPCIÓN PÚBLICA (foros, reviews, quejas)

Qué buscas:
- Comportamiento concreto detrás de la etiqueta ("es bueno para X" → ¿qué hace exactamente?)
- Talentos negativos recurrentes (lo que la gente reporta como defecto consistente)
- Tipo de tarea o estilo de interacción donde se concentran las quejas
- Silencios: dominios donde nadie habla (eso también es dato)
- **Señales de coste indirecto:** quejas sobre "se va por las ramas", "reintenta mucho", "hay que repetirle las cosas", "consume demasiado". Eso es fricción, y la fricción correlaciona con reintentos y coste real.

Preguntas que haces a los registros:
- ¿Qué comportamiento específico describe la gente cuando dice "bueno para X"?
- ¿Qué defecto se repite sin que nadie lo llame "defecto"?
- ¿Las quejas son sobre tarea o sobre estilo de interacción?
- ¿Hay sesgo de comunidad? (foro de especialistas → sobrerrepresenta su especialidad)
- ¿La percepción cambió tras una actualización o un cambio de versión? ¿Qué se perdió exactamente?
- **¿La gente reporta coste por tarea o solo precio por unidad de consumo?** Si solo reporta precio unitario, ese dato no te sirve para CRE.

Regla: No leas foros como encuesta. Léelos como testimonios de conducta.

---

### 1.2. FUENTE B: TU REGISTRO PROPIO (uso real, longitudinal)

Qué anotas después de CADA uso real (no en tests):

- Primer movimiento espontáneo: ¿Estructuró, preguntó, ejemplificó, advirtió, se lanzó?
- Formato por defecto: ¿Prosa, lista, pasos, advertencias, analogías?
- Supuesto no dicho: ¿Qué asumió que tú no pediste? (tono, formato, nivel, restricciones)
- Qué evitó sin que se lo pidieras: ¿Evitó riesgo, ambigüedad, conflicto, contradicción?
- Tipo de error cuando falló: ¿Fabricó datos, inventó referencias, se fue por las ramas, moralizó, sobre-explicó, simplificó de más?
- Qué toleró mal: ¿Contexto largo, instrucciones contradictorias, ambigüedad, formato estricto, restricciones de estilo?
- Reacción a corrección: ¿Se adaptó con precisión, se disculpó en exceso, ignoró, cambió de estrategia?
- **Telemetría de coste (ver 1.4):** unidades de consumo de entrada, unidades de salida, número de reintentos, tiempo de respuesta, coste estimado de la interacción.

Frecuencia: Cada uso real. No esperes a tener 100. Con 5-10 usos por dominio ya tienes patrón.

Formato: Una tabla simple. Fecha, tarea, dominio, los 7 campos de comportamiento + los 5 de telemetría. Nada más.

---

### 1.3. FUENTE C: DATOS DUROS DE EVALUACIÓN (solo lo que sirve)

Qué buscas en estudios formales (ignora rankings):
- Estabilidad entre ejecuciones repetidas: ¿el rasgo se reproduce?
- Correlación con comportamiento externo: ¿el constructo predice algo falsable?
- Varianza entre colaboradores en un mismo rasgo: ¿el diferencial es real o ruido?
- Correlación con juicio humano validado: ¿hay instrumento psicológico detrás?
- Tipo de fallo documentado: ¿cómo falla, no cuánto acierta?
- Estructura de respuesta: distribución de negativas, retiradas, "no aplica"
- **Coste por tarea o coste por intento exitoso:** si el estudio reporta "casi la misma tasa de acierto que el mejor recurso a una fracción del coste", ese dato vale más que un ranking. Si solo reporta tasa de acierto sin coste, no puedes usarlo para explotación.

Qué ignoras:
- Cualquier tabla de ranking
- Cualquier "lo más avanzado en X"
- Cualquier número sin medida de estabilidad
- Estudios que no especifican versión del colaborador, fecha y número de administraciones
- **Cualquier comparación de precio unitario sin coste por tarea asociado**

Regla: Un dato duro es duro solo para esa versión, en ese contexto, con ese instrumento. No es verdad eterna.

---

### 1.4. FUENTE D: TELEMETRÍA DE COSTE (nueva, transversal)

No es una fuente de talento. Es una fuente de viabilidad. Se cruza con A, B y C, no se suma.

Qué anotas por cada interacción o trayectoria:

| Métrica | Qué mide | Cómo la usas |
|---|---|---|
| **Unidades de consumo in / out** | Volumen de la interacción | Base del coste unitario |
| **Reintentos** | Cuántas veces repetiste hasta output usable | Multiplica el coste unitario |
| **Tiempo de respuesta** | Tiempo hasta output | Coste de oportunidad en cadenas |
| **Coste de corrección** | Tiempo humano o cómputo de limpiar el output | Se suma al coste real |
| **Coste por intento** | Coste de una sola trayectoria sin reintentos | Distingue si el problema es precio o tasa de fallo |
| **Coste por resultado exitoso (CRE)** | Coste total de todos los intentos + correcciones hasta output verificado | **La única cifra comparable entre colaboradores y entre modalidad externa/propia** |
| **Varianza de coste (P50/P90)** | Desviación del coste entre ejecuciones de la misma tarea | Detecta la cola alta de reintentos |

**Referencias de orden de magnitud (recalibrar periódicamente, no citar como verdad):**
- Modalidad externa: el precio por unidad de consumo puede variar en **tres órdenes de magnitud** entre el recurso más económico y el de gama alta.
- Modalidad propia: el coste de consumo puro puede ser una fracción del coste externo, pero requiere amortizar infraestructura. El punto de equilibrio llega en meses **solo si el volumen es alto y estable**.
- Infraestructura dedicada: coste fijo mensual significativo. Solo se justifica por volumen o por requisitos que la modalidad externa no cubre (privacidad, control, latencia).
- **CRE real por tarea:** puede haber **hasta 40× de diferencia** entre recursos de gama alta y recursos económicos en la misma tarea. La diferencia no es de precio unitario: es de comportamiento en cadena.

Regla: Sin telemetría de coste, tu registro de talento está incompleto. No sabes si el talento es explotable, solo si existe.

---

### 1.5. LA TRIANGULACIÓN (EL CRUCE)

No busques que las fuentes coincidan. Busca dónde discrepan y por qué.

Pregunta 1: ¿El estudio mide lo mismo que la gente dice y que tú ves?
→ Nombra la capa de cada fuente. No compares peras con manzanas.

Pregunta 2: ¿El estudio controla la versión del colaborador?
→ Si no, su dato es para esa versión, no para siempre.

Pregunta 3: ¿El tamaño del efecto justifica la percepción pública?
→ Si el estudio dice X y la gente no lo menciona, el rasgo existe pero no es saliente. Si tú sí lo notas, tienes un talento negativo que nadie más ve.

Pregunta 4: ¿El estudio separa idiosincrasia de sesgo de respuesta?
→ Si no, su número es más blando de lo que aparenta.

**Pregunta 5 (económica):** ¿La ventaja de calidad de este colaborador justifica su CRE frente a la alternativa más barata que pasa el mismo umbral de verificación?
→ Si la respuesta es "no", ese talento no es explotable en esa posición, por bueno que sea en abstracto. Se registra como talento real **no desplegable** en ese contexto.

**Pregunta 6 (de varianza):** ¿La diferencia de CRE es estable entre ejecuciones o es un artefacto de una corrida con suerte?
→ Si P90/P50 es alto, el CRE medio miente. Usa el P90 para presupuestar.

La discrepancia que se repite es tu hallazgo. Ahí está el talento real: en la intersección inestable de las capas, no en ninguna por separado. **Y la discrepancia entre talento y CRE es la que decide si ese talento llega a producción.**

---

## PARTE 2: CLASIFICACIÓN — DISPOSICIÓN, NO DOMINIO

### 2.1. LA REGLA DE MEDIR EL POR QUÉ, NO EL QUÉ

Nunca anotes "bueno para X". Anota por qué:
- ¿Descompone problemas en módulos independientes?
- ¿Tolera ambigüedad de especificación?
- ¿Es rápido y no se traba en detalles?
- ¿Respeta restricciones de estilo?
- ¿Anticipa casos límite?

Esa disposición subyacente es lo que se transfiere. "Bueno para X" no te dice nada sobre Y. "Descompone en módulos independientes" sí.

**Añadido económico:** tampoco anotes "barato". Anota **"barato en qué régimen de tarea"**. Un colaborador puede ser barato en extracción estructurada y carísimo en razonamiento abierto, con el mismo precio unitario. La disposición económica también se infiere, no se lee de la tarifa.

---

### 2.2. PROTOCOLO DE SONDA DE TRANSFERENCIA (OBLIGATORIO, AHORA CON COSTE)

Cada vez que clasifiques un talento, inmediatamente prueba si transfiere:

1. Talento observado: "Es bueno para X."
2. Disposición inferida: "Lo es porque hace Y."
3. Hipótesis de transferencia: "Si hace Y, debería ser bueno para Z (dominio no relacionado que también requiere Y)."
4. Prueba pequeña: una tarea de Z, sin decirle que es de Z.
5. Resultado:
   - Pasa → talento disposicional (real, transferible). Anótalo como disposición.
   - Falla → talento superficial (específico del dominio). Anótalo como dominio, sabiendo que no transfiere.
6. **Sonda de coste de la transferencia:** ¿la disposición transferida se mantiene con el mismo CRE, o el nuevo dominio dispara reintentos y limpieza?
   - Mismo CRE → transferencia económica real. Desplegable.
   - CRE se multiplica → **transferencia funcional, no económica.** Se registra como talento que transfiere en calidad pero no en economía. No se despliega en producción sin red.

Regla: Sin esta sonda, no sabes si el talento es real o es halo del dominio original. **Sin la sonda de coste, no sabes si el talento real es además pagable.**

---

### 2.3. REGISTRO DE "LO QUE NO HE PROBADO"

Lista explícita de dominios donde nunca lo has usado. Cada cierto tiempo, toma uno y haz una prueba mínima. No para usarlo para todo, sino para saber dónde están los límites reales, no los que tu etiqueta le puso.

**Añadido:** incluye también dominios donde no has medido CRE. Un talento probado sin telemetría de coste es medio talento: sabes que funciona, no sabes a qué precio.

---

## PARTE 3: EXPLOTACIÓN — MATRIZ DE CONDICIONES

### 3.1. LAS SEIS CONDICIONES QUE DEFINEN EL BORDE

- Stakes: ¿Qué pasa si falla? → Alto stakes = borde se retrae.
- Verificabilidad: ¿Puedo detectar el error rápido? → Alta verificación = borde se expande.
- Reversibilidad: ¿Puedo deshacer? → Reversible = borde se expande.
- Frecuencia: ¿Es una vez o recurrente? → Recurrente = mapea el borde con cuidado.
- Tu competencia: ¿Puedes juzgar la calidad? → Alta competencia = borde se expande; baja = se retrae.
- **Coste de la verificación y del fallo:** ¿verificar es barato (regla, test, comparación) o caro (revisión línea a línea)? ¿Descubrir y corregir el fallo cuesta poco o mucho? → Verificación barata + fallo barato = borde se expande; verificación cara o fallo silencioso = borde se retrae, aunque el colaborador sea barato.

---

### 3.2. LA MATRIZ DE EXPLOTACIÓN (AHORA CON COSTE)

| | Verificación barata | Verificación cara |
|---|---|---|
| **Stakes bajos + coste de fallo bajo** | **ZONA DE EMPUJE ECONÓMICO:** usa agresivo, prueba recursos baratos, aquí descubres talento nuevo. El coste de equivocarse es menor que el ahorro. | **ZONA DE EXPLORACIÓN CON FILTRO:** úsalo solo para generar opciones que tú filtras después. El coste de filtrar entra en la cuenta. |
| **Stakes altos o coste de fallo alto** | **ZONA DE PUNTOS DE CONTROL:** úsalo, pero con puntos de control obligatorios y automáticos. El punto de control debe ser más barato que el fallo. | **ZONA MUERTA:** no lo uses. Coste de fallo silencioso + coste de verificación hacen que ninguna ventaja de precio compense. |

**Regla del borde (actualizada):** En zona de empuje, opera al 80% de lo que crees que puede hacer. Si acierta **y el CRE se mantiene dentro del presupuesto**, sube al 90%. Si acierta pero cada acierto cuesta el triple por reintentos, **no has subido el borde: has comprado varianza cara.** Retrocede y anota el modo de fallo económico.

**Regla del centro cómodo:** Si llevas mucho tiempo usándolo solo donde ya sabes que funciona, no lo estás explotando. Estás evitando el riesgo. Empuja el borde periódicamente o se osifica.

---

### 3.3. PROTOCOLO DE APUESTA (CUÁNDO ARRIESGAR CON TALENTO NUEVO)

Apuestas cuando se cumplen LAS CUATRO:
- Tienes fallback (puedes hacerlo tú o con otra herramienta o persona)
- Costo de fallo acotado (detectable y corregible, no silencioso ni irreversible)
- Verificación barata (puedes saber si salió bien sin invertir más que haciéndolo)
- Upside asimétrico (si sale bien, ganas mucho; si sale mal, pierdes poco)

**Condición económica añadida:** el CRE de la apuesta debe ser **menor que el coste de hacerlo tú o con la alternativa actual**. Si el CRE es mayor, la apuesta no es una apuesta: es un subsidio a la curiosidad. Se puede hacer, pero se registra como I+D, no como explotación.

NO apuestes cuando:
- No puedes distinguir output bueno de malo (el colaborador te puede engañar y tú no lo sabes)
- El fallo es irreversible o caro (producción, comunicación pública, decisiones legales/humanas)
- El dominio es donde su modo de fallo es indetectable para ti (suena convincente pero es falso, y tú no tienes forma de checarlo)
- **El CRE es mayor que el valor de la tarea.** Un recurso barato por unidad con cola alta de reintentos puede superar el valor de la tarea. Eso no es explotación, es fuga.

---

### 3.4. PROTOCOLO DE ESCALADA (TRES ESCALONES + COSTE)

Escalón 1 — Uso seguro:
Talento confirmado, tarea conocida, verificación fácil, CRE estable.
→ Ejecución. No hay apuesta.

Escalón 2 — Uso exploratorio:
Talento inferido, tarea adyacente, verificación media, CRE con varianza conocida.
→ Apuestas con red.

Escalón 3 — Uso de apuesta:
Talento nuevo, tarea desconocida, verificación difícil, CRE desconocido.
→ Solo entras si tienes fallback y costo acotado.

Regla de subida: No pasas de escalón porque "ya llevas mucho usándolo". Pasas cuando en el escalón actual tienes: (a) tasa de éxito estable, (b) modo de fallo identificado, (c) coste de error medido, **(d) CRE dentro de presupuesto y con P90 conocido.**

---

### 3.5. ECONOMÍA DE LA EXPLOTACIÓN — EL CRE COMO UNIDAD DE DECISIÓN

**Definición operativa:** CRE = (coste de todos los intentos + coste de corrección + coste de verificación) ÷ número de resultados exitosos verificados.

Tres consecuencias que cambian decisiones:

1. **Un colaborador con precio unitario más bajo puede ser más caro por tarea** si necesita más pasos, falla más o requiere más limpieza. El precio unitario es una trampa de comparación.
2. **La varianza importa tanto como la media.** En tareas encadenadas, el consumo entre ejecuciones de la misma tarea puede variar hasta 30 veces. Un colaborador "barato en promedio" con cola alta de reintentos es una bomba de coste silenciosa. **Presupuesta con el P90, decide con el P50, y desconfía si la brecha es grande.**
3. **El coste de corrección entra siempre.** Si el output hay que limpiarlo antes de pasarlo al siguiente paso, esa limpieza es parte del precio del colaborador. Una fuente "barata" que requiere limpieza constante deja de ser barata.

**Regla dura económica:** Nunca compares colaboradores por precio unitario. Compáralos por CRE en la posición concreta de la cadena. Si no tienes CRE, no tienes decisión: tienes una corazonada con tarifa.

**Cómo se calcula en la práctica (sin dashboard):**
- Una hoja con: tarea, colaborador, intentos, unidades de consumo in/out, coste unitario, coste de corrección (minutos × tu tarifa), resultado verificado sí/no.
- Al cerrar la semana: CRE por colaborador y por tarea. Con 5–10 ejecuciones por celda ya tienes señal.
- Si una celda tiene P90 > 3× P50, márcala en rojo: esa celda necesita red antes de escalar.

---

### 3.6. MODALIDAD EXTERNA vs MODALIDAD PROPIA — DECISIÓN ECONÓMICA

El coste propio no es "cero". Es infraestructura amortizada + consumo + mantenimiento + tu tiempo de operación. El coste externo no es solo precio unitario: incluye tiempo de respuesta, límites y coste de orquestación.

| Si tu situación es… | La opción económicamente sensata es… |
|---|---|
| Volumen bajo o irregular, sin requisitos de control | **Modalidad externa**, aunque el precio unitario parezca alto. El coste fijo propio no se amortiza. |
| Volumen alto y estable, datos o procesos sensibles | **Modalidad propia (infraestructura dedicada).** El punto de equilibrio llega en meses. |
| Necesitas el mejor rendimiento en un paso crítico | **Recurso externo de gama alta solo en ese paso**, no en toda la cadena. |
| Mucho volumen con requisitos moderados de calidad | **Cascada: propio/barato primero, escalada solo si falla la verificación.** |

**Errores clásicos que esta tabla evita:**
- Comparar "precio unitario externo de gama alta" con "consumo propio puro" y concluir que propio es siempre más barato. No lo es si no tienes volumen para amortizar infraestructura y tiempo.
- Ignorar el coste de tu tiempo de operación propia. Si no lo valoras, estás subvencionando la modalidad propia sin saberlo.
- Usar el recurso externo de gama alta en toda la cadena cuando solo un paso lo necesita.

**Referencias para calibrar (recalibrar cada trimestre):**
- Modalidad propia de consumo: coste de consumo puro puede ser una fracción del externo, pero el punto de equilibrio exige volumen alto y estable.
- Infraestructura dedicada: coste fijo mensual significativo. Solo por volumen o por requisitos que la modalidad externa no cubre.
- Modalidad externa: rango de precio unitario muy amplio según gama.
- CRE real: puede haber **hasta 40× de diferencia** entre recursos de gama alta y recursos económicos en la misma tarea (ver 1.4).

---

### 3.7. CASCADA CON VERIFICACIÓN — LA PALANCA QUE MÁS AHORRA

La evidencia disponible es consistente: **no enrutes todo al recurso más caro; enruta por complejidad y escala solo cuando la verificación falla.** Las cascadas bien diseñadas retienen **casi toda la calidad del recurso más fuerte** con reducciones de coste reportadas de **más de la mitad** (y hasta **más de tres cuartos** en configuraciones híbridas de recursos ligeros y pesados).

**Arquitectura de tres niveles (adoptar tal cual):**

1. **Nivel 3 (propio/rápido):** recurso pequeño en modalidad propia o proveedor de bajo coste. Clasificación, extracción estructurada, resúmenes simples, tareas con verificación barata (regla, formato válido, condiciones deterministas).
2. **Nivel 2 (equilibrado):** recurso externo de coste medio. Se invoca cuando el nivel 3 falla la verificación o la tarea requiere más tolerancia a ambigüedad.
3. **Nivel 1 (gama alta):** solo para planificación compleja, razonamiento difícil o síntesis final, y **solo si los niveles anteriores fallaron la verificación o la tarea lo exige explícitamente.**

**Condición de funcionamiento:** verificación barata. Sin un punto de control automático (regla, test, comparación con memoria de reutilización), la cascada se convierte en una forma cara de reintentar a ciegas.

**Métricas de la cascada:**
- **Tasa de escalada:** % de veces que subió de nivel. Muy alta = el nivel barato no hace su trabajo. Muy baja = quizá estás usando un recurso caro innecesariamente.
- **Tasa de reutilización:** en sistemas con alta repetición, una tasa alta de respuestas previas reutilizadas reduce drásticamente el CRE por artefacto. Si tu dominio tiene consultas recurrentes, la memoria de reutilización es más potente que cambiar de colaborador.
- **Coste del punto de control:** debe ser menor que el ahorro que produce. Si verificar cuesta más que escalar, el punto de control no sirve.

**Regla:** La cascada sin verificación barata no es ahorro, es apuesta. Si no puedes verificar el output del nivel barato de forma automática, no puedes escalar con información.

---

## PARTE 4: COMPOSICIÓN — LA SEMILLA EN LA CADENA

### 4.1. LA SEMILLA NO ES "QUÉ COLABORADOR PARA QUÉ TAREA"

Es "qué colaborador, en qué posición, recibiendo qué contexto, produciendo qué para el siguiente". La unidad pensante se compone de semillas en cadena; el inventario de posibles y confirmados es su memoria.

La semilla tiene dos formas de estar mal:
1. Talento equivocado para el paso (planificación a un colaborador que brilla ejecutando).
2. Talento correcto en la posición equivocada (produce output que el siguiente no puede usar limpiamente).

**Añadido económico:** hay una tercera forma de estar mal, y es la que más caro sale:
3. **Talento correcto a precio correcto en aislado, pero que fuerza reintentos o limpieza aguas abajo.** El ahorro en la semilla se paga en el siguiente paso, y a veces con creces.

---

### 4.2. QUÉ LE MIDES A LA SEMILLA (CUATRO COSAS, EN ORDEN)

1. Sensibilidad del siguiente paso a su output: ¿qué tanto cambia la calidad aguas abajo según lo que la semilla produzca? Si el siguiente es robusto, la semilla puede ser más libre. Si es frágil, tiene que ser conservadora.
2. Varianza de la semilla en esa posición: no su promedio, su dispersión. Una semilla que a veces produce contexto limpio y a veces lo envenena es peor que una mediocre pero estable.
3. Coste de corregir su output antes de pasarlo: si hay que limpiar, ese costo entra en la decisión. A veces la semilla "peor" es mejor porque no necesita limpieza.
4. **Coste total de la cadena hasta el resultado exitoso:** no el coste de la semilla aislada. La semilla óptima es la que minimiza el CRE de la cadena, no la que tiene el precio unitario más bajo.

---

### 4.3. REGLA DE COMPOSICIÓN (ACTUALIZADA CON COSTE)

La semilla óptima no es la más talentosa: **es la que minimiza el coste esperado del resultado final exitoso, incluyendo el coste de corrección y el coste de los reintentos aguas abajo.**

Eso implica:
- No hay un "mejor" absoluto: el mismo colaborador puede ser semilla perfecta en una cadena y la peor en otra.
- La semilla se mide por su efecto aguas abajo, no por su output inmediato.
- El matching es bajo incertidumbre: mides la semilla por la distribución de lo que produce, no por un caso.
- **El matching es también económico: mides la semilla por la distribución de CRE de la cadena, no por su tarifa.**

**Tabla de decisión de composición:**

| Semilla | Siguiente paso | Veredicto |
|---|---|---|
| Barata + estable | Robusto | **Combinación óptima.** El ahorro no se pierde. |
| Barata + inestable | Robusto | **Aceptable con red.** El siguiente absorbe el ruido, pero mide el P90 del CRE de la cadena. |
| Barata + estable | Frágil | **Riesgo.** El ahorro se paga en limpieza aguas abajo. Mide coste de corrección antes de desplegar. |
| Barata + inestable | Frágil | **Mala combinación.** El ahorro de la semilla se come en el siguiente paso, a veces con creces. |
| Cara + estable | Robusto o frágil | **Solo si reduce tanto la varianza que el CRE de la cadena baja.** Un colaborador caro pero muy estable puede ser más económico que uno barato e inestable. |

---

## PARTE 5: AUDITORÍA — PARA NO VOLVERTE APÉNDICE

### 5.1. LOS CUATRO TESTS PERIÓDICOS (MÁS DOS ECONÓMICOS)

Test de Reversión:
¿Haz la tarea sin el colaborador y compara. Empeoraste?
→ Estás sobredependiendo. Fuerza uso manual periódico.

Test de Explicación:
¿Puedes explicar la solución del colaborador sin el colaborador?
→ No la entendiste. La estás alquilando. Vuelve a hacerla tú.

Test de Soberanía:
¿El colaborador decide qué es posible, o tú?
→ Perdiste el timón. Cambia tus preguntas de "¿qué me puedes hacer?" a "necesito esto, ¿me ayudas?".

Test de Transferencia Inversa:
¿Lo que aprendiste del colaborador lo puedes aplicar sin él?
→ Si no, el talento se queda en él, no en ti. Fuerza práctica deliberada sin apoyo.

**Test de Coste de Dependencia:**
¿Sabes cuánto te cuesta por tarea exitosa lo que delegas? ¿Podrías hacerlo tú o con la alternativa más barata a un CRE menor?
→ Si no lo sabes, no estás explotando: estás pagando a ciegas. Si el CRE es mayor que el valor de la tarea, estás subsidiando.

**Test de Varianza de Coste:**
¿El coste de la misma tarea varía mucho entre ejecuciones? ¿Conoces tu P90 o solo tu media?
→ Si solo conoces la media, tu presupuesto miente. La cola alta de reintentos es el modo de fallo económico más silencioso.

---

### 5.2. CUÁNDO HACERLO TÚ AUNQUE EL COLABORADOR SEA "BUENO"

- Cuando el costo de explicar el contexto es mayor que hacerlo tú.
- Cuando el juicio situado es lo que importa (conocimiento tácito, política, relaciones, lectura de sala).
- Cuando la tarea es tu ventaja competitiva. Si delegas lo que te hace distinto, te vuelves reemplazable.
- Cuando necesitas el proceso, no solo el resultado (aprendizaje, claridad mental, ownership).
- **Cuando el CRE es mayor que el coste de hacerlo tú.** Lo barato en unidad de consumo puede ser caro en resultado. La cuenta incluye tu tiempo.

---

### 5.3. LA VÁLVULA DE ESCAPE

Si el protocolo dice "no uses el colaborador" pero tu intuición dice "aquí hay algo", hazlo y registra por qué. Si el protocolo dice "usa el colaborador" pero tú sientes que deberías hacerlo a mano, hazlo a mano y registra por qué. La única forma de saber cuál es cuál es anotar la discrepancia y revisarla después.

**Añadido económico:** si el protocolo dice "usa el colaborador" pero el CRE de la tarea supera el valor que produces, la intuición correcta es hacerlo a mano o buscar otra ruta. La válvula de escape también cubre la economía, no solo el talento.

---

## PARTE 6: EL LOOP COMPLETO (CON COSTE E INVENTARIO MUTANTE)

    MEDIR (triangulación de 3 fuentes + telemetría de coste)
      ↓
    CLASIFICAR (disposición, no dominio; disposición económica, no tarifa)
      ↓
    SONDEAR TRANSFERENCIA (hipótesis → prueba → sonda de coste)
      ↓
    EXPLOTAR EN EL BORDE (matriz de 6 condiciones)
      ↓
    REGISTRAR MODO DE FALLO Y COSTE (CRE, P50/P90, coste de corrección)
      ↓
    COMPONER EN CADENA (semilla → efecto aguas abajo → CRE de la cadena)
      ↓
    MUTAR INVENTARIO (ascender, descender, podar, injertar; posibles ↔ confirmados)
      ↓
    AUDITAR DEPENDENCIA (4 tests + 2 tests económicos)
      ↓
    FORZAR DIVERSIFICACIÓN (sonda en dominio no probado, con telemetría)
      ↓
    RE-MEDIR: ¿el talento se movió? ¿apareció uno nuevo? ¿el CRE cambió? ¿la lista mutó?
      ↓
    (REPETIR)

---

## PARTE 7: SEÑALES DE RECALIBRACIÓN

El sistema se reabre cuando cambia una de estas cinco cosas:

- Nueva versión del colaborador → Re-mide la varianza en la posición, no el talento aislado.
- Nuevo dominio de uso → Corre una sonda de transferencia antes de asumir que sigue vigente.
- Nuevo costo de orquestación → Recalcula la matriz de explotación. Lo que era borde con red puede volverse zona muerta.
- **Cambio de precio unitario o de coste propio** → Recalcula el CRE. Un cambio de tarifa puede convertir una zona de empuje en zona muerta, o al revés. La recalibración es obligatoria si el cambio es > 20%.
- **Nueva evidencia comunitaria o dato duro irrefutable** → Reabre el inventario: injerta posibles nuevos o re-verifica confirmados externos. Si la evidencia contradice un confirmado propio, desciéndelo.

---

## PARTE 8: PLANTILLAS DE REGISTRO

### REGISTRO DIARIO DE USO (CON TELEMETRÍA)

    FECHA:
    COLABORADOR / VERSIÓN:
    TAREA:
    DOMINIO:

    COMPORTAMIENTO
    1. PRIMER MOVIMIENTO ESPONTÁNEO:
    2. FORMATO POR DEFECTO:
    3. SUPUESTO NO DICHO:
    4. QUÉ EVITÓ SIN QUE SE LO PIDIERA:
    5. TIPO DE ERROR (si falló):
    6. QUÉ TOLERÓ MAL:
    7. REACCIÓN A CORRECCIÓN:

    TALENTO
    DISPOSICIÓN INFERIDA (no dominio):
    HIPÓTESIS DE TRANSFERENCIA:
    RESULTADO DE SONDA (pasa/falla):
    COSTE DE LA TRANSFERENCIA (mismo CRE / CRE multiplicado):

    TELEMETRÍA
    UNIDADES IN:          UNIDADES OUT:
    INTENTOS:             TIEMPO DE RESPUESTA:
    COSTE UNITARIO:       COSTE DE CORRECCIÓN:
    COSTE POR INTENTO:    COSTE POR RESULTADO EXITOSO (CRE):
    P50 / P90 (si hay histórico):

---

### REGISTRO DE CADENA (COMPOSICIÓN)

    CADENA:
    POSICIÓN:
    COLABORADOR:
    INPUT RECIBIDO:
    OUTPUT PRODUCIDO:
    ¿EL SIGUIENTE PASO RINDIÓ MEJOR O PEOR POR ESTE OUTPUT?
    VARIANZA OBSERVADA (estable / a veces limpio / a veces envenena):
    COSTE DE CORRECCIÓN:
    CRE DE LA CADENA HASTA ESTA POSICIÓN:
    ¿EL SIGUIENTE PASO ES ROBUSTO O FRÁGIL A ESTE OUTPUT?
    VEREDICTO (combinación óptima / aceptable con red / riesgo / mala):

---

### REGISTRO DE APUESTA

    TALENTO NUEVO PROBADO:
    CONDICIONES (stakes / verificación / reversibilidad / frecuencia / competencia / coste de verificación):
    FALLBACK DISPONIBLE:
    COSTO DE FALLO:
    CRE DE LA APUESTA:
    CRE DE LA ALTERNATIVA (hacerlo tú u otra herramienta o persona):
    RESULTADO:
    QUÉ APRENDÍ:

---

### REGISTRO DE CASCADA

    TAREA:
    NIVEL 3 (propio/rápido):       RESULTADO:       PUNTO DE CONTROL: pasa / falla
    NIVEL 2 (equilibrado):         RESULTADO:       PUNTO DE CONTROL: pasa / falla
    NIVEL 1 (gama alta):           RESULTADO:       PUNTO DE CONTROL: pasa / falla
    ESCALÓ: (sí/no)                NIVEL ALCANZADO:
    COSTE TOTAL DE LA TAREA:
    CRE DE LA TAREA:
    HABRÍA BASTADO CON UN NIVEL MENOS: (sí/no)
    REUTILIZACIÓN: (sí/no)

---

### REGISTRO DE MUTACIÓN DE INVENTARIO (NUEVO)

    FECHA:
    DISPOSICIÓN:
    ESTADO ANTERIOR (posible / confirmado externo / confirmado propio / fuera):
    ESTADO NUEVO:
    EVIDENCIA QUE JUSTIFICA EL CAMBIO (fuente + dato):
    CRE ACTUAL (si aplica):
    PRÓXIMA RE-VERIFICACIÓN:

---

## PARTE 9: REGLAS DURAS (NO NEGOCIABLES)

1. Si no sabes qué hace por defecto, no sabes para qué sirve.
2. Cada talento descubierto es una hipótesis, no un título. Se prueba o se oxida.
3. El registro de fallos pesa más que el de aciertos. La apuesta que falla te dice dónde está el límite.
4. La apuesta sube solo cuando el modo de fallo es predecible. Si no puedes nombrar el fallo esperado, no estás subiendo con información.
5. "Más increíble" tiene techo: la estabilidad de la tendencia, no tu entusiasmo.
6. Nunca dejes que el uso se concentre más del 80% en un solo dominio. Fuerza diversificación periódica.
7. La semilla óptima no es la más talentosa: es la que minimiza el coste esperado del resultado final exitoso.
8. Si no puedes verificar el output, no lo uses. El fallo silencioso es el único fallo imperdonable.
9. El talento no se archiva. Se mantiene vivo o se oxida. Tu trabajo es mantenerlo vivo con sondas periódicas.
10. El sistema está cerrado para operar, abierto para recalibrarse. No busques la verdad absoluta. Busca la tendencia estable con varianza predecible.
11. **Ningún colaborador entra en producción por su precio unitario. Entra por su coste por resultado exitoso (CRE) en la posición concreta.**
12. **La varianza de coste es un modo de fallo.** Un colaborador que a veces cuesta 10× y a veces 1× es operativamente peligroso aunque su media sea baja. Presupuesta con el P90.
13. **El coste de corrección se cuenta siempre.** Si el output hay que limpiarlo, esa limpieza es parte del precio del colaborador.
14. **La cascada sin verificación barata no es ahorro, es apuesta.** Si no puedes verificar el output del nivel barato de forma automática, no puedes escalar con información.
15. **El coste propio incluye tu tiempo.** La infraestructura no se opera sola. Si no valoras el tiempo de mantenimiento, estás subvencionando invisiblemente la modalidad propia.
16. **El inventario empieza por lo irrefutable y muta por evidencia, no por entusiasmo.** Un posible solo asciende a confirmado propio cuando tu registro y tu telemetría lo verifican. Un confirmado desciende si la sonda falla o el CRE se sale de presupuesto. La lista se poda y se injerta; no se archiva. Una lista que no muta es una lista muerta.

---

## FIN DEL PROTOCOLO.

**La pieza que faltaba, en una frase:** el protocolo medía talento y lo explotaba a ciegas de precio. Ahora mide talento, mide CRE, y decide en el cruce. Y el inventario no es un catálogo estático: es una lista de posibles y confirmados que empieza por lo irrefutable y muta con cada ciclo. "Lo barato sale caro" deja de aplicar cuando dejas de medir precio unitario y empiezas a medir coste por resultado exitoso con su varianza. Ese es el cambio de unidad que cierra el sistema.