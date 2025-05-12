
# working not completed
def fractional_knapsack(profit,weight,total_capacity):
    total_items = len(profit)
    dp = [[0 for i in range(total_capacity+1)] for i in range(total_items+1)]

    for wt in range(1,total_items+1):
        for curr_cap in range(1,total_capacity+1):
            if curr_cap >= weight[wt-1]:
                dp[wt][curr_cap] = dp[wt-1][curr_cap-weight[wt-1]] + profit[wt-1]
            else:
                fractional_profit = (curr_cap / weight[wt-1]) * profit[wt-1]
                dp[wt][curr_cap] = max(dp[wt-1][curr_cap],fractional_profit)

    print(dp)
    return dp[total_items][total_capacity]
    


profit = [60,100,30]
weight = [10,20,30]

print(fractional_knapsack(profit,weight,50))