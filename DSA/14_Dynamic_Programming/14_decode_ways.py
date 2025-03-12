


# def decode_ways1(s):
#     n = len(s)

#     # def decode1(i):
#     #     if i >= n:
#     #         return 1

#     #     if s[i] == '0':
#     #         return 0

#     #     if i == n-2 and int(s[i]) <= 2 and int(s[i+1]) <= 6:
#     #         return 2
        
#     #     return decode1(i+1) + decode1(i+2)
#     # return decode1(0)


#     def decode2(s):
#         if s == "":
#             return 1


#         if len(s) == 1:
#             if s[0] == '0':
#                 return 0
#             else:
#                 return 1
        
#         if s[0] == '0':
#             return 0

#         if int(s[0]) > 2 or int(s[1]) > 6:
#             return decode2(s[1:])

#         # if len(s) == 2:
#         #     if int(s[0]) <= 2 and int(s[1]) 
#         # <= 6 and s[1] != '0': 
#         #         return 2
#         #     else: 
#         #         return 1
            
#         return decode2(s[1:]) + decode2(s[2:])
#     return decode2(s)


def decode_ways(s):
    n = len(s)
    if s[0] == '0':
        return 0
    
    if n == 1:
        return 1

    def decode(i):
        if i == n - 1:
            if s[i] == '0':
                return 0
            else:
                return 1
            
        a = s[i]
        a += s[i+1]

        if s[i] == '0':
            return 1 - decode(i+1)
        elif a <= '26':
            return 1 + decode(i+1)
        else:
            return decode(i+1)
        
    return decode(0)
            
        

def decode_ways4(s):
    n = len(s)
    if s[0] == '0':
        return 0
    if n == 1:
        return 1
    
    dp = [1 for i in range(n)]
    dp[0] = 1
    dp[1] = 1

    for i in range(1,n):
        if s[i] == '0':
            dp[i] = dp[i-1] - 1
        elif s[i-1] <= '2' and s[i] <= '6' and s[i-1] != '0':
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    return dp[n-1]


s1 = "12"
s2 = "226"
s3 = "06"
s4 = "122016"
s5 = "10"
s6 = "123123"
s7 = "2611055971756562"
s8 = "2101"

print(decode_ways(s1))
print(decode_ways(s2))
print(decode_ways(s3))
print(decode_ways(s4))
print(decode_ways(s5))
print(decode_ways(s6))
print(decode_ways(s7))
print(decode_ways(s8))
print()
print(decode_ways4(s1))
print(decode_ways4(s2))
print(decode_ways4(s3))
print(decode_ways4(s4))
print(decode_ways4(s5))
print(decode_ways4(s6))
print(decode_ways4(s7))
print(decode_ways4(s8))


