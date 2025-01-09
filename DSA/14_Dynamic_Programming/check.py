

def helper1(nums):
    n = len(nums)
    res = [0]
    def help(i,curr,total):
        if i == n or nums[i] < curr:
            return 
        
        if nums[i] > curr:
            res[0] = max(res[0],total)

        help(i+1,nums[i],total+1)
        help(i+1,curr,total)

    help(0,float("-inf"),0)
    return res[0]



def helper2(nums):
    n = len(nums)

    def help(i,curr):
        if i == n:
            return 0
        
        if curr > nums[i]:
            return help(i+1,curr)
        
        return 1 + max(help(i+1,nums[i]),help(i+1,curr))
    

    return help(0,float("-inf"))



nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]
print(helper1(nums1))
print(helper1(nums2))
print(helper1(nums3))
print()
print(helper2(nums1))
print(helper2(nums2))
print(helper2(nums3))