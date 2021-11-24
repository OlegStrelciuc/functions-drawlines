
def drawLine(length, direction):
    if direction == "h" :
        y = "-"*length
        print(y)
    if direction == "v" :
        y = "|\n"*length
        print(y)

drawLine (5,"h")
drawLine (3,"v")

