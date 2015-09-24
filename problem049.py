#!/usr/bin/python3
#-*- coding: utf-8 -*-

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

    result = []
    for a in sorted(all):
        if a >= 1000:
            result.append(a)

    return result

maxVal = 10000

primes = sundaram(maxVal)

for p in primes:
    p2 = p  + 3330
    p3 = p2 + 3330
    if p2 in primes and p3 in primes:
        if (sorted(str(p)) == sorted(str(p2)) and \
            sorted(str(p2)) == sorted(str(p3))):
            print(p, p2, p3, str(p) + str(p2) + str(p3))

