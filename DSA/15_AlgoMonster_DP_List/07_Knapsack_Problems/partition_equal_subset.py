




def canPartition1(nums) -> bool:
    n = len(nums)

    total = sum(nums)
    if total % 2 == 1:
        return False
    
    mid = total // 2

    def check(i,sum):
        if i == n or sum > mid:
            return False

        if sum == mid:
            return True
        
        include = check(i+1,sum+nums[i])
        if include:
            return True
        exclude = check(i+1,sum)
        return include or exclude

        # return check(i+1,sum+nums[i]) or check(i+1,sum)
    return check(0,0)




def canPartition2(nums) -> bool:
    n = len(nums)

    total = sum(nums)
    if total % 2 == 1:
        return False
    
    target = total // 2

    # 2D - Array
    # dp = [[False for i in range(target+1)]for i in range(n+1)]
    # dp[0][0] = True
    # for i in range(1,n+1):
    #     for j in range(target+1):
    #         take = False
    #         if j >= nums[i-1]:
    #             take = dp[i-1][j-nums[i-1]]
    #         no_take = dp[i-1][j]
    #         dp[i][j] = take or no_take
    # return dp[n][target]


    # 1D - Array
    # prev = [False for i in range(target+1)]
    # dp = [False for i in range(target+1)]
    # prev[0] = True

    # for i in range(n):
    #     for j in range(target+1):
    #         take = False
    #         if j >= nums[i]:
    #             take =  prev[j-nums[i]]
    #         noTake = prev[j]
    #         dp[j] = take or noTake
    #     prev = dp.copy()
    # return dp[target]


    # 1D - Array Optimization
    dp = [False for i in range(target+1)]
    dp[0] = True

    for i in range(n):
        for j in range(target,nums[i]-1,-1):
            dp[j] = dp[j] or dp[j-nums[i]]
            # More Optimization
            # if dp[target]:
                # return True
    return dp[target]




nums1 = [1,5,11,5]
nums2 = [1,2,3,5]

print('Memoization')
print(canPartition1(nums1))
print(canPartition1(nums2))
print('DP')
print(canPartition2(nums1))
print(canPartition2(nums2))