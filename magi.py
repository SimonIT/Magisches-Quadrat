dimension = 11


def magi1():
    x = int(dimension / 2)
    y = 0
    val = 1
    maggi = {(x, y): val}
    val += 1
    while val <= dimension ** 2:
        y_new = y - 1
        x_new = x + 1
        if y_new < 0:
            y_new = dimension - 1
        elif y_new > dimension - 1:
            y_new = 0
        if x_new < 0:
            x_new = dimension - 1
        elif x_new > dimension - 1:
            x_new = 0
        if (x_new, y_new) in maggi:
            if y + 1 > dimension - 1:
                y_new = 0
            else:
                y_new = y + 1
            x_new = x
        x = x_new
        y = y_new
        maggi[(x, y)] = val
        val += 1
    show_maggi(maggi)


def magi2():
    return


def show_maggi(maggi):
    for i in range(0, dimension):
        for j in range(0, dimension):
            print(maggi[(j, i)], end="|")
        print()


while True:
    print(
        "(N) Eingabe der Dimension (3-11 / Default: 3)\n(1) Darstellen des magischen Quadrats nach Algorithmus 1\n(2) Darstellen des magischen Quadrats nach Algorithmus 2\n(X) Exit")
    choice = input()
    if (choice.lower() == "n"):
        dimension_input = int(input("Dimension: "))
        if (dimension_input % 2 == 1):
            dimension = dimension_input
    elif (choice == "1"):
        magi1()
    elif (choice == "2"):
        magi2()
    elif (choice.lower() == "x"):
        exit()
