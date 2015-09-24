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

    return sorted(all)

maxVal = 1000000

primes = sundaram(maxVal)

number = 0
prime = 0

for i in range(0, 3):
    sum = 0
    for j in range(0, 1000):
        sum += primes[i+j]

        for test in primes:
            if sum == test:
                if j+1 > number:
                    number = j+1
                    prime = sum
                    print(number, prime, i)
                    break
            elif test > sum:
                break

print(number, prime)

