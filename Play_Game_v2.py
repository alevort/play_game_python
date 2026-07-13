import sys
 
"""
El módulo sys en Python proporciona acceso a varios parámetros 
y funciones del sistema, especialmente útiles para interactuar 
con el intérprete
 
https://docs.python.org/es/3.10/library/sys.html
"""
 
# help(sys)

def rectangle(width, height):
    """
    Draws a rectangle using characters.
    """

    if width < 1 or height < 1:
        return

    for row in range(height):

        line = ""

        for column in range(width):

            if (row == 0 or row == height - 1) and (column == 0 or column == width - 1):
                line += "o"

            elif row == 0 or row == height - 1:
                line += "-"

            elif column == 0 or column == width - 1:
                line += "|"

            else:
                line += " "

        print(line)


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


if __name__ == "__main__":
    main()