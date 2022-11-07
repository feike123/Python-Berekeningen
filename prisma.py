import math

# berekening voor prisma
def berekening(breedte, hoogte, diepte):
    # berekening voor de inhoud
    grondvlak = int(breedte) * int(diepte)
    inhoud = int(grondvlak) * int(hoogte)
    inhoud = round(inhoud, 3)
    print("de inhoud is " + str(inhoud))
    # berekening voor de oppervlakte
    x = int(grondvlak) + int(hoogte)
    y = int(breedte) + int(diepte)
    oppervlakte = 2 * int(x) * int(y)
    oppervlakte = round(oppervlakte, 3)
    print("de oppervlakte is " + str(oppervlakte))