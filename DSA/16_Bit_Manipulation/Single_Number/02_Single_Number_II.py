


def Single_Number_II_1(nums):
    total_bits = 31 #32->(0-31)
    ans = 0

    for bitIndex in range(total_bits+1):
        cnt = 0
        for i in range(len(nums)):
            # check ith bit
            if nums[i] & (1 << bitIndex):
                cnt += 1
        # set ith-bit
        if cnt % 3 == 1:
            ans = ans | (1 << bitIndex)

        # For python implementation, converstion into negative numbers
        if ans >= (1 << 31): # If sign bit is set
            ans = ans - (1 << 32) # Convert to correct negative number
    return ans


def Single_Number_II_2(nums):
    n = len(nums)
    nums.sort()

    for i in range(1,n,3):
        if nums[i] != nums[i-1]:
            return nums[i-1]
    return nums[n-1]


def Single_Number_II_3(nums):
    ones = 0
    twos = 0

    for i in range(len(nums)):
        ones = (ones ^ nums[i]) & (~twos)
        twos = (twos ^ nums[i]) & (~ones)
    return ones



nums1 = [2,2,3,2]
nums2 = [0,1,0,1,0,1,99]
nums3 = [-2,-2,1,1,4,1,4,4,-4,-2]

print(Single_Number_II_1(nums1))
print(Single_Number_II_1(nums2))
print(Single_Number_II_1(nums3))
print()
print(Single_Number_II_2(nums1))
print(Single_Number_II_2(nums2))
print(Single_Number_II_2(nums3))
print()
print(Single_Number_II_3(nums1))
print(Single_Number_II_3(nums2))
print(Single_Number_II_3(nums3))