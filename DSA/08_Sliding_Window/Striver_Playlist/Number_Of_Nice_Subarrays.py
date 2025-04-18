

def no_of_nice_subarrays1(nums,k):
    n = len(nums)
    cnt = 0

    for i in range(n):
        check = 0
        for j in range(i,n):
            if nums[j] % 2 == 1:
                check += 1
            if check == k:
                cnt += 1
    return cnt



def no_of_nice_subarrays2(nums,k):
    n = len(nums)

    def nice_subarrays(goal):
        sum = 0
        cnt = 0
        l = 0
        for r in range(n):
            sum += nums[r] % 2
            while sum > goal:
                sum -= nums[l] % 2
                l += 1
            cnt += r - l + 1                
        return cnt

    return nice_subarrays(k) - nice_subarrays(k-1)

    



nums1 = [1,1,2,1,1]
nums2 = [2,2,2,1,2,2,1,2,2,2]


print('Brute-force')
print(no_of_nice_subarrays1(nums1,3))
print(no_of_nice_subarrays1(nums2,2))
print('Sliding Window')
print(no_of_nice_subarrays2(nums1,3))
print(no_of_nice_subarrays2(nums2,2))