#!/usr/bin/python3
#-*- coding: utf-8 -*-

def f(i):
    sum = 1
    for a in range(1, i+1):
        sum *= a
    return sum

def prob(n, k):
    return f(n)/(f(k)*f(n-k))

print(7*(1 - (prob(60,20)/prob(70,20))))

