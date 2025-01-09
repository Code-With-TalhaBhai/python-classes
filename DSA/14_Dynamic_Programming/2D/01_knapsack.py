

def knapsack01_a(cap,val,weight):
    maxi = [0]
    n = len(val)

    # with external variable -> 1st way
    # def knapsack1(i,wt,items):
    #     if wt > cap:
    #         return

    #     if i == n or wt == cap:
    #         maxi[0] = max(maxi[0],items)
    #         return 

    #     knapsack1(i+1,wt+weight[i],items+val[i])
    #     knapsack1(i+1,wt,items)
    # knapsack1(0,0,0)
    # return maxi[0]


    # without external variable -> 2nd way
    # def knapsack2(i,wt,items):
    #     if wt > cap:
    #         return 0
        
    #     if i == n or wt == cap:
    #         return items

    #     return max(knapsack2(i+1,wt+weight[i],items+val[i]),knapsack2(i+1,wt,items))
    # return knapsack2(0,0,0)


    
    # 3rd way
    # def knapsack3(i,wt):
    #     if i == n-1 or wt == cap:
    #         return 0

    #     if wt + weight[i+1] > cap:
    #         return knapsack3(i+1,wt)

    #     return max(val[i+1]+knapsack3(i+1,wt+weight[i+1]),knapsack3(i+1,wt))
    # return knapsack3(-1,0)


    # def knapsack4(i,wt):
    #     if i == 0 or wt == 0:
    #         return 0

    #     if weight[i-1] > wt:
    #         return knapsack4(i-1,wt)

    #     return max(val[i-1]+knapsack4(i-1,wt-weight[i-1]),knapsack4(i-1,wt))
    # return knapsack4(n,cap)

    def knapsack5(i,wt):
        if i == n or wt > cap:
            return 0

        if wt + weight[i] > cap:
            return knapsack5(i+1,wt)

        return max(val[i]+knapsack5(i+1,wt+weight[i]),knapsack5(i+1,wt))
    return knapsack5(0,0)


def knapsack01_b(capacity,val,wt):
    n = len(val)

    # memo1 = [[-1 for i in range(capacity+1)] for j in range(n+1)]
    # def knapsack(i,rem):
    #     if i == 0 or rem < 0:
    #         return 0;
    
    #     if memo1[n][rem] != -1:
    #         return memo1[n][rem]

    #     if rem < wt[i-1]:
    #         memo1[i][rem] = knapsack(i-1,rem);
    #     else:
    #         memo1[i][rem] = max(val[i-1]+knapsack(i-1,rem-wt[i-1]),knapsack(i-1,rem))
    #     return memo1[i][rem]
    # knapsack(n,capacity)
    # return memo1[n][capacity]


    # memo2 = [[-1 for i in range(capacity+1)] for j in range(n+1)]
    # def knapsack2(i,sum):
    #     if i == n or sum > capacity:
    #         return 0

    #     if memo2[i][sum] != -1:
    #         return memo2[i][sum]

    #     if wt[i] + sum > capacity:
    #         memo2[i][sum] = knapsack2(i+1,sum)
    #     else:
    #         memo2[i][sum] = max(val[i]+knapsack2(i+1,sum+wt[i]),knapsack2(i+1,sum))
    #     return memo2[i][sum]


    memo3 = [[-1 for i in range(capacity+1)] for j in range(n+1)]
    def knapsack3(i,sum,total):
        if sum > capacity:
            return 0
        
        if i == n or sum == capacity:
            return total

        if memo3[i][sum] != -1:
            return memo3[i][sum]

        memo3[i][sum] = max(knapsack3(i+1,sum+wt[i],total+val[i]),knapsack3(i+1,sum,total))
        return memo3[i][sum]

    knapsack3(0,0,0)
    return memo3[0][0]






def knapsack01_c(capacity,val,wt):
    n = len(val)
    dp = [[0 for i in range(capacity+1)] for j in range(n+1)]


    for i in range(1,n+1):
        for cap in range(1,capacity+1):
            # if cap == 0 or i == 0:
                # dp[i][cap] = 0
                # continue
            if cap >= wt[i-1]:
                dp[i][cap] = max(val[i-1] + dp[i-1][cap-wt[i-1]],dp[i-1][cap])
            else:
                dp[i][cap] = dp[i-1][cap]
    return dp[n][capacity]



def knapsack01_d(capacity,val,wt):
    n = len(wt)

    # 1D Array
    dp = [0]*(capacity+1)
    # print(dp)

    for i in range(1,n+1):
        for w in range(capacity,0,-1):
            if w >= wt[i-1]:
                dp[w] = max(dp[w],dp[w-wt[i-1]]+val[i-1])
    return dp[capacity]



capacity = 4
val = [1, 2, 3]
wt = [4, 5, 1] 

capacity2 = 5
val2 = [10, 40, 30, 50]
wt2 = [5, 4, 6, 3] 


capacity3 = 3
val3 = [1,2,3]
wt3 = [4,5,6]

# Brute Force - Backtracking
print('With Recurrsion')
print(knapsack01_a(capacity,val,wt))
print(knapsack01_a(capacity2,val2,wt2))
print(knapsack01_a(capacity3,val3,wt3))

# Memoization
print('With Memoization')
print(knapsack01_b(capacity,val,wt))
print(knapsack01_b(capacity2,val2,wt2))
print(knapsack01_b(capacity3,val3,wt3))

# Tabulation
print('With Tabulation')
print(knapsack01_c(capacity,val,wt))
print(knapsack01_c(capacity2,val2,wt2))
print(knapsack01_c(capacity3,val3,wt3))


# Space Optimization
print('With Space Optimization')
print(knapsack01_d(capacity,val,wt))
print(knapsack01_d(capacity2,val2,wt2))
print(knapsack01_d(capacity3,val3,wt3))