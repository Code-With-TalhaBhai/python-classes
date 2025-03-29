

def minimumDeleteSum(s1,s2):
    m = len(s1)
    n = len(s2)


    def min_delete(i,j,y,z):
        ...

    return min_delete(0,0,0,0)




def minimumDeleteSum2(s1,s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(1,m+1):
        dp[0][i] = ord(s1[i-1])

    for j in range(1,n+1):
        dp[j][0] = ord(s2[j-1])

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[j-1] != s2[i-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1] - dp[i-1][j]

    print(dp)
    return dp[n][m]


# print(minimumDeleteSum1('sea','eat'))
# print(minimumDeleteSum1('delete','leet'))
print()
print(minimumDeleteSum2('sea','eat'))
# print(minimumDeleteSum2('delete','leet'))