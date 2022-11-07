import math

# berekening voor parallelogram
def berekening(zijde, hoogte):
    oppervlakte = int(zijde) * int(hoogte)
    oppervlakte = round(oppervlakte, 3)
    print("de oppervlakte is " + str(oppervlakte))