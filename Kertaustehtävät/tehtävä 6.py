lista = []

luku = int(input("Anna arvo: "))

while luku != 0:
    lista.append(luku)

    print("Lista lisäysjärjestyksessä:", lista)
    print("Lista järjestettynä:", sorted(lista))

    luku = int(input("Anna arvo: "))