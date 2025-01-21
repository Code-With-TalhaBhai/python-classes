

def buy_sell_brute_force(prices):
    n = len(prices)
    maxi = 0

    for i in range(n):
        for j in range(i+1,n):
            maxi = max(maxi,prices[j]-prices[i])            
    return maxi


def buy_sell_dp(prices):  
    n = len(prices)
    l,r = 0,1
    maxi = 0
    
    # 1st approach
    # while r < n:
    #     if prices[r] < prices[l]:
    #         l = r
    #     else:
    #         maxi = max(maxi,prices[r]-prices[l])
    #     r += 1
    # return maxi


    # 2nd approach
    mini = prices[0]
    for i in range(1,n):
        maxi = max(maxi,prices[i]-mini)
        mini = min(mini,prices[i])

    return maxi



prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]


print(buy_sell_brute_force(prices1))
print(buy_sell_dp(prices1))
print()
print(buy_sell_brute_force(prices2))
print(buy_sell_dp(prices2))
