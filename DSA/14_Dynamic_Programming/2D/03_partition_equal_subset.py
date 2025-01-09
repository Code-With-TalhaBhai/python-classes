

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



def canPartition1_memo(nums):
    n = len(nums)

    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    
    target = total_sum // 2

    # memo = [[-1 for i in range(target+1)] for j in range(n+1)]
    # def canPart1(i,k):
    #     if memo[i][k] != -1:
    #         return memo[i][k]
        
    #     if i == 0 or k < 0:
    #         return False
        
    #     if k == 0:
    #         return True
        
    #     memo[i][k] = canPart1(i-1,k-nums[i-1]) or canPart1(i-1,k)
    #     return memo[i][k]

    # canPart1(n,target)
    # return memo[n][target]


    # memo1 = [[-1 for i in range(target+1)] for i in range(n)]
    # def canPart2(i,k):
    #     if memo1[i-1][k] != -1:
    #         return memo1[i-1][k]
        
    #     if i == 0 or k < 0:
    #         return False
        
    #     if k == 0:
    #         return True
        
    #     memo1[i-1][k] = canPart2(i-1,k-nums[i-1]) or canPart2(i-1,k)
    #     return memo1[i-1][k]

    # canPart2(n,target)
    # return memo1[n-1][target]


    memo2 = [[-1 for i in range(target)] for i in range(n)]

    def canPart3(i,sum):
        if i == n or sum > target:
            return False
        
        if sum == target:
            return True
        
        if memo2[i][sum] != -1:
            return memo2[i][sum]
        
        memo2[i][sum] = canPart3(i+1,sum+nums[i]) or canPart3(i+1,sum)
        return memo2[i][sum]


    canPart3(0,0)
    return memo2[0][0]


    



def canPartition2(nums):
    n = len(nums)

    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    
    target = total_sum // 2
    dp = [[False for i in range(target+1)] for i in range(n+1)]
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



def canPartition3(nums):
    n = len(nums)

    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    
    target = total_sum // 2 
    prev = [False]*(target+1)
    curr = [False]*(target+1)
    prev[0] = True

    for i in range(1,n+1):
        for j in range(target+1):
            if j >= nums[i-1]:
                curr[j] = prev[j] or prev[j-nums[i-1]]
            else:
                curr[j] = prev[j]
        prev = curr.copy()
    
    return prev[target]


nums1 = [1,5,11,5]
nums2 = [1,2,3,5]

print('with recurrsion')
print(canPartition1(nums1))
print(canPartition1(nums2))
print('with memoization')
print(canPartition1_memo(nums1))
print(canPartition1_memo(nums2))
print('with tabulation')
print(canPartition2(nums1))
print(canPartition2(nums2))

print('with space-optimized')
print(canPartition3(nums1))
print(canPartition3(nums2))