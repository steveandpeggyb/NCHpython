from __future__ import with_statement

import numpy as np
import decimal, time

def pi_gauss_legendre():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2                
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1                
        pi = None
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            piold = pi
            pi    = (a + b) * (a + b) / (4 * t)
            if pi == piold:  # equal within given precision
                break
    return +pi

starttime=time.process_time()
decimal.getcontext().prec = 10001   #8751
pi = pi_gauss_legendre()
stoptime=time.process_time()
# print(pi)
duration = stoptime - starttime
decimalPlaces = len(str(pi))-2
CharPerSec = decimalPlaces/duration

print(f'Decimal Places Calculated: ' + str(decimalPlaces))
print('After {0:5.4f} seconds of computation, {1:d} decimal places were computed resulting is a {2:5.3f} decimals/second.'.format(duration, decimalPlaces, CharPerSec))
