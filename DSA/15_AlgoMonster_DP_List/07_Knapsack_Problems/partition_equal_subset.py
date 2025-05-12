


from xml.etree.ElementInclude import include


def canPartition(nums) -> bool:
    n = len(nums)

    total = sum(nums)
    if total % 2 == 1:
        return False
    
    mid = total // 2

    def check(i,sum):
        if i == n or sum > mid:
            return False

        if sum == mid:
            return True
        
        include = check(i+1,sum+nums[i])
        if include:
            return True
        exclude = check(i+1,sum)
        return include or exclude

        # return check(i+1,sum+nums[i]) or check(i+1,sum)
    return check(0,0)


nums1 = [1,5,11,5]
nums2 = [1,2,3,5]

print(canPartition(nums1))
print(canPartition(nums2))