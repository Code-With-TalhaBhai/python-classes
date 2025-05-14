




matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]


matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



matrix3 = []


def multiply(mat1,mat2,mat3):
    
    for i in range(len(mat1)):
        mat3.append([])
        for j in range(len(mat2[0])):
            ans = 0
            for k in range(len(mat2[0])):
                for k in range(len(mat1)):
                    ...
                ans = mat1[0]
                mat3[i].append(ans)
    return mat3


print(multiply(matrix1,matrix2,matrix3))