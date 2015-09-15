#!/usr/bin/python
#-*- coding: utf-8 -*-

# 28433 * 2**7830457 + 1
# a * 2^b + 1

form = 10000000000

k10 = 2**10000 % form
m7_83 = k10**783 % form
last = 2**457 * m7_83 % form
last = last * 28433 % form
last += 1

print(last)

