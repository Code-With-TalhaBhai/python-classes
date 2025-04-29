


def LIS1(nums):
    n = len(nums)
    memo = {}

    def LIS(i,prev_largest):
        if i == n:
            return 0
        if (i,prev_largest) in memo:
            return memo[(i,prev_largest)]
        
        inc = 0
        if nums[i] > prev_largest:
            inc = 1 + LIS(i+1,nums[i])


        exc = LIS(i+1,prev_largest)
        # return max(inc,exc)
        memo[(i,prev_largest)] = max(inc,exc)
        return memo[(i,prev_largest)]
    return LIS(0,float('-inf'))


def LIS2(nums):
    n = len(nums)
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2,n+1):
    # for i in range(1,n):
        if nums[i-1] > nums[i-2]:
            dp[i] += 1
        dp[i] += dp[i-1]
    return dp[n]


nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]
nums4 = [4,10,4,3,8,9]


print(LIS1(nums1))
print(LIS1(nums2))
print(LIS1(nums3))
print(LIS1(nums4))
print()
print(LIS2(nums1))
print(LIS2(nums2))
print(LIS2(nums3))
print(LIS2(nums4))