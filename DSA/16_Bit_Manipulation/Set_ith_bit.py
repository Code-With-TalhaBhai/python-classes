



def set_ith_bit(num,i):

    res = num | (1 << i)
    return res









print(set_ith_bit(13,1)) # 1101 -> 1111 (when we change 1th bit it becomes 15)
print(set_ith_bit(8,2)) # 1000 -> 1100 (when we change 2th bit it becomes 12)