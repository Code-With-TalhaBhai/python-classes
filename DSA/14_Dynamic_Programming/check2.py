


def longest_increasing_subsequence(nums):
    n = len(nums)
    res = [0]

    def LIS(i,prev,target):
        if i == n or prev > nums[i]:
            res[0] = max(res[0],target)
            return
        

        LIS(i+1,nums[i],target+1)
        LIS(i+1,nums[i],0)


    LIS(0,float("-inf"),0)
    return res[0]







nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]


print(longest_increasing_subsequence(nums1))
print(longest_increasing_subsequence(nums2))
print(longest_increasing_subsequence(nums3))