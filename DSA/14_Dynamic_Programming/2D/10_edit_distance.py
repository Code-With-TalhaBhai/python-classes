



def edit_distance1(word1,word2):

    # def edit1(i,j):
    #     if i == len(word1):
    #         return len(word2) - j

    #     if j == len(word2):
    #         return len(word1) - i

    #     if word1[i] == word2[j]:
    #         return edit1(i+1,j+1)

    #     return 1 + min(
    #         edit1(i,j+1), # insert
    #         edit1(i+1,j), # delete
    #         edit1(i+1,j+1) # update
    #     )
    # return edit1(0,0)


    def edit2(i,j):
        if i == 0:
            return j

        if j == 0:
            return i


        if word1[i-1] == word2[j-1]:
            return edit2(i-1,j-1)

        return 1 + min(
            edit2(i,j-1), # insert
            edit2(i-1,j), # delete
            edit2(i-1,j-1) # update
        )


    return edit2(len(word1),len(word2))



def edit_distance2(word1,word2):
    m = len(word1)
    n = len(word2)
    memo = [[-1 for i in range(n+1)] for j in range(m+1)]

    # def edit1(i,j):
    #     if memo[i][j] != -1:
    #         return memo[i][j]

    #     if i == m:
    #         return n - j

    #     if j == n:
    #         return m - i


    #     if word1[i] == word2[j]:
    #         memo[i][j] = edit1(i+1,j+1)
    #         return memo[i][j]

    #     memo[i][j] = 1 + min(
    #         edit1(i,j+1),
    #         edit1(i+1,j),
    #         edit1(i+1,j+1)
    #     )
    #     return memo[i][j]
    # return edit1(0,0)


    def edit2(i,j):
        if memo[i][j] != -1:
            return memo[i][j]

        if i == 0:
            return j

        if j == 0:
            return i


        if word1[i-1] == word2[j-1]:
            memo[i][j] = edit2(i-1,j-1)
        else:
            memo[i][j] = 1 + min(
                edit2(i,j-1), # insert
                edit2(i-1,j), # delete
                edit2(i-1,j-1) # update
            )
        return memo[i][j]
    return edit2(len(word1),len(word2))



def edit_distance3(word1,word2):
    m = len(word1)
    n = len(word2)

    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(m+1):
        dp[0][i] = i

    for j in range(n+1):
        dp[j][0] = j

    # dp[0][0] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if word2[i-1] == word1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

    return dp[n][m]




word1 = "horse"
word2 = "ros"
word3 = "intention"
word4 = "execution"


# Using Recurrsion
print(edit_distance1(word1,word2))
print(edit_distance1(word3,word4))
# Using Memoization
print(edit_distance2(word1,word2))
print(edit_distance2(word3,word4))
# Using Tabulation
print(edit_distance3(word1,word2))
print(edit_distance3(word3,word4))