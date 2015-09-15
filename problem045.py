# -*- coding: utf-8 -*-
# Slow solution :(

minVal = 143
maxVal = 100000

triag = [int(n * (n + 1) / 2) for n in range(minVal, maxVal)]
print("Triangle")
penta = [int(n * (3*n - 1) / 2) for n in range(minVal, maxVal)]
print("Pentagonal")
hexa  = [int(n * (2*n - 1)) for n in range(minVal, maxVal)]
print("Hexagonal")

for t in triag:
    nomatch = 0
    for p in penta:
        if p == t:
            for h in hexa:
                if h == t:
                    print(t)
                    break
                elif h > t:
                    nomatch = 1
                    break
            if nomatch:
                break
            elif p > t:
                break
