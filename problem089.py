#!/usr/bin/python
#-*- coding: utf-8 -*-

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_optimizer(s):
    num = 0
    last = 0

    # Convert to integer
    for c in s:
        if last == 0:
            last = roman[c]
            num += last
        else:
            if roman[c] > last:
                num -= last * 2
                last = roman[c]
                num += last
            else:
                last = roman[c]
                num += last

    # Optimize roman printout
    rLen = 0
    rem = num

# Numerals must be arranged in descending order of size.
# M, C, and X cannot be equalled or exceeded by smaller denominations.
# D, L, and V can each only appear once.
# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.

    while (rem > 0):
        if rem >= 1000:  # M
            rLen += 1
            rem -= 1000
        elif rem >= 900:
            rLen += 2
            rem -= 900

        elif rem >= 500: # D
            rLen += 1
            rem -= 500
        elif rem >= 400:
            rLen += 2
            rem -= 400

        elif rem >= 100: # C
            rLen += 1
            rem -= 100
        elif rem >= 90:
            rLen += 2
            rem -= 90

        elif rem >= 50:  # L
            rLen += 1
            rem -= 50
        elif rem >= 40:
            rLen += 2
            rem -= 40

        elif rem >= 10:  # X
            rLen += 1
            rem -= 10
        elif rem >= 9:
            rLen += 2
            rem -= 9

        elif rem >= 5:   # V
            rLen += 1
            rem -= 5
        elif rem >= 4:
            rLen += 2
            rem -= 4

        elif rem >= 1:   # I
            rLen += 1
            rem -= 1
              
    print(s + " : " + str(num))
    return rLen

original_chars = 0
shortened_chars = 0

with open("p089_roman.txt", 'r') as f:
    for row in f:
        row = row.replace("\n", "")

        # Sum original chars
        original_chars += len(row)

        # Sum shortened chars
        shortened_chars += roman_optimizer(row)

print(original_chars - shortened_chars)

