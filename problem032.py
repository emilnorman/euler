#!/usr/bin/python3
#-*- coding: utf-8 -*-

a = set()

for m1 in range(1, 2000):
    for m2 in range(1, 2000):
        p = m1 * m2
        s = str(m1) + str(m2) + str(p)

        if len(s) == 9:
            if '1' in s and '2' in s and '3' in s and \
               '4' in s and '5' in s and '6' in s and \
               '7' in s and '8' in s and '9' in s:
                print(m1, m2, p)
                if p not in a:
                    a.add(p)

print(a)
print(sum(a))

