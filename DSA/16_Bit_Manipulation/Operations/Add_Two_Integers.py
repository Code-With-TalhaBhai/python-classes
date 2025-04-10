


def sum(num1: int, num2: int) -> int:

    while num2 != 0:
        carry = num1 & num2 # With carry
        num1 = num1 ^ num2  # without_carry
        num2 = (carry << 1) 
    return num1


def sum1(num1: int, num2: int) -> int:
    full_bits = (1 << 32) - 1
    num1 = full_bits & num1
    num2 = full_bits & num2

    while num2 != 0:
        carry = num1 & num2 # With carry
        num1 = num1 ^ num2  # without_carry
        num2 = (carry << 1) & full_bits


     # If the sign bit is set (MSB), convert to negative
    if (num1 >> 31) & 1:
        return ~((~num1) & full_bits)
    else:
        return num1







print(sum(12,7))
print(sum(10,100))
print('to handle negative numbers')
print(sum1(-6,50))
print(sum1(-1,1))