


def coin_change_II_1(coins,amount):
    def helper(i,sum):
        if i == len(coins) or sum > amount:
            return 0

        if sum == amount:
            return 1
        
        return helper(i,sum+coins[i]) + helper(i+1,sum)

    return helper(0,0)


def coin_change_II_2(coins,amount):
    memo = {}

    #1st way -> (Three overlapping sets)
    # def helper(i,sum):
    #     if i == len(coins) or sum > amount:
    #         return 0
        
    #     if (i,sum) in memo:
    #         return memo[(i,sum)]
        
    #     if sum == amount:
    #         return 1
        
    #     memo[(i,sum)] = helper(i,sum+coins[i]) + helper(i+1,sum)
    #     return memo[(i,sum)]
    
    # return helper(0,0)

    #2nd way
    def helper2(i,remainder):
        if i < 0 or remainder < 0:
            return 0
        
        if (i,remainder) in memo:
            return memo[(i,remainder)]
        
        if remainder == 0:
            return 1
        
        memo[(i,remainder)] = helper2(i,remainder-coins[i]) + helper2(i-1,remainder)
        return memo[(i,remainder)]
    return helper2(len(coins)-1,amount)



def coin_change_II_3(coins,amount):
    n = len(coins)
    dp = [[0 for i in range(amount+1)] for i in range(n+1)]
    dp[0][0] = 1

    for i in range(1,n+1):
        for j in range(amount+1):   
            dp[i][j] = dp[i-1][j]

            if (j - coins[i-1] >= 0):
                dp[i][j] += dp[i][j-coins[i-1]]
    return dp[n][amount]







coins1 = [1,2,5]
coins2 = [10]


print('recurrsion')
print(coin_change_II_1(coins1,5))
print(coin_change_II_1(coins2,10))

print('memoization')
print(coin_change_II_2(coins1,5))
print(coin_change_II_2(coins2,10))


print('with DP')
print(coin_change_II_3(coins1,5))
print(coin_change_II_3(coins2,10))