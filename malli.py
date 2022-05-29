# Arvosanataulukko, joka on alussa tyhjä, mutta siihen lisätään käyttäjän syöttämiä kurssiarvosanoja
arvosanat = []


# Apufunktio laskemaan taulukossa esiintyvien numeroiden summa
def taulukonSumma(numerot):
    summa = 0
    for numero in numerot:
        summa += numero
    return summa

# Apufunktio laskemaan keskiarvo tuodusta taulukosta, hyödyntäen "taulukonSumma"-funktiota
def keskiarvo(numerot):
    lkm = len(numerot)
    summa = taulukonSumma(numerot)
    ka = summa/lkm
    return ka

# "Pääohjelma", joka toivottaa käyttäjän tervetulleeksi ja alustaa kaiken.
print("Tervetuloa laskemaan oma keskiarvosi lukuvuoden päätteeksi. Syötä numeroita ja paina \"enter\", kun olet valmis kirjoita \"laske\", niin ohjelma laskee keskiarvosi.")
print() 
while(True):
    kasky = input()
    if kasky == "laske":
        keskiarvo = keskiarvo(arvosanat)
        print("Keskiarvosi on: " + str(keskiarvo))
        break
    else:
        arvosanat.append(int(kasky))
    














