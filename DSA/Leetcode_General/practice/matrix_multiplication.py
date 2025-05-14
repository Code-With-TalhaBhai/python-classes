




matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]


matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# matrix1 = [
#     [1,1],
#     [1,0]
# ]

# matrix2 = [
#     [34],
#     [21]
# ]


matrix3 = []


def multiply(mat1,mat2,mat3):
    
    for i in range(len(mat1)):
        mat3.append([])
        for j in range(len(mat2[0])):
            ans = 0
            for k in range(len(mat1[0])):
            # for k in range(len(mat2)):
                ans += mat1[i][k] * mat2[k][j]
            mat3[i].append(ans)
    return mat3


print(multiply(matrix1,matrix2,matrix3))