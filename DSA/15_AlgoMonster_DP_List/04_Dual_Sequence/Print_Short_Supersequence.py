

def shortestCommonSupersequence(str1,str2):
    m = len(str1)
    n = len(str2)

    dp = [['' for i in range(m+1)] for i in range(n+1)]

    # find LCS
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1] + str1[j-1]
            else:
                left = dp[i-1][j]
                top = dp[i][j-1]
                dp[i][j] = left if len(left) > len(top) else top

    LCS = dp[n][m]
    supersequence = ''

    
    # After finding LCS including characters which is not common
    i,j = 0,0
    for s in LCS:
        while s != str1[i]:
            supersequence += str1[i]
            i += 1
        while s != str2[j]:
            supersequence += str2[j]
            j += 1

        supersequence += s
        i += 1
        j += 1

    supersequence += str1[i:] + str2[j:]
    return supersequence



str1 = "abac"
str2 = "cab"


str3 = "aaaaaaaa"
str4 = "aaaaaaaa"

print(shortestCommonSupersequence(str1,str2))
print(shortestCommonSupersequence(str3,str4))