A = [[2, 1], [3, 4]]
B = [[3, 1], [1, 2]]
rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])
if cols_A != rows_B:
    print("Matrices cannot be multiplied")
else:
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                C[i][j] += A[i][k] * B[k][j]
    print("Matrix A:")
    for row in A:
        print(row)
    print("Matrix B:")
    for row in B:
        print(row)
    print("Matrix C (A * B):")
    for row in C:
        print(row)

