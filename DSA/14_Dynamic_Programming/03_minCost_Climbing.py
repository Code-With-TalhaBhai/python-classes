
# Recurrsion
def minCost_Climbing1(cost):
    n = len(cost)

    def min_cost1(i,curr_cost):
        if i < 2:
            return curr_cost
        return min(min_cost1(i-1,curr_cost+cost[i-1]),min_cost1(i-2,curr_cost+cost[i-2]))


    def min_cost2(i):
        if i < 2:
            return 0
        return min(cost[i-1]+min_cost2(i-1),cost[i-2]+min_cost2(i-2))


    def min_cost3(i):
        if i >= n-2:
            return 0

        return min(cost[i+1]+min_cost3(i+1),cost[i+2]+min_cost3(i+2))

    # return min_cost1(n,0)
    # return min_cost2(n)
    return min_cost3(-1)
    




def minCost_Climbing2(cost):
    n = len(cost)

    memo = {0:0,1:0}
    # memo = {}
    def min_cost1(i):
        if i in memo:
            return memo[i]
        # if i < 2: # with empty memo={}
            # return 0

        memo[i] = min(cost[i-2]+min_cost1(i-2),cost[i-1]+min_cost1(i-1))
        return memo[i]


    memo = {n-1:0,n-2:0}
    def min_cost2(i):
        if i in memo:
            return memo[i]

        memo[i] = min(cost[i+1]+min_cost2(i+1),cost[i+2]+min_cost2(i+2))
        return memo[i]


    # return min_cost1(n)
    return min_cost2(-1)


def minCost_Climbing3(cost):
    n = len(cost)
    dp = [0]*(n+1)

    # 1st way
    for i in range(2,n+1):
        dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

    # 2nd way
    # for i in range(n-3,-2,-1):
    #     dp[i] = min(dp[i+1]+cost[i+1],dp[i+2]+cost[i+2])

    return dp[n]


def minCost_Climbing4(cost):
    n = len(cost)
    prev1 = min(cost[0],cost[1])
    prev2 = min(cost[1]+prev1,cost[2]+cost[0])
    curr = 0

    for i in range(2,n):
        curr = min(cost[i-1]+prev1,cost[i-2]+prev2)
        prev2 = prev1
        prev1 = curr
    return curr



cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]

# Recurrsion
print('recurrsion')
print(minCost_Climbing1(cost1))
print(minCost_Climbing1(cost2))


# Memoization(Top-Down)
print('memoization')
print(minCost_Climbing2(cost1))
print(minCost_Climbing2(cost2))
# Tabulation(Bottom-Up)
print('tabulation')
print(minCost_Climbing3(cost1))
print(minCost_Climbing3(cost2))
# Bottom-Up No-space DP
print('No-space DP')
print(minCost_Climbing4(cost1))
print(minCost_Climbing4(cost2))

