import math

# berekening voor cilinder
def berekening(doorsnede, hoogte):
    straal = int(doorsnede) / 2
    inhoud = math.pi * int(straal) ** 2 * int(hoogte)
    inhoud = round(inhoud, 3)
    print("de inhoud is " + str(inhoud))