# In binary, we can only calculate multiple of number which is x * (2 ^ k)


x = 7
print(x * 1,x << 0) # 1 === 2 ^ 0 
print(x * 2,x << 1) # 2 === 2 ^ 1
print(x * 4,x << 2)
print(x * 8,x << 3)
print(x * 16,x << 4)

