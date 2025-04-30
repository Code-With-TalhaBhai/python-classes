



def maxSumAfterPartitioning(arr,k):
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





arr = [1,15,7,9,2,5,10]
k = 3

print(maxSumAfterPartitioning(arr,k))