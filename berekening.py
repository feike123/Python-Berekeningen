import math

import rechthoek
import cirkel
import driehoek

choice = input("kies je figuur ")

# rechthoek
if choice == str("1"):
    x = input("breedte ")
    y = input("lengte ")
    rechthoek.berekening(x, y)

# cirkel
if choice == str("2"):
    x = input("doorsnede ")
    cirkel.berekening(x)

# driehoek
if choice == str("3"):
    x = input("basis ")
    y = input("hoogte ")
    driehoek.berekening(x, y)