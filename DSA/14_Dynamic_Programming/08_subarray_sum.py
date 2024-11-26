

# Brute Force -> O(N^2)
def max_subarray_sum1(nums):
    n = len(nums)
    maxi = float("-inf")

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            maxi = max(maxi,sum)
    return maxi


# DP-> Kadane Algorithm -> O(n)
def max_subarray_sum2(nums):
    sum = 0
    maxi = nums[0]

    for num in nums:
        sum += num
        maxi = max(maxi,sum)


        if sum < 0:
            sum = 0
    return maxi



nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [5,4,-1,7,8]

print('brute-force')
print(max_subarray_sum1(nums1))
print(max_subarray_sum1(nums2))
print()
print('Kadane Algorithm')
print(max_subarray_sum2(nums1))
print(max_subarray_sum2(nums2))