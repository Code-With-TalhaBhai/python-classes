



def maxSumAfterPartitioning1(arr,k):
    n = len(arr)
    memo : dict[int,float] = {n:0}

    def max_partition(i):
        if i in memo:
            return memo[i]
        
        max_nums = float('-inf')
        final = float('-inf')
        for j in range(i,min(i+k,n)):
            max_nums = max(max_nums,arr[j])
            sub_array_sum = max_nums * (j-i+1)
            final = max(final,sub_array_sum + max_partition(j+1))
        memo[i] = final
        return memo[i]
    return max_partition(0)




def maxSumAfterPartitioning2(arr,k):
    n = len(arr)
    dp = [0] * (n+1)

    # for i in range(1,n+1):
    #     maxVal = 0
    #     for j in range(1,min(i,k)+1):
    #         maxVal = max(maxVal,arr[i-j])
    #         dp[i] = max(dp[i],dp[i-j] + maxVal * j)
    # return dp[n]

    for i in range(1,n+1):
        maxVal = 0
        for j in range(min(i,k)):
            maxVal = max(maxVal,arr[i-j-1])
            dp[i] = max(dp[i],dp[i-j-1]+maxVal*(j+1))
    return dp[n]



arr = [1,15,7,9,2,5,10]
k = 3

print(maxSumAfterPartitioning1(arr,k))
print(maxSumAfterPartitioning2(arr,k))