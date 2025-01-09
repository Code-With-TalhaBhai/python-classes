


def maxProduct_subarray(nums):
    n = len(nums)

    max_product = nums[0]
    curr_product = nums[0]

    for i in range(1,n):
        curr_product *= nums[i]
        max_product = max(max_product,curr_product)

        if curr_product <= 0:
            curr_product = 1
    return max_product



nums1 = [2,3,-2,4]
nums2 = [-2,0,-1]


print(maxProduct_subarray(nums1))
print(maxProduct_subarray(nums2))