import math

# berekening voor rechthoek
def berekening(breedte, lengte):
    # berekening voor de omtrek
    omtrek = int(breedte) * 2 + int(lengte) * 2
    omtrek = round(omtrek, 3)
    print("de omtrek is " + str(omtrek))
    # berekening voor de oppervlakte
    oppervlakte = int(breedte) * int(lengte)
    oppervlakte = round(oppervlakte, 3)
    print("de oppervlakte is " + str(oppervlakte))
