# !/usr/bin/python3
# -*- coding: utf-8 -*-

dig_sum = 0

for a in str(2 ** 1000):
    dig_sum += int(a)

print("Sum: " + str(dig_sum))
