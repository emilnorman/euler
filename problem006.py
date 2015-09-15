#!/usr/bin/python

sum_square = 0
square_sum = 0

for i in xrange(1, 101):
    square_sum += i

square_sum **= 2

print(square_sum)

for i in xrange(1, 101):
    sum_square += i ** 2

print(sum_square)

print("Diff: " + str(square_sum - sum_square))
