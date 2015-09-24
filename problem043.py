#!/usr/bin/python3
# -*- coding: utf-8 -*-

def pandigit(a):
    defined = 0
    all = set()
    for c in a:
        if c != '':
            defined += 1
            all.add(c)

    if len(all) != defined:
        return False
    else:
        return True

def gen(factor):
    res = []
    i = 1
    while(i*factor < 1000):
        f = "{0:03d}".format(i*factor)
        if pandigit(f):
            res.append(f)
        i += 1

    return res

def addNewNum(inPos, offset, newAlts):
    outPos = []

    for alt in newAlts:
        if inPos[offset + 1] == alt[1] and inPos[offset + 2] == alt[2]:
            tmp = list(inPos)
            tmp[offset] = alt[0]
            if pandigit(tmp):
                outPos.append(tmp)

    return outPos

# Generate possible parts    
f17 = gen(17)
f13 = gen(13)
f11 = gen(11)
f7 = gen(7)
f5 = gen(5)
f3 = gen(3)
f2 = gen(2)

#    d1d2d3=406 is divisible by 2
#    d2d3d4=063 is divisible by 3
#    d3d4d5=635 is divisible by 5
#    d4d5d6=357 is divisible by 7
#    d5d6d7=572 is divisible by 11
#    d6d7d8=728 is divisible by 13
#    d7d8d9=289 is divisible by 17

resultSum = 0

resArr = ['']*10
for base in f17:
    resArr[7] = base[0]
    resArr[8] = base[1]
    resArr[9] = base[2]

    for a in addNewNum(resArr, 6, f13):
        for b in addNewNum(a, 5, f11):
            for c in addNewNum(b, 4, f7):
                for d in addNewNum(c, 3, f5):
                    for e in addNewNum(d, 2, f3):
                        for f in addNewNum(e, 1, f2):
                            # find missing number
                            for g in range(0, 10):
                                f[0] = str(g)
                                if pandigit(f):
                                    print(f)
                                    resultSum += int(''.join(f))
                                    break

print("Sum: " + str(resultSum))

