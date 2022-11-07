import math

# berekening voor cirkel
def berekening(doorsnede):
    omtrek = math.pi * int(doorsnede)
    omtrek = round(omtrek, 3)
    print("de omtrek is " + str(omtrek))
    oppervlakte = int(doorsnede) ** 2 * math.pi / 4
    oppervlakte = round(oppervlakte, 3)
    print("de oppervlakte is " + str(oppervlakte))
    