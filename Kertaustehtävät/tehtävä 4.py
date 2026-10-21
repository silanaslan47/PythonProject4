from math import sqrt

luku = int(input("Anna kokonaisluku: "))

while luku != 0:
    if luku < 0:
        print("Virheellinen numero")
    elif luku > 0:
        print("Luvun neliöjuuri on", sqrt(luku))

    luku = int(input("Anna kokonaisluku: "))