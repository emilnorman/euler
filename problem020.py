# !/usr/bin/python3
# -*- coding: utf-8 -*-

import math

dig_sum = 0

for a in str(math.factorial(100)):
    dig_sum += int(a)

print("Sum: " + str(dig_sum))
