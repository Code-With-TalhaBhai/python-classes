


def numSubarraysWithSum1(nums, goal: int) -> int:
    n = len(nums)
    cnt = 0
    sum = 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            if sum == goal:
                cnt += 1
    return cnt




def numSubarraysWithSum2(nums, goal: int) -> int:
    n = len(nums)
    cnt = 0
    prefix_sum = 0
    occurence = {0:1}

    for i in range(n):
        prefix_sum += nums[i]
        if prefix_sum - goal in occurence:
            cnt += occurence[prefix_sum-goal]
        
        if prefix_sum in occurence:
            occurence[prefix_sum] += 1
        else:
            occurence[prefix_sum] = 1
    return cnt



def numSubarraysWithSum3(nums, goal: int) -> int:
    n = len(nums)

    def find_goal(k):
        if k < 0:
            return 0
        
        cnt = 0
        sum = 0
        l = 0
        for r in range(n):
            sum += nums[r]
            while sum > k:
                sum -= nums[l]
                l += 1 
            cnt += r - l + 1
            print(cnt)
        return cnt
    return find_goal(goal) - find_goal(goal-1)


nums = [1,0,1,0,1]
print('brute-force')
print(numSubarraysWithSum1(nums,2))
print('Optimal-> Dictionary(HashMap)')
print(numSubarraysWithSum2(nums,2))
print('Optimized-> Sliding Window')
print(numSubarraysWithSum3(nums,2))
print(numSubarraysWithSum3([0,0,0,0,0],0))
