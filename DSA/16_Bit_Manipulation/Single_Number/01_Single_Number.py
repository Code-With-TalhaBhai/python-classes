


def single_number(nums):
    
    k = nums[0]
    for i in range(1,len(nums)):
        k = k ^ nums[i]

    return k




nums1 = [4,1,2,1,2]
nums2 = [2,2,1]
nums3 = [1]


print(single_number(nums1))
print(single_number(nums2))
print(single_number(nums3))