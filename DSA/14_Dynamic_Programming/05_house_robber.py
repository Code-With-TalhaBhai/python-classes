

# Recurrsion
def house_robber1(nums):
    n = len(nums)

    #1st way 
    def rob(i):
        if i < 0:
            return 0

        return max(nums[i]+rob(i-2),rob(i-1))
    return rob(n-1)

    # 2nd way
    # def rob(i):
    #     if i >= n:
    #         return 0
        
    #     return max(nums[i]+rob(i+2),rob(i+1))
    # return rob(0)

    # 3rd way
    # def rob(i,amt):
    #     if i >= n:
    #         return amt
        
    #     return max(rob(i+2,nums[i]+amt),rob(i+1,amt))
    # return rob(0,0)



def house_robber2(nums):
    n = len(nums)
    memo = {
        -1: 0,
        -2: 0,
    }

    def rob(i):
        if i in memo:
            return memo[i]

        memo[i] = max(nums[i]+rob(i-2),rob(i-1))
        return memo[i]
    return rob(n-1)

    # 2nd way
    # memo = {
    #     n : 0,
    #     n+1 : 0
    # }

    # def rob(i):
    #     if i in memo:
    #         return memo[i]
        
    #     memo[i] = max(nums[i]+rob(i+2),rob(i+1))
    #     return memo[i]
    # return rob(0)


def house_robber3(nums):
    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1],nums[i]+dp[i-2])

    return dp[n-1]


def house_robber4(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    #1st way
    # prev = nums[0]
    # curr = max(nums[0],nums[1])
    # for i in range(2,n):
    #     prev,curr = curr,max(nums[i]+prev,curr)


    #2nd way
    prev1 = nums[0]
    prev2 = max(nums[0],nums[1])
    curr = prev2
    for j in range(2,n):
        curr = max(nums[j]+prev1,prev2)
        prev1 = prev2
        prev2 = curr
    return curr


nums1 = [1,2,3,1]
nums2 = [2,7,9,3,1]
nums3 = [7,3,2,8,2,1,10]
print('with recurrsion')
print(house_robber1(nums1))
print(house_robber1(nums2))
print(house_robber1(nums3))
print()
print('with memoization')
print(house_robber2(nums1))
print(house_robber2(nums2))
print(house_robber2(nums3))
print()
print('with tabulation')
print(house_robber3(nums1))
print(house_robber3(nums2))
print(house_robber3(nums3))
print()
print('bottom-up Constant Space')
print(house_robber4(nums1))
print(house_robber4(nums2))
print(house_robber4(nums3))

