


def minSum(nums1,nums2):
    first_sum = 0
    second_sum = 0

    first_zeros = 0
    second_zeros = 0

    for num in nums1:
        if num == 0:
            first_zeros += 1
        first_sum += num
    

    for num in nums2:
        if num == 0:
            second_zeros += 1
        second_sum += num

    first_sum += first_zeros
    second_sum += second_zeros


    if first_sum > second_sum and second_zeros == 0 or first_sum < second_sum and first_zeros == 0:
        return -1
    
    
    return max(first_sum,second_sum)
    







nums1 = [3,2,0,1,0]
nums2 = [6,5,0]

nums3 = [2,0,2,0]
nums4 = [1,4]

print(minSum(nums1,nums2))
print(minSum(nums3,nums4))
