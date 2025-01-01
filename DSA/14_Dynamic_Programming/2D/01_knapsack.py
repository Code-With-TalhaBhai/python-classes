

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


    def knapsack4(i,wt):
        if i == 0 or wt == 0:
            return 0

        if weight[i-1] > wt:
            return knapsack4(i-1,wt)

        return max(val[i-1]+knapsack4(i-1,wt-weight[i-1]),knapsack4(i-1,wt))
    return knapsack4(n,cap)



def knapsack01_b(capacity,val,wt):
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



# Tabulation
print('With Tabulation')
print(knapsack01_b(capacity,val,wt))
print(knapsack01_b(capacity2,val2,wt2))
print(knapsack01_b(capacity3,val3,wt3))