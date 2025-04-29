


def stoneGameVII_1(stones):
    n = len(stones)
    prefix_sum = [0 for i in range(n+1)]

    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + stones[i]

    def get_sum(i,j):
        return prefix_sum[j] - prefix_sum[i]
    

    memo = {}
    def game(i,j):
        if i >= j:
            return 0
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        left = get_sum(i+1,j) - game(i+1,j)
        right = get_sum(i,j-1) - game(i,j-1)

        # left = (prefix_sum[j] - prefix_sum[i+1]) - game(i+1,j)
        # right = (prefix_sum[j-1] - prefix_sum[i]) - game(i,j-1)
        memo[(i,j)] = max(left,right)
        return memo[(i,j)]
    return game(0,n)


def stoneGameVII_2(stones):
    n = len(stones)
    prefix_sum = [0 for i in range(n+1)]

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(n-i+1):
            ...






stones1 = [5,3,1,4,2]
stones2 = [7,90,5,1,100,10,10,2]

print(stoneGameVII_1(stones1))
print(stoneGameVII_1(stones2))
print()
print(stoneGameVII_2(stones1))
print(stoneGameVII_2(stones2))