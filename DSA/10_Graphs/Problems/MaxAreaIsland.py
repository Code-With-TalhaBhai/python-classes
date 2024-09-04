# leetcode 695
def maxAreaOfIsland(grid):
    maxArea = 0
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])

    def dfs(row,col,area):
        if row == no_of_rows or row < 0 or col < 0 or col == no_of_cols or grid[row][col] == 0:
            return
        
        grid[row][col] = 0
        area[0] += 1
        dfs(row+1,col,area)
        dfs(row,col+1,area)
        dfs(row,col-1,area)
        dfs(row-1,col,area)

    for row in range(no_of_rows):
        for col in range(no_of_cols):
            if grid[row][col] == 1:
                area = [0]
                dfs(row,col,area)
                maxArea = max(maxArea,area[0])
    return maxArea




grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]


print(maxAreaOfIsland(grid))
