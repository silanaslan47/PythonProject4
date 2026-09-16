luvut = []

luku = input('Anna luku:')

while luku != '':
    luvut.append(float(luku))
    luku = input('Anna luku:')

if len(luvut) > 0:
    print('Pienin luku:', min(luvut))
    print('Suurin luku:', max(luvut))
    