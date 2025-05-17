

def target_sum1(nums,target):
    n = len(nums)
    memo = {}

    def target_sum(i,curr_sum):
        if i == n:
            if curr_sum == target:
                return 1
            return 0

        if (i,curr_sum) in memo:
            return memo[(i,curr_sum)]

        memo[(i,curr_sum)] = target_sum(i+1,curr_sum+nums[i]) + target_sum(i+1,curr_sum-nums[i])
        return memo[(i,curr_sum)]
    return target_sum(0,0)


nums1 = [1,1,1,1,1]
target1 = 3

nums2 = [1]
target2 = 1


print('With Recurrsion')
print(target_sum1(nums1,target1))
print(target_sum1(nums2,target2))