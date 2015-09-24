#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def isPenta(number):
    num = (math.sqrt(1+24*number) + 1.0) / 6.0
    return (num == int(num))

notDone = True
j = 1
while(notDone):
    j += 1
    p1 = int(j*(3*j-1)/2)

    for k in range(1, j):
        p2 = int(k*(3*k-1)/2)

        if isPenta(p1-p2) and isPenta(p1+p2):
            print(p1-p2, p1, p2)
            notDone = False

