# !/usr/bin/python
# -*- coding: utf-8 -*-

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def next_prime(p):
    temp = p + 2

    for i in xrange(3, temp, 2):
        if ((temp % i) == 0):
            return next_prime(temp)

    return temp

n = 2
prime = 3

while(n < 10001):
    prime = next_prime(prime)
    n += 1
    print(n, prime)

print("n:"),
print(n)

print("prime:"),
print(prime)
