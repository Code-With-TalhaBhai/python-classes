


def interleaving_string_1(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return False
    
    def interleave(i,j,k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        a = (i < len(s1)) and (s1[i] == s3[k]) and interleave(i+1,j,k+1)
        b = (j < len(s2)) and (s2[j] == s3[k]) and interleave(i,j+1,k+1)
        return a or b
    return interleave(0,0,0)


def interleaving_string_2(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return False
    
    memo = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    def interleave(i,j,k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        if memo[i][j] != False:
            return memo[i][j]

        a = (i < len(s1)) and (s1[i] == s3[k]) and interleave(i+1,j,k+1)
        b = (j < len(s2)) and (s2[j] == s3[k]) and interleave(i,j+1,k+1)
        memo[i][j] = a or b
        return memo[i][j]

    return interleave(0,0,0)
        
    


def interleaving_string_3(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return False

    if len(s1) == 0:
        return s2 == s3

    if len(s2) == 0:
        return s1 == s3
        

    dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]


    dp[len(s1)][len(s2)] = True
    for i in range(len(s1),-1,-1):
        for j in range(len(s2),-1,-1):
            k = i + j
            if i < len(s1) and s1[i] == s3[k] and dp[i+1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[k] and dp[i][j+1]:
                dp[i][j] = True
    return dp[0][0]

    # dp[0][0] = True
    # for j in range(1, len(s2)+1):
    #     dp[0][j] = (s2[j-1] == s3[j-1]) and dp[0][j-1]

    # # Fill the first column (when s2 is empty)
    # for i in range(1, len(s1)+1):
    #     dp[i][0] = (s1[i-1] == s3[i-1]) and dp[i-1][0]

    # # Process all characters of s1 and s2
    # for i in range(1, len(s1)+1):
    #     for j in range(1, len(s2)+1):
    #         k = i + j
    #         dp[i][j] = (s1[i-1] == s3[k-1] and dp[i-1][j]) or (s2[j-1] == s3[k-1] and dp[i][j-1])
    # return dp[len(s1)][len(s2)]








s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s4 = "aabcc"
s5 = "dbbca"
s6 = "aadbbbaccc"


s7 = "YX"
s8 = "XZ"
s9 = "XYXZ"

print('With Recurrsion')
print(interleaving_string_1(s1,s2,s3))
print(interleaving_string_1(s4,s5,s6))
print(interleaving_string_1(s7,s8,s9))
print('With Memoization')
print(interleaving_string_2(s1,s2,s3))
print(interleaving_string_2(s4,s5,s6))
print(interleaving_string_2(s7,s8,s9))
print('With Tabulation')
print(interleaving_string_3(s1,s2,s3))
print(interleaving_string_3(s4,s5,s6))
print(interleaving_string_3(s7,s8,s9))




