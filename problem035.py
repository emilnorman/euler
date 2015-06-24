# !/usr/bin/python
# -*- coding: utf-8 -*-

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

def sundaram(limit):
    # All primes except 2

    # Generate base table
    all = list(range(1, int((limit - 2) / 2), 1))

    # Remove numbers
    for j in range(1, limit):
        for i in range(1, j + 1):
            cur = i + j + (2 * i * j)
            if (len(all) >= cur):
                all[cur - 1] = 0
            else:
                break
    return all

upper_limit = 1000
primes = [2]
circ_primes = []

print("Generating primes...")
list = sundaram(upper_limit)

for item in list:
    if (item != 0):
        primes.append((2 * item) + 1)

del list
print(" done")

# Test circular primes
for prime in primes:
    if (len(str(prime)) == 1):
        circ_primes.append(prime)
    else:
        for steps in range(1, len(str(prime))):
            print(prime, steps)

print(primes)
print(circ_primes)