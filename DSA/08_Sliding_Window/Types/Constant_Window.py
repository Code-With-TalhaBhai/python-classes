


def constantWindow(nums,k):
    n = len(nums)
    maxSum = 0

    for i in range(k):
        maxSum += nums[i]

    j = k
    sum = maxSum
    while j < n:
        sum += nums[j]
        sum -= nums[j-k]
        maxSum = max(sum,maxSum)
        j += 1
    return maxSum

nums = [1,2,3,4,5,6,1]
print(constantWindow(nums,4))
