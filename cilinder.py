import math

def berekening(doorsnede, hoogte):
    straal = int(doorsnede) / 2
    inhoud = math.pi * int(straal) ** 2 * hoogte
    print("de inhoud is " + str(inhoud))