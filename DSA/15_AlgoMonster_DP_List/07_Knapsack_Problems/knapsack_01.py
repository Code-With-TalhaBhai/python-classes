

def knapsack01(profit,weight,total_capacity):

    total_items = len(profit)
    dp = [[0 for i in range(total_capacity+1)] for i in range(total_items+1)]


    for curr_item_wt in range(1,total_items+1):
        for curr_cap in range(1,total_capacity+1):
            if curr_cap >= weight[curr_item_wt-1]:
                dp[curr_item_wt][curr_cap] = dp[curr_item_wt-1][curr_cap-weight[curr_item_wt-1]] + profit[curr_item_wt-1]
            else:
                dp[curr_item_wt][curr_cap] = dp[curr_item_wt-1][curr_cap]

    print(dp)
    return dp[total_items][total_capacity]








profit = [4,5,6]
weight = [1,2,3]

print(knapsack01(profit,weight,4))
