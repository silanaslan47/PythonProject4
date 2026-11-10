lentoasemat = {}

while True:
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoasema")
    print("3 = Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        koodi = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi

    elif valinta == "2":
        koodi = input("Anna ICAO-koodi: ")

        if koodi in lentoasemat:
            print(lentoasemat[koodi])
        else:
            print("Lentoasemaa ei löytynyt")

    elif valinta == "3":
        break