



def divide_two_integers(dividend,divisor):
    if dividend == 0:
        return 0
    
    signed = False
    if dividend < 0 and divisor > 0:
        signed = True
    elif dividend > 0 and divisor < 0:
        signed = True

    dividend = abs(dividend)
    divisor = abs(divisor)

    ans = 0
    while dividend >= divisor:
        cnt = 0
        while (divisor << cnt + 1) < dividend:
            cnt += 1
        dividend -= (divisor << cnt)
        ans += 1 << cnt


        res = -ans if signed == True else ans 
        # out of bound values - constraint max value stored can be 2 ^ 31 and -2 ^ 31
        if res > (1 << 31) - 1:
            return (1 << 31) - 1 # max-integer value
        if res < -(1 << 31) - 1:
            return -(1 << 31) - 1 # min-integer value
        
        return res


print(divide_two_integers(10,3))
print(divide_two_integers(7,-3))
print(divide_two_integers(57,1))