# !/usr/bin/python3
# -*- coding: utf-8 -*-

# !/usr/bin/python3
# -*- coding: utf-8 -*-

sum = 0

for i in range(1, 1001):
    sum += i ** i

print("Last digits: " + str(sum)[-10:])
