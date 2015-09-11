import math

def NumOfDivisors(num):
    divisors = 0
    s = round(math.sqrt(num))
    
    for i in range(1, s + 1):
        if num % i == 0:
            divisors += 2
    return divisors + 1

# Generate triangular numbers
triagNum = 0
current = 1

nod = 0

while(nod < 500):
    triagNum += current
    current += 1
    nod = NumOfDivisors(triagNum)

print(current, triagNum, nod)
