# !/usr/bin/python
# -*- coding: utf-8 -*-

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime 
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
# left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.

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

print("Generating primes")
upper_limit = 10000000
list = sundaram(upper_limit)
primes = [2]

for item in list:
    if (item != 0):
        primes.append((2 * item) + 1)
del list

print("Filtering out primes")
possibility = []
for prime in primes:
    p = str(prime)
    if (p[0] != "3" and p[0] != "7"):
        pass
    elif (p[-1] != "3" and p[-1] != "7"):
        pass
    else:
        possibility.append(prime)
del primes

truncable = []
print("Verify primes - step 1")
for prime in possibility:
    for i in range(len(str(prime))):
        if (int(str(prime)[i:]) not in possibility):
            break
        elif (i == len(str(prime)) - 1):
            truncable.append(prime)

res = []
print("Verify primes - step 2")
for prime in truncable:
    for i in range(len(str(prime)), 0, -1):
        if (int(str(prime)[:i]) not in possibility):
            break
        elif (i == len(str(prime)) - 1):
            res.append(prime)

print(truncable)
print(res)