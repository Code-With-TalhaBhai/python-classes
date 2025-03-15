

def uniquePathsWithObstacles1(obstacleGrid) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    memo = {(m-1,n-1):1}

    def unique(i,j):
        if i == m or j == n or obstacleGrid[i][j] == 1:
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]
        

        memo[(i,j)] = unique(i+1,j) + unique(i,j+1)
        return memo[(i,j)]

    return unique(0,0)


def uniquePathsWithObstacles2(obstacleGrid) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0]:
        return 0

    dp = [[0 for i in range(n)] for i in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1 or (i == 0 and j == 0):
                continue

            if i - 1 >= 0:
                dp[i][j] += dp[i-1][j]
            
            if j - 1 >= 0:
                dp[i][j] += dp[i][j-1]

    return dp[m-1][n-1]




obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid2 = [[0,1],[0,0]]

print(uniquePathsWithObstacles1(obstacleGrid1))
print(uniquePathsWithObstacles1(obstacleGrid2))
print()
print(uniquePathsWithObstacles2(obstacleGrid1))
print(uniquePathsWithObstacles2(obstacleGrid2))