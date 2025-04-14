


def longestOnes_1(nums, k: int) -> int:
    n = len(nums)
    r,l = 0,0
    max_len = 0
    no_of_zeroes = 0

    # [1,1,1,0,0,0,1,1,1,1,0]
    while r < n:
        if nums[r] == 0:
            no_of_zeroes += 1

        while no_of_zeroes > k:
            if nums[l] == 0:
                no_of_zeroes -= 1
            l += 1
        max_len = max(max_len,r-l+1)
        r += 1
    return max_len



def longestOnes_2(nums, k: int) -> int:
    n = len(nums)
    r,l = 0,0
    max_len = 0
    no_of_zeroes = 0

    while r < n:
        if nums[r] == 0:
            no_of_zeroes += 1

        if no_of_zeroes > k:
            if nums[l] == 0:
                no_of_zeroes -= 1
            l += 1

        max_len = max(max_len,r-l+1)
        r += 1
    return max_len

    

nums1 = [1,1,1,0,0,0,1,1,1,1,0]
nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]

print(longestOnes_1(nums1,2))
print(longestOnes_1(nums1,3))
print('Optimal')
print(longestOnes_2(nums1,2))
print(longestOnes_2(nums1,3))