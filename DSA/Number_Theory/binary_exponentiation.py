


a = 2
b = 8
# b = 9
res = 1

while b > 0:
    if b % 2 == 1:
        res *= a

    a *= a
    b = b // 2


print(res)