a = [[4, 6, 7, 8], [3, 7, 2, 7], [7, 3, 7, 5]]
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[j][i] = a[i][j]

print("Transpose Matrix:")
for row in c:
    print(row)
