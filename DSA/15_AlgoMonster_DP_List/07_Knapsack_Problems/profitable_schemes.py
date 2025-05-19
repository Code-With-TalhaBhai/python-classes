


def profitableSchemes(n: int, minProfit: int, group, profit) -> int:
    MOD = 10**9+7
    memo = {}

    def profitable(i,curr_sum,members):
        if i == len(profit):
            if curr_sum >= minProfit:
                return 1
            return 0
        
        if (i,curr_sum,members) in memo:
            return memo[(i,curr_sum,members)]
        
        take = 0
        if members + group[i] <= n:
            take = profitable(i+1,curr_sum+profit[i],members+group[i])
        noTake = profitable(i+1,curr_sum,members)
        total =  take + noTake
        memo[(i,curr_sum,members)] = total % MOD
        return memo[(i,curr_sum,members)]
    return profitable(0,0,0)



n1 = 5
minProfit1 = 3
group1 = [2,2]
profit1 = [2,3]


n2 = 10
minProfit2 = 5
group2 = [2,3,5]
profit2 = [6,7,8]


print(profitableSchemes(n1,minProfit1,group1,profit1))
print(profitableSchemes(n2,minProfit2,group2,profit2))
