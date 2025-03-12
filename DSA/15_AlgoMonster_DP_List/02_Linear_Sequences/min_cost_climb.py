

def min_cost_climbing1(cost,i=1,memo={}):
# def min_cost_climbing1(cost,n,memo={}):

    # if i-1 in memo:
    #     return memo[i-1]
    # print(memo)

    if i >= len(cost):
        return 0

    # memo[i-1] = min(cost[i-1]+min_cost_climbing1(cost,i+1),cost[i]+min_cost_climbing1(cost,i+2))
    return min(cost[i-1]+min_cost_climbing1(cost,i+1),cost[i]+min_cost_climbing1(cost,i+2))
    # return memo[i-1]

    # if n in memo:
    #     return memo[n]

    # if n <= 1:
    #     return 0
    
    # memo[n] =  min(cost[n-1]+min_cost_climbing1(cost,n-1),cost[n-2]+min_cost_climbing1(cost,n-2))
    # return memo[n]

cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]

print(min_cost_climbing1(cost1))
print(min_cost_climbing1(cost2))

# print(min_cost_climbing1(cost1,len(cost1)))
# print(min_cost_climbing1(cost2,len(cost2)))