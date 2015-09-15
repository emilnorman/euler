#!/usr/bin/python

def verify_num(num):
    for d in range(20, 2, -1):
        if (num % d != 0):
            return False

    return True

print(range(20, 2, -1))

val = 90

while (1):
    if verify_num(val):
        print("Ans: " + str(val))
        break

    val += 90

