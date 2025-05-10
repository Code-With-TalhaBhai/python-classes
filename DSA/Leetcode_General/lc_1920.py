

def buildArray(nums):
    n = len(nums)
    for i in range(n):
        nums[i] = (nums[nums[i]] % n) * n + nums[i]

    for i in range(n):
        nums[i] = nums[i] // n
    return nums


nums = [0,2,1,5,3,4]
print(buildArray(nums))