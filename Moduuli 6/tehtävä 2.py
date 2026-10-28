import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))

noppa = 0

while noppa != tahkot:
    noppa = heita_noppaa(tahkot)
    print(noppa)