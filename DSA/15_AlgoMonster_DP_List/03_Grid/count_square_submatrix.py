

def countSquares1(matrix) -> int:
    
    rows = len(matrix)
    cols = len(matrix[0])
    memo = {}

    def dfs(i,j):
        if i == rows or j == cols or matrix[i][j] == 0:
            return 0

        if (i,j) in memo:
            return memo[(i,j)]

        memo[(i,j)] = 1 + min(
            dfs(i,j+1),
            dfs(i+1,j),
            dfs(i+1,j+1)
        )
        return memo[(i,j)]
    
    res = 0
    for r in range(rows):
        for c in range(cols):
            res += dfs(r,c)
    return res


def countSquares2(matrix) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0 for i in range(cols+1)] for i in range(rows+1)]
    res = 0

    for r in range(1,rows+1):
        for c in range(1,cols+1):
            if matrix[r-1][c-1] == 1:
                dp[r][c] = 1

                if dp[r][c-1] > 0 and dp[r-1][c] > 0 and dp[r-1][c-1] > 0:
                    dp[r][c] += dp[r-1][c-1] 
            res += dp[r][c]

    return res        
            



matrix1 = [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
]

matrix2 = [
    [1,0,1],
    [1,1,0],
    [1,1,0]
]


print(countSquares1(matrix1))
print(countSquares1(matrix2))
print()
print(countSquares2(matrix1))
print(countSquares2(matrix2))
