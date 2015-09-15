data = []

# Load data from file
with open("p067_triangle.txt", 'r') as f:
    for row in f:
        # Split to list and convert to int 
        rowData = [int(i) for i in row.replace("\n", "").split(" ")] 
        data.append(rowData)

# Step backwards through the levels
for l in range(len(data) - 1, -1, -1):
    # Sum pairs and add to previous level
    for i in range(0, len(data[l]) - 1):
        data[l - 1][i] += max(data[l][i], data[l][i + 1])

# Print result
print(data[0][0])
