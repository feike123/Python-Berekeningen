import math

# berekening voor vlieger
def berekening(basis, hoogte1, hoogte2):
    oppervlakte = int(basis) * int(hoogte1) / 2 + int(basis) * int(hoogte2)
    oppervlakte = round(oppervlakte, 3)
    print("de opervlakte is " + str(oppervlakte))