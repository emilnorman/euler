m = []

# Load data from file
with open("p081_matrix.txt", 'r') as f:
    for row in f:
        # Split to list and convert to int 
        rowData = [int(i) for i in row.replace("\n", "").split(",")] 
        m.append(rowData)

size = len(m[0])

# First row
for col in range(1, size):
    m[0][col] += m[0][col - 1]

for row in range(1, size):
    # First col
    m[row][0] += m[row - 1][0]

    for col in range(1, size):
        m[row][col] += min(m[row - 1][col], m[row][col - 1])

print(m[size - 1][size - 1])
