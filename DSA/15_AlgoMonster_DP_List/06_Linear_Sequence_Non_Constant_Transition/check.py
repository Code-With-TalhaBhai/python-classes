


def LIS(nums):
    n = len(nums)

    def count_lis(i,prev_large):
        if i == n:
            return 0
        
        taken = 0
        if nums[i] > prev_large:
            taken = 1 + count_lis(i+1,nums[i])
        skip = count_lis(i+1,prev_large)

        return max(taken,skip)
    return count_lis(0,float('-inf'))




nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]
nums4 = [4,10,4,3,8,9]

print(LIS(nums1))
print(LIS(nums2))
print(LIS(nums3))
print(LIS(nums4))