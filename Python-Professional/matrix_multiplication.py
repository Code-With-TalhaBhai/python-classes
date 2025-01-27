



def Matrix_Multiplication(First_M,Second_M):
    p = len(First_M)
    q = len(Second_M[0])
    r = len(Second_M)

    if len(First_M[0]) != len(Second_M):
        return "Muliplication would not calculated as Cols of M1 not equal to Rows of M2"

    M = [[-1 for i in range(q)]for j in range(p)]
    for i in range(p):
        for j in range(q):
            mul = 0
            for k in range(r):
                mul += First_M[i][k] * Second_M[k][j]
            M[i][j] = mul
    return M


M1 = [
    [1,3,4],
    [2,4,6]
]

M2 = [
    [1,2,3],
    [3,2,1],
    [1,2,4]
]

M3 = [
    [3,4],
    [7,2],
    [5,9]
]

M4 = [
    [3,1,5],
    [6,9,7]
]

print(Matrix_Multiplication(M1,M2))
print(Matrix_Multiplication(M3,M4))
