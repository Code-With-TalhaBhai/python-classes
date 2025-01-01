

def canPartition1(nums) -> bool:
    n = len(nums)

    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    
    target = total_sum // 2
    
    def partition(i,sum):
        if sum == target:
            return True
        
        if i == n or sum > target:
            return False
        
        return partition(i+1,sum+nums[i]) or partition(i+1,sum)
    return partition(0,0)


def canPartition2(nums):
    n = len(nums)

    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    
    target = total_sum // 2
    dp = [[False for i in range(target+1)]]*(n+1)
    dp[0][0] = True


    for i in range(1,n+1):
        for t in range(target+1):
            if t == 0:
                dp[i][t] = True
            elif t >= nums[i-1]:
                dp[i][t] = dp[i-1][t] or dp[i-1][t-nums[i-1]]
            else:
                dp[i][t] = dp[i-1][t]

    return dp[n][target]


nums1 = [1,5,11,5]
nums2 = [1,2,3,5]

print('with recurrsion')
print(canPartition1(nums1))
print(canPartition1(nums2))

print('with tabulation')
print(canPartition2(nums1))
print(canPartition2(nums2))