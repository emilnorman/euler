# !/usr/bin/python
# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def next_prime(p):
    temp = p + 2

    for i in xrange(3, temp, 2):
        if ((temp % i) == 0):
            return next_prime(temp)

    return temp

prime = 3
base = 600851475143
divisor = 0

while(prime < base):
    if ((base % prime) == 0):
        dividor = prime
        print("--> " + str(prime))
    else:
        print("    " + str(prime))

    prime = next_prime(prime)

print("Largest prime: " + str(prime))
