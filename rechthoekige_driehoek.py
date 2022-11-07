import math

# berekening voor rechthoekige driehoek
def berekening(zijdeA, zijdeB):
    zijdeC = int(zijdeA) ** 2 + int(zijdeB) ** 2
    zijdeC = math.sqrt(zijdeC)
    zijdeC = round(zijdeC, 3)
    print("zijde c is " + str(zijdeC))