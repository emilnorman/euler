#!/usr/bin/python3
#-*- coding: utf-8 -*-

p = 5

powers = [i**p for i in range(0, 10)]

tot_sum = 0

for i in range(2, 200000):
    s = str(i)
    s_sum = 0

    for c in s:
        s_sum += powers[int(c)]

    if s_sum == i:
        tot_sum += i        
        print(i)

print("----------")
print(tot_sum)

