

def uniquePaths1(m: int, n: int) -> int:
    
    memo = {(m-1,n-1):1}
    def unique(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i == m or j == n:
            return 0
        

        memo[(i,j)] = unique(i+1,j) + unique(i,j+1)
        return memo[(i,j)]
    
    # return unique(0,0)
    unique(0,0)
    return memo[(0,0)]



def uniquePaths2(m,n):
    dp = [[1 for i in range(n)] for i in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


    return dp[m-1][n-1]




m1 = 3
n1 = 7
m2 = 3
n2 = 2
print(uniquePaths1(m1,n1))
print(uniquePaths1(m2,n2))
print()
print(uniquePaths2(m1,n1))
print(uniquePaths2(m2,n2))