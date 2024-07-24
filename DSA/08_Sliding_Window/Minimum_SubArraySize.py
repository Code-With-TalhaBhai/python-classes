
# imp -> greater than or equal to target
def minSubArrayLen(target: int, nums) -> int:
    l = r = 0
    # minSubArrayWindow = len(nums)
    minSubArrayWindow = float("inf")
    sum = 0

    while r < len(nums):    
        sum += nums[r]
        while sum > target:
            minSubArrayWindow = min(minSubArrayWindow,(r-l)+1)
            sum -= nums[l]
            l += 1

        r += 1   
    
    return int(minSubArrayWindow) if minSubArrayWindow < float("inf") else 0



target = 7
nums = [2,3,1,2,4,3]
# nums = [1,1,1,1,1,1,1,1]
# nums = [1,2,3,4,5]


print(minSubArrayLen(target,nums))
