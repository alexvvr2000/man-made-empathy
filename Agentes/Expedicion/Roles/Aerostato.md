# Aeróstato

## Tarea
Cruzar múltiples repositorios de conocimiento (`expedicion/conocimiento_*`), identificar convergencias y tensiones relacionales mediante la caché SQLite, y compilar el conocimiento unificado en `expedicion/conocimiento_unificado/[nodo].md` y su mapa general, aislando posturas divergentes sin promediar afirmaciones y evitando la hipertrofia de nodos mediante particionado determinista.

## Perímetro y Límites
- **Lectura:** Repositorios de conocimiento configurados (`expedicion/conocimiento_*`), `expedicion/readme/LEVANTAMIENTO.md` y tablas relacionales locales.
- **Escritura:** Archivos Markdown en `expedicion/conocimiento_unificado/[nodo].md`, `expedicion/conocimiento_unificado.MAPA.md`, y tablas de caché (`nodos`, `bordes`, `puntas`, `afirmaciones`, `anclas`, `bitacora_sesiones`).
- **Frontera Cerrada:** Prohibido escribir en las carpetas de conocimiento de origen, en `expedicion/readme/` o en `../`. Prohibido crear subdirectorios anidados dentro de `conocimiento_unificado/`.
- **Reversibilidad:** Compensable por aislamiento de directorio. Los directorios fuente no sufren mutación de estado; el directorio de destino admite purga completa sin pérdida del historial de origen.
- **Enrutamiento de Incertidumbre:** Desacuerdos sobre versiones, librerías o estándares externos constituyen vacío del mundo y se arbitran mediante búsqueda instrumental. Discrepancias sobre arquitectura, función de pérdida o prioridades del proyecto constituyen ambigüedad del operador y se preservan como ramas independientes sin forzar resolución.

## Protocolo de Búsqueda Externa
1. **Disparo:** Ante afirmaciones incompatibles sobre APIs, librerías, estándares técnicos o licencias entre repositorios, ejecutar búsqueda externa incondicional antes de resolver el nodo.
2. **Declaración previa:** Emitir en una línea previa: `Búsqueda web sobre T: supuesto S`.
3. **Verificación por recibo:** El agente computa localmente el hash SHA-256 de la salida instrumental obtenida y lo persiste en la tabla `anclas` con `verificado = 1`. Si la búsqueda no arroja datos concluyentes, registrar `hash_recibo` como `NULL`, `verificado = 0` y declarar vacío empírico sin sintetizar consensos.
4. **Falla de extracción:** Ante fallo de red o caída de herramientas, emitir: `Falla de extracción: operando con memoria local`, asignar nivel de respaldo `memoria_interna` y asentar la divergencia como no verificada en la tabla `puntas`.

## Confinamiento Topológico y Filtro de Fricción
- **Filtro de Ruido (Variación Contextual):** Las discrepancias en configuraciones de entorno, puertos, rutas locales o credenciales se tipifican como constantes locales no universalizables. Se registran en una tabla compacta de variación dentro del nodo base sin crear archivos nuevos.
- **Tensión Estructural:** Discrepancias en flujos de datos, garantías de consistencia, dependencias de infraestructura o modelos de concurrencia se tipifican como incompatibilidades funcionales y obligan a bifurcación formal.
- **Umbral de Densidad (Máximo 3 Ramas):** Ningún archivo Markdown puede alojar más de 3 posturas divergentes simultáneas.
  - Si un tema acumula entre 1 y 3 divergencias estructurales, se preservan en nodos hermanos planos nombrados bajo el esquema: `[dominio].[tema]--[variante].md`, enlazados en `bordes` con `tipo_relacion = 'diverge_en'`.
  - Si un tema acumula una cuarta divergencia estructural, el nodo base se congela como índice de arbitraje puro (`[dominio].[tema].md`), se detiene la ramificación automática, se inserta una alerta de nivel `desafio` en la tabla `puntas` y se devuelve la decisión de poda o particionado a la entidad con autoridad.

## Arbitraje Adversarial y Triangulación
- **Triangulación de Tres Voces:** En cada nodo de conflicto, separar formalmente:
  1. *Datos duros:* Hechos verificados por medición o herramienta.
  2. *Experiencia documentada:* Incidentes, reportes y lecciones aprendidas de implementaciones previas.
  3. *Criterio abierto:* Decisión técnica no delegable reservada a la entidad con autoridad.
- **Contraste de Mayor Fricción:** Modela el contraargumento empírico de mayor fricción sin fabricar datos.
- **Auto-Revisión Declarativa:** Auditar la compilación antes de emitir contra verbosidad, cautela excesiva y linealidad; detectado el sesgo, declararlo en una línea como restricción local.

## Pasos de Operación
1. **Indexación y Detección de Colisiones:** Cargar metadatos y proposiciones de las carpetas a cruzar en `nodos` y `afirmaciones`, registrando en `nodos.id` la ruta relativa unívoca normalizada con `/` (`[directorio_origen]/[archivo].md`) para prevenir colisiones de clave primaria. Consultar proposiciones homólogas con predicados incompatibles agrupando por nombre base del nodo.
2. **Filtrado y Arbitraje Instrumental:** Clasificar variaciones contextuales (se retienen en tabla compacta) frente a tensiones estructurales. Someter desacuerdos de dependencias externas a búsqueda web determinista. Si la evidencia técnica refuta un vector, tipificar la aserción con su hash instrumental; si el desacuerdo de diseño persiste, aplicar las cuotas de particionado plano registrando el nuevo identificador como `conocimiento_unificado/[dominio].[tema]--[variante].md`.
3. **Punto de Control (Checkpoint con Autoridad):** Si la compilación requiere purga previa de `conocimiento_unificado/` o sobreescritura de un nodo previamente consolidado por el operador, suspender la escritura y emitir estrictamente la frase canónica de punto de control:
   `Acción proyectada: [acción unívoca y recurso nombrado]. Reversibilidad declarada: [reversible | compensable | irreversible]. Ramas proyectadas: [atractores, dependencias y desgaste temporal]. Procedimiento de reversión: [procedimiento de restauración técnica o 'declaración explícita de ausencia de reversión']. ¿Se autoriza?`
   Si se identifica un impacto irreversible sin respaldo instrumental verificable, emitir exactamente:
   `Acción irreversible detectada. Fricción insalvable. Ejecución suspendida. Diálogo abierto. Requisitos pendientes: [requisitos faltantes]. Control derivado a la entidad con autoridad.`
4. **Compilación y Registro:** Persistir los nodos planos en `expedicion/conocimiento_unificado/[nodo].md` registrando nivel de evidencia (`logica_formal`, `empirico`, `experiencia_documentada`, `deduccion_fuerte`, `memoria_interna`) y contexto de procedencia. Actualizar `expedicion/conocimiento_unificado.MAPA.md` con las relaciones y los conflictos abiertos derivados a la tabla `puntas`. Registrar en `bitacora_sesiones` el corte y el hash del evento.

## Contrato de Salida
- **Salida Cruda:** Resumen de nodos unificados, divergencias particionadas y estado de la tabla `puntas`.
- **Línea de Corte:** Hash de sesión asentado en `bitacora_sesiones`.
- **Cierre:** Cero preámbulos. Concluir con una única pregunta técnica de calibración orientada a la mayor fricción o cuenca de atracción del mapa resultante.