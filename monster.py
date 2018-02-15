from characters import *

# Konstruktor mit Basiskonstruktor
class Monster(Character):
    def __init__(self, lebenspunkteMax, lebenspunkte, angriff, defensive, geschicklichkeit, initiative, name):
        super(Monster, self).__init__(lebenspunkteMax, lebenspunkte, angriff, defensive, geschicklichkeit, initiative, name)


    # Aktionsauswahl
    def AktionWaehlen(self):
        self._gewAktion = 0
        # Prüfen ob Raserei aktiv ist. Wenn ja dann keine Auswahl möglich
        if self._RaserAktiv:
            printL(self._name + "ist in Wilder Raserei und kann keine Aktion wählen")
            self._gewAktion = 1
            return "Angriff"
        else:
            clear()
            # Ermitteln einer Zufallszahl zwischen 1 und 4
            eingabe = random.randint(1, 4)
            # Auswertung der Zufallszahl
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
                # input()
                printL("Auswahl: " + str(eingabe))
                self._gewAktion = 0
                return "ungültig"
    #Aktion Ende

    # Fähigkeitauswahl
    def FaehigkeitWaehlen(self):
        self._gewFaehigkeit = 0
        clear()
        printL("Bitte Aktion wählen.(1 = Kraft sammeln, 2 = Anvisieren, 3 = Unterbrechen, 4 = Raserei, 5 = Raub)")
        # Ermitteln einer Zufallszahl zwischen 1 und 6
        eingabe = random.randint(1, 6)
        # Auswertung der Zufallszahl
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
            # input()
            self._gewAktion = 0
            return "ungültig"
    # Fähigkeit Ende
