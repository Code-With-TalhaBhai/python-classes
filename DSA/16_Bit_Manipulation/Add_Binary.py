


def add_binary1(a,b):
    carry = 0
    x = len(a) - 1
    y = len(b) - 1
    res = ''

    while x >= 0 or y >= 0 or carry == 1:
        sum = carry
        if x >= 0:
            sum += int(a[x])
        if y >= 0:
            sum += int(b[y])

        # if sum == 0:
        #     res = '0' + res
        #     carry = 0
        # elif sum == 1:
        #     res = '1' + res
        #     carry = 0
        # elif sum == 2:
        #     res = '0' + res
        #     carry = 1
        # elif sum == 3:
        #     res = '1' + res
        #     carry = 1

        bit = '0'
        if sum == 1:
            bit = '1'
            carry = 0
        elif sum == 2:
            bit = '0'
            carry = 1
        elif sum == 3:
            bit = '1'
            carry = 1
        
        res = bit + res
        x -= 1
        y -= 1
    return res


def add_binary2(a,b):
    
    a = int(a,2)
    b = int(b,2)



    while b != 0:
        carry = a & b
        a = a ^ b #(Without Carry)
        b = carry << 1
    return bin(a)[2:]




a1 = "11"
b1 = "1"
a2 = "1010"
b2 = "1011"

print('Without Bitwise-Operators')
print(add_binary1(a1,b1))
print(add_binary1(a2,b2))
print('With Bitwise-Operators')
print(add_binary2(a1,b1))
print(add_binary2(a2,b2))