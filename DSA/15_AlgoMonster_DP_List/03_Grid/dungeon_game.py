


def calculateMinimumHP1(dungeon):
    rows = len(dungeon)
    cols = len(dungeon[0])


    dp = [[float("inf") for i in range(cols+1)] for i in range(rows+1)]
    dp[rows-1][cols] = 1
    dp[rows][cols-1] = 1


    # for r in range(rows-1,-1,-1):
    #     for c in range(cols-1,-1,-1):
    #         curr_elem = dungeon[r][c]
    #         min_hp = min(dp[r+1][c],dp[r][c+1])

    #         if curr_elem <= 0:
    #             dp[r][c] = min_hp + abs(curr_elem)
    #         elif curr_elem > 0:
    #             if curr_elem >= min_hp:
    #                 dp[r][c] = 1
    #             else:
    #                 dp[r][c] = min_hp - curr_elem


    for r in range(rows-1,-1,-1):
        for c in range(cols-1,-1,-1):
            min_hp = min(dp[r+1][c],dp[r][c+1])
            dp[r][c] = max(min_hp-dungeon[r][c],1)
    return dp[0][0]


def calculateMinimumHP2(dungeon):
    rows = len(dungeon)
    cols = len(dungeon[0])

    dp = [float("inf") for i in range(cols+1)]
    dp[cols-1] = 1

    for r in range(rows-1,-1,-1):
        for c in range(cols-1,-1,-1):
            min_hp = min(dp[c],dp[c+1])
            dp[c] = max(1,min_hp-dungeon[r][c])
    return dp[0]


dungeon1 = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon2 = [[0]]
dungeon3 = [[-1,1]]


print(calculateMinimumHP1(dungeon1))
print(calculateMinimumHP1(dungeon2))
print(calculateMinimumHP1(dungeon3))
print()
print(calculateMinimumHP2(dungeon1))
print(calculateMinimumHP2(dungeon2))
print(calculateMinimumHP2(dungeon3))