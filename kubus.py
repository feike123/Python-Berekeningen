import math

# berekening voor kubus
def berekening(breedte, hoogte, diepte):
    inhoud = int(breedte) * int(hoogte) * int(diepte)
    inhoud = round(inhoud, 3)
    print("de inhoud is " + str(inhoud))