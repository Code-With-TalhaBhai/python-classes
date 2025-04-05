


def remove_last_set_bit_1(num):

    temp = 1
    while not(num & temp):
        temp = temp << 1

    res = num  & ~(temp)
    return res



def remove_last_set_bit_2(num):
    
    prev = num - 1  # As the number after prev, changes the set bit and whole remains same
    res = num & prev
    return res

print('With Loop')
print(remove_last_set_bit_1(12)) # 1100->1000(By removing last set bit it becomes 8)
print(remove_last_set_bit_1(8)) # 1000->0000(By removing last set bit it becomes 0)
print('More Optimized, Without Loop')
print(remove_last_set_bit_2(12)) # 1100->1000(By removing last set bit it becomes 8)
print(remove_last_set_bit_2(8)) # 1000->0000(By removing last set bit it becomes 0)
