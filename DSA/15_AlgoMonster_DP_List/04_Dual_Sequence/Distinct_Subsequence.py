


def distinct_subsequences1(s,t):
    memo = {}
    # def distinct(i,j):
    #     if j == len(t):
    #         return 1
        
    #     if i == len(s):
    #         return 0
        
    #     if (i,j) in memo:
    #         return memo[(i,j)]
        
    #     if s[i] == t[j]:
    #         memo[(i,j)] = distinct(i+1,j+1) + distinct(i+1,j)
    #         return memo[(i,j)]
    #     memo[(i,j)] = distinct(i+1,j)
    #     return memo[(i,j)]
    # return distinct(0,0)

    m = len(s)
    n = len(t)

    def distinct(i,j):
        if j == n:
            return 1
        
        if i == m:
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        if s[i] == t[j]:
            memo[(i,j)] = distinct(i+1,j+1) + distinct(i+1,j)
            return memo[(i,j)]
        
        memo[(i,j)] = distinct(i+1,j)
        return memo[(i,j)]
    return distinct(0,0)





def distinct_subsequences2(s,t):
    m = len(s)
    n = len(t)

    dp = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(m+1):
        dp[0][i] = 1


    for i in range(1,n+1):
        # 1st way
        # for j in range(1,m+1):
        #     if s[j-1] == t[i-1]:
        #         dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        #     else:
        #         dp[i][j] = dp[i][j-1]

        # 2nd way
        for j in range(1,m+1):
            dp[i][j] = dp[i][j-1]
            if s[j-1] == t[i-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[n][m]



s1 = "rabbbit"
t1 = "rabbit"

s2 = "babgbag"
t2 = "bag"


print(distinct_subsequences1(s1,t1))
print(distinct_subsequences1(s2,t2))
print()
print(distinct_subsequences2(s1,t1))
print(distinct_subsequences2(s2,t2))