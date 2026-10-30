# ALMAS — dónde van los entes que viven en la colmena

**Cuándo se abre:** **cuando se copia una colmena, y hay que saber dónde poner a los entes.**

## Lo que hay aquí

**Cada ente que vive en la colmena, con su carpeta y su casa entera:**

```plaintext
Almas/
└── <el ente>/
    ├── LEEME.md                qué hace
    ├── NOMBRE.md               su nombre, y por qué ése
    ├── ciclo alma de niño.prs  el fijo, y lo primero
    ├── procesos base/          cuatro, y no crecen
    ├── ciclos/                 los suyos
    ├── memoria continua/       lo que acumuló
    ├── evolucion/              lo que aprendió
    └── bin/                    sus herramientas
```

**Y un ente NO trae `bin/`: eso es del proyecto.** **El ente trae sus tareas, y cada tarea su `_herramientas/`.**

**Y aquí no hay entes: es la plantilla.** **Los de verdad están en [`../../../../biblioteca/Almas/`](../../../../biblioteca/Almas/).**

## Prueba

**¿Cada ente viene completo? ¿Hay alguno que dependa de otro para funcionar?**

**Falsificador:** un ente a medias; un ente que copia lo de otro en vez de citarlo.
