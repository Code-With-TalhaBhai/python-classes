


def find_xor(n)->int:

    #brute_force
    # xor = 0
    # for i in range(n+1):
    #     xor ^= i
    # return xor

    #Optimized
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    if n % 4 == 3:
        return 0
    if n % 4 == 0:
        return n
    


def find_xor_in_range(l,r):
    #brute-force
    # xor = 0
    # for i in range(l,r+1):
    #     xor ^= i
    # return xor

    # Optimized
    xor1 = find_xor(l-1)
    xor2 = find_xor(r)
    final_xor = xor1 ^ xor2
    return final_xor



# find xor of range(0,8)
print(find_xor(9))
print(find_xor_in_range(5,9))