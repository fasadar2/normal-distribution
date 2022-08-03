import math
import random as rnd
import numpy as np
NV_MAGICCONST = 4 * math.exp(-0.5) / math.sqrt(2.0)
def normalvariatee(a,b,size):
    reqest = np.zeros(size)
    for i in range(size):
        reqest[i] =normalvariate(a,b)

    return reqest
def normalvariate( mu=0.0, sigma=1.0):
        random = rnd.random
        while True:
            u1 = random()
            u2 = 1.0 - random()
            z = NV_MAGICCONST * (u1 - 0.5) / u2
            zz = z * z / 4.0
            if zz <= -math.log(u2):
                break
        return mu + z * sigma