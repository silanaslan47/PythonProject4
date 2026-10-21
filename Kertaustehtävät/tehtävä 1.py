tuntipalkka = float(input('Anna tuntipalkkka: '))
tunnit = float(input('Anna tehdyt tunnit: '))
viikonpaiva = input('Anna viikonpäivä: ')

if viikonpaiva == 'sunnuntai':
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print('Päiväpalkka:', paivapalkka)
