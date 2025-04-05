

def convertToBase7(num: int) -> str:
    ans = ''
    
    base_7 = num
    if num < 0:
        base_7 = abs(base_7)

    while base_7 != 0:
        rem = base_7 % 7
        base_7 = base_7 // 7
        ans = str(rem) + ans

    return '-' + ans if num < 0 else ans


print(convertToBase7(100))
print(convertToBase7(-7))