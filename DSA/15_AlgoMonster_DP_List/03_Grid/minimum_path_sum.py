


from itertools import count


def minPathSum1(grid):

    m = len(grid)
    n = len(grid[0])

    memo = {(m-1,n-1):grid[m-1][n-1]}
    def minSum(i,j):
        if i == m or j == n:
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]

        if i + 1 < m and j + 1 < n:
            memo[(i,j)] = min(grid[i][j] + minSum(i+1,j),grid[i][j] + minSum(i,j+1))
        elif i + 1 >= m:
            memo[(i,j)] = grid[i][j] + minSum(i,j+1) 
        else:
            memo[(i,j)] = grid[i][j] + minSum(i+1,j)
        return memo[(i,j)]
    return minSum(0,0)



def minPathSum2(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for i in range(n)] for i in range(m)]


    for i in range(m):
        for j in range(n):
            num = grid[i][j]
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = min(num+dp[i-1][j],num+dp[i][j-1])
            elif i - 1 >= 0:
                dp[i][j] = num + dp[i-1][j]
            else:
                dp[i][j] = num + dp[i][j-1]
    return dp[m-1][n-1]



def minPathSum3(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            ...
            


grid1 = [[1,3,1],[1,5,1],[4,2,1]]
grid2 = [[1,2,3],[4,5,6]]

print(minPathSum1(grid1))
print(minPathSum1(grid2))
print()
print(minPathSum2(grid1))
print(minPathSum2(grid2))
print()
print(minPathSum3(grid1))
print(minPathSum3(grid2))