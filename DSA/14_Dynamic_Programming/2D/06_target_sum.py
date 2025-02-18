

def target_sum1(nums,target):
    
    def helper(i,sum):
        if i == len(nums) and sum == target:
            return 1
        
        if i == len(nums):
            return 0
        
        return helper(i+1,sum+nums[i]) + helper(i+1,sum-nums[i])
    return helper(0,0)



def target_sum2(nums,target):
    memo = {}
    def helper(i,sum):
        if i == len(nums) and sum == target:
            return 1
        
        if i == len(nums):
            return 0
        
        if (i,sum) in memo:
            return memo[(i,sum)]
        
        memo[(i,sum)] = helper(i+1,sum+nums[i]) + helper(i+1,sum-nums[i])
        return memo[(i,sum)]
    return helper(0,0)





nums1 = [1,1,1,1,1]
target1 = 3

nums2 = [1]
target2 = 1


print('With Recurrsion')
print(target_sum1(nums1,target1))
print(target_sum1(nums2,target2))


print('With Memoization')
print(target_sum2(nums1,target1))
print(target_sum2(nums2,target2))
