# tareas/ — la piel que crece

**Empieza vacía, y crece cuando entra una tarea.** **Y se rehace cada vez: no se llena de cajones.**

## Una tarea, y son cuatro renglones

```plaintext
Entra:      [qué necesita para empezar]
Falla si:   [qué la deja mal]
Sale:       [qué entrega]
Consume:    [quién lo usa]
```

**Y además declara su modo:** **`solo-lectura` o `escribe`.** **Sin modo, el ente no la corre: el silencio no es permiso.**

## Cómo se ve

```
tareas/
├── privado/
│   ├── privado.tra      el corte
│   └── rastro.tra       lo que dejó la última vez
└── tu tarea/
```

**Y la plantilla está arriba, en `../plantilla.tra`, para copiar y llenar.**

## Lo que una tarea no es

**No es un deseo.** **Si no puedes llenar «falla si», todavía no es una tarea.**
