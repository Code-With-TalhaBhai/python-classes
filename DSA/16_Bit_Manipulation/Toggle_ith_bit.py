


def toggle_ith_bit(num,i):
    
    res = num ^ (1 << i)
    return res



print(toggle_ith_bit(13,2)) # 1101 -> 1001 (when we toggle 2th bit it becomes 9)
print(toggle_ith_bit(8,2)) # 1000 -> 1100 (when we toggle 2th bit it becomes 12)