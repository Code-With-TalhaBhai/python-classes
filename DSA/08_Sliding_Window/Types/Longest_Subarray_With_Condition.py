# Longest Subarray less than equal to sum


def longest_subaray_with_sum1(nums,k):
    
    l,r = 0,0
    max_len = 0
    sum = 0

    while r < len(nums):
        sum += nums[r]
        while sum > k:
            sum -= nums[l]
            l += 1
        
        max_len = max(max_len,r-l+1)
        r += 1
    return max_len



def longest_subaray_with_sum2(nums,k):
    n = len(nums)

    sum = 0
    l,r = 0,0
    max_len = 0

    while r < n:
        if sum + nums[r] > k:
            sum -= nums[l]
            l += 1
        else:
            sum += nums[r]
            max_len = max(max_len,r-l+1)
            r += 1
    return max_len



nums1 = [2,15,1,3,10]
nums2 = [2,15,2,3,10]
print(longest_subaray_with_sum1(nums1,14))
print(longest_subaray_with_sum1(nums2,2))
print('Optimized')
print(longest_subaray_with_sum2(nums1,14))
print(longest_subaray_with_sum2(nums2,2))