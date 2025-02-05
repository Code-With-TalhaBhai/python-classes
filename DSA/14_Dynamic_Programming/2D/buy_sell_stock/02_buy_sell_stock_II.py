

def buy_sell_stock_ii_1(prices):
    
    def helper(i,canBuy):
        if i == len(prices):
            return 0

        if canBuy:
            buy = helper(i+1,False) - prices[i]
            skip = helper(i+1,True)
            return max(buy,skip)
        else:
            sell = helper(i+1,True) + prices[i]
            skip = helper(i+1,False)
            return max(sell,skip)
    return helper(0,1)


def buy_sell_stock_ii_2(prices):
    memo = {}
    def helper(i,canBuy):
        if i == len(prices):
            return 0

        if (i,canBuy) in memo:
            return memo[(i,canBuy)]


        if canBuy:
            buy = helper(i+1,False) - prices[i]
            skip = helper(i+1,True)
            memo[(i,canBuy)] = max(buy,skip)
        else:
            sell = helper(i+1,True) + prices[i]
            skip = helper(i+1,False)
            memo[(i,canBuy)] = max(sell,skip)
        return memo[(i,canBuy)]
    return helper(0,1)



def buy_sell_stock_ii_3(prices):
    profit = 0

    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit




prices1 = [7,1,5,3,6,4]
prices2 = [1,2,3,4,5]

print('with recurrsion')
print(buy_sell_stock_ii_1(prices1))
print(buy_sell_stock_ii_1(prices2))
print('with memoization')
print(buy_sell_stock_ii_2(prices1))
print(buy_sell_stock_ii_2(prices2))
print('with dp')
print(buy_sell_stock_ii_3(prices1))
print(buy_sell_stock_ii_3(prices2))