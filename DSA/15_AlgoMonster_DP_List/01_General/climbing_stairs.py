


def climbStairs1(n,memo):
    if n in memo:
        return memo[n]
    
    if n < 0:
        return 0
    
    memo[n] = climbStairs1(n-1,memo) + climbStairs1(n-2,memo)
    return memo[n]


def climbStairs2(n):
    tab = [0] * (n+1)
    tab[1] = 1
    tab[2] = 2

    if n <= 2:
        return n

    for i in range(3,n+1):
        tab[i] = tab[i-1] + tab[i-2]

    return tab[n]
        




print(climbStairs1(2,{0:1}))
print(climbStairs1(3,{0:1}))
print(climbStairs1(6,{0:1}))
print()
print(climbStairs2(2))
print(climbStairs2(3))
print(climbStairs2(6))
