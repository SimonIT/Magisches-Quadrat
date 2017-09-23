import webbrowser
import os

'''
/********************************************************************************
* Name:        Simon Bullik         Klasse: DQI16                               *
* Prog.Name:   Bullik_magiQuad      Magische Quadrate erstellen                 *
* Version:     1.0                  Datum: 14.08.2017                           *
* Progsprache: Python3              OS: Microsoft Windows 10                    *
* *******************************************************************************/
'''


def create_magi_1(dimension=3, multiplicator=1):
    x = int(dimension / 2)  # Startwert X in der Mitte des Quadrats
    y = 0  # Startwret Y oben
    val = 1  # Startwert ist eins
    magi = {(x, y): val * multiplicator}  # Eintragen des Wertes in das Dictionary
    val += 1  # Erhöhe den Wert um 1
    while val <= dimension ** 2:  # Wiederhohle bis der Wer größer als dimension^2 ist
        y_new = y - 1  # Gehe einen nach oben
        x_new = x + 1  # Gehe einen nach rechts
        if y_new < 0:  # Wenn die neue Position nach oben nicht im Feld ist
            y_new = dimension - 1  # Setze die Y Koordinate nach ganz unten
        elif y_new > dimension - 1:  # Wenn die neue Position nach unten nicht im Feld ist
            y_new = 0  # Setze Y Koordinate nach ganz oben
        if x_new < 0:  # Wenn die neue Position nach links nicht im Feld ist
            x_new = dimension - 1  # Setze die neue x Koordinate nach ganz rechts
        elif x_new > dimension - 1:  # Wenn die neue Position rechts nicht im Feld ist
            x_new = 0  # Setze die neue x Koordinate nach anz links
        if (x_new, y_new) in magi:  # Wenn es die neuen Koordinaten schon im Dictionary sind
            if y + 1 > dimension - 1:  # Wenn Das Feld unter dem alten Feld außerhalb des Quadrats ist
                y_new = 0  # Setze die Y Koordinaten nach ganz oben
            else:
                y_new = y + 1  # Sonst Setze die y Koordinate auf das Feld unter dem alten Feld
            x_new = x  # Die x Koordinate bleibt gelich zum alten Feld
        x = x_new
        y = y_new
        magi[(x, y)] = val * multiplicator  # Eintragen des Werts in das Dictionary
        val += 1  # Erhöhen des Werts
    return magi


def create_magi_2(dimension=3, multiplicator=1):
    x = int(dimension / 2)  # Startwert X in der Mitte des Quadrats
    y = int(dimension / 2) + 1  # Startwert Y Feld ein Feld unter der Mitte
    val = 1  # Startwert ist eins
    magi = {(x, y): val * multiplicator}  # Eintragen des Wertes in das Dictionary
    val += 1  # Erhöhe den Wert um 1
    while val <= dimension ** 2:  # Wiederhohle bis der Wer größer als dimension^2 ist
        y_new = y + 1  # Gehe einen nach unten
        x_new = x + 1  # Gehe einen nach rechts
        if y_new < 0:  # Wenn die neue Position nach oben nicht im Feld ist
            y_new = dimension - 1  # Setze die Y Koordinate nach ganz unten
        elif y_new > dimension - 1:  # Wenn die neue Position nach unten nicht im Feld ist
            y_new = 0  # Setze Y Koordinate nach ganz oben
        if x_new < 0:  # Wenn die neue Position nach links nicht im Feld ist
            x_new = dimension - 1  # Setze die neue x Koordinate nach ganz rechts
        elif x_new > dimension - 1:  # Wenn die neue Position rechts nicht im Feld ist
            x_new = 0  # Setze die neue x Koordinate nach anz links
        if (x_new, y_new) in magi:  # Wenn es die neuen Koordinaten schon im Dictionary sind
            if y + 2 > dimension - 1:  # Wenn das Feld um mind. ein Feld nicht im Feld sind
                if y + 2 > dimension:  # Wenn das Felder um mind. zwei Feld nicht im Feld sind
                    y_new = 1  # Setzte die Y Koordinate auf eins
                else:
                    y_new = 0  # Sonst setzt die y Kooridnate auf null
            else:
                y_new = y + 2  # Setze die Y Koordinate um zwei nach unten
            x_new = x  # Setze die X Koordinate auf die alten
        x = x_new
        y = y_new
        magi[(x, y)] = val * multiplicator  # Eintragen des Werts in das Dictionary
        val += 1  # Erhöhen des Werts
    return magi


def show_magi(magi):
    width = 0  # Setze die breite auf null

    if "PYCHARM_HOSTED" not in os.environ:  # Wenn das Programm nicht in PyCharm läuft
        width = os.get_terminal_size().columns  # Setze die breite auf die Terminalbreite

    vertical = []  # Initilisierung der Liste für die vetikale Summen
    sum = "|"  # Startwert für die Summenzeile
    diag = 0  # Initialisierung diagonale Summe
    for i in range(0, dimension):  # Für jede Zeile
        row = "|"  # Anfangszeichen einer Zeile ist |
        horizontal = 0  # Initialisiere die horizontale Summe auf null
        vertical.append(0)  # Füge für jede Spaltensumme den Startwert null ein
        for j in range(0, dimension):  # Für jede Spalte
            row += " " + str(magi.get((j, i))).ljust(len(str((
                                                                 dimension ** 3 + dimension) / 2))) + "|"  # Füge der Zeile den Wert an, auf die Breite der Summen angepasst
            horizontal += magi.get((j, i))  # Addiere den Wert zu der Zeilensumme
            vertical[i] += magi.get((j, i))  # Addiere den Wert zur Spaltensumme
        row += "| " + str(horizontal).ljust(len(str((dimension ** 3 + dimension) / 2)))  # Füge der Zeile die Summe an
        sum += " " + str(vertical[i]).ljust(
            len(str((dimension ** 3 + dimension) / 2))) + "|"  # Füge die Spaltensumme zusammen
        diag += magi.get((i, i))  # Addiere die Diagonalsumme
        print(row.center(width))  # Gebe die Spalte aus
    sum += "| " + str(diag).ljust(
        len(str((dimension ** 3 + dimension) / 2)))  # Füge zur Ausgabe die Diagonalsumme hinzu
    separate = ""  # Initialisierung der Trennungslinie
    for i in range(0, len(row)):
        separate += "-"  # Füge nach der Länge der Zeilen Bindestriche an
    print(separate.center(width))  # Gebe die die Trennlinie aus
    print(sum.center(width))  # Gebe die vertikalen Summen aus
    print()  # Mache einen Absatz


def saveHTML(magi):
    # Füge das Grundgerüst der HTML Datei an
    html = "<!DOCTYPE html>\n" \
           "<html>\n" \
           "<head>\n" \
           "<meta charset=\"UTF-8\">\n" \
           "<meta name=\"author\" content=\"Simon Bullik\">\n" \
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" \
           "<title>Magisches Quadrat</title>\n" \
           "<link rel=\"stylesheet\" href=\"style.css\" type=\"text/css\">\n" \
           "<script src=\"script.js\"></script>\n" \
           "</head>\n" \
           "<body>\n" \
           "<h1>Magisches Quadrat</h1>\n" \
           "<p>Dimension: " + str(dimension) + "</p>\n" \
                                               "<label for=\"turns\">Drehungen</label><input id=\"turns\" type=\"range\" step=\"90\" min=\"0\" max=\"360\" value=\"0\" onchange=\"rotate()\"><br>\n" \
                                               "<button type=\"button\" onclick=\"toggle()\" id=\"control\">Zeige Kontrolle</button>\n" \
                                               "<table id=\"magi\">\n"
    vertical = []  # Initialisierung der Liste für die vertikale Summen
    diag = 0  # Startwert für die diagonlae Summe
    for i in range(0, dimension):  # Für jede Zeile
        vertical.append(0)  # Füge den Startwert für die vertikale Summe hinzu
        html += "<tr>\n"  # Füge der HTML Sruktur den Start einer neuen Zeile an
        sum = 0  # Startwert der Zeilensumme
        for j in range(0, dimension):  # Für jede Spalte
            sum += magi.get((j, i))  # Addiere den Wert zur Zeilensumme
            html += "<td>" + str(magi.get((j, i))) + "</td>\n"  # Füge den Wert als HTML Tabellen Celle hinzu
            vertical[i] += magi.get((j, i))  # Addiere den Wert zur vertikalen Summe
        diag += magi.get((i, i))  # Addiere den Wert zur digonalen Summe
        html += "<td class=\"sum\">" + str(sum) + "</td>\n"  # Füge die Zeilensumme als HTML Tabbeln Zelle hinzu
        html += "</tr>\n"  # Schließe die Zeile in HTML
    html += "<tr>\n"  # Fange neue Zeile in HTML an
    for i in vertical:
        html += "<td class=\"sum\">" + str(i) + "</td>\n"  # Füge jede vertikale Summe zu HTML hinzu
    html += "<td class=\"sum\">" + str(diag) + "</td>\n" \
                                               "</tr>" \
                                               "</table>\n" \
                                               "</body>\n" \
                                               "</html>"  # Füge die Diagonale Summe an und schließe das Dokument

    with open('magi.html', 'w', encoding='utf-8') as htmlFile:  # öffne die HTML Datei zum Schreiben
        htmlFile.write(html)  # Schreibe das HTML

    path = os.path.abspath("magi.html")  # Bekomme den absoluten Pfad zur HTML Datei
    webbrowser.open_new_tab("file://" + path)  # Öffne die HTML Datei als neuer Tab im Webbrowser


def rotate(magi, turns=0):
    for i in range(turns):  # Für dir Anzahl der Drehungen
        magi_old = magi  # Mach ein Backup des aktuellen Quadrats
        magi = {}  # lösche das Quadrat
        for i in range(0, dimension):  # für jede Zeile
            for j in range(0, dimension):  # für jede Spalte
                magi[(i, j)] = magi_old.get(
                    (dimension - 1 - j, i))  # Füge den Wert von seinem "alten" Platz auf seinen neuen ein
    return magi


if __name__ == "__main__":
    dimension = 3  # Standarddimension
    multiplicator = 1  # Standardmultiplikator
    turns = 0  # Standardanzahl der Drehungen
    while True:  # wiederhohle unendlich
        print(
            "(N) Eingabe der Dimension (3-11 / Default: 3)\n"
            "(K) Eingabe des Multiplikators (Default: 1)\n"
            "(T) Eingabe der Anzahl der Drehungen (Default: 0)\n"
            "(1) Darstellen des magischen Quadrats nach Algorithmus 1\n"
            "(2) Darstellen des magischen Quadrats nach Algorithmus 2\n"
            "(3) Speichern als „magi.html“ nach Algorithums 1\n"
            "(4) Speichern als „magi.html“ nach Algorithums 2\n"
            "(X) Exit")  # Gebe das Menü aus
        choice = input()  # Erwarte die Eingabe was geamcht werden soll
        if choice.lower() == "n":  # wenn n eingegeben wurde
            dimension_input = int(input("Dimension: "))  # Abfrage der Dimension
            if dimension_input % 2 == 1 and dimension_input > 2:  # Wenn die Zahl ungerade und größer als zwei ist
                dimension = dimension_input  # Setze die Dimension auf die eingegebene Dimension
        elif choice.lower() == "k":  # Wenn k eingegeben wurde
            multiplicator = float(input("Multiplikator: "))  # setze den Multiplikator auf die Eingabe
        elif choice.lower() == "t":  # Wenn t eingegeben wurde
            turns = int(input("Drehungen: "))  # Setze die Anzahl der Drehungen auf die Eingabe
        elif choice == "1":  # Wenn 1 eingegeben wurde
            show_magi(rotate(create_magi_1(dimension, multiplicator),
                             turns))  # zeige das magische Qudrat nach Algorythmus 1 mit den entsprechenden Drehunge und dem Multiplikator an
        elif choice == "2":  # Wenn 2 eingegeben wurde
            show_magi(rotate(create_magi_2(dimension, multiplicator),
                             turns))  # zeige das magische Qudrat nach Algorythmus 2 mit den entsprechenden Drehunge und dem Multiplikator an
        elif choice == "3":  # Wenn 3 eingegeben wurde
            saveHTML(rotate(create_magi_1(dimension, multiplicator),
                            turns))  # speichere das magische Qudrat nach Algorythmus 1 mit den entsprechenden Drehunge und dem Multiplikator als HTML Datei
        elif choice == "4":  # Wenn 4 eingegeben wurde
            saveHTML(rotate(create_magi_2(dimension, multiplicator),
                            turns))  # speichere das magische Qudrat nach Algorythmus 2 mit den entsprechenden Drehunge und dem Multiplikator als HTML Datei
        elif choice.lower() == "x":  # Wenn x eingegeben wurde
            exit()  # Schließe das Programm
