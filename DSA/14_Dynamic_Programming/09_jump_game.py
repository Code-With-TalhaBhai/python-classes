


def jump_game1(nums):
    n = len(nums)

    def jump(i):
        if i == n-1:
            return True
        
        if nums[i] == 0:
            return False
        
        for j in range(i+1,i+nums[i]+1):
            if jump(j):
                return True
        
        return False
    return jump(0)



def jump_game2(nums):
    n = len(nums)
    memo = {n-1:True}

    def jump(i):
        if i in memo:
            return memo[i]
        
        # if i == n-1:
        #     return True

        # if nums[i] == 0:
            # return False
        
        for j in range(i+1,i+nums[i]+1):
            memo[j] = jump(j)
            if memo[j] == True:
                return True


        memo[i] = False
        return False
    return jump(0)



def jump_game3(nums):
    n = len(nums)
    goal = n-1

    for i in range(n-2,-1,-1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False




nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

# Recurrsive
print(jump_game1(nums1))
print(jump_game1(nums2))

# Memoization -> Top-Down
print(jump_game2(nums1))
print(jump_game2(nums2))


# Tabulation -> Bottom-Up
print(jump_game3(nums1))
print(jump_game3(nums2))