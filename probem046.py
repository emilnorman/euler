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

    return sorted(all)

maxVal = 100000

primes = sundaram(maxVal)

squares = [i * i for i in range(1, 1001)]

for i in range(3, maxVal, 2):
    if i not in primes:
        # Composite
        for p in primes:
            solved = 0
            if p >= i:
                print(i)
                exit()
            else:
                for s in squares:
                    if i == (p + 2*s):
                        solved = 1
                        break
                    elif i < (p + 2*s):
                        break
                if solved:
                    break
