
# Solved - Time Limit Exceeded
def jump_game(nums,idx):
    # print(idx)
    max_jump = nums[idx]
    if idx + max_jump >= len(nums)-1:
        return True

    for i in range(1,max_jump+1):
        if jump_game(nums,idx+i):
            return True

    return False


nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
nums3 = [2,0,0]
nums4 = [2,5,0,0]
nums5 = [1,2,0,1]
nums6 = [3,0,8,2,0,0,1]
nums7 = [3,0,8,3,0,0,1,1,1,1,2,3]

print(jump_game(nums1,0))
print(jump_game(nums2,0)) 
print(jump_game(nums3,0))
print(jump_game(nums4,0))
print(jump_game(nums5,0))
print(jump_game(nums6,0))
print(jump_game(nums7,0))