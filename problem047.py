#!/usr/bin/python3
#-*- coding: utf-8 -*-

import math

def sundaram(limit):
    # Generate base table
    all = list(range(1, round((limit - 2) / 2), 1))

    # Remove numbers
    for j in range(1, limit):
        for i in range(1, j + 1):
            cur = i + j + (2 * i * j)
            if (len(all) >= cur):
                all[cur - 1] = 0
            else:
                break

    # remove duplicates
    all = set(all)
    
    all = [2*p + 1 for p in all]
    all[0] = 2

    return sorted(all)

maxVal = 1000000

primes = sundaram(maxVal)

distFactors = 4
lastOk = 0
row = 0

for i in range(99999, 200000):
    rem = float(i)
    factors = set()
    while(rem > 1):
        for p in primes:
            if p > rem:
                break
            if rem % p == 0:
                factors.add(p)
                rem /= p

    if len(factors) == distFactors:
        if lastOk == i-1:
            row += 1
        else:
            row = 1

        lastOk = i

    if row == 4:
        print(lastOk-distFactors+1)
        break


