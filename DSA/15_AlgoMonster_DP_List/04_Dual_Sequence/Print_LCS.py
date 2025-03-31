


def LCS1(text1,text2):
    m = len(text1)
    n = len(text2)

    # memo = {}
    # def print_lcs(i,j):
    #     if j == n or i == m:
    #         return ''
        
    #     if (i,j) in memo:
    #         return memo[(i,j)]
        
    #     if text1[i] == text2[j]:
    #         memo[(i,j)] = print_lcs(i+1,j+1) + text2[j]
    #         return memo[(i,j)]
        
    #     first = print_lcs(i+1,j)
    #     second = print_lcs(i,j+1)

    #     memo[(i,j)] = first if len(first) > len(second) else second
    #     return memo[(i,j)]
    # return print_lcs(0,0)


    memo = {}
    def lcs_recursive(X, Y, m, n):
        if m == 0 or n == 0:
            return ""
        
        # if (m,n) in memo:
        #     return memo[(m,n)]
        
        if X[m - 1] == Y[n - 1]:
            return lcs_recursive(X, Y, m - 1, n - 1) + X[m - 1]
            # memo[(m,n)] = lcs_recursive(X, Y, m - 1, n - 1) + X[m - 1]
            # return memo[(m,n)]
        else:
            left = lcs_recursive(X, Y, m - 1, n)
            right = lcs_recursive(X, Y, m, n - 1)
            return left if len(left) > len(right) else right
            # memo[(m,n)] = left if len(left) > len(right) else right
            # return memo[(m,n)]
    return lcs_recursive(text1,text2,m,n)





def LCS2(text1,text2):
    m = len(text1)
    n = len(text2)

    dp = [['' for i in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[j-1] == text2[i-1]:
                dp[i][j] = dp[i-1][j-1] + text1[j-1]
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
    return dp[n][m]


text1 = "abcde"
text2 = "ace"

text3 = "abc"
text4 = "def"


print(LCS1(text1,text2))
print(LCS1(text3,text4))
print()
print(LCS2(text1,text2))
print(LCS2(text3,text4))