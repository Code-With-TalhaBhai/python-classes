
# Brute-Force
def longestCommonSubsequence1(text1,text2):

    # def LCS1(i,j):
    #     if i == len(text1) or j == len(text2):
    #         return 0
        
    #     if text1[i] == text2[j]:
    #         return 1 + LCS1(i+1,j+1)
        
    #     return max(LCS1(i,j+1),LCS1(i+1,j))
    # return LCS1(0,0)


    def LCS2(i,j):
        if i == 0 or j == 0:
            return 0
        
        if text1[i-1] == text2[j-1]:
            return 1 + LCS2(i-1,j-1)
        
        return max(LCS2(i,j-1),LCS2(i-1,j))
    return LCS2(len(text1),len(text2))


# Memoization
def longestCommonSubsequence2(text1,text2):
    memo = [[-1 for i in range(len(text2))] for i in range(len(text1))]


    def LCS1(i,j):
        if i == len(text1) or j == len(text2):
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        if text1[i] == text2[j]:
            return 1 + LCS1(i+1,j+1)
        
        memo[i][j] = max(LCS1(i,j+1),LCS1(i+1,j))
        return memo[i][j]
    return LCS1(0,0)


    # def LCS2(i,j):
    #     if i == 0 or j == 0:
    #         return 0
        
    #     if memo[i-1][j-1] != -1:
    #         return memo[i][j]
        
    #     if text1[i-1] == text2[j-1]:
    #         memo[i-1][j-1] = 1 + LCS2(i-1,j-1)
    #         return memo[i-1][j-1]
        
    #     memo[i-1][j-1] = max(LCS2(i,j-1),LCS2(i-1,j))
    #     return memo[i-1][j-1]
    
    # return LCS2(len(text1),len(text2))


def longestCommonSubsequence3(text1,text2):
    n = len(text1)
    m = len(text2)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if text2[i-1] == text1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

    # for i in range(m-1,-1,-1):
    #     for j in range(n-1,-1,-1):
    #         if text2[i] == text1[j]:
    #             dp[i][j] = dp[i+1][j+1] + 1
    #         else:
    #             dp[i][j] = max(dp[i+1][j],dp[i][j+1])

    # return dp[0][0]





text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence1(text1,text2))
print(longestCommonSubsequence2(text1,text2))
print(longestCommonSubsequence3(text1,text2))

text3 = "abc"
text4 = "abc"
print(longestCommonSubsequence1(text3,text4))
print(longestCommonSubsequence2(text3,text4))
print(longestCommonSubsequence3(text3,text4))


text5 = "abc"
text6 = "def"
print(longestCommonSubsequence1(text5,text6))
print(longestCommonSubsequence2(text5,text6))
print(longestCommonSubsequence3(text5,text6))

