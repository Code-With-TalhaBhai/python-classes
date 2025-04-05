



def isPowerOfTwo(nums):
    if nums == 0:
        return False


    # res = nums & (nums - 1)

    # if res == 0:
    #     return True
    # else:
    #     return False

    return  nums & (nums - 1) == 0









print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))