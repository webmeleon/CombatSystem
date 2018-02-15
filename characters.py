import random
from tools import *
# Import für Abstrakte classen und Methoden
# ABC wird an class übergeben!
from abc import ABC, abstractmethod


# Abstract Class Character
class Character(ABC):

    # Konstruktor mit Attribute
    def __init__(self, lebenspunkteMax, lebenspunkte, angriff, defensive, geschicklichkeit, initiative, name):
        self._lebenspunkteMax = lebenspunkteMax     # generelles Charakter Attribute
        self._lebenspunkte = lebenspunkte           # generelles Charakter Attribute
        self._angriff = angriff                      # generelles Charakter Attribute
        self._defensive = defensive                 # generelles Charakter Attribute
        self._geschicklichkeit = geschicklichkeit   # generelles Charakter Attribute
        self._initative = initiative                # generelles Charakter Attribute
        self._name = name                           # generelles Charakter Attribute
        self._KraftSammelnAktiv = 0                 # Dieses Attribut gibt an, ob Krafsammeln aktiv ist und wenn ja, wie lange noch
        self._AnvisierenAktiv = 0                   # Dieses Attribut gibt an, ob Anvisieren aktiv ist und wenn ja, wie lange noch
        self._RaserAktiv = False                    # Dieses Attribut gibt an, ob Raserei aktiv ist
        self._VerteidigenAktiv = False              # Dieses Attribut gibt an, ob Verteidigen aktiv ist
        self._gewAktion = 0                         # Dieses Attribut gibt an, welche Kampfaktion gewählt wurde (int 0-3)
        self._gewFaehigkeit = 0                     # Dieses Attribut gibt an, welche Fähigkeit gewählt wurde ( int 0-5)


    # Für alle Charaktere nötige Accessoren bereitstellen
    # Diese sind teilweise für das reine Kampfsystem nicht nötig
    # Sie werden erst bei der Einbettung in das Hauptspiel nötig
    def get_lebenspunkteMax(self):
        return self._lebenspunkteMax


    def get_lebenspunkte(self):
        return self._lebenspunkte


    def get_angriff(self):
        return self._angriff


    def get_defensive(self):
        return self._defensive


    def get_geschicklichkeit(self):
        return self._geschicklichkeit


    def get_initiative(self):
        return self._initative


    def get_name(self):
        return self._name


    def get_kraftsammelnAktiv(self):
        return self._KraftSammelnAktiv


    def set_kraftsammelnAktiv(self,kraftsammelnAktiv):
        self._KraftSammelnAktiv = kraftsammelnAktiv


    def get_anvisierenAktiv(self):
        return self._AnvisierenAktiv


    def set_anvisierenAktiv(self, anvisierenAktiv):
        self._AnvisierenAktiv = anvisierenAktiv


    def get_raserAktiv(self):
        return self._RaserAktiv


    def get_verteidigenAktiv(self):
        return self._VerteidigenAktiv


    def set_verteidigenAktiv(self, verteidigenAktiv):
        self._VerteidigenAktiv = verteidigenAktiv


    def get_gewAktion(self):
        return self._gewAktion


    def set_gewAktion(self, gewAktion):
        self._gewAktion = gewAktion


    def get_gewFaehigkeit(self):
        return self._gewFaehigkeit


    def set_gewFaehigkeit(self, gewFaehigkeit):
        self._gewFaehigkeit = gewFaehigkeit


    # Grundfunktionen festlegen
    @abstractmethod
    def AktionWaehlen(self):
        raise NotImplementedError("AktionWaehlen() wurde nicht implementiert")


    @abstractmethod
    def FaehigkeitWaehlen(self):
        raise NotImplementedError("FaehigkeitWaehlen() wurde nicht implementiert")


    # Für alle Charaktere gleichen Aktionen festlegen

    # Methode welche immer bei einem Treffer ausgeführt wird.
    def GetroffenWerden(self, gegang, unterbr):

        erlSchaden = 0

        # Prüfen ob der Angriff des Gegners eine Unterbrechung verursacht
        if unterbr == True:
            self.UnterbrochenWerden()

        # Ermitteln des tatsächlich erlittenen Schadens
        if self._VerteidigenAktiv == True:
            erlSchaden = gegang - (self._defensive * 3)
            if erlSchaden >= 0:
                self._lebenspunkte = self._lebenspunkte - erlSchaden
            else:
                erlSchaden = 0
                self._lebenspunkte = self._lebenspunkte - erlSchaden
            clear()
            printL(self._name + " erleidet " + str(erlSchaden) + " Schaden")
            input()
        else:
            erlSchaden = gegang - self._defensive
            if erlSchaden >= 0:
                self._lebenspunkte = self._lebenspunkte - erlSchaden
            else:
                erlSchaden = 0
                self._lebenspunkte = self._lebenspunkte - erlSchaden
            clear()
            printL(self._name + " erleidet " + str(erlSchaden) + " Schaden")
            print("gegang: -> " + str(gegang) + " defensive: -> " + str(self._defensive))

    # Bei allen Methoden wird der Wert als "return" zurück geliefert, der
    # als "Angriffswert" in der Aufrufenden Methode verwendet werden soll
    # Außer bei den "passiven" (z.B. UnterbochenWerden)

    def Angreifen(self, gsVerteidiger):
        # Berechnung ob ein kritischer Treffer erfolgt
        ergebnisVerteidiger = 0
        ergebnisAngreifer = 0
        ergebnis = 0
        krit = False


        if self._AnvisierenAktiv > 0:
            # Entscheiden ob Berechnung mit Anvisieren erfolgt oder ohne
            # Berechnung mit Anvisieren
            ergebnisVerteidiger = random.randint(1, 13) + (2 * gsVerteidiger)
            ergebnisAngreifer = random.randint(1, 13) + (2 * self._geschicklichkeit)
            ergebnis = ergebnisVerteidiger - ergebnisAngreifer
            if ergebnis > 0:
                krit = True
            else:
                krit = False
        else:
            # Berechnung ohne Anvisieren
            ergebnisVerteidiger = random.randint(1, 13) + (2 * gsVerteidiger)
            ergebnisAngreifer = random.randint(1, 13) + self._geschicklichkeit
            ergebnis = ergebnisVerteidiger - ergebnisAngreifer
            if ergebnis > 0:
                if random.randint(1, 101) < self._geschicklichkeit:
                    krit = True
                else:
                    krit = False
            else:
                krit = False
        # Brechnung kritischer Treffer abgeschlossen
        # Ausgabe wer angreift und ob der Angriff kritisch ist

        clear()
        printL(self._name + " greift seinen Gegner an.")

        printL("Krit JA - NEIN: -> " + str(krit))

        if krit:
            printL(self._name + " landet einen kritischen Treffer")
        # Entscheiden welche Stati aktiv sind und somit über den gelieferten Angriffsfaktor
        if krit and (self._KraftSammelnAktiv > 0) and self._RaserAktiv:
            return self._angriff * 8
        elif ((krit and (self._KraftSammelnAktiv > 0)) or (krit and self._RaserAktiv)):
            return self._angriff * 4
        elif (self._KraftSammelnAktiv > 0) or self._RaserAktiv:
            return self._angriff * 2
        elif krit:
            return self._angriff * 2
        else:
            return self._angriff
        # Entscheidung abgeschlossen

    def Verteidigen(self):
        clear()
        printL(self._name + " verteidigt sich")
        self._VerteidigenAktiv = True
        return 0

    def Kraftsammeln(self):
        clear()
        printL(self._name + " sammelt seine Kräfte")
        self._KraftSammelnAktiv = 3
        return 0

    def Anvisieren(self):
        clear()
        printL(self._name + " visiert seinen Gegner an.")
        input()
        self._AnvisierenAktiv = 3
        return 0

    def Unterbrechen(self, gsVerteidiger):
        clear()
        printL(self._name + " versucht seinen Gegner zu unterbrechen")
        return self.Angreifen(gsVerteidiger) / 2


    def UnterbrochenWerden(self):
        printL("Der Angriff des Gegners unterbricht die aktiven Fähigkeiten von " + self._name)
        self._KraftSammelnAktiv = 0
        self._AnvisierenAktiv = 0
        self._RaserAktiv = False


    def Raserei(self, gsVerteidiger):
        clear()
        printL(self._name + " verfällt in wilde Raserei!!!")
        self._RaserAktiv = True
        return self.Angreifen(gsVerteidiger)

    # Hier muss bei der Überführung in das Hauptspiel selbstverständlich noch
    # eine Logik ergänzt werden, welche dem Ausführenden TAler bringt!!!
    def Raub(self, gsVerteidiger):
        clear()
        printL(self._name + " versucht seinen Gegner zu berauben.")
        return ((self.Angreifen(gsVerteidiger)) * 80) / 100


    # Methode welche die gewählte Aktion oder Fähigkeit aufruft
    # liefert den ausgeteilten Schaden zurück
    def Ausfuehren(self, gsVerteidiger):
        print("Ausführen AKTIV!!! --- >")
        input("Enter Ausführe")
            # Gewählte Fähigkeit aufrufen
        if self.get_gewFaehigkeit() != 0:
            print("Faehigkeit wird gewählt: -->" + str(self._gewFaehigkeit) + "gsVerteidiger --> " + str(gsVerteidiger))
            input("Enter Faehigkeit")
            # switch/case Ersatz, da kein switch in Python möglich
            if self._gewFaehigkeit == 1:
                print("1 Faehigkeit")
                input()
                return self.Kraftsammeln()
            if self._gewFaehigkeit == 2:
                print("2 Faehigkeit")
                input()
                return self.Anvisieren()
            if self._gewFaehigkeit == 3:
                print("3 Faehigkeit")
                input()
                return self.Unterbrechen(gsVerteidiger)
            if self._gewFaehigkeit == 4:
                print("4 Faehigkeit")
                input()
                return self.Raserei(gsVerteidiger)
            if self._gewFaehigkeit == 5:
                print("5 Faehigkeit")
                input()
                return self.Raub(gsVerteidiger)
            if 6 <= self._gewFaehigkeit <= 0:
                print("KEINE Faehigkeit")
                input()
                return 0
        else:
            print("gewAktion: --> " + str(self._gewAktion))
            input("Enter Aktion")
            # gewählte Aktion aufrufen
            if self._gewAktion == 1:
                return self.Angreifen(gsVerteidiger)
            if self._gewAktion == 2:
                return self.Verteidigen()
            if 3 <= self._gewAktion <= 0:
                return 0
        # Ende der Methode
