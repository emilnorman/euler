# !/usr/bin/python
# -*- coding: utf-8 -*-
import math

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.

# Generate binary palindromic binary numbers below
# 1000000 (11110100001001000000)

def palindromic(string):
    half = math.floor(len(string) / 2)
    if (string[::-1][:half] == string[:half]):
        return True
    else:
        return False

count = 0
sum = 0

for i in range(999999, 0, -2):
    binary = bin(i)
    binary = binary[2:]

    if (palindromic(binary)):
        # Binary palindronic

        if (palindromic(str(i))):
            print(binary, i)
            count += 1
            sum += i

print(count, sum)
