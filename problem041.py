# -*- coding: utf-8 -*-

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

    return all

maxVal = 10000000

primes = sundaram(maxVal)

largest = 0

for p in primes:
    length = len(str(p))
    if len(set(str(p))) == length:
        for i in range(1, length + 1):
            if not str(i) in str(p):
                break

            if i == length:
                print(p, length)
                largest = max(largest, p)

print(largest)
