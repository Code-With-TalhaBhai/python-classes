


def kadane_algorithm(nums):
    n = len(nums)
    maxi = float("-inf")
    sum = 0

    for i in range(n):
        sum += nums[i]
        maxi = max(sum,maxi)
        if sum < 0:
            sum = 0
    return maxi





nums1 = [1,5,4,2,9,9,9]
nums2 = [-2,1,-3,4,-1,2,1,-5,4]


print(kadane_algorithm(nums1))
print(kadane_algorithm(nums2))