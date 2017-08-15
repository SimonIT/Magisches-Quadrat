'''
/********************************************************************************
* Name:        Simon Bullik         Klasse: DQI16                               *
* Prog.Name:   Bullik_magiQuad      Magische Quadrate erstellen                 *
* Version:     1.0                  Datum: 14.08.2017                           *
* Progsprache: Python               OS: Microsoft Windows 7                     *
* *******************************************************************************/
'''
def magi_1(dimension):
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


def magi_2(dimension):
    x = int(dimension / 2)
    y = int(dimension / 2) + 1
    val = 1
    maggi = {(x, y): val}
    val += 1
    while val <= dimension ** 2:
        y_new = y + 1
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
            if y + 2 > dimension - 1:
                if y + 2 > dimension:
                    y_new = 1
                else:
                    y_new = 0
            else:
                y_new = y + 2
            x_new = x
        x = x_new
        y = y_new
        maggi[(x, y)] = val
        val += 1
    show_maggi(maggi)


def show_maggi(maggi):
    for i in range(0, dimension):
        for j in range(0, dimension):
            print(" " + str(maggi[(j, i)]).ljust(len(str(dimension ** 2))) + " ", end="|")
        print()


if __name__ == "__main__":
    dimension = 3
    while True:
        print(
        "(N) Eingabe der Dimension (3-11 / Default: 3)\n(1) Darstellen des magischen Quadrats nach Algorithmus 1\n(2) Darstellen des magischen Quadrats nach Algorithmus 2\n(X) Exit")
        choice = input()
        if choice.lower() == "n":
            dimension_input = int(input("Dimension: "))
            if dimension_input % 2 == 1 and dimension_input > 2:
                dimension = dimension_input
            else:
                dimension = 3
        elif choice == "1":
            magi_1(dimension)
        elif choice == "2":
            magi_2(dimension)
        elif choice.lower() == "x":
            exit()
