oikea_käyttäjätunnus = 'opiskelija'
oikea_salasana = 'python123'

yritykset = 0

while yritykset < 5:
    tunnus = input('Anna käyttäjätunnus:')
    salasana = input('Anna salasana:')

    if tunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
        print('Tervetuloa')
        break
    else:
        yritykset = yritykset + 1

if yritykset == 5:
    print('Pääsy evätty')