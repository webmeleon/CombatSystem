from arena import *

def main():

    # TestChars()


    neueArena = Arena()

    #m = Monster(100, 70, 10, 3, 5, 2, "Bisum")
    #m.set_gewAktion(1)
    #print("Test:->" + str(m.Ausfuehren(0)))

    neueArena.Kampf()



    # input("Ende -> Push Enter")


def TestChars():

    # Charakter anlegen
    y = Spieler(100, 70, 10, 3, 5, 2, "Yoda", 3, 9, 100)
    x = Monster(100, 70, 10, 3, 5, 2, "Bisum")

    print("Funktionen Testen!!!")
    print(y.get_name())
    print(x.get_name())





# Main Aufruf
if __name__ == '__main__':
        main()
