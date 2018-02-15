from spieler import *
from monster import *

class Arena(object):
    # Statische Methode -> ermittelt ob zuerst Held oder Ki am Zug ist
    @staticmethod
    def __HeldZuErst(HeldIni, KiIni):

        # Randomwerte generieren -> wer fängt an
        if (random.randint(1, 7) + HeldIni) > (random.randint(1, 7) + KiIni):
            print("Held beginnt")
            return True
        elif (random.randint(1, 7) + HeldIni) < (random.randint(1, 7) + KiIni):
            print("Ki beginnt")
            return False
        else:
            if random.randint(1, 3) == 2:
                # Held beginnt
                return True
            else:
                # Ki beginnt
                return False

        # Kampfreihenfolge fertig ermitteln

    @staticmethod
    def Kampf():
        # stellt Attribute zur Verfügung, welche die Informationen aufnehmen, welche Aktion als nächtes ausgeführt werden soll
        HeldAktion = ""
        HeldFaehigkeit = ""
        KIAktion = ""
        KIFaehigkeit = ""
        angerichteterSchaden = 0

        # Initialisiert Einen steurbaren Helden und einen KI gesteuerten Kampfteilnehmer.
        # Im Hauptspiel sind diese Werte variabel und werden von außen übergeben.

        # held = Spieler(300, 300, 30, 25, 20, 15, "Yoda", 8, 10, 3500)
        held = Monster(300, 200, 30, 25, 20, 15, "Yoda")
        ki = Monster(200, 200, 25, 20, 15, 10, "Bisasam")

        # Kampfbeginn wird angesagt
        printL(held.get_name() + " trifft auf " + ki.get_name() + ". Der Kampf beginnt")

        input("Push Enter")
        # Beginn einer Kampfschleife, welche so lange abgearbeitet wird, bis einer der Kampfteilnehmer keine Lebenspunkte mehr hat.
        while (held.get_lebenspunkte() > 0) and (ki.get_lebenspunkte() > 0):

            # wählen der nächsten Kampfaktion
            # Held
            while True:
                HeldAktion = held.AktionWaehlen()
                if held.get_gewAktion() == 3:
                    HeldFaehigkeit = held.FaehigkeitWaehlen()
                    if not held.get_gewFaehigkeit() == 0:
                        break
                if not held.get_gewAktion() == 0 and held.get_gewFaehigkeit() == 0:
                    break

            # Ki
            while True:
                KIAktion = ki.AktionWaehlen()
                if ki.get_gewAktion() == 3:
                    KIFaehigkeit = ki.FaehigkeitWaehlen()
                    if not ki.get_gewFaehigkeit() == 0:
                        break
                if not ki.get_gewAktion() == 0 and ki.get_gewFaehigkeit() == 0:
                    break

            # Auswahl Kampfaktion Ende

            # Abarbeiten der gewählten Kampfaktion
            # Abfragen wer beginnt
            if Arena.__HeldZuErst(held.get_initiative(), ki.get_initiative()):

                # Held führt Aktion zuerst aus
                # Ermittelt den Schaden der vom Held zugefügt wird auf Grundlage
                # der gewählten Aktion / Fähigkeit und der Geschicklichkeit des Gegners.

                angerichteterSchaden = held.Ausfuehren(ki.get_geschicklichkeit())
                # Entscheidet ob die Aktion des Helden den Gegner zusätzlich unterbricht oder nicht.

                if HeldFaehigkeit == "Unterbrechen":
                    ki.GetroffenWerden(angerichteterSchaden, True)
                else:
                    ki.GetroffenWerden(angerichteterSchaden, False)
                # Die Ki wurde getroffen und Ihre Werte wurden manipuliert.

                # Prüfen ob die Ki besiegt ist
                if ki.get_lebenspunkte() <= 0:
                    break
                # Jetzt wird die Ki ihren Zug ausführen

                # Ermittelt den Schaden der von der Ki zugeführt wird auf Grundlage
                # der gewählten Aktion / Fähigkeit und der Geschicklichkeit des Helden.

                angerichteterSchaden = ki.Ausfuehren(held.get_geschicklichkeit())
                # Entscheidet ob die Aktion der KI den Helden zusätzlich unterbricht oder nicht.
                if KIFaehigkeit == "Unterbrechen":
                    held.GetroffenWerden(angerichteterSchaden, True)
                else:
                    held.GetroffenWerden(angerichteterSchaden, False)
                # Der Held wurde getroffen und sein Werte wurden manupuliert

                # Prüfen ob der Held besiegt ist
                if held.get_lebenspunkte() <= 0:
                    break
                # Ende der Prüfung
            # genau das selbe wie zuvor wird ausgeführt aber in der umgekehrten Reihenfolge.
            else:
                # KI führt Aktionen zuerst aus
                # Ermittelt den Schaden der von der KI zugefügt wird auf Grundlage
                # der gewählten Aktion / Fähigkeit und der Geschicklichkeit des Helden.

                angerichteterSchaden = ki.Ausfuehren(held.get_geschicklichkeit())
                # Entscheidet ob die Aktion der KI den Helden zusätzlich unterbricht oder nicht.

                if KIFaehigkeit == "Unterbrechen":
                    held.GetroffenWerden(angerichteterSchaden, True)
                else:
                    held.GetroffenWerden(angerichteterSchaden, False)
                # Der Held wurde getroffen und seine Werte wurden manipuliert.
                # Prüfen ob der Held besiegt ist
                if held.get_lebenspunkte() <= 0:
                    break
                # Prüfen ob der Held besiegt wurde
                # Jetzt wird der Held seine Aktion ausführen.
                # Ermittelt den Schaden der vom Held zugefügt wird auf Grundlage
                # der gewählten Aktion / Fähigkeit und der Geschicklichkeit des Gegners.

                angerichteterSchaden = held.Ausfuehren(ki.get_geschicklichkeit())
                # Entscheidet ob die Aktion des Helden den Gegner zusätzlich unterbricht oder nicht.
                if HeldFaehigkeit == "Unterbrechen":
                    ki.GetroffenWerden(angerichteterSchaden, True)
                else:
                    ki.GetroffenWerden(angerichteterSchaden, False)
                # Die Ki wurde getroffen und ihre Werte wurden manipuliert.
                # Prüfen ob die Ki besiegt wurde

                if ki.get_lebenspunkte() <= 0:
                    break
                # Ende der Prüfung

            # Kampfaktionen sind abgearbeitet


            # Die temporären Statusveränderungen werden um 1 dekrementiert
            held.set_kraftsammelnAktiv(held.get_kraftsammelnAktiv() - 1)
            ki.set_kraftsammelnAktiv(ki.get_kraftsammelnAktiv() - 1)
            held.set_anvisierenAktiv(held.get_anvisierenAktiv() - 1)
            ki.set_anvisierenAktiv(ki.get_anvisierenAktiv() - 1)
            held.set_verteidigenAktiv(False)
            ki.set_verteidigenAktiv(False)
            # Gewählte Fähigkeiten und Aktionen werden zurückgesetzt
            HeldAktion = ""
            HeldFaehigkeit = ""
            KIAktion = ""
            KIFaehigkeit = ""
            angerichteterSchaden = 0
            held.set_gewAktion(0)
            ki.set_gewAktion(0)
            held.set_gewFaehigkeit(0)
            ki.set_gewFaehigkeit(0)

            # Feststellen wie viel Lebenspunkte die Kontrahenten noch haben.
            clear()
            printL("Am Ende der Kampfrunde hat " + held.get_name() + " noch " + str(held.get_lebenspunkte()) + " LP und " + ki.get_name() + " noch " + str(ki.get_lebenspunkte()) + " LP.")
            printL("Der Kamp dauert an")
            # input("Push Enter")
        # Ende der Kampfschleife

        # Anzeigen und zurückgeben wer den Kampf gewonnen hat
        if held.get_lebenspunkte() <= 0:
            # Verloren
            printL("Der Kampf ist vorbei. " + held.get_name() + " ist gestorben...")
            # input()
            return False
        else:
            # Gewonnen
            printL("Der Kampf ist vorbei. " + held.get_name() + " hat gewonnen!!!")
            # input()
            return True
        # Ende
