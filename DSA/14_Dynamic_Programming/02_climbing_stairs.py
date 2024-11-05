
# 1. Without DP -> Recurrsion Backtracking
from pydoc import cli


def climbStairs1(n: int) -> int:
    if n == 1 or n == 2:
        return n 

    return climbStairs1(n-1) + climbStairs1(n-2)


# 2. Top-Down Approach (Memoization)

def climbStairs2(n):
    memoize = {}

    def climb(i):
        if i == 1 or i == 2:
            return i

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



print(climbStairs1(5))
print(climbStairs2(5))
print(climbStairs3(5))
print(climbStairs4(5))