#   https://www.youtube.com/watch?v=SPajuBiS5hc

import math

def estimate_pi(length, n):
    radius = float((length) / math.sqrt(2-(2*(math.cos((math.radians(360)/n))))))
    diameter = 2 * radius
    circumference = (length * n)
    return(float(circumference/diameter))

print(str(estimate_pi(1,500000)))
