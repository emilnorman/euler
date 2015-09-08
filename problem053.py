count = 0
f = [1]

for i in range(1, 101):
    f.append(f[i-1] * i)

for n in range(1, 101):
    for r in range(1, n + 1):
        c = f[n]/(f[r]*f[n-r])
        if c > 1000000:
            count += 1

print(count)
