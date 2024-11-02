

def twoSum(nums,target):
    i,j = 0,len(nums)-1

    sum = float("inf")
    while sum != target:
        sum = nums[i] + nums[j]
        if sum == target:
            i += 1
            j += 1
        elif sum > target:
            j -= 1
        elif sum < target:
            i += 1

    return [i,j]




numbers1 = [2,7,11,15]
print(twoSum(numbers1,9))

numbers2 = [-1,0]
print(twoSum(numbers2,-1))

numbers3 = [2,3,4]
print(twoSum(numbers3,6))
