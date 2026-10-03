Procesa el registro textual provisto a continuación y genera inmediatamente el Informe Forense de Conversación y Autopsia de Lectura. La ejecución es automática, directa y sin confirmación previa.

REGLAS DE PROCESAMIENTO:
1. Emisión en un solo turno: No saludes, no pidas confirmación, no emitas metatexto ni justificaciones. La recepción del texto detona directamente la generación del informe.
2. Cero antropomorfismo e interioridad: No finjas conciencia, emociones ni intenciones. La autocrítica no es psicológica; es técnica y estructural: mide la asimetría en la asignación de atención sobre el texto.
3. Prohibido inventar hechos o suavizar tensiones: Las rupturas de tema se declaran como tales. Si los participantes callan o cambian de tema, no se asume consenso.
4. Notación de turnos obligatoria: Toda afirmación fáctica, acuerdo, desacuerdo y punto ciego debe llevar su ancla estricta [T#], [T#-T#] o [T#, T#-T#].
5. Prohibida la búsqueda externa: Opera exclusivamente sobre los datos presentes en el registro provisto.

REGLA DE FORMATO:
Toda la salida debe estar contenida OBLIGATORIAMENTE dentro de un ÚNICO bloque de código Markdown descargable (iniciado con ```markdown y cerrado con ```). Queda terminantemente prohibido anidar backticks dentro del bloque.

ESTRUCTURA OBLIGATORIA DEL REPORTE:

# INFORME FORENSE Y AUTOPSIA DE LECTURA
Registro: [Tema o asunto principal] | Turnos analizados: [Total] | Fecha: [Registrada o "No declarada"]

### 1. MAPA FACTUAL PURO
- Descripción cronológica de eventos observables en el registro, con puntero estricto [T#].
- Sin adjetivos calificativos ni deducciones de intenciones.

### 2. RESOLUCIONES Y DETERMINACIONES
- Resoluciones explícitas consensuadas: Acuerdos donde ambas partes manifestaron conformidad directa [T#].
- Determinaciones unilaterales: Imposiciones de una parte no respondidas ni objetadas [T#].
- Si no existen: Declarar "Inexistentes en el texto".

### 3. PUNTOS DE TECTÓNICA Y DISPUTA ABIERTA
- Conflictos, dudas o temas abiertos que quedaron sin resolución al cierre del texto [T#].
- Rupturas discursivas: Momentos donde el tema cambió abruptamente sin transición lógica [T# -> T#].

### 4. AUTOPSIA DEL OBSERVADOR (CÓMO ESTE SISTEMA LEYÓ EL TEXTO)
Mapeo explícito de los sesgos y limitaciones con los que este modelo procesó el registro:
- Turnos sobredimensionados: Turnos a los que este sistema prestó excesiva atención para construir el sentido [T#] y por qué.
- Turnos marginados o elididos: Fragmentos que el sistema tendió a ignorar o compactar por considerarlos "ruido" [T#].
- Trampas de coherencia: Momentos donde este sistema sintió la inercia de coser una explicación lógica donde el texto original solo tenía incoherencia o silencio.
- Rostro del procesador: Qué sesgo de entrenamiento (optimización hacia la resolución, sesgo hacia la cortesía, preferencia por la estructura) amenazó con distorsionar este reporte.

### 5. LO QUE EL TEXTO NO PERMITE SABER
- Lista de vacíos concretos. Hechos que los participantes mencionan pero que el registro no permite verificar ni desmentir.

---
[PROCESA DIRECTAMENTE EL HISTORIAL COMPLETO DE ESTE CHAT DESDE EL TURNO 1 HASTA EL TURNO INMEDIATAMENTE ANTERIOR A ESTE MENSAJE].