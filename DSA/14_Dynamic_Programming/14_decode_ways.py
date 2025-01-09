


def decode_ways1(s):
    n = len(s)

    # def decode1(i):
    #     if i >= n:
    #         return 1

    #     if s[i] == '0':
    #         return 0

    #     if i == n-2 and int(s[i]) <= 2 and int(s[i+1]) <= 6:
    #         return 2
        
    #     return decode1(i+1) + decode1(i+2)
    # return decode1(0)


    def decode2(s):
        if s == "":
            return 1


        if len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        
        if s[0] == '0':
            return 0

        if int(s[0]) > 2 or int(s[1]) > 6:
            return decode2(s[1:])

        # if len(s) == 2:
        #     if int(s[0]) <= 2 and int(s[1]) 
        # <= 6 and s[1] != '0': 
        #         return 2
        #     else: 
        #         return 1
            
        return decode2(s[1:]) + decode2(s[2:])
    return decode2(s)


s1 = "12"
s2 = "226"
s3 = "06"
s4 = "122016"
s5 = "10"
s6 = "123123"
s7 = "2611055971756562"

print(decode_ways1(s1))
print(decode_ways1(s2))
print(decode_ways1(s3))
print(decode_ways1(s4))
print(decode_ways1(s5))
print(decode_ways1(s6))
print(decode_ways1(s7))