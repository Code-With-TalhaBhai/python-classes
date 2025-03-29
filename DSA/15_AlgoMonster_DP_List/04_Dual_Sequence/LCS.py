


def LCS1(text1,text2):
    m = len(text1)
    n = len(text2)
    memo = {}

    def lcs(i,j):
        if i == m or j == n:
            return 0
        
        if i in memo:
            return memo[(i,j)]
        
        if text1[i] == text2[j]:
            memo[(i,j)] = 1 + lcs(i+1,j+1)
            return memo[(i,j)]
        
        memo[(i,j)] = max(lcs(i+1,j),lcs(i,j+1))
        return memo[(i,j)]
    return lcs(0,0)



def LCS2(text1,text2):
    m = len(text1)
    n = len(text2)
    dp = [[0 for i in range(m+1)] for i in range(n+1)]


    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[j-1] == text2[i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
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
print(LCS2("ezupkr","ubmrapg"))