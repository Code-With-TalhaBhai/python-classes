


def coin_change(coins,total):
    n = len(coins)

    def change(i,sum):
        if sum == total:
            return 1
        
        if sum > total or i >= n:
            return 0

        return change(i,sum+coins[i])+change(i+1,sum)
    return change(0,0)



coins1 = [1,2,5]
coins2 = [186,419,83,408]


print(coin_change(coins1,11))
print(coin_change(coins2,6249))
