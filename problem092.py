#!/usr/bin/python3
#-*- coding: utf-8 -*-

import math

print("Precalculating squares")
precalc = []
for i in range(0, 10000000):
    s = str(i)
    tmp = 0
    for c in s:
        tmp += int(c)**2
    precalc.append(tmp)

print("Iterating")
at89 = 0

for i in range(2, 10000000):
    if i % 100000 == 0:
        print(i)

    tmp = i
    while(tmp != 1 and tmp != 89):
        tmp = precalc[tmp]

    if tmp == 89:
        at89 += 1

print(at89)

