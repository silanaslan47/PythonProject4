import random

noppien_maara = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(noppien_maara):
    noppa = random.randint(1, 6)
    summa = summa + noppa

print("Silmälukujen summa on", summa)


