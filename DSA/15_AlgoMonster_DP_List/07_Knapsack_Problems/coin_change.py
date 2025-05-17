


def min_coin_change1(coins,target):
    n = len(coins)
    memo = {}

    def coin_change(i,curr_sum):
        if curr_sum == target:
            return 0
        
        if curr_sum > target or i == n:
            return float('inf')

        if (i,curr_sum) in memo:
            return memo[(i,curr_sum)]

        memo[(i,curr_sum)] = min(
            1 + coin_change(i,curr_sum+coins[i]),
            coin_change(i+1,curr_sum)
        )
        return memo[(i,curr_sum)]

    change = coin_change(0,0)
    return -1 if change == float('inf') else change





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