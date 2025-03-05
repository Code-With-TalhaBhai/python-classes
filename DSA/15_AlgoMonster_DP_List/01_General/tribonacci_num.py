


def tribonacci1(n,memo):
    if n in memo:
        return memo[n]
    
    memo[n] = tribonacci1(n-1,memo) + tribonacci1(n-2,memo) + tribonacci1(n-3,memo)
    return memo[n]


def tribonacci2(n):
    tab = [0] * (n+1)
    if n <= 1:
        return n

    tab[1] = 1
    tab[2] = 1

    if n > 2:
        for i in range(3,n+1):
            tab[i] = tab[i-1] + tab[i-2] + tab[i-3]

    return tab[n]



print(tribonacci1(4,{0:0,1:1,2:1}))
print(tribonacci1(25,{0:0,1:1,2:1}))

print(tribonacci2(4))
print(tribonacci2(25))