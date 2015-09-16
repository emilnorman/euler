#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
start_time = time.time()

## Find abundant numbers
abundant = []

for n in range(10, 28124):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum > n:
        abundant.append(n)

print("--- %s seconds ---" % (time.time() - start_time))
print("Found {} abundant numbers".format(len(abundant)))

# Calculate possible sums of abundant numbers
abun_sum = set()

for a in abundant:
    for b in abundant:
        c = a + b
        if c < 28124:
            abun_sum.add(c)
        else:
            break

print("--- %s seconds ---" % (time.time() - start_time))       
print("Found {} sums of abundant numbers".format(len(abun_sum)))

result = 0

for n in range(1, 28124):
    if n not in abun_sum:
        result += n

print("--- %s seconds ---" % (time.time() - start_time))       
print(result)

