

def uniquePaths1(m: int, n: int) -> int:

    # 1st way
    # paths = [0]
    # def find_paths1(i,j):
    #     if i == m-1 and j == n-1:
    #         paths[0] += 1
    #         return
        
    #     if i == m or j == n:
    #         return
        
    #     # towards bottom
    #     find_paths1(i+1,j)
    #     # towards right
    #     find_paths1(i,j+1)
    # find_paths1(0,0)
    # return paths[0]

    # 2nd way
    # def find_paths2(i,j):
    #     if (i == 0 and j == 0):
    #         return 1

    #     if i < 0 or j < 0:
    #         return 0

    #     return find_paths2(i-1,j) + find_paths2(i,j-1)
    # return find_paths2(m-1,n-1)
    

    def find_paths3(i,j):
        if i == m-1 and j == n-1:
            return 1

        if i >= m or j >= n:
            return 0

        return find_paths3(i+1,j) + find_paths3(i,j+1)
    return find_paths3(0,0)


def uniquePaths2(m,n):

    memo = {(m-1,n-1):1}
    #1st way
    def findPaths(i,j):
        if (i,j) in memo:
            return memo[(i,j)]

        if i >= m or j >= n:
            return 0

        memo[(i,j)] = findPaths(i+1,j) + findPaths(i,j+1)
        return memo[(i,j)]

    findPaths(0,0)
    return memo[(0,0)]


    #2nd way
    # memo = {
    #     (0,0) : 1
    # }
    # def findPaths2(i,j):
    #     if i == m or j == n:
    #         return 

    #     if not(i == 0 and j == 0):
    #         up = 0
    #         left = 0

    #         if (i-1,j) in memo:
    #             up = memo[(i-1,j)]
    #         if (i,j-1) in memo:
    #             left = memo[(i,j-1)]

    #         memo[(i,j)] = up+left


    #     findPaths2(i,j+1)
    #     findPaths2(i+1,j)

    # findPaths2(0,0)
    # return memo[(m-1,n-1)]



def uniquePaths3(m,n):
    dp = []
    for _ in range(m):
        dp.append([0]*n)

    dp[0][0] = 1


    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            top = 0
            left = 0
            
            if i-1 >= 0:
                top = dp[i-1][j]
            if j-1 >= 0:
                left = dp[i][j-1]

            dp[i][j] = top+left

    return dp[m-1][n-1]



def uniquePaths4(m,n):
    memo = {
        (0,0) : 1
    }

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            up = 0
            down = 0

            if (i-1,j) in memo:
                up = memo[(i-1,j)]
            if (i,j-1) in memo:
                down = memo[(i,j-1)]
            memo[(i,j)] = up+down
        
    return memo[(m-1,n-1)]

print('with recurrsion')
print(uniquePaths1(3,7))
print(uniquePaths1(3,2))
print(uniquePaths1(4,4))
print('with memoization')
print(uniquePaths2(3,7))
print(uniquePaths2(3,2))
print(uniquePaths2(4,4))
print('with tabulation')
print(uniquePaths3(3,7))
print(uniquePaths3(3,2))
print(uniquePaths3(4,4))
print('with tabulation + memoization')
print(uniquePaths4(3,7))
print(uniquePaths4(3,2))
print(uniquePaths4(4,4))
