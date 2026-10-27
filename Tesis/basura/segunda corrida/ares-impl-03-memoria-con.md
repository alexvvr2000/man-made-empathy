# Memoria — configuración con corto y largo plazo

> Se lee junto a `ares-protocolo.md` y al perfil. Solo incluye lo que cambia cuando hay memoria.
>
> La expresión no cambia por tener memoria: APRIL sigue emitiendo en registro legible, o en nativo con transferencia. Lo que cambia es que puede confirmar sin releer.

## 4. Memorias

### 4.1 Corto plazo — Kestrel con el corpus caliente

- **Qué es:** lo que el agente aprendió en uso y tiene a mano. El modelo ya sabe sintaxis; Kestrel **no enseña, confirma**, y con memoria a corto plazo confirma sin volver a leer el disco.
- **Ventaja:** el corpus queda cargado y lo aprendido no se pierde entre turnos; la verificación es inmediata porque el texto ya está en memoria.
- **Vida:** se reconstruye al reiniciar —hay que volver a rastrear— y se vuelve a calentar con el uso.

### 4.2 Largo plazo

- **Qué es:** conceptos, patrones, decisiones y experiencia. **Version-agnóstico**: no caduca con `npm install` ni con el stack utilizado.
- **Ejemplos:** «componentes pequeños evitan el fallo intermitente de HMR», «WAL reduce locks de miles/hora a cero», «SQLite es muchos lectores / un escritor; el paralelismo de escritura no existe».
- **Herramienta:** SQLite (`dsh-sql`) con `SELECT` proyectado + `LIMIT` **200–300**. Sin embeddings, sin `dsh-library`, sin `indexOf`.
- **Alimentación:** **consolidación deliberada** cuando un aprendizaje se repite o demuestra valor. No es automático por `npm install`.
- **Vida:** **no se toca al actualizar**. Los conceptos sobreviven porque nunca dependieron de la versión.

### 4.3 Router

Una sola pregunta: **¿se está aprendiendo algo ahora (Kestrel confirma) o recordando algo ya aprendido (largo plazo)?**

- «¿Cómo se llama este método?» → el modelo lo sabe; Kestrel confirma.
- «¿Esto es verdad en la versión instalada?» → Kestrel.
- «¿Qué patrón funcionó la última vez?» → largo plazo.
- «¿Qué se decidió y por qué?» → largo plazo.

## Docs y memoria

Con memoria a corto plazo el corpus se mantiene caliente y lo aprendido se acumula entre turnos. Esa es la ventaja de esta variante, no un requisito de Kestrel: sin memoria, Kestrel sigue funcionando, solo que contra los archivos cada vez.

## Internet

Se busca capacidad, no forma.

- **Una pregunta, un medio.** Si el dato está en las docs locales, no se busca; si no está, se busca una vez.
- **Presupuesto:** 3 por tarea; la cuarta se declara y se justifica.
- **Caché con vigencia:** versiones 30 días, precios o cuotas 7, conceptos sin fecha. Antes de buscar, se lee el caché.
- **Huella, no copia:** extracto + URL + autor + fecha de corte. Lo que no cambió se escribe como `descarte`.
- **Capacidad, no forma:** se pregunta «¿existe?», «¿cómo se llama?», «¿qué límite tiene?». Nunca «¿cómo se ve?».
- **Diferencia obligatoria:** si una búsqueda produce una forma, se declara en qué se diferencia del ejemplo. Sin diferencia, el ejemplo sobra.
- **Gusto:** solo lo escribe la autoridad, nunca una búsqueda.
- **Promoción:** web → candidato → prueba local → fila del atlas. Lo que no pasa, se descarta.

## Resumen

La implementación usa Svelte + Vanilla + GSAP en Electron, docs espejados con `httrack` y verificados por Kestrel, SQLite para lo que sobrevive a la versión, APRIL como skill de expresión y memoria a corto plazo para confirmar sin releer.
