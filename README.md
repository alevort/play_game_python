# play_game_python

Lenguaje: Python
Tipo de proyecto: Aplicación de consola (CLI, Command Line Interface)
Categoría: Programa/script de Python
Función: Dibuja rectángulos en la terminal a partir de argumentos de la línea de comandos.

# Errores que se han ido resolviendo de despliegue y configuracion de la aplicacion, despues viene toda la descripcion del ejercicio y como hemos ido resolviendo

PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> & C:/Users/neonb/AppData/Local/Programs/Python/Python315/python.exe "c:/Users/neonb/Documents/Ciberseguridad Ironhack/AP09_PlayGame/Play_Game_v2 - extras.py"
uso: python main.py <ancho> <alto> [A|B|C]
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> py Play_Game_v2.py 5 3 A  
Uso: python main.py <ancho> <alto>  
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> py "Play_Game_v2 - extras.py" 5 3 A
o---o  
| |  
o---o  
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> py "Play_Game_v2 - extras.py" 5 3 B
B///B  
/ /  
B///B  
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> py "Play_Game_v2 - extras.py" 5 3 C
OxAxO
xOBOx
OxAxO
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git --version
git version 2.54.0.windows.1
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> pwd

Path

---

C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame

PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git init
Initialized empty Git repository in C:/Users/neonb/Documents/Ciberseguridad Ironhack/AP09_PlayGame/.git/
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git status
On branch master

No commits yet

Untracked files:
(use "git add <file>..." to include in what will be committed)
Play_Game.py
Play_Game_v2 - extras.py
Play_Game_v2.py

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git add .
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git commit -m "AP09 Play Game terminado"
[master (root-commit) b219a40] AP09 Play Game terminado
3 files changed, 225 insertions(+)
create mode 100644 Play_Game.py
create mode 100644 Play_Game_v2 - extras.py
create mode 100644 Play_Game_v2.py
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git remote add origin https://github.com/alevort/play_game_python  
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git branch -M main
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git push -u origin main
To https://github.com/alevort/play_game_python
! [rejected] main -> main (fetch first)
error: failed to push some refs to 'https://github.com/alevort/play_game_python'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git pull origin main --allow-unrelated-histories
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 867 bytes | 61.00 KiB/s, done.
From https://github.com/alevort/play_game_python

- branch main -> FETCH_HEAD
- [new branch] main -> origin/main
  Merge made by the 'ort' strategy.
  README.md | 1 +
  1 file changed, 1 insertion(+)
  create mode 100644 README.md
  PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git push -u origin main
  Enumerating objects: 8, done.
  Counting objects: 100% (8/8), done.
  Delta compression using up to 16 threads
  Compressing objects: 100% (7/7), done.
  Writing objects: 100% (7/7), 2.12 KiB | 723.00 KiB/s, done.
  Total 7 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
  remote: Resolving deltas: 100% (2/2), done.
  To https://github.com/alevort/play_game_python
  b6ad770..8e69f4c main -> main
  branch 'main' set up to track 'origin/main'.
  PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git status
  On branch main
  Your branch is up to date with 'origin/main'.

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified: README.md

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git add README.md
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git commit -m "Actualizado README con documentación del proyecto"
[main 1176a6d] Actualizado README con documentación del proyecto
1 file changed, 127 insertions(+), 1 deletion(-)
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 2.29 KiB | 2.29 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/alevort/play_game_python
8e69f4c..1176a6d main -> main
PS C:\Users\neonb\Documents\Ciberseguridad Ironhack\AP09_PlayGame>

## Enunciado

Ejercicio
Escribe una función rectangle() que reciba dos números enteros (x, y)

Esta función debe imprimir un rectángulo de caracteres en pantalla con:

'o' en las esquinas
'-' en los bordes horizontales
'|' en los bordes verticales
' ' espacios en el interior
Reglas
Si x < 1 o y < 1, no se debe imprimir nada
No se permiten bucles infinitos ni errores
Solo imprime lo que se indica (nada extra)
No toques la función main()
Añadir un DocString a la función rectangle()
Utiliza el módulo sys para leer argumentos de línea de comandos
Las funciones y variables deben ser claras y descriptivas, y deben estar en inglés
Main()
import sys

"""
El módulo sys en Python proporciona acceso a varios parámetros
y funciones del sistema, especialmente útiles para interactuar
con el intérprete

https://docs.python.org/es/3.10/library/sys.html
"""

help(sys)

Copiar

Explicar
def main():
if len(sys.argv) == 3:
try:
x = int(sys.argv[1])
y = int(sys.argv[2])
rectangle(x, y)
except ValueError:
print("Los argumentos deben ser números enteros")
else:
print("Uso: python main.py <ancho> <alto>")

Copiar

Explicar
"""
Este bloque se asegura de que la función `main()` solo se ejecute
cuando este archivo se ejecuta directamente desde la línea de comandos,
y no cuando se importa como módulo en otro archivo

**name** es una variable especial de Python:

- Si el archivo se ejecuta directamente: **name** == "**main**"
- Si el archivo se importa desde otro archivo: **name** == "nombre_del_modulo"
  """

if **name** == "**main**":
main()

Copiar

Explicar
rectangle(5,3) debería mostrar esto:
$>python play_game.py 5 3
o---o
|   | 
o---o
$>

Copiar

Explicar
rectangle(5,1) debería mostrar esto:
$>python play_game.py 5 1
o---o 
$>

Copiar

Explicar
rectangle(1,1) debería mostrar esto:
$>python play_game.py 1 1
o
$>

Copiar

Explicar
rectangle(1,5) debería mostrar esto:
$>python play_game.py 1 5
o
| 
|
| 
o
$>

Copiar

Explicar
Bonus
Mejora tu función rectangle() para que acepte un tercer argumento type que determine el estilo del dibujo. Puede ser 'A', 'B' o 'C'

Para el tipo 'A' si el rectángulo es de 5, 3 deberá mostrar esto:
$>python play_game.py 5 3 A
o---o
|   | 
o---o
$>

Copiar

Explicar
Para el tipo 'B' si el rectángulo es de 5, 3 deberá mostrar esto:
$>python play_game.py 5 3 B
B///B
/   / 
B///B
$>

Copiar

Explicar
Para el tipo 'C' si el rectángulo es de 5, 3 deberá mostrar esto:
$>python play_game.py 5 3 C
OxAxO
xOBOx 
OxAxO
$>

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

## Nota final

En el estilo **C** el enunciado únicamente muestra el resultado para un rectángulo de tamaño **5x3**, pero no explica ninguna regla para generar el dibujo en tamaños diferentes. Por este motivo se ha realizado una interpretación propia del patrón mostrado, intentando mantener la distribución de los caracteres y reproducir el ejemplo proporcionado lo más fielmente posible. Al no existir una especificación más detallada, esta implementación representa una propuesta basada en el único ejemplo facilitado en el ejercicio.
