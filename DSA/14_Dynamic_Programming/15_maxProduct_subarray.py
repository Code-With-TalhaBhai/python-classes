

def maxProduct_subarray1(nums):
    n = len(nums)
    maxi = float('-inf')

    for i in range(n):
        mul = 1
        for j in range(i,n):
            mul *= nums[j]
            maxi = max(maxi,mul)
    return maxi


def maxProduct_subarray2(nums):
    n = len(nums)
    prev_min = 1
    prev_max = 1
    maxi = float("-inf")

    for i in range(n):
        prev_min *= nums[i]
        prev_max *= nums[i]

        maxi = max(maxi,prev_min,prev_max)
        if prev_max <= 0:
            prev_max = 1
    return maxi



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
nums3 = [0,2]
nums4 = [2,3,-2,4,-1]

# brute-force
print(maxProduct_subarray1(nums1))
print(maxProduct_subarray1(nums2))
print(maxProduct_subarray1(nums3))
print()
print(maxProduct_subarray2(nums1))
print(maxProduct_subarray2(nums2))
print(maxProduct_subarray2(nums3))
print()
# print(maxProduct_subarray(nums1))
# print(maxProduct_subarray(nums2))
# print(maxProduct_subarray(nums3))