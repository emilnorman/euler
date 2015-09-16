#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
from fractions import gcd

start_time = time.time()

# (a*10 + b)/(c*10 + d)

num = 1
denom = 1


for a in range(1, 10):
    for c in range(1, 10):
        for d in range(1, 10):
            if ((a*10.0 + c)/(c*10 + d)) == (1.0*a / d):
                if (a*10 + c) != (c*10 + d):
                    num *= (a*10 + c)
                    denom *= (c*10 + d)
                    print(a*10 + c, c*10 + d)

print("--- %s seconds ---" % (time.time() - start_time))       
print(num, denom)
print(denom/num)

