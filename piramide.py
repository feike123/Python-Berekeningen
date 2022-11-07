import math

# berekening voor piramide
def berekening(hoogte, breedte):
    oppervlakte = int(breedte) ** 2
    inhoud = int(oppervlakte) * int(hoogte) / 3
    inhoud = round(inhoud, 3)
    print("de inhoud is " + str(inhoud))