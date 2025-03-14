


def decode_ways1(s):
    n = len(s)

    def decode(i):
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        

        count = decode(i+1)

        if i + 2 <= n and s[i] != '0' and s[i:i+2] <= '26':
            count += decode(i+2)

        return count
    return decode(0)
            

def decode_ways2(s):
    n = len(s)
    memo = {n: 1}

    # 1st way
    # def decode(i):
    #     if i in memo:
    #         return memo[i]
    #     if s[i] == '0':
    #         return 0
        

    #     count = decode(i+1)

    #     if i + 2 <= n and s[i] != '0' and s[i:i+2] <= '26':
    #         count += decode(i+2)

    #     memo[i] = count
    #     return memo[i]


    # 2nd way 
    def decode(i):
        if i in memo:
            return memo[i]
        if s[i] == '0':
            return 0
        

        memo[i] = decode(i+1)

        if i + 2 <= n and s[i] != '0' and s[i:i+2] <= '26':
            memo[i] += decode(i+2)
        return memo[i]
    return decode(0)


def decode_ways3(s):
    n = len(s)
    if s[0] == '0':
        return 0
    

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1


    for i in range(2,n+1):
        if s[i-1] != '0':
            dp[i] = dp[i-1]

        if s[i-2:i] >= '10' and s[i-2:i] <= '26':
            dp[i] += dp[i-2]

    return dp[n]



def decode_ways4(s):
    n = len(s)
    if s[0] == '0':
        return 0
    
    subprev = 1
    prev = 1

    for i in range(2,n+1):
        curr = 0

        if s[i-1] != '0':
            curr = prev


        if s[i-2:i] >= '10' and s[i-2:i] <= '26':
            curr += subprev

        subprev = prev
        prev = curr

    return prev
            
    
    


s1 = "12"
s2 = "226"
s3 = "06"
s4 = "122016"
s5 = "10"
s6 = "123123"
s7 = "2611055971756562"
s8 = "2101"

print('With Recurrsion')
print(decode_ways1(s1))
print(decode_ways1(s2))
print(decode_ways1(s3))
print(decode_ways1(s4))
print(decode_ways1(s5))
print(decode_ways1(s6))
print(decode_ways1(s7))
print(decode_ways1(s8))

print('With Memoization')
print(decode_ways2(s1))
print(decode_ways2(s2))
print(decode_ways2(s3))
print(decode_ways2(s4))
print(decode_ways2(s5))
print(decode_ways2(s6))
print(decode_ways2(s7))
print(decode_ways2(s8))


print('With Tabulation')
print(decode_ways3(s1))
print(decode_ways3(s2))
print(decode_ways3(s3))
print(decode_ways3(s4))
print(decode_ways3(s5))
print(decode_ways3(s6))
print(decode_ways3(s7))
print(decode_ways3(s8))


print('Space-Optimized')
print(decode_ways4(s1))
print(decode_ways4(s2))
print(decode_ways4(s3))
print(decode_ways4(s4))
print(decode_ways4(s5))
print(decode_ways4(s6))
print(decode_ways4(s7))
print(decode_ways4(s8))


