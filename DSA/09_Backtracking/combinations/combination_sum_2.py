# Incomplete


# def combination_sum2(candidates,target):
#     sol,res = [],[]
#     sum = [0]
    
#     def backtrack(i,sum):
#         if i == len(candidates):
#             reverse_sol = reversed(sol)
#             if sum[0] == target and reverse_sol not in res:
#             # if sum[0] == target:
#                 res.append(sol.copy())
#             # res.append(sol.copy())
#             return

#         backtrack(i+1,sum)
#         num = candidates[i]
#         sol.append(num)
#         sum[0] += num

#         backtrack(i+1,sum)
#         sol.pop()
#         sum[0] -= num

#     # backtrack(0,sum)
#     backtrack(0,sum)
#     return res


def combination_sum2(candidates,target):
    sol,res = [],[]
    sum = [0]
    nums = sorted(candidates)
    print(nums)

    def backtrack(x):
        if sum[0] == target:
            res.append(sol.copy())

        if sum[0] >= target or x == len(nums):
            return
        
        for i in range(x,len(nums)):
            # if (i + 1) < len(nums) and nums[i] == nums[i+1]:
            # if (i + 1) < len(nums) and nums[i-1] == nums[i]: # wrong
            if i > 0 and nums[i] == nums[i-1]:
            # if nums[i] == nums[i+1]:
                sol.append(nums[i])
                sum[0] += nums[i]
                continue
            else:
                num = nums[i]
                sum[0] += num
                sol.append(num)
                backtrack(i+1)
                sum[0] -= num
                sol.pop()


    backtrack(0)
    return res




candidates = [10,1,2,7,6,1,5]
target = 8
# candidates = [2,5,2,1,2]
# target = 5
# candidates = [2,5,2]
print(combination_sum2(candidates,target))
print('working')