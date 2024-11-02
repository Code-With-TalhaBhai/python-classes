

def sortedSquares(nums):
    n = len(nums)
    res = []

    i,j = 0,n-1

    while i <= j:
        first_square = nums[i]**2
        second_square = nums[j]**2

        if first_square >= second_square:
            res.insert(0,first_square)
            i += 1
        elif second_square >= first_square:
            res.insert(0,second_square)
            j -= 1  
    return res

    # More Opimize
    # while i <= j:
    #     first_square = nums[i]**2
    #     second_square = nums[j]**2

    #     if first_square >= second_square:
    #         res.append(first_square)
    #         i += 1
    #     elif second_square >= first_square:
    #         res.append(second_square)
    #         j -= 1  
    # return res[::-1] # reverse array


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))