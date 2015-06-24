#!/usr/bin/python

terms = [0, 1]
value = terms[0] + terms[1]

sum = 0

while(value < 4000000):
    if not (value % 2):
        sum += value

    # Update
    terms[0] = terms[1]
    terms[1] = value
    value = terms[0] + terms[1]

print(sum)
