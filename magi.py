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
    magi = {(x, y): val * multiplicator}
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
        if (x_new, y_new) in magi:
            if y + 1 > dimension - 1:
                y_new = 0
            else:
                y_new = y + 1
            x_new = x
        x = x_new
        y = y_new
        magi[(x, y)] = val * multiplicator
        val += 1
    return magi


def magi_2(dimension, multiplicator):
    x = int(dimension / 2)
    y = int(dimension / 2) + 1
    val = 1
    magi = {(x, y): val * multiplicator}
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
        if (x_new, y_new) in magi:
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
        magi[(x, y)] = val * multiplicator
        val += 1
    return magi


def show_magi(magi):
    width = 0

    if "PYCHARM_HOSTED" not in os.environ:
        width = os.get_terminal_size().columns

    horizontal = []
    sum = "|"
    diag = 0
    for i in range(0, dimension):
        horizontal.append(0)
    for i in range(0, dimension):
        row = "|"
        vert = 0
        for j in range(0, dimension):
            row += " " + str(magi.get((j, i))).ljust(len(str((dimension ** 3 + dimension) / 2))) + "|"
            vert += magi.get((j, i))
            horizontal[i] += magi.get((j, i))
        row += "| " + str(vert).ljust(len(str((dimension ** 3 + dimension) / 2)))
        sum += " " + str(horizontal[i]).ljust(len(str((dimension ** 3 + dimension) / 2))) + "|"
        diag += magi.get((i, i))
        print(row.center(width))
    sum += "| " + str(diag).ljust(len(str((dimension ** 3 + dimension) / 2)))
    separate = ""
    for i in range(0, len(row)):
        separate += "-"
    print(separate.center(width))
    print(sum.center(width), end="")
    print()


def saveHTML(magi):
    html = "<!DOCTYPE html>\n" \
           "<html>\n" \
           "<head>\n" \
           "<meta charset=\"UTF-8\">\n" \
           "<meta name=\"author\" content=\"Simon Bullik\">\n" \
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" \
           "<title>Magisches Quadrat</title>\n" \
           "<link rel=\"stylesheet\" href=\"style.css\">\n" \
           "<script src=\"script.js\"></script>\n" \
           "</head>\n" \
           "<body>\n" \
           "<h1>Magisches Quadrat</h1>\n" \
           "<p>Dimension: " + str(dimension) + "</p>\n" \
                                               "<button type=\"button\" onclick=\"toggle()\" id=\"control\">Zeige Kontrolle</button>\n" \
                                               "<table>\n"

    horizontal = []
    diag = 0
    for i in range(0, dimension):
        horizontal.append(0)
    for i in range(0, dimension):
        html += "<tr>\n"
        sum = 0
        for j in range(0, dimension):
            sum += magi.get((j, i))
            html += "<td>" + str(magi.get((j, i))) + "</td>\n"
            horizontal[i] += magi.get((j, i))
        diag += magi.get((i, i))
        html += "<td class=\"sum\">" + str(sum) + "</td>\n"
        html += "</tr>\n"
    html += "<tr>\n"
    for i in horizontal:
        html += "<td class=\"sum\">" + str(i) + "</td>\n"
    html += "<td class=\"sum\">" + str(diag) + "</td>\n" \
                                               "</tr>" \
                                               "</table>\n" \
                                               "</body>\n" \
                                               "</html>"

    with open('magi.html', 'w', encoding='utf-8') as htmlFile:
        htmlFile.write(html)

    path = os.path.abspath("magi.html")
    webbrowser.open_new_tab("file://" + path)


def rotate(magi):
    array2 = {}
    for i in range(0, dimension):
        for j in range(0, dimension):
            array2[(i, j)] = magi.get((dimension - 1 - j, i))
    return array2


if __name__ == "__main__":
    dimension = 3
    multiplicator = 1
    while True:
        print(
            "(N) Eingabe der Dimension (3-11 / Default: 3)\n"
            "(K) Eingabe des Multiplikators (Default: 1)\n"
            "(1) Darstellen des magischen Quadrats nach Algorithmus 1\n"
            "(2) Darstellen des magischen Quadrats nach Algorithmus 2\n"
            "(3) Speichern als „magi.html“ nach Algorithums 1\n"
            "(4) Speichern als „magi.html“ nach Algorithums 2\n"
            "(X) Exit")
        choice = input()
        if choice.lower() == "n":
            dimension_input = int(input("Dimension: "))
            if dimension_input % 2 == 1 and dimension_input > 2:
                dimension = dimension_input
            else:
                dimension = 3
        elif choice.lower() == "k":
            multiplicator = float(input("Multiplikator: "))
        elif choice == "1":
            show_magi(magi_1(dimension, multiplicator))
        elif choice == "2":
            show_magi(magi_2(dimension, multiplicator))
        elif choice == "3":
            saveHTML(magi_1(dimension, multiplicator))
        elif choice == "4":
            saveHTML(magi_2(dimension, multiplicator))
        elif choice == "5":
            show_magi(rotate(magi_1(dimension, multiplicator)))
        elif choice.lower() == "x":
            exit()
