

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

    
        
# def min_cost_climb(cost,n,curr_cost):
#     if n < 2:
#         return curr_cost


#     return min(min_cost_climb(cost,n-1,curr_cost+cost[n-1]),min_cost_climb(cost,n-2,curr_cost+cost[n-2]))


# cost1 = [10,15,20]
# # cost1 = [10,15]
# cost2 = [1,100,1,1,1,100,1,1,100,1]


# print(min_cost_climb(cost1,len(cost1),0))
# print(min_cost_climb(cost2,len(cost2),0))


def rob(nums,i,amt):
    
    if i >= len(nums):
        return amt

    return max(rob(nums,i+2,amt+nums[i]),rob(nums,i+1,amt))


def rob1(nums):
    n = len(nums)
    memo = {}

    def robin(i):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]

        memo[i] = max(nums[i]+robin(i+2),robin(i+1))
        return memo[i]

    robin(0)
    return max(memo[0],memo[1])


nums1 = [1,2,3,1]
nums2 = [2,7,9,3,1]
nums3 = [7,3,2,8,2,1,10]

print(rob(nums1,0,0))
print(rob(nums2,0,0))
print(rob(nums3,0,0))

print(rob1(nums1))
print(rob1(nums2))
print(rob1(nums3))