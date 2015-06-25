# !/usr/bin/python3
# -*- coding: utf-8 -*-

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

# i (1, 2, ... , n), n > 1
# i < 10000

largest = (0, 0, 0)

for i in range(1, 10000):
#     print("--->" + str(i))
    factor = 1
    sum = i
    while (sum < 1000000000):
        if (sum > largest[0]):
            largest = (sum, i, factor)

        factor += 1
        tmp = i * factor
        sum *= 10 ** len(str(tmp))
#         print("* " + str(tmp) + " - " + str(len(str(tmp))))
        sum += tmp

        print(sum)

#     print(" :" + str(largest))

print(largest)

# 999973182
