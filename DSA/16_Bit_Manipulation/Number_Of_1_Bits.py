


def hammingWeight(n):
    
    set_bits = 0
    while n != 0:
        n = n & (n-1)
        set_bits += 1
    return set_bits







print(hammingWeight(11))
print(hammingWeight(128))