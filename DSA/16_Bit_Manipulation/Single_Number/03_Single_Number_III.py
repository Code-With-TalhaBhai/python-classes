


def singleNumber(nums):
    n = len(nums)

    xor = 0
    for i in range(n):
        xor ^= nums[i]

    # finding rightmost set-bit
    rightmost_bit = (xor & xor-1) ^ xor

    bucket_1 = 0
    bucket_2 = 0

    for i in range(n):
        if nums[i] & rightmost_bit:
            bucket_1 ^= nums[i]
        else:
            bucket_2 ^= nums[i]

    return [bucket_1,bucket_2]





nums1 = [1,2,1,3,2,5]
nums2 = [-1,0]
nums3 = [0,1]

print(singleNumber(nums1))
print(singleNumber(nums2))
print(singleNumber(nums3))
