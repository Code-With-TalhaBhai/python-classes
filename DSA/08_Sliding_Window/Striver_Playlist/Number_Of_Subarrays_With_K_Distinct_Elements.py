


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
    


nums1 = [1,2,1,2,3]
nums2 = [1,2,1,3,4]

print('brute-force')
print(number_of_subarrays_with_k_distinct_elements1(nums1,2))
print(number_of_subarrays_with_k_distinct_elements1(nums2,3))
print('')