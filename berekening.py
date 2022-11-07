import math

import rechthoek
import cirkel
import driehoek
import rechthoekige_driehoek
import vlieger
import kubus
import cilinder
import piramide
import parallelogram
import trapezium
import prisma

choice = input("""kies je figuur
 1 voor rechthoek
 2 voor cirkel
 3 voor driehoek
 4 voor rechthoekige driehoek
 5 voor vlieger
 6 voor kubus
 7 voor cilinder
 8 voor piramide
 9 voor parallelogram
 10 voor trapezium
 11 voor prisma
 """)

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

# rechthoekige driehoek
if choice == str("4"):
    x = input("zijde a ")
    y = input("zijde c ")
    rechthoekige_driehoek.berekening(x, y)

# vlieger
if choice == str("5"):
    x = input("basis ")
    y = input("hoogte 1 ")
    z = input("hoogte 2 ")
    vlieger.berekening(x, y, z)

# kubus
if choice == str("6"):
    x = input("breedte ")
    y = input("hoogte ")
    z = input("diepte ")
    kubus.berekening(x, y, z)

# cilinder
if choice == str("7"):
    x = input("doorsnede ")
    y = input("hoogte ")
    cilinder.berekening(x, y)

# piramide
if choice == str("8"):
    x = input("hoogte ")
    y = input("breedte ")
    piramide.berekening(x, y)

# parallelogram
if choice == str("9"):
    x = input("zijde ")
    y = input("hoogte ")

# trapezium
if choice == str("10"):
    a = input("zijde a ")
    b = input("zijde b ")
    c = input("zijde c ")
    d = input("zijde d ")
    x = input("hoogte ")
    trapezium.berekening(a, b, c, d, x)

# prisma
if choice == str("11"):
    x = input("breedte ")
    y = input("hoogte ")
    z = input("diepte ")
    prisma.berekening(x, y, z)