


def jump_game(nums):
    n = len(nums)
    maxi = 0


    for i in range(n):
        if i > maxi:
            return False
        maxi = max(maxi,i+nums[i])
        # if maxi >= n: # Optimizations
        #     return True
    return True


print(jump_game([2,3,1,1,4]))