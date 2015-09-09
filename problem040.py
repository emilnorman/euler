c = 0
d1 = 0
d10 = 0
d100 = 0
d1000 = 0
d10000 = 0
d100000 = 0
d1000000 = 0

for i in range(1, 200000):
    c += len(str(i))

    if c >= 1 and d1 == 0:
        d1 = i

    elif c >= 10 and d10 == 0:
        d10 = int(str(i)[-(c-11)])

    elif c >= 100 and d100 == 0:
        d100 = int(str(i)[-(c-102)])

    elif c >= 1000 and d1000 == 0:
        d1000 = int(str(i)[-(c-1002)])

    elif c >= 10000 and d10000 == 0:
        d10000 = int(str(i)[-(c-10002)])

    elif c >= 100000 and d100000 == 0:
        d100000 = int(str(i)[-(c-100002)])

    elif c >= 1000000 and d1000000 == 0:
        d1000000 = int(str(i)[-(c-1000002)])

print(d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000)
