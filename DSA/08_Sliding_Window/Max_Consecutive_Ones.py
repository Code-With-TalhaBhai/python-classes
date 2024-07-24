

def longestOnes(nums, k: int) -> int:
    l = 0
    r = 0

    maxOnes = 0
    numZeros = 0

    while r < len(nums):

        if nums[r] == 0:
            numZeros += 1

        while numZeros > k:
            if nums[l] == 0:
                numZeros -= 1
            l += 1

        maxOnes = max(maxOnes,(r-l)+1)
        r += 1
        # print(maxOnes)

    return maxOnes




nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(longestOnes(nums,k))