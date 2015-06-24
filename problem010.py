# !/usr/bin/python
# -*- coding: utf-8 -*-

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sundaram(limit):
    # All primes except 2

    # Generate base table
    all = range(1, (limit - 2) / 2, 1)


    # Remove numbers
    for j in xrange(1, limit):
        for i in xrange(1, j + 1):
            cur = i + j + (2 * i * j)
            if (len(all) >= cur):
                all[cur - 1] = 0
            else:
                break
    return all


goal = 2000000

list = sundaram(goal)

sum = 2L

for item in list:
    if (item != 0):
        prime = (2 * item) + 1
        sum += prime
        print(prime)

print(sum)
