

def coin_change_II_1(coins,amount):
    n = len(coins)
    memo = {}


    def change(i,curr_sum):
        if curr_sum == amount:
            return 1
        
        if i == n or curr_sum > amount:
            return 0

        if (i,curr_sum) in memo:
            return memo[(i,curr_sum)]


        memo[(i,curr_sum)] = change(i,curr_sum+coins[i]) + change(i+1,curr_sum)
        return memo[(i,curr_sum)]
    return change(0,0)




coins1 = [1,2,5]
coins2 = [10]


print('recurrsion')
print(coin_change_II_1(coins1,5))
print(coin_change_II_1(coins2,10))