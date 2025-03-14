


def decode_ways1(s):
    n = len(s)
    memo = {n: 1}

    def decode(i):
        #     return 1
        if i in memo:
            return memo[i]
        if s[i] == '0':
            return 0
        

        memo[i] = decode(i+1)

        if i + 2 <= n and s[i] != '0' and s[i:i+2] <= '26':
            memo[i] += decode(i+2)

        # memo[i] = count
        return memo[i]

    return decode(0)


def decode_ways2(s):
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


    




s1 = "12"
s2 = "226"
s3 = "06"


print(decode_ways1(s1))
print(decode_ways1(s2))
print(decode_ways1(s3))
print()
print(decode_ways2(s1))
print(decode_ways2(s2))
print(decode_ways2(s3))