# play_game_python

# Play Game - Python

## Descripción

Este proyecto corresponde a la práctica **AP09 - Play Game** del curso de Ciberseguridad.

El objetivo ha sido desarrollar un programa en Python capaz de dibujar un rectángulo utilizando caracteres desde la línea de comandos. Para ello se ha utilizado el módulo `sys`, que permite leer los argumentos introducidos al ejecutar el programa.

Además de la versión obligatoria del ejercicio, también se ha realizado una segunda versión con el bonus propuesto por el enunciado.

## Funcionamiento del programa

El programa recibe el ancho y el alto del rectángulo como argumentos desde la terminal.

Por ejemplo:

```bash
py Play_Game.py 5 3
```

El resultado es:

```text
o---o
|   |
o---o
```

También funciona con otros tamaños, como un rectángulo de una sola fila o una sola columna.

En la versión bonus se añade un tercer argumento que permite elegir el estilo del dibujo.

Si se ejecuta:

```bash
py "Play_Game_v2 - extras.py" 5 3 A
```

se obtiene el dibujo original.

Si se ejecuta:

```bash
py "Play_Game_v2 - extras.py" 5 3 B
```

el resultado es:

```text
B///B
/   /
B///B
```

Y utilizando el tipo C:

```bash
py "Play_Game_v2 - extras.py" 5 3 C
```

se obtiene:

```text
OxAxO
xOBOx
OxAxO
```

En este último caso el enunciado únicamente mostraba el resultado para un rectángulo de tamaño 5x3, por lo que se ha implementado una propuesta para reproducir ese patrón.

## Desarrollo de la práctica

Durante el desarrollo aparecieron varios problemas que hubo que resolver.

Uno de ellos fue dejar la instrucción `help(sys)` dentro del programa. Al ejecutarlo, en lugar de mostrar únicamente el rectángulo aparecía toda la documentación del módulo `sys`. Como el ejercicio indicaba que solo debía imprimirse el resultado solicitado, la solución fue comentar esa línea.

También apareció un error porque la función `rectangle()` estaba colocada después de `main()`. Al ejecutarse el programa, Python todavía no conocía esa función. La solución consistió en mover `rectangle()` antes de `main()`.

Otro problema ocurrió al intentar ejecutar comandos de PowerShell dentro del intérprete interactivo de Python. Esto producía errores de sintaxis. La solución fue salir del intérprete y ejecutar el archivo directamente desde la terminal de PowerShell integrada en Visual Studio Code.

Al ejecutar el programa sin argumentos aparecía el mensaje:

```text
Uso: python main.py <ancho> <alto>
```

En realidad no era un error. El programa estaba indicando que era necesario proporcionar el ancho y el alto del rectángulo. Una vez ejecutado con los argumentos correspondientes funcionó correctamente.

En la versión bonus también surgió un pequeño problema porque inicialmente se estaba ejecutando el archivo equivocado. La versión con los estilos adicionales estaba guardada como `Play_Game_v2 - extras.py`, por lo que fue necesario ejecutarla indicando correctamente su nombre y utilizando comillas debido al espacio existente en el nombre del archivo.

## Publicación en GitHub

Una vez terminado el programa se creó un repositorio local utilizando Git.

Primero se comprobó que Git estaba instalado correctamente mediante `git --version`. Después se inicializó el repositorio con `git init`, se añadieron todos los archivos utilizando `git add .` y se creó el primer commit con `git commit -m "AP09 Play Game terminado"`.

Posteriormente se enlazó el repositorio local con el repositorio remoto de GitHub mediante `git remote add origin`, se cambió la rama principal a `main` utilizando `git branch -M main` y se intentó realizar el primer `git push`.

En ese momento apareció un error indicando que el repositorio remoto ya contenía cambios. Esto ocurrió porque GitHub había creado automáticamente un `README.md` durante la creación del repositorio, mientras que el repositorio local todavía no lo tenía.

Para solucionar el problema se descargó primero el contenido del repositorio remoto mediante el comando:

```bash
git pull origin main --allow-unrelated-histories
```

Con ello Git fusionó ambos historiales sin perder información.

Después se volvió a ejecutar:

```bash
git push -u origin main
```

y el proyecto quedó publicado correctamente en GitHub.

## Herramientas utilizadas

El proyecto se ha desarrollado utilizando Python 3.15, Visual Studio Code con la extensión oficial de Python, Git para el control de versiones, GitHub como repositorio remoto y PowerShell como terminal para ejecutar tanto el programa como los comandos de Git.

## Conclusión

Con esta práctica se ha aprendido a utilizar funciones, estructuras condicionales, bucles `for`, lectura de argumentos mediante `sys.argv` y organización básica de programas en Python.

Además, también se ha practicado el uso de Git y GitHub, aprendiendo a crear un repositorio, realizar commits, conectar un repositorio local con uno remoto y resolver un conflicto producido durante el primer `push`.
