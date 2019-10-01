#Python 3.7 - Calculate Pi using Archimedes Method.
#Pi to 75 Places for reference

import math
from decimal import *
getcontext().prec = 100

#Perim = perimeter of the polygon
#Dia = Diameter of circle & polygon
#PolySides = number of sides of polygon
#SideLen = Side length 1 for beginning equilateral triangle
#radius_a = radius to slice radius_a = sqrt((1^) - (SideLen/2)^2)
#radius_b = 1 - radius_a
#SideLenNew = sqrt((radius_b^2) + (SideLen2 / 2)^2))

pi = 0
PolySides = 6   #Start with hexagon -> Isosceles (equilateral) triangles (all sides equal)
SideLen = 1     #All sides in equilateral triangle = 1 also = radius
Perim = 6       #Initial perimeter of hexagon
Dia = 2         #Diameter is 2

while PolySides < 1000000000000000000000000000000:             #30 x 0. Loop
    SideLen2 = Decimal(SideLen) / Decimal(2)                   #Half of SideLen
    radius_a = Decimal((1**2)-(SideLen/2)**2).sqrt()           #Length of radius_a
    radius_b = Decimal(1) - Decimal(radius_a)                  #Length of radius_b
    SideLenNew = Decimal((radius_b**2)+(SideLen2**2)).sqrt()   #Length of the "new side"
    PolyCircum = Decimal(PolySides * SideLen)                  #Number of polygon sides times each side length
    pi = PolyCircum / Dia                                      #Current approximation of pi
    print('Polygon Sides: ', PolySides, ' Pi=', format(pi, '0.50'))
    SideLen = SideLenNew                                       #Keep the "new" side length for the next round
    PolySides = PolySides * 2
