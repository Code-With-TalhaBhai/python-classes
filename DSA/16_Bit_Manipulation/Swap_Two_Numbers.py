



a = 45
b = 15


a = a ^ b
b = a ^ b  # b = (a^b)^b = a ^ (b ^ b) = a
a = a ^ b  # a = (a^b)^b = (a ^ b) ^ a = (a ^ a) ^ b = b

# After, we swapped two numbers
print(a,b)