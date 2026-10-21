sanat = ["omena", "banaani", "koira", "mansikka", "auto", "tietokone"]

maara = 0

for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1

print("Yli 5 kirjainta sisältäviä sanoja on:", maara)