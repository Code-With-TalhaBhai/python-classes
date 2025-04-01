

def minimumDeleteSum1(s1,s2):
    m = len(s1)
    n = len(s2)

    memo = {}
    def min_delete(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i == m:
            sum = 0
            for k in range(j,n):
                sum += ord(s2[k])
            return sum
        if j == n:
            sum = 0
            for k in range(i,m):
                sum += ord(s1[k])
            return sum
        
        if s1[i] == s2[j]:
            memo[(i,j)] = min_delete(i+1,j+1)
            return memo[(i,j)]
        
        first = ord(s1[i]) + min_delete(i+1,j)
        second = ord(s2[j]) + min_delete(i,j+1)
        memo[(i,j)] = min(first,second)
        return memo[(i,j)]
    return min_delete(0,0)




def minimumDeleteSum2(s1,s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(1,m+1):
        dp[0][i] = ord(s1[i-1]) + dp[0][i-1]

    for j in range(1,n+1):
        dp[j][0] = ord(s2[j-1]) + dp[j-1][0]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1]+ord(s1[j-1]),dp[i-1][j]+ord(s2[i-1]))
    return dp[n][m]


print(minimumDeleteSum1('sea','eat'))
print(minimumDeleteSum1('delete','leet'))
print()
print(minimumDeleteSum2('sea','eat'))
print(minimumDeleteSum2('delete','leet'))