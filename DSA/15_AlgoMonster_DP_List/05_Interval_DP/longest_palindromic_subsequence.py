



def longestPalindromeSubseq1(s):
    n = len(s)
    palindrome = s[::-1]
    memo = {}

    def longest_palindrome(i,j):
        if i == len(s) or j == len(palindrome):
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        if s[i] == palindrome[j]:
            memo[(i,j)] = 1 + longest_palindrome(i+1,j+1)
        else:
            memo[(i,j)] = max(longest_palindrome(i+1,j),longest_palindrome(i,j+1))
        return memo[(i,j)]
    return longest_palindrome(0,0)



def longestPalindromeSubseq2(s):
    n = len(s)
    palindrome = s[::-1]
    
    dp = [[0 for i in range(n+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == palindrome[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][n]


def longestPalindromeSubseq3(s):
    n = len(s)
    dp = [[0 for i in range(n+1)] for i in range(n+1)]

    for i in range(1,n+1):
    #     for j in range(1,n+1):
    #         if s[i-1] == s[n-j]:
    #             dp[i][j] = dp[i-1][j-1] + 1
    #         else:
    #             dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    # return dp[n][n]
        for j in range(n-1,-1,-1):
            if s[i-1] == s[j]:
                dp[i][j] = dp[i-1][j+1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j+1])
    return dp[n][0]


s1 = "bbbab"
s2 = "cbbd"


print(longestPalindromeSubseq1(s1))
print(longestPalindromeSubseq1(s2))
print()
print(longestPalindromeSubseq2(s1))
print(longestPalindromeSubseq2(s2))
print()
print(longestPalindromeSubseq3(s1)) # without reversing string
print(longestPalindromeSubseq3(s2))