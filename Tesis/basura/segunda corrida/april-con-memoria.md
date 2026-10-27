# APRIL — variante con memoria

> Esta parte se lee junto a `compartido.md`. Aquí solo lo que cambia cuando hay memoria.

## 4. Memorias

### 4.1 Corto Plazo — Kestrel con el corpus caliente

- **Qué es**: lo que el agente aprendió en uso y tiene a mano. El modelo ya sabe sintaxis; Kestrel **no enseña, confirma**, y con memoria a corto plazo confirma sin volver a leer el disco.
- **Ventaja**: el corpus queda cargado y lo aprendido no se pierde entre turnos; la verificación es inmediata porque el texto ya está en memoria.
- **Vida**: se reconstruye al reiniciar —hay que volver a rastrear— y se vuelve a calentar con el uso.

### 4.2 Largo Plazo

- **Qué es**: conceptos, patrones, decisiones y experiencia. **Version-agnóstico**: no caduca con `npm install` ni stack utilizado.
- **Ejemplos**: "componentes pequeños evitan el fallo intermitente de HMR", "WAL reduce locks de miles/hora a cero", "SQLite es muchos lectores / un escritor; el paralelismo de escritura no existe".
- **Herramienta**: SQLite (`dsh-sql`) con `SELECT` proyectado + `LIMIT` **200–300**. Sin embeddings, sin `dsh-library`, sin `indexOf`.
- **Alimentación**: **Consolidación deliberada** cuando un aprendizaje se repite o demuestra valor. No es automático por `npm install`.
- **Vida**: **No se toca al actualizar**. Los conceptos sobreviven porque nunca dependieron de la versión.

### 4.3 Router

Una sola pregunta: **¿estoy aprendiendo algo ahora (Kestrel confirma) o recordando algo ya aprendido (largo plazo)?**

- "¿Cómo se llama este método?" → modelo lo sabe; Kestrel confirma.
- "¿Esto que estoy diciendo es verdad en la versión instalada?" → Kestrel.
- "¿Qué patrón me funcionó la última vez?" → largo plazo.
- "¿Qué decidimos y por qué?" → largo plazo.

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
## 10. En Una Frase

**Svelte + Vanilla + GSAP (2D y 3D falso) en Electron nativo, docs rastreables con `httrack`, Kestrel para corto plazo y SQLite para conceptos a largo plazo, `dsh-agent-teams` con un capitán que delega en subagentes durables, usa una skill de UI cuando toca, y sigue reglas de orquestación predefinidas para armar el DAG.** Todo lo demás fuera.
