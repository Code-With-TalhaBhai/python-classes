
# 1. Without DP -> Recurrsion Backtracking


def climbStairs1a(n: int) -> int:
    if n == 1 or n == 2:
        return n 
    return climbStairs1a(n-1) + climbStairs1a(n-2)


def climbStairs1b(n,i=0):
    # def climb_stairs(i):
    #     if i == n:
    #         return 1
    #     if i > n:
    #         return 0    
    #     return climb_stairs(i+1) + climb_stairs(i+2)
    # return climb_stairs(0)

    if i == n:
        return 1
    if i > n:
        return 0
    
    return climbStairs1b(n,i+1) + climbStairs1b(n,i+2)


def climbStairsc1c(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    return climbStairsc1c(n-1) + climbStairsc1c(n-2)



# 2. Top-Down Approach (Memoization)
def climbStairs2(n):
    memoize = {
        1 : 1,
        2 : 2
    }

    def climb(i):
        # if i == 1 or i == 2: # with empty memoize = {}
        #     return i

        # with 1,2 key defined in memoize
        if i in memoize:
            return memoize[i]

        memoize[i] = climb(i-1) + climb(i-2)
        return memoize[i]
    return climb(n)





# 3. Bottom-up approach(Tabulation)
def climbStairs3(n):
    if n <= 2:
        return n

    # 1st way
    # dp = [0,1,2]
    # for i in range(3,n+1):
    #     new = dp[i-1] + dp[i-2]
    #     dp.append(new)

    # 2nd way
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]


# 4. Bottom-up No-memory DP
def climbStairs4(n):
    if n <= 2:
        return n

    prev1 = 2
    prev2 = 1
    curr = n

    for i in range(2,n):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr


print('Recurrsion')
print(climbStairs1a(5))
print(climbStairs1b(5))
print(climbStairsc1c(5))
print('Memoization->Top Down')
print(climbStairs2(5))
print('Tabulation->Bottom up')
print(climbStairs3(5))
print('No-memory Dp')
print(climbStairs4(5))