


def subset_sum_equals_k_1(nums,k):
    n = len(nums)

    def subset_sum(i,sum):
        if sum == k:
            return True
        
        if i == n or sum > k:
            return False
        
        return subset_sum(i+1,nums[i]+sum) or subset_sum(i+1,sum)
    return subset_sum(0,0)



def subset_sum_equals_k_2(nums,k):
    n = len(nums)
    memo = [[-1 for _ in range(k+1)]]*(n+1)


    def subset_sum(i,sum):
        if sum == k:
            return True

        if i == n or sum > k:
            return False

        if memo[i][sum] != -1:
            return memo[i][sum]
        
        memo[i][sum] = subset_sum(i+1,nums[i]+sum) or subset_sum(i+1,sum)
        return memo[i][sum]

    subset_sum(0,0)
    return memo[0][0]



def subset_sum_equals_k_3(nums,k):
    n = len(nums)

    # dp = [[False for i in range(k+1)]]*(n+1)
    dp = [[False for i in range(k+1)] for j in range(n+1)]
    dp[0][0] = True
    
    for i in range(1,n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = True

            elif j >= nums[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]


    return dp[n][k]
            
            


nums1 = [1,1,1]
k1 = 2
nums2 = [1,2,3]
k2 = 4

# with recurrsion
print('with recurrsion')
print(subset_sum_equals_k_1(nums1,k1))
print(subset_sum_equals_k_1(nums2,k2))

# with memoization
print('with memoization')
print(subset_sum_equals_k_2(nums1,k1))
print(subset_sum_equals_k_2(nums2,k2))


# with tabulation
print('with tabulation')
print(subset_sum_equals_k_3(nums1,k1))
print(subset_sum_equals_k_3(nums2,k2))