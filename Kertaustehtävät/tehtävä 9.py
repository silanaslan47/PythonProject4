tuotteet = []
maarat = []

jatketaan = "Kyllä"

while jatketaan == "Kyllä":
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaan = input("Jatketaanko tuotantoa? ")

print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(tuotteet[i], ":", maarat[i], "kpl")