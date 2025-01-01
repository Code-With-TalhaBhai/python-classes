
def min_coin_change1(coins,amount):
    n = len(coins)
    total_num = [float('inf')]

    # 1st way
    def coin_change1(i,sum,no_of_coins):
        if sum == amount:
            total_num[0] = min(no_of_coins,total_num[0])
            return 

        if i >= n or sum > amount:
            return
        
        coin_change1(i,sum+coins[i],no_of_coins+1)
        coin_change1(i+1,sum,no_of_coins)
    # coin_change1(0,0,0)

    # 2nd way
    # def coin_change2(i,rem,no_of_coins):
    #     if rem == 0:
    #         total_num[0] = min(total_num[0],no_of_coins)
    #         return

    #     if rem < 0 or i == n:
    #         return
        
    #     coin_change2(i,rem-coins[i],no_of_coins+1)
    #     coin_change2(i+1,rem,no_of_coins)
    # coin_change2(0,amount,0)


    # return -1 if total_num[0] == float('inf') else total_num[0]



    # 3rd way -> without external variable
    def coin_change3(coins,rem,i,no_of_changes):
        if rem == 0:
            return no_of_changes
        
        if i <= -1 or rem < 0:
            return float("inf")

        return min(
            coin_change3(coins,rem-coins[i],i,no_of_changes+1),
            coin_change3(coins,rem,i-1,no_of_changes)
            )

    total_coin_changes = coin_change3(coins,amount,n-1,0)
    return -1 if total_coin_changes == float("inf") else total_coin_changes



def min_coin_change2(coins,amount):
    n = len(coins)
    total_num = [float('inf')]
    memo = {0:0}

    def coin_change(rem):
        if rem in memo:
            return memo[rem]
        
        coin_change(rem-1)

        for coin in coins:
            val = rem-coin
            if val >= 0 and val in memo:
                memo[rem] = memo[val]+1

    coin_change(amount)
    if amount in memo:
        return memo[amount]
    return -1



def min_coin_change3(coins,amount):
    n = len(coins)

    dp = [float("inf")]*(amount+1)
    dp[0] = 0

    for amt in range(1,amount+1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt],dp[amt-coin]+1)


    return -1 if dp[amount] == float("inf") else dp[amount]



coins1 = [1,2,5]
coins2 = [2]
coins3 = [1]
coins4 = [186,419,83,408]
coins5 = [2,5,10,1]

print('With Recurrsion')
print(min_coin_change1(coins1,11))
print(min_coin_change1(coins2,3))
print(min_coin_change1(coins3,0))
print(min_coin_change1(coins4,6249))
print(min_coin_change1(coins5,27))
print('With Memoization') # not working yet
print(min_coin_change2(coins1,11))
print(min_coin_change2(coins2,3))
print(min_coin_change2(coins3,0))
print(min_coin_change2(coins4,6249))
print(min_coin_change2(coins5,27))
print('with Tabulation')
print(min_coin_change3(coins1,11))
print(min_coin_change3(coins2,3))
print(min_coin_change3(coins3,0))
print(min_coin_change3(coins4,6249))
print(min_coin_change3(coins5,27))