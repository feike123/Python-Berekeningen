import math

def berekening(breedte, hoogte, diepte):
    grondvlak = int(breedte) * int(diepte)
    inhoud = int(grondvlak) * int(hoogte)
    print("de inhoud is " + str(inhoud))
    x = int(grondvlak) + int(hoogte)
    y = int(breedte) + int(diepte)
    oppervlakte = 2 * int(x) * int(y)
    print("de oppervlakte is " + str(oppervlakte))