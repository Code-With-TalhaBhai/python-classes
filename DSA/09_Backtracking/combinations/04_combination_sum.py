

def combination_sum_iv(nums,target):
    n = len(nums)
    memo = {}

    # def combination(i,curr_sum):
    #     if curr_sum == target:
    #         return 1

    #     if i == n or curr_sum > target:
    #         return 0

    #     if (i,curr_sum) in memo:   
    #         return memo[(i,curr_sum)]

    #     total = 0
    #     for i in range(n):
    #         total += combination(i,curr_sum+nums[i])
    #     memo[(i,curr_sum)] = total
    #     return memo[(i,curr_sum)]



    def combination(i,curr_sum):
        if curr_sum == target:
            return 1

        if i == n or curr_sum > target:
            return 0
        
        if (i,curr_sum) in memo:
            return memo[(i,curr_sum)]
        
        memo[(i,curr_sum)] = combination(0,curr_sum+nums[i]) + combination(i+1,curr_sum)
        return memo[(i,curr_sum)]
    return combination(0,0)


nums1 = [9]
target1 = 3
nums2 = [1,2,3]
target2 = 4



print(combination_sum_iv(nums1,target1))
print(combination_sum_iv(nums2,target2))