#!/usr/bin/python

t1 = 999
t2 = 999

largest = (0, 0, 0)

for t1 in xrange(999, 0, -1):
    for t2 in xrange(999, 0, -1):
        prod = t1 * t2

        if (str(prod)[::-1] == str(prod)):
            if (prod > largest[0]):
                largest = (prod, t1, t2)

print("Largest palindrome product: " + str(largest))
