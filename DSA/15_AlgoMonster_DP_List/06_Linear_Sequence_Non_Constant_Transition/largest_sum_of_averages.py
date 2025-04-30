


def largestSumOfAverages(nums, k: int) -> float:
    n = len(nums)
    memo = {}

    def largest_sum(i,cnt):
        if (i,cnt) in memo:
            return memo[(i,cnt)]
            
        if i == n:
            return 0
        if cnt == k:
            return float('-inf')
        

        curr_avg_sum = 0
        nums_sum = 0
        final = float('-inf')
        for j in range(i,n):
            nums_sum += nums[j]
            curr_avg_sum = nums_sum / (j - i + 1)
            final = max(final,curr_avg_sum + largest_sum(j+1,cnt+1))
        memo[(i,cnt)] = final
        return memo[(i,cnt)]
        # return final
    return largest_sum(0,0)




nums1 = [9,1,2,3,9]
k1 = 3

nums2 = [1,2,3,4,5,6,7]
k2 = 4

print(largestSumOfAverages(nums1,k1))
print(largestSumOfAverages(nums2,k2))