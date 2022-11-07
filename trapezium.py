import math

# berekening voor trapezium
def berekening(zijdeA, zijdeB, zijdeC, zijdeD, hoogte):
    # berekening voor de omtrek
    omtrek = int(zijdeA) + int(zijdeB) + int(zijdeC) + int(zijdeC)
    omtrek = round(omtrek, 3)
    print("de omtrek is " + str(omtrek))
    # berekening voor de oppervlakte
    x = int(zijdeA) + int(zijdeC)
    oppervlakte = 0.5 * int(x) * 4
    oppervlakte = round(oppervlakte, 3)
    print("de oppervlakte is " + str(oppervlakte))