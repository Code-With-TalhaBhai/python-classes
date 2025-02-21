


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


    # pat can't appear as a subsequence
    # in txt
    if len(t) > len(s):
        return 0

    # Create a 2D list initialized with 0
    dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

    # Initializing first row with all 1s. An empty string
    # is a subsequence of all.
    for j in range(len(s) + 1):
        dp[0][j] = 1

    # Fill mat[][] in bottom-up manner
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
          
            # If last characters don't match, then value
            # is the same as the value without the last character in txt.
            if t[i - 1] != s[j - 1]:
                dp[i][j] = dp[i][j - 1]
            else:
              
                # Value is obtained considering two cases:
                # a) All substrings without last character in txt
                # b) All substrings without last characters in both.
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1])
                
                
    # print(dp)
    return dp[len(t)][len(s)]



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



# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         m, n = len(s), len(t)
#         dp = [[0] * (n + 1) for _ in range(m + 1)]

#         for i in range(m + 1):
#             dp[i][n] = 1

#         for sIndex in range(m - 1, -1, -1):
#             for tIndex in range(n - 1, -1, -1):
#                 dp[sIndex][tIndex] = dp[sIndex + 1][tIndex]

#                 if s[sIndex] == t[tIndex]:
#                     dp[sIndex][tIndex] += dp[sIndex + 1][tIndex + 1]

#         return dp[0][0]