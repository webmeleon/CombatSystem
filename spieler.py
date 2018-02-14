from kampfsystem.characters import *

# Konstruktor mit Basiskonstruktor
class Spieler(Character):
    def __init__(self, lebenspunkteMax, lebenspunkte, angriff, defensive, geschicklichkeit, initiative, name, lv, cp, ep):
        super(Spieler, self).__init__(lebenspunkteMax, lebenspunkte, angriff, defensive, geschicklichkeit, initiative, name)
        self.lv = lv
        self.cp = cp
        self.ep = ep


    # Spieler eigene Funktionen:
    # Aktionsauswahl
    # Bei der Überführung in das Hauptspiel müssen noch die Aktionen Gegenstand benutzen und Fliehen hinzugefügt werden!!!
    def AktionWaehlen(self):
        self._gewAktion = 0
        #Prüfen ob Raserei "aktiv" ist. Wenn ja, dann keine Aktionsauswahl möglich.
        if self._RaserAktiv:
            printL(self._name + "ist in Wilder Raserei und kann keine Aktion wählen")
            self._gewAktion = 1
            return "Angriff"
        else:
            clear()
            printL("Bitte Aktion wählen.(1 = Angriff, 2 = Verteidigen, 3 = Fähigkeit wählen)")

            # Eingabe Prüfen
            while True:

                # Versuche die Eingabe auszuwerten als Zahl oder auch als Berechnung
                try:
                    eingabe = int(eval(input("Ihre Eingabe: ")))
                # Versuch ist gescheitert eingabe wird auf 0 gesetzt somit ist die Auswahl nicht gültig
                except(NameError, ValueError, TypeError, RuntimeError):
                    eingabe = 0

                if type(eingabe) == int and 0 < eingabe < 4:
                    if eingabe == 1:
                        self._gewAktion = 1
                        printL("Auswahl: " + str(eingabe))
                        return "Angriff"
                    elif eingabe == 2:
                        self._gewAktion = 2
                        printL("Auswahl: " + str(eingabe))
                        return "Verteidigen"
                    elif eingabe == 3:
                        self._gewAktion = 3
                        printL("Auswahl: " + str(eingabe))
                        return "Fähgikeit"
                    else:
                        printL("Auswahl nicht gültig")
                        printL("Auswahl: " + str(eingabe))
                        self._gewAktion = 0
                        return "ungültig"
                else:
                    printL("Auswahl nicht gültig -> nicht 1-3")
                    printL("Auswahl: " + str(eingabe))
                    self._gewAktion = 0
                    return "ungültig"
    # Ende Aktionswahl


    def FaehigkeitWaehlen(self):

        self._gewFaehigkeit = 0

        clear()
        printL("Bitte Aktion wählen.(1 = Kraft sammeln, 2 = Anvisieren, 3 = Unterbrechen, 4 = Raserei, 5 = Raub)")
        # Eingabe Prüfen
        while True:

            # Versuche die Eingabe auszuwerten als Zahl oder auch als Berechnung
            try:
                eingabe = int(eval(input("Ihre Eingabe: ")))
            # Versuch ist gescheitert eingabe wird auf 0 gesetzt somit ist die Auswahl nicht gültig
            except(NameError, ValueError, TypeError, RuntimeError, SystemError):
                eingabe = 0

            if type(eingabe) == int and 0 < eingabe < 6:
                if eingabe == 1:
                    self._gewFaehigkeit = 1
                    printL("Auswahl: " + str(eingabe))
                    return "Kraft sammeln"
                elif eingabe == 2:
                    self._gewFaehigkeit = 2
                    printL("Auswahl: " + str(eingabe))
                    return "Anvisieren"
                elif eingabe == 3:
                    self._gewFaehigkeit = 3
                    printL("Auswahl: " + str(eingabe))
                    return "Unterbrechen"
                elif eingabe == 4:
                    self._gewFaehigkeit = 4
                    printL("Auswahl: " + str(eingabe))
                    return "Raserei"
                elif eingabe == 5:
                    self._gewFaehigkeit = 5
                    printL("Auswahl: " + str(eingabe))
                    return "Raub"
                else:
                    printL("Auswahl nicht gültig")
                    printL("Auswahl: " + str(eingabe))
                    self._gewAktion = 0
                    return "ungültig"
            else:
                printL("Eingabe nicht gültig -> nicht 1-5")
                printL("Auswahl: " + str(eingabe))
                self._gewFaehigkeit = 0
                return "ungültig"
                # Ende Fähigkeit