leiviskat = int(input('Leiviskät:'))
naulat = int(input('Naulat:'))
luodit = float(input('Luodit:'))

luodit = leiviskat * 20 * 32 + naulat *32 + luodit
grammat = luodit * 13.3

kilot = int(grammat / 1000)
grammat = grammat % 1000

print('Massa on', kilot, 'kg ja', grammat, 'g')
