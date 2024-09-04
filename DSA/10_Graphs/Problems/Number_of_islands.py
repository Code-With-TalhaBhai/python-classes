

def numIslands(grid) -> int:
    row_len = len(grid)
    col_len = len(grid[0])

    def dfs(i,j):
        if i < 0 or i == row_len or j < 0 or j == col_len or grid[i][j] == '0':
            return
        else:
            grid[i][j] = '0'

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)


    number_of_islands = 0

    for row in range(row_len):
        for col in range(col_len):
            if grid[row][col] == "1":
                dfs(row,col)
                number_of_islands += 1


    return number_of_islands


grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid1))
print(numIslands(grid2))