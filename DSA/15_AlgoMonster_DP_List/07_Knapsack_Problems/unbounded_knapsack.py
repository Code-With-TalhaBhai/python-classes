


def unbounded_knapsack(profit,weight,total_capacity):
    total_items = len(profit)
    dp = [[0 for i in range(total_capacity+1)] for i in range(total_items+1)]

    for wt in range(1,total_items+1):
        for curr_cap in range(1,total_capacity+1):
            if curr_cap >= weight[wt-1]:
                dp[wt][curr_cap] = max(dp[wt][curr_cap - weight[wt-1]] + profit[wt-1], dp[wt-1][curr_cap])
            else:
                dp[wt][curr_cap] = dp[wt-1][curr_cap]
            

    return dp[total_items][total_capacity]

profit = [4,7,6]
weight = [1,2,3]

print(unbounded_knapsack(profit,weight,4))