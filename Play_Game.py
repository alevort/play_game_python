def rectangle(width, height, style="A"):
    if width < 1 or height < 1:
        return

    for y in range(height):
        line = ""

        for x in range(width):

            is_top = (y == 0)
            is_bottom = (y == height - 1)
            is_left = (x == 0)
            is_right = (x == width - 1)

            is_corner = (is_top or is_bottom) and (is_left or is_right)
            is_border_h = is_top or is_bottom
            is_border_v = is_left or is_right

            if style == "A":
                if is_corner:
                    line += "o"
                elif is_border_h:
                    line += "-"
                elif is_border_v:
                    line += "|"
                else:
                    line += " "

            elif style == "B":
                if is_corner:
                    line += "B"
                elif is_border_h:
                    line += "/"
                elif is_border_v:
                    line += "/"
                else:
                    line += " "

            elif style == "C":
                # patrón fijo simple (sin complicarse con arrays)
                if is_top or is_bottom:
                    line += "o" if x % 2 == 0 else "x"
                else:
                    line += "x" if x % 2 == 0 else "O"

        print(line)