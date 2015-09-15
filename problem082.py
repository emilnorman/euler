# m = [[131, 673, 234, 103, 18],
     # [201,96,342,965,150],
     # [630,803,746,422,111],
     # [537,699,497,121,956],
     # [805,732,524,37,331]]

m = []

# Load data from file
with open("p082_matrix.txt", 'r') as f:
    for row in f:
        # Split to list and convert to int 
        rowData = [int(i) for i in row.replace("\n", "").split(",")] 
        m.append(rowData)

size = len(m[0])

# Find shortest path to second col
for row in range(0, size):
    m[row][1] += m[row][0]

# Find shortest path to next columns
for col in range(2, size):
    tempCol = []

    for row in range(0, size):
        # right
        altR = m[row][col - 1] + m[row][col]

        # right and up
        altRU = altR
        for r in range(row, size):
            # Sum up
            sumC = 0
            for i in range(row, r+1):
                sumC += m[i][col]

            altRU = min(altRU, m[r][col - 1] + sumC)

        # right and down
        altRD = altR
        for r in range(0, row):
            # Sum down
            sumC = 0
            for i in range(r, row+1):
                sumC += m[i][col]

            altRD = min(altRD, m[r][col - 1] + sumC)

        # Find minimal cost
        tempCol.append(min(altR, altRU, altRD))

    # Store temp values
    for row in range(0, size):
        m[row][col] = tempCol[row]

result = m[0][-1]

for row in range(1, size):
    result = min(result, m[row][-1] )

print(result)
