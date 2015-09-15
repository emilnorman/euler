#!/usr/bin/python

part1 = range(0, 1000, 3)
part2 = range(0, 1000, 5)

all = set(part1 + part2)

print(sum(all))
