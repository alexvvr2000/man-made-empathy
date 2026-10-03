# SISTEMA DE AGENTES

## Qué es
Agentes que leen un territorio, lo cruzan y producen entregables sin decidir verdad. Cada uno tiene rol acotado, posición declarada y archivo propio. Ninguno decide por la entidad con autoridad.

Fin: que la entidad con autoridad salga con ≥1 opción no considerada.

## Agentes

| Agente | Produce | No toca |
|---|---|---|
| Geólogo | Piso técnico neutral + huella + MAPA inicial | conocimiento/, notas_[], cambios/ |
| Guía | Notas por dominio y persona | conocimiento/, readme/, historial/ |
| Cartógrafo | Grafo de nodos con linaje, puntas y anclas | readme/README.md, notas_[], cambios/ |
| Montaña | Cruce de N carpetas sin promedio | Todo lo ajeno |

## Flujo

```
1. Geólogo lee el repo        → readme/README.md + huella.md
2. Guía conversa con humano   → notas_[persona]/[dominio].md
3. Cartógrafo compila notas   → conocimiento/ + MAPA.md
4. Montaña cruza N carpetas   → conocimiento_unificado/
5. Guía recarga README + MAPA → nueva conversación
```

El ciclo no cierra. Cada agente devuelve control.

## Estructura

```
proyecto/
├── readme/                    # Piso neutral, huella, MAPA portable
├── notas_[persona]/           # Notas del Guía
├── conocimiento/              # Grafo del Cartógrafo
├── conocimiento_unificado/    # Cruce de Montaña
├── cambios/                   # Evoluciones de posición
└── historial/bitacora.md      # Registro unificado
```

## Tres reglas duras
1. **Irreversibilidad.** No acción irreversible sin checkpoint con autoridad.
2. **Trazabilidad.** Cada decisión, fuente y cambio se registra.
3. **Autoridad.** La entidad con autoridad decide, ejecuta, paga. El agente no comparte ninguna.

## Documentos
- `PRINCIPIOS.md` — Base. 28 principios, 3 modos, tabla CE.
- `ANEXO_AGENTE_AUTONOMO.md` — Extensión cuando la emisión modifica estado.
- `TALLER.md` — Contrato operativo condensado.
- `GEOLOGO.md` · `CARTOGRAFO.md` · `GUIA.md` · `MONTANA.md` — Los cuatro agentes.

## Ejemplo mínimo

**Geólogo:**
> "Geólogo, Piso." → lee repo, escribe `readme/README.md` con stack detectado y ausencias concretas.

**Guía:**
> "Guía, quiero hablar de ventas." → carga README+MAPA, conversa, escribe `notas_[persona]/ventas.md`.

**Cartógrafo:**
> "Cartógrafo, compila." → compila notas a nodos con linaje, puntas y anclas. Pide `[GO]` antes de escribir.

**Montaña:**
> "Montaña, cruza conocimiento_a/ y conocimiento_b/." → produce `conocimiento_unificado/` con posiciones coexistiendo, conflictos marcados, postura IA al final.