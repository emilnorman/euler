# !/usr/bin/python3
# -*- coding: utf-8 -*-

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

# i (1, 2, ... , n), n > 1
# i < 10000

def is_pandigital(num):
    s = str(num)

    if ('1' in s and '2' in s and '3' in s and '4' in s and '5' in s and
        '6' in s and '7' in s and '8' in s and '9' in s):
        return True

    return False

largest = (0, 0, 0)

for i in range(1, 100000):
    factor = 1
    sum = i
    while (sum < 1000000000):
        if (is_pandigital(sum)):
            if (sum > largest[0]):
                largest = (sum, i, factor)

        factor += 1
        tmp = i * factor
        sum *= 10 ** len(str(tmp))
        sum += tmp

print(largest)
