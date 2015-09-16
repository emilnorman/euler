#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
import math

start_time = time.time()

factor = [0] * 10

for n in range(0, 10):
    factor[n] = math.factorial(n)

print(factor)

result = 0

for i in range(10, 100000):
    sum = 0
    string = str(i)
    for char in string:
        sum += factor[int(char)]

    if sum == i:
        print(i)
        result += i

print("--- %s seconds ---" % (time.time() - start_time))       
print(result)

