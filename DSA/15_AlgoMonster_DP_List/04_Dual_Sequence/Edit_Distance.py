


def minDistance1(word1,word2):
    m = len(word1)
    n = len(word2)


    memo = {(m,n):0}

    def min_dist(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i == m:
            # return 1 + min_dist(i,j+1) # inserting
            return n - j

        if j == n:
            # return 1 + min_dist(i+1,j) # deleting
            return m - i

        
        if word1[i] == word2[j]:
            memo[(i,j)] = min_dist(i+1,j+1)
            return memo[(i,j)]
        
        
        memo[(i,j)] =  min(
            1 + min_dist(i,j+1), # inserting
            1 + min_dist(i+1,j+1), # replacing
            1 + min_dist(i+1,j) # deleting
        )
        return memo[(i,j)]
    return min_dist(0,0)




def minDistance2(word1,word2):
    m = len(word1)
    n = len(word2)

    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(m+1):
        dp[0][i] = i
    for j in range(n+1):
        dp[j][0] = j
    

    for i in range(1,n+1):
        for j in range(1,m+1):
            if word1[j-1] == word2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) + 1
    return dp[n][m]



word1 = "horse"
word2 = "ros"

word3 = "intention"
word4 = "execution"


print(minDistance1(word1,word2))
print(minDistance1(word3,word4))
print()
print(minDistance2(word1,word2))
print(minDistance2(word3,word4))