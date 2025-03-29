


def distinct_subsequences1(s,t):

    def helper(i,j):
        if j == len(t):
            return 1
        
        if i == len(s):
            return 0

        if s[i] == t[j]:
            return helper(i+1,j+1) + helper(i+1,j)
        else:
            return helper(i+1,j)
        
    return helper(0,0)


def distinct_subsequences2(s,t):
    memo = {}

    def helper(i,j):
        if j == len(t):
            return 1

        if i == len(s):
            return 0

        if (i,j) in memo:
            return memo[(i,j)]

        if s[i] == t[j]:
            memo[(i,j)] = helper(i+1,j+1) + helper(i+1,j)
        else:
            memo[(i,j)] = helper(i+1,j)

        return memo[(i,j)]


    helper(0,0)
    return memo[(0,0)]
        

def distinct_subsequences3(s,t):
    m = len(s)
    n = len(t)

    # pat can't appear as a subsequence
    # in txt
    if len(t) > len(s):
        return 0

    # Create a 2D list initialized with 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initializing first row with all 1s. An empty string
    # is a subsequence of all.
    for j in range(m + 1):
        dp[0][j] = 1

    # Fill mat[][] in bottom-up manner
    # for i in range(1, len(t) + 1):
    #     for j in range(1, len(s) + 1):
          
    #         # If last characters don't match, then value
    #         # is the same as the value without the last character in txt.
    #         if t[i - 1] != s[j - 1]:
    #             dp[i][j] = dp[i][j - 1]
    #         else:
              
    #             # Value is obtained considering two cases:
    #             # a) All substrings without last character in txt
    #             # b) All substrings without last characters in both.
    #             dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1])


                
    # print(dp)
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


print('With Recurrsion')
print(distinct_subsequences1(s1,t1))
print(distinct_subsequences1(s2,t2))
print('With Memoization')
print(distinct_subsequences2(s1,t1))
print(distinct_subsequences2(s2,t2))
print('With Tabulation')
print(distinct_subsequences3(s1,t1))
print(distinct_subsequences3(s2,t2))


