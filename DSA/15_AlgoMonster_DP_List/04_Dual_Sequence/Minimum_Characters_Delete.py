# Minimum characters delete to make strings equal


def minimum_characters_delete1(s1,s2):
    m = len(s1)
    n = len(s2)

    memo = {}
    def min_delete(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i == m:
            return n - j
        if j == n:
            return m - i
        
        if s1[i] == s2[j]:
            memo[(i,j)] = min_delete(i+1,j+1)
            return memo[(i,j)]
        
        first = 1 + min_delete(i+1,j)
        second = 1 + min_delete(i,j+1)
        memo[(i,j)] = min(first,second)
        return memo[(i,j)]
    return min_delete(0,0)



def minimum_characters_delete2(s1,s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i

    for i in range(m+1):
        dp[0][i] = i

    for i in range(1,n+1):
        for j in range(1,m+1):       
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
    return dp[n][m]


print(minimum_characters_delete1('sea','eat'))
print(minimum_characters_delete1('delete','leet'))
print()
print(minimum_characters_delete2('sea','eat'))
print(minimum_characters_delete2('delete','leet'))