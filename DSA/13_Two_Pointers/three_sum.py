from typing import List


def threeSum(nums: List[int]):
    nums.sort()
    n = len(nums)
    final = []
    # print(nums)

    for i in range(len(nums)-1):

        if nums[i] > 0:
            break

        j = i + 1
        k = n - 1
        left_negative = abs(nums[i])


        while j < k:
            while j+1 < n and nums[j] == nums[j+1]:
                j += 1

            right_positive = nums[j] + nums[k]

            if left_negative - right_positive == 0:
                final.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
            
            if left_negative > right_positive:
                j += 1
            elif left_negative < right_positive:
                k -= 1

    return final





nums1 = [-1,0,1,2,-1,-4] # [-4,-1,-1,0,1,2]
nums2 = [-2,1,1,-1,0]


print(threeSum(nums1))
print(threeSum(nums2))