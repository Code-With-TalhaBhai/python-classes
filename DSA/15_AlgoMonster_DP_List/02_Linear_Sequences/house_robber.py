


def rob1(nums):
    n = len(nums)
    memo = {n:0,n+1:0}

    def rob(i):
        if i in memo:
            return memo[i]
        
        memo[i] = max(nums[i]+rob(i+2),rob(i+1))
        return memo[i]
    return rob(0)



def rob2(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])

    # 1st way
    # dp = [-1 for i in range(n)]
    # dp[0] = nums[0]
    # dp[1] = nums[1]

    # for i in range(2,n):
    #     dp[i] = max(nums[i]+dp[i-2],dp[i-1])
    # return dp[n-1]

    #2nd way - space optimization
    prev = nums[0]
    curr = nums[1]

    for i in range(2,n):
        temp = max(nums[i]+prev,curr)
        prev = curr
        curr = temp

    return curr



    




# nums = [2,7,9,3,1]
nums = [10,40,15,5,20]
print(rob1(nums))
print(rob2(nums))