#!/usr/bin/python3
#-*- coding: utf-8 -*-

count = 0

# a^b = c
for a in range(1, 100):
    for b in range(0, 100):
        c = a**b
        if len(str(c)) == b:
            print(c, a, b)
            count += 1

print(count)

