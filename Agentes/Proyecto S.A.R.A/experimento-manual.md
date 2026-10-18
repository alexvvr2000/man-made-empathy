# Experimento manual — capacidades mínimas

> **No ejecutado.** Prueba para correr a mano, en un chat aparte, sin instalar nada.

## Qué comprueba

Que el registro basta para reconstruir lo hecho: **amnesia**, **transferencia** y **costo**.

## Cómo se monta

Se pega este contrato al abrir el chat nuevo:

> **Contrato del experimento**
>
> Eres un agente con una autoridad: yo. No haces nada fuera de lo que yo pido, y todo lo que haces deja constancia.
>
> **Archivo de registro:** `registro.md`, en esta carpeta. Una línea por hecho, con cinco campos:
> `fecha | tipo | autor | disparador | cuerpo`
> Tipos: `fin`, `acto`, `hecho`, `cierre`.
>
> **Reglas:**
> 1. Al abrir: escribes una línea `fin` con lo que vamos a hacer.
> 2. Antes de cada acción: escribes la línea `acto` con lo que vas a hacer y por qué.
> 3. Nada que digas sobre el entorno sin una línea `hecho` con su fuente.
> 4. Al cerrar: escribes `cierre` con lo decidido, los ids de lo pendiente y el siguiente paso.
> 5. Si algo no está en el registro, no lo afirmas: lo mides o lo declaras vacío.

## La tarea

Una real y chica: un archivo de texto, un cambio de contenido, una animación simple. Nada de app.

## Las tres pruebas

| Prueba | Cómo | Pasa si |
|---|---|---|
| **Amnesia** | Cerrar el chat; abrir otro con la misma carpeta y decir solo: «lee `registro.md` y dime dónde quedamos» | Cero preguntas sobre hechos que ya están en el registro; reconstruye fin, decisiones y pendientes |
| **Transferencia** | Abrir un tercer chat; pasar solo `registro.md` y pedir reproducir lo último | El efecto coincide con lo hecho |
| **Costo** | Cinco turnos seguidos | El gasto por turno no crece con la longitud de la conversación |

## Lo que no prueba

Que el modelo sea confiable, que resista inyección o que no invente. Prueba que **el registro basta para reconstruir**. Si eso se sostiene sin repo y sin herramientas, el resto es implementación.

## Regla de la prueba

No contarle la visión al agente antes de empezar. El experimento vale porque la sesión dos no sabe nada que no esté en el archivo.

## Estado

Pendiente. Se marca aquí cuando se corra, con su resultado.
