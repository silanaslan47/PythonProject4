import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija cm: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
else:
    print("Toinen pizza antaa paremman vastineen rahalle.")