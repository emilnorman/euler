# calculate divisors
result = [0, 0]

def divisors(n):
    res = 0

    for i in range(1, n):
        if n % i == 0:
            res += i
    return res

for n in range(2, 10000):
    if (n % 1000 == 0):
        print(n)

    result.append(divisors(n))

# Compare
match = 0
sum = 0
for n in range(2, 10000):
    try:
        if result[result[n]] == n and n != result[n]:
            print(n, result[n])
            match += 1
            sum += n
    except:
        pass

print("\nResult:")
print(match)
print(sum)
