import sys

"""
el modulo sys permite leer los argumentos que escribimos
al ejecutar el programa desde la terminal
"""


def rectangle(width, height, draw_type="A"):
    """
    dibuja un rectangulo con diferentes estilos
    """

    # si el ancho o el alto son menores que 1 no hace nada
    if width < 1 or height < 1:
        return

    # elegimos los caracteres segun el tipo
    if draw_type == "A":
        corner = "o"
        horizontal = "-"
        vertical = "|"

    elif draw_type == "B":
        corner = "B"
        horizontal = "/"
        vertical = "/"

    # recorremos todas las filas
    for row in range(height):

        line = ""

        # recorremos todas las columnas
        for column in range(width):

            # tipo c
            if draw_type == "C":

                # primera y ultima fila
                if row == 0 or row == height - 1:

                    if column == 0 or column == width - 1:
                        line += "O"

                    elif column == width // 2:
                        line += "A"

                    else:
                        line += "x"

                # filas del centro
                else:

                    if column == 0 or column == width - 1:
                        line += "x"

                    elif column == width // 2:
                        line += "B"

                    else:
                        line += "O"

            # tipos a y b
            else:

                # esquinas
                if (row == 0 or row == height - 1) and (column == 0 or column == width - 1):
                    line += corner

                # borde superior e inferior
                elif row == 0 or row == height - 1:
                    line += horizontal

                # bordes laterales
                elif column == 0 or column == width - 1:
                    line += vertical

                # interior
                else:
                    line += " "

        print(line)


def main():

    # version normal
    if len(sys.argv) == 3:

        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])

            rectangle(x, y)

        except ValueError:
            print("los argumentos deben ser numeros enteros")

    # version bonus
    elif len(sys.argv) == 4:

        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])

            draw_type = sys.argv[3].upper()

            # si el tipo no es correcto avisa
            if draw_type not in ["A", "B", "C"]:
                print("el tipo debe ser A, B o C")
                return

            rectangle(x, y, draw_type)

        except ValueError:
            print("los argumentos deben ser numeros enteros")

    else:
        print("uso: python main.py <ancho> <alto> [A|B|C]")


if __name__ == "__main__":
    main()