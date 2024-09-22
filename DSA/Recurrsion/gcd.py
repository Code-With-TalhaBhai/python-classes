

def findGCD(nums):
    a,b = min(nums),max(nums)

    # Through loop
    # while a != 0:
    #     a,b = b%a,a
    # return b


    # Through Recurrsion
    def find(a,b):
        if a == 0:
            return b

        return find(b%a,a)


    return find(a,b)





nums1 = [2,5,6,9,10]
nums2 = [7,5,6,8,3]

print(findGCD(nums1))
print(findGCD(nums2))
