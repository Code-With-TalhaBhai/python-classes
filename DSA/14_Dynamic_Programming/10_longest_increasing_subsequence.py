
# not working yet
def longest_increasing_subbsequence1(nums):
    n = len(nums)

    def helper(i):
        j = i - 1
        if j == -1:
            return 0
        
        total = 1+helper(i-1)

        if nums[i] > nums[j]:
            return 1

        return total

    maxi = float("-inf")
    for i in range(1,n):
        maxi = max(maxi,helper(i))

    return maxi


def longest_increasing_subsequence2(nums):
    n = len(nums)

    maxi = 1
    dp = [1]*n


    # for i in range(1,n):
    #     j = i-1
    #     k = i
    #     while j > -1:
    #         if nums[k] > nums[j]:
    #             nums_len[i] += 1
    #             maxi = max(maxi,nums_len[i])
    #             # print(nums_len)
    #             k = j
    #         j -= 1

    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                # dp[i] += 1
                # maxi = max(maxi,dp[i])
                dp[i] = max(dp[i],dp[j]+1)

    # print(dp)
    return max(dp)
    # return maxi





nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]

# not working yet
# print(longest_increasing_subbsequence1(nums1))
# print(longest_increasing_subbsequence1(nums2))
# print(longest_increasing_subbsequence1(nums3))


print(longest_increasing_subsequence2(nums1))
print(longest_increasing_subsequence2(nums2))
print(longest_increasing_subsequence2(nums3))
