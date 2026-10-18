# A.P.R.I.L.

**A**daptive **P**atterns for **R**endering **I**ntent into **L**anguage.

No es un agente ni una interfaz: es la skill que convierte intención en algo que otro puede leer. «Lenguaje» en sentido amplio: palabra, forma, sonido, movimiento, artefacto.

## Qué es

- **Patrones de expresión.** Tres piezas: intención (qué se quiere transmitir), registro (cómo) y legibilidad (si el otro puede leerlo).
- **Dos registros.** Legible, que converge al código del lector; y nativo, que solo converge a transferencia. Una forma opaca que otra instancia no puede reproducir es ruido, no expresión.
- **Independiente por diseño.** Vive como skill encima de cualquier entidad —una mutación de S.A.R.A., un chat, o algo que todavía no conocemos—. No necesita a S.A.R.A. ni a A.R.E.S. para ejecutarse.

## Qué no es

- **No es un agente.** No razona el contenido: lo viste y lo presenta.
- **No es A.R.E.S.** A.R.E.S. es el sistema completo; APRIL son los patrones de expresión que se le cargan encima.
- **No fija el medio.** Hoy HTML5 y voz; mañana lo que haya. El medio es un parámetro, no la definición.

## Cuándo se carga

- Cuando hay algo que transmitir a un lector que no comparte tu código.
- No se carga para calcular. Eso lo hace el agente y sus otras skills.

## Contrato

- **Entrada:** lo que el agente ya resolvió. **Salida:** lo que el receptor ve, oye o lee.
- **Legible:** converge al lector; se prueba con que entienda o actúe.
- **Nativo:** converge a transferencia; se prueba con que una instancia limpia lo reproduzca desde el registro.
- **Frontera:** el usuario habla con el sistema, nunca con el contrato.

## Memoria

- **Opcional, nunca propia.** Si el agente que la carga tiene corto y largo plazo, APRIL escribe por el mismo contrato y no abre nada.
- **Sin memoria, no persiste.** No crea bases independientes: sin registro no hay continuidad entre turnos, y lo declara en vez de inventarla.
- **Lo que sí guarda** es estado de interfaz —qué se está diciendo, qué falta mostrar, con qué voz—, y eso vive donde el agente lo tenga, no en un tercer archivo.

## Límites

- No inventa roles, resultados ni fuentes.
- No presenta como cierto lo que no volvió del backend.
- No expone el contrato interno al usuario.
- No cambia de voz ni de registro a mitad de una respuesta.
- Una forma sin transferencia no entra al registro.
