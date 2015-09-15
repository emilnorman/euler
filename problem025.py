cmp = 10**999

f1 = 1
f2 = 1
index = 2

while f2 < cmp:
    tmp = f1 + f2
    f1 = f2
    f2 = tmp
    index += 1

print(index)
