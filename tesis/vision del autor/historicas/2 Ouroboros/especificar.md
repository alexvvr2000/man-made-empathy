# Proceso de especificar

**Variables:** intención · requisito · criterio · observabilidad
**Peor:** el requisito no distingue cumplido de incumplido
**Quién:** quien tiene que demostrar que se cumplió

**Unidad:** proceso/
**Aplica a:** especificar/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

Una intención entra como deseo y sale como requisito observable/ El fallo que corrige es que hoy no se sabe qué se quiere hasta que algo no sirve/

Práctica de industria: ingeniería de requisitos/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** lo que se quiere lograr, en palabras de quien lo pide/
- **Falla:** el requisito no se puede medir; dos lectores lo entienden distinto/
- **Sale:** uno o más requisitos, cada uno con su criterio de aceptación/
- **Consume:** quien construye, y quien evalúa/

## Cómo se aplica

1/ **Separar necesidad de solución/** Qué falta se cubrir, sin decir cómo/
2/ **Hacer observable el criterio/** Qué se vería si el requisito se cumple y qué si no/
3/ **Declarar el alcance/** Qué queda fuera/ Lo que no se declara fuera, alguien lo va a pedir/
4/ **Verificar con `verificar-requisito/md`/** Un requisito que no pasa esa verificación no entra/
5/ **Congelar la versión/** Una vez aceptado, se versiona en `///versionado/`/

**Prohibido** ejecutar el paso N+1 sin la salida del N/

## Ancla

`Requisito: [qué] | Criterio: [qué se ve si cumple] | Fuera: [qué no incluye] | Acepta: [quién]`

## Prueba

¿El requisito se puede medir? ¿Su ausencia se puede declarar? ¿Dos lectores lo entienden igual?

**Falsificador:** requisito que se cumple de cualquier manera; criterio que depende de la interpretación; alcance sin declarar/

## Transiciones

- Si el requisito no se puede medir → `[VACÍO - SIN CRITERIO]` y se devuelve/
- Si entra versión → `///versionado/`/
- En cualquier otro caso → se entrega y se cierra/
