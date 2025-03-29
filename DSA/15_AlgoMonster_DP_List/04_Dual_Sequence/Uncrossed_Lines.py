


def maxUncrossedLines1(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    memo = {}

    def uncrossed(i,j):
        if i == m or j == n:
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        if nums1[i] == nums2[j]:
            memo[(i,j)] =  1 + uncrossed(i+1,j+1)
            return memo[(i,j)]
        
        memo[(i,j)] =  max(uncrossed(i+1,j),uncrossed(i,j+1))
        return memo[(i,j)]
    return uncrossed(0,0)


def maxUncrossedLines2(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    curr_dp = [0] * (m+1)
    prev_dp = [0] * (m+1)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if nums1[j-1] == nums2[i-1]:
                curr_dp[j] = prev_dp[j-1] + 1
            else:
                curr_dp[j] = max(curr_dp[j-1],prev_dp[j])
        prev_dp = curr_dp.copy()
        # prev_dp = curr_dp[:]
    return curr_dp[m]



nums1 = [1,4,2]
nums2 = [1,2,4]
nums3 = [2,5,1,2,5]
nums4 = [10,5,2,1,5,2]
nums5 = [1,3,7,1,7,5] 
nums6 = [1,9,2,5,1]

print(maxUncrossedLines1(nums1,nums2))
print(maxUncrossedLines1(nums3,nums4))
print(maxUncrossedLines1(nums5,nums6))
print()
print(maxUncrossedLines2(nums1,nums2))
print(maxUncrossedLines2(nums3,nums4))
print(maxUncrossedLines2(nums5,nums6))
