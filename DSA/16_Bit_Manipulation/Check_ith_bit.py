


def check_ith_bit(num,i):
    
    # With left-shift operator
    if num & (1 << i):
        return 1
    else:
        return 0

    # With right-shift operator
    # if (num >> i) & 1:
    #     return 1
    # else:
    #     return 0 


print(check_ith_bit(13,1)) # 1101 -> 1 bit is 1 (starting from 0 right)
print(check_ith_bit(8,3)) # 1000 -> 3 bit is 1