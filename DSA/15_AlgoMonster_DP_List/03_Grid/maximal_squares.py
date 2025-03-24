

def maximal_squares1(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    maxi = float("-inf")
    memo = {}

    def dfs(r,c):
        if r == rows or c == cols or matrix[r][c] == '0':
            return 0
        
        if (r,c) in memo:
            return memo[(r,c)]
        
        memo[(r,c)] = 1 + min(
            dfs(r+1,c),
            dfs(r,c+1),
            dfs(r+1,c+1)
        )
        return memo[(r,c)]

    for i in range(rows):
        for j in range(cols):
            maxi = max(maxi,dfs(i,j)**2)
    return maxi




def maximal_squares2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    maxi = float("-inf")
    dp = [[0 for i in range(cols+1)] for i in range(rows+1)]

    for r in range(1,rows+1):
        for c in range(1,cols+1):
            if matrix[r-1][c-1] == '1':
                dp[r][c] = 1 + min(
                    dp[r][c-1],
                    dp[r-1][c],
                    dp[r-1][c-1]
                )
            maxi = max(maxi,dp[r][c])
    return maxi**2

    
    




matrix1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix2 = [["0","1"],["1","0"]]
matrix3 = [["0"]]
matrix4 = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]


print(maximal_squares1(matrix1))
print(maximal_squares1(matrix2))
print(maximal_squares1(matrix3))
print()
print(maximal_squares2(matrix1))
print(maximal_squares2(matrix2))
print(maximal_squares2(matrix3))