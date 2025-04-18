


from collections import defaultdict
from email.policy import default


def number_of_subarrays_with_k_distinct_elements1(nums,k):
    n = len(nums)
    cnt = 0

    for i in range(n):
        check = {}
        for j in range(i,n):
            check[nums[j]] = True
            if len(check) == k:
                cnt += 1
            elif len(check) > k:
                break
    return cnt
    

def number_of_subarrays_with_k_distinct_elements2(nums,k):
    n = len(nums)

    def subarrays_with_k(q):
        cnt = 0
        check_nums = defaultdict(int)
        l = 0
        for r in range(n):
            check_nums[nums[r]] += 1
            while l < n and len(check_nums) > q:
                check_nums[nums[l]] -= 1
                if check_nums[nums[l]] == 0:
                    check_nums.pop(nums[l])
                l += 1
            cnt += r - l + 1
        return cnt
    return subarrays_with_k(k) - subarrays_with_k(k-1)




nums1 = [1,2,1,2,3]
nums2 = [1,2,1,3,4]

print('brute-force')
print(number_of_subarrays_with_k_distinct_elements1(nums1,2))
print(number_of_subarrays_with_k_distinct_elements1(nums2,3))
print('Optimized-Sliding_Window')
print(number_of_subarrays_with_k_distinct_elements2(nums1,2))
print(number_of_subarrays_with_k_distinct_elements2(nums2,3))