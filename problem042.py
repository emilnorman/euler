#!/usr/bin/python3
# -*- coding: utf-8 -*-

with open("p042_words.txt", "r") as file:
    row = file.readline()
    words = row.upper().replace("\"", "").split(",")

# Find longest word
maxlen = 0
for word in words:
    maxlen = max(maxlen, len(word))

# Calculate triangle numbers
tria_target = maxlen * 30

t = [1]
i = 2
while(t[-1] <= tria_target):
    t.append(int(i*(i+1)/2))
    i += 1

# Check words
result = 0

for word in words:
    s = 0
    for c in word:
        s += ord(c) - 64

    if s in t:
        result += 1
        print(word)

print(result)

