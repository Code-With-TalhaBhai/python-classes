

# def min_cost_climb(cost,n,curr_cost):
#     if n >= len(cost):
#         return curr_cost
    
#     # curr_cost += cost[n-1]
#     return min(min_cost_climb(cost,n+1,curr_cost+cost[n-2]),min_cost_climb(cost,n+1,curr_cost+cost[n-1]))


# def min_cost_climb(cost,n,curr_cost):

#     def min_cost_climb1(n,curr_cost):
#         if n >= len(cost):
#             return curr_cost

#         curr_cost += cost[n]
#         return min(min_cost_climb1(n+1,curr_cost),min_cost_climb1(n+2,curr_cost))

#     def min_cost_climb2(n,curr_cost):
#         if n >= len(cost):
#             return curr_cost

#         curr_cost += cost[n]
#         return min(min_cost_climb2(n+1,curr_cost),min_cost_climb2(n+2,curr_cost))

#     return min(min_cost_climb1(0,0),min_cost_climb2(1,0))

    
        
def min_cost_climb(cost,n,curr_cost):
    if n < 2:
        return curr_cost


    return min(min_cost_climb(cost,n-1,curr_cost+cost[n-1]),min_cost_climb(cost,n-2,curr_cost+cost[n-2]))


cost1 = [10,15,20]
# cost1 = [10,15]
cost2 = [1,100,1,1,1,100,1,1,100,1]


print(min_cost_climb(cost1,len(cost1),0))
print(min_cost_climb(cost2,len(cost2),0))