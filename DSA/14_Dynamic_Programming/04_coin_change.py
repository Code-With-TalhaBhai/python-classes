


def min_coin_change(coins,amount):
    n = len(coins)
    total_num = [0]

    def coin_change(i,sum,no_of_coins):
        if sum == amount:
            total_num[0] = no_of_coins
            return True

        # if i == len(coins) or sum > amount:
        if i < 0 or sum > amount:
            # print(sum)
            return False
        

        if coin_change(i,sum+coins[i],no_of_coins+1):
            return True

        
        if coin_change(i-1,sum,no_of_coins):
            return True
        

    if not coin_change(n-1,0,0):
    # if not coin_change(0,0,0):
        return -1
    
    return total_num[0]

    


coins1 = [1,2,5]
coins2 = [2]
coins3 = [1]


print(min_coin_change(coins1,11))
print(min_coin_change(coins2,3))
print(min_coin_change(coins3,0))