


def num_trees1(n,dp={0:1,1:1}):
    if n in dp:
        return dp[n]
    
    sum = 0
    for j in range(1,n+1):
        sum += num_trees1(j-1) * num_trees1(n-j)
    dp[n] = sum
    return dp[n]




def num_trees2(n):
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1

    for i in range(2,n+1):
        for j in range(1,i):
            dp[i] += dp[j]*dp[i-j]
    return dp[n]


print('Memoization')
print(num_trees1(3))
print(num_trees1(1))
print('Bottom-Up DP')
print(num_trees2(3))
print(num_trees2(1))