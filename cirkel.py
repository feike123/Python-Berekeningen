import math

def berekening(doorsnede):
    omtrek = math.pi * int(doorsnede)
    print("de omtrek is " + str(omtrek))
    oppervlakte = int(doorsnede) ** 2 * math.pi / 4
    print("de oppervlakte is " + str(oppervlakte))
    