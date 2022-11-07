import math

# berekening voor driehoek
def berekening(basis, hoogte):
    oppervlakte = int(basis) * int(hoogte) / 2
    oppervlakte = round(oppervlakte, 3)
    print("de oppervlakte is " + str(oppervlakte))