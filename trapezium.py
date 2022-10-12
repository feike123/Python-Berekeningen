import math

def berekening(zijdeA, zijdeB, zijdeC, zijdeD, hoogte):
    omtrek = int(zijdeA) + int(zijdeB) + int(zijdeC) + int(zijdeC)
    print("de omtrek is " + str(omtrek))
    x = int(zijdeA) + int(zijdeC)
    oppervlakte = 0.5 * int(x) * 4
    print("de oppervlakte is " + str(oppervlakte))