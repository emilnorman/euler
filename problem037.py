# !/usr/bin/python3
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

print("Step 1: Generating primes")
upper_limit = 1000000
list = sundaram(upper_limit)
primes = [2]

for item in list:
    if (item != 0):
        primes.append((2 * item) + 1)
del list
print("done")

# - Primes has to start and end with either 3 or 7
# - Primes can only contain 1,2,3,5,7,9
# - 2, 3, 5, and 7 are not considered to be truncatable primes.

print("Step 2: Filtering out primes - has to start/end with 3 or 7")
step2 = []
for p in primes:
    ps = str(p)
    if (ps[0] != "2" and ps[0] != "3" and ps[0] != "5" and ps[0] != "7"):
        # Does not start with 3, 5, 7 or 2
        pass
    elif (ps[-1] != "3" and ps[-1] != "7"):
        # Does not end with 3 or 7
        pass
    elif (p < 10):
        pass
    else:
        step2.append(p)

print("done")

print("Step 3: Filtering out primes - can only contain 1,2,3,5,7,9")
step3 = []
for p in step2:
    ps = str(p)
    for i in range(len(ps)):
        if (ps[i] != '1' and ps[i] != '2' and ps[i] != '3' \
            and ps[i] != '5' and ps[i] != '7' and ps[i] != '9'):
            break
        elif (i == len(ps) - 1):
            step3.append(p)
print("done")

print("Step 4: Verify primes - truncable from left")
step4 = []
for p in step3:
    ps = str(p)
    for i in range(len(ps)):
        if (int(ps[i:]) not in primes):
            break
        elif (i == len(ps) - 1):
            step4.append(p)
print("done")

step5 = []
print("Step 5: Verify primes - truncable from right")
for p in step4:
    ps = str(p)
    for i in range(len(ps), 0, -1):
        if (int(ps[:i]) not in primes):
            break
        elif (i == 1):
            step5.append(p)

print("done")

print(step5)
print(len(step5))
print(sum(step5))
