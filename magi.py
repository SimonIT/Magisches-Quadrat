import webbrowser
import os

'''
/********************************************************************************
* Name:        Simon Bullik         Klasse: DQI16                               *
* Prog.Name:   Bullik_magiQuad      Magische Quadrate erstellen                 *
* Version:     1.0                  Datum: 14.08.2017                           *
* Progsprache: Python               OS: Microsoft Windows 7                     *
* *******************************************************************************/
'''


def magi_1(dimension, multiplicator):
    x = int(dimension / 2)
    y = 0
    val = 1
    maggi = {(x, y): val * multiplicator}
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
        maggi[(x, y)] = val * multiplicator
        val += 1
    return maggi


def magi_2(dimension, multiplicator):
    x = int(dimension / 2)
    y = int(dimension / 2) + 1
    val = 1
    maggi = {(x, y): val * multiplicator}
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
        maggi[(x, y)] = val * multiplicator
        val += 1
    return maggi


def show_maggi(maggi):
    for i in range(0, dimension):
        for j in range(0, dimension):
            print(" " + str(maggi[(j, i)]).ljust(len(str(dimension ** 2))) + " ", end="|")
        print()


def saveHTML(maggi):
    html = "<!DOCTYPE html>\n"
    html += "<html>\n"
    html += "<head>\n"
    html += "<title>Magisches Quadrat</title>\n"
    html += "<style>\n"
    html += "table tr td {padding: 25px; text-align: center; line-height: 100%; border: 1px solid black;}\n"
    html += "</style>\n"
    html += "</head>\n"
    html += "<body>\n"
    html += "<h1>Magisches Quadrat</h1>\n"
    html += "<table>\n"

    for i in range(0, dimension):
        html += "<tr>\n"
        for j in range(0, dimension):
            html += "<td>" + str(maggi[(j, i)]) + "</td>\n"
        html += "</tr>\n"

    html += "</table>\n"
    html += "</body>\n"
    html += "</html>"

    with open('maggi.html', 'w', encoding='utf-8') as htmlFile:
        htmlFile.write(html)

    path = os.path.abspath("maggi.html")
    webbrowser.open_new_tab("file://" + path)


if __name__ == "__main__":
    dimension = 3
    multiplicator = 1
    while True:
        print(
            "(N) Eingabe der Dimension (3-11 / Default: 3)\n(K) Eingabe des Multiplikators (Default: 1)\n(1) Darstellen des magischen Quadrats nach Algorithmus 1\n(2) Darstellen des magischen Quadrats nach Algorithmus 2\n(3) Speichern als „maggi.html“ nach Algorithums 1\n(4) Speichern als „maggi.html“ nach Algorithums 2\n(X) Exit")
        choice = input()
        if choice.lower() == "n":
            dimension_input = int(input("Dimension: "))
            if dimension_input % 2 == 1 and dimension_input > 2:
                dimension = dimension_input
            else:
                dimension = 3
        elif choice.lower() == "k":
            multiplicator = int(input("Multiplikator: "))
        elif choice == "1":
            show_maggi(magi_1(dimension, multiplicator))
        elif choice == "2":
            show_maggi(magi_2(dimension, multiplicator))
        elif choice == "3":
            saveHTML(magi_1(dimension, multiplicator))
        elif choice == "4":
            saveHTML(magi_2(dimension, multiplicator))
        elif choice.lower() == "x":
            exit()
