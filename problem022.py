# !/usr/bin/python
# -*- coding: utf-8 -*-

with open ("p022_names.txt", 'r') as file:
    names = sorted(file.read().replace('\"', '').split(","))

char_base = 64

sum = 0

for i, name in enumerate(names):
    name_sum = 0

    for char in name:
        name_sum += ord(char) - char_base

    sum += name_sum * (i + 1)

print(sum)
