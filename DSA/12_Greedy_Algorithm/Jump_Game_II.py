



def jump_game_ii_recurrsive(nums):
    n = len(nums)

    def jmp(i):
        if i >= n-1:
            return 0
        
        mini = float('inf')
        for j in range(1,nums[i]+1):
            if i + j < n:
                mini = min(mini,1 + jmp(i+j))
        return mini
    return jmp(0)


def jump_game_ii_optimized(nums):
    n = len(nums)
    l,r = 0,0
    jumps = 0

    while r < n - 1:
        farthest = 0
        while l <= r:
            farthest = max(farthest,l+nums[l])
            l += 1
        l = r + 1
        r = farthest
        jumps += 1
    return jumps





print(jump_game_ii_recurrsive([2,3,1,1,4]))
print(jump_game_ii_recurrsive([2,3,0,1,4]))
print()
print(jump_game_ii_optimized([2,3,1,1,4]))
print(jump_game_ii_optimized([2,3,0,1,4]))