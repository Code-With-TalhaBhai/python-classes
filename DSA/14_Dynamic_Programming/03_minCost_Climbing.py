


def minCost_Climbing(cost):  
    n = len(cost)

    def min_cost(i):
        if i >= n:
            return 0
        

        return cost[i] + min(min_cost(i+1),min_cost(i+2))


    return min_cost(0)





cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]


print(minCost_Climbing(cost1))
print(minCost_Climbing(cost2))