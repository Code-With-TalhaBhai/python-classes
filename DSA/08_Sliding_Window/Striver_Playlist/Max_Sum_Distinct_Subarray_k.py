


from collections import defaultdict


def maximumSubarraySum(nums, k: int) -> int:
    n = len(nums)
    l = 0
    maxi = 0
    sum = 0
    nums_freq = defaultdict(int)
    unique = 0

    for r in range(n):
        nums_freq[nums[r]] += 1
        if nums_freq[nums[r]] == 1:
            unique += 1
        sum += nums[r]

        # while l < r and (len(nums_freq) > k or r - l + 1 > k):
        while l < r and (unique > k or r - l + 1 > k):
            nums_freq[nums[l]] -= 1
            if nums_freq[nums[l]] == 0:
                nums_freq.pop(nums[l])
                unique -= 1
            sum -= nums[l]
            l += 1

        # if len(nums_freq) == k:
        if unique == k:
            maxi = max(sum,maxi)
    return maxi




nums1 = [1,5,4,2,9,9,9]
nums2 = [4,4,4]

print(maximumSubarraySum(nums1,3))
print(maximumSubarraySum(nums2,3))