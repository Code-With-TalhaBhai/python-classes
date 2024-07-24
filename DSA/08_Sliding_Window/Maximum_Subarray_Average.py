
def findMaxAverage(nums, k: int) -> float:
    
    sum = 0
    max_avg = 0.0
    
    for i in range(k):
        sum += nums[i]

    max_avg = sum / k

    for i in range(k,len(nums)):
        sum += nums[i]
        sum -= nums[i-k]
        max_avg = max(max_avg,sum/k)
            
    return max_avg







nums = [1,12,-5,-6,50,3]
k = 4


print(findMaxAverage(nums,k))