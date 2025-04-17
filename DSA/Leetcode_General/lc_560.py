


def subarraySum1(nums, k: int) -> int:
    n = len(nums)
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            if sum == k:
                cnt += 1
    return cnt


def subarraySum2(nums, k: int) -> int:
    n = len(nums)
    cnt = 0
    occurence = {0:1}
    prefix_sum = 0

    for i in range(n):
        prefix_sum += nums[i]

        if prefix_sum - k in occurence:
            cnt += occurence[prefix_sum-k]

        if prefix_sum not in occurence:
            occurence[prefix_sum] = 1
        else:
            occurence[prefix_sum] += 1

    return cnt





nums = [1,2,3]
print('brute-force')
print(subarraySum1(nums,3))
print('Optimized')
print(subarraySum2(nums,3))
print(subarraySum2([1],0))

