# !/usr/bin/python
# -*- coding: utf-8 -*-

# a + b + c = 1000
# a² + b² = c²
# a < b < c

for c in range(1, 998, 1):
    print("c: " + str(c))
    for b in range(1, c, 1):
        for a in range(1, b, 1):
            if (a + b + c == 1000):
                if ((a * a + b * b) == c * c):
                    print("Got it: (a,b,c)"),
                    print(a, b, c)
                    print("a*b*c = " + str(a * b * c))
                    exit(0)
