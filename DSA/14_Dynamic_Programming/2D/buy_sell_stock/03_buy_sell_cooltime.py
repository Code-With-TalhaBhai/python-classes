


def buy_sell_stock_cooltime(prices):
    
    def maxProfit(i,bal):
        if i >= len(prices):
            ...


        return max(maxProfit(i,bal-prices[i]),maxProfit(i+1,bal))

    return maxProfit(0,0)




prices1 = [1,2,3,0,2]
prices2 = [1]


print(buy_sell_stock_cooltime(prices1))
print(buy_sell_stock_cooltime(prices2))