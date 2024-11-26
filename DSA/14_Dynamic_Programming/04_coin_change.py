
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
    coin_change1(0,0,0)

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

    return -1 if total_num[0] == float('inf') else total_num[0]


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




coins1 = [1,2,5]
coins2 = [2]
coins3 = [1]
coins4 = [186,419,83,408]

print('With Recurrsion')
print(min_coin_change1(coins1,11))
print(min_coin_change1(coins2,3))
print(min_coin_change1(coins3,0))
print(min_coin_change1(coins4,6249))
print('With Memoization')
print(min_coin_change2(coins1,11))
print(min_coin_change2(coins2,3))
print(min_coin_change2(coins3,0))
print(min_coin_change2(coins4,6249))