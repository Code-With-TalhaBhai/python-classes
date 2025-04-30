


def LIS1(nums):
    n = len(nums)
    memo = {}

    def LIS(i,prev_largest):
        if i == n:
            return 0
        if (i,prev_largest) in memo:
            return memo[(i,prev_largest)]
        
        inc = 0
        if nums[i] > prev_largest:
            inc = 1 + LIS(i+1,nums[i])


        exc = LIS(i+1,prev_largest)
        # return max(inc,exc)
        memo[(i,prev_largest)] = max(inc,exc)
        return memo[(i,prev_largest)]
    return LIS(0,float('-inf'))


def LIS2(nums):
    n = len(nums)
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2,n+1):
    # for i in range(1,n):
        if nums[i-1] > nums[i-2]:
            dp[i] += 1
        dp[i] += dp[i-1]
    return dp[n]



def LIS3(nums):
    n = len(nums)
    lis_arr = [nums[0]]


    for i in range(1,n):
        if nums[i] <= lis_arr[0]:
            lis_arr[0] = nums[i]
        elif nums[i] > lis_arr[-1]: #[10,9,2,5,3,7,101,18]
            lis_arr.append(nums[i])
        else: # binary-search
            lower_bound = 0
            upper_bound = len(lis_arr) - 1

            while lower_bound <= upper_bound:
                mid = (lower_bound + upper_bound) // 2
                if nums[i] > lis_arr[mid]:
                    lower_bound = mid + 1
                else:
                    upper_bound = mid - 1
            lis_arr[lower_bound] = nums[i]
    return len(lis_arr)
    




nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]
nums4 = [4,10,4,3,8,9]
nums5 = [10,9,2,5,3,4]


print('With Recurrsion')
print(LIS1(nums1))
print(LIS1(nums2))
print(LIS1(nums3))
print(LIS1(nums4))
print(LIS1(nums5))
print('With Dynammic Programming')
print(LIS2(nums1))
print(LIS2(nums2))
print(LIS2(nums3))
print(LIS2(nums4))
print(LIS2(nums5))
print('With Binary Search')
print(LIS3(nums1))
print(LIS3(nums2))
print(LIS3(nums3))
print(LIS3(nums4))
print(LIS3(nums5))
print(LIS3([3,5,6,2,5,4,19,5,6,7,12]))