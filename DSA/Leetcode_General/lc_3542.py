



def minOperations(nums):
    n = len(nums)

    mini = float('inf')
    min_occurence = 0
    other_occurence = 0

    i = 0
    
    while i < n:
        item = nums[i]
        if i > 0 and nums[i] == nums[i-1]:
            ...

        if item < mini:
            min_occurence = 0
            mini = item
        
        min_occurence += 1

    return n - min_occurence






nums1 = [0,2]
nums2 = [3,1,2,1]
nums3 = [1,2,1,2,1,2]