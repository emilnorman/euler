size = 21

m = [[0] * size] * size

# Fill first row
m[0] = [1] * size

for row in range(1, size):
    # Fill first col
    m[row][0] = 1
    
    for col in range(1, size):
        m[row][col] = m[row - 1][col] + m[row][col - 1]

print(m[size - 1][size - 1])
