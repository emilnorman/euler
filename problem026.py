#!/usr/bin/python3
#-*- coding: utf-8 -*-

from decimal import *

def find_recurring(s):
    length = 1
    while(length < len(s)/2):
        if (s[0:length] == s[length:2*length] and s[0:length] == s[2*length:3*length]):
            return s[0:length]
        length += 1

    return None

decimals = 3000
limit = decimals / 2.0

getcontext().prec = decimals

longest_frac = ""
longest_div = 0

for i in range(2, 1001):
    frac = Decimal(1)/Decimal(i)

    # Strip "0." and last char to avoid rounding errors
    st = str(frac)[2:-1]

    if (len(st) >= limit):
        seq = None
        seq_tmp = None

        for offset in range(0, 10):
            seq_tmp = find_recurring(st[offset:])
            if (seq_tmp != None) and (seq == None or len(seq) > len(seq_tmp)):
                seq = seq_tmp

        if seq != None and (len(seq) > len(longest_frac) and len(seq) < limit):
            longest_frac = seq
            longest_div = i

print("1/" + str(longest_div))
print("{}-digit recurring cycle: ".format(len(longest_frac)) + longest_frac)

