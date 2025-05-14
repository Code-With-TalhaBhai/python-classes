

# To Find fibonacci_sequence through matrix, we do:
# 
# [[f(n)],[f(n-1)]] = [[1,1],[1,0]] * [[f(n-1)],[f(n-2)]] 



T = [
    [1,1],
    [1,0]
]

matrix = [
    [34], # f(n-1)->f(9)
    [21]  # f(n-2)->f(8)
]



def matrix_multiply(mat1,mat2):
    mat3 = []
    for i in range(len(mat1)):
        mat3.append([])
        for j in range(len(mat2[0])):
            ans = 0
            for k in range(len(mat1[0])):
            # for k in range(len(mat2)):
                ans += mat1[i][k] * mat2[k][j]
            mat3[i].append(ans)
    return mat3 # whole matrix
    # return mat3[0][0]
print(matrix_multiply(T,matrix))


print('Using matrix_exponentiation is to find fibonacci_sequence')

# [[f(n)],[f(n-1)]] = (T^n-1) * [[f(1),f(0)]],where T is
# T = [
#   [1, 1],
#   [1, 0]
# ]

def matrix_exponentiation(matrix,pow):
    m = len(matrix)
    n = len(matrix[0])
    res = [[int(i == j) for j in range(n)] for i in range(m)]


    while pow > 0:
        if pow % 2 == 1:
            res = matrix_multiply(matrix,res)
        matrix = matrix_multiply(matrix,matrix)
        pow = pow // 2
    return res


def fib(n):
    T = [[1,1],
        [1,0]]

    F = [
        [1],
        [0]
    ]

    res = matrix_multiply(matrix_exponentiation(T,n-1),F)
    return res[0][0]


print(fib(10))