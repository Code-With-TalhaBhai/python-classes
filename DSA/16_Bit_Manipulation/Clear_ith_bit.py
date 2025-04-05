


def clear_ith_bit(num,i):
    
    res = num & ~(1 << i)
    return res



print(clear_ith_bit(13,2)) # 1101 -> 1001 (when we clear 2th bit it becomes 9)
print(clear_ith_bit(8,3)) # 1000 -> 0000 (when we clear 3th bit it becomes 0)
