

from collections import deque


def orangesRotting(grid):
    no_of_rows = len(grid) 
    no_of_cols = len(grid[0])
    count = [-1]
    visited = set()

    # def dfs(i,j,vis_count):
    #     if i < 0 or i == no_of_rows or j < 0 or j == no_of_cols or grid[i][j] == 0 or grid[i][j] == 3:
    #         return 
        
    #     grid[i][j] = 3
    #     if vis_count not in visited:
    #         count[0] += 1
    #     visited.add(vis_count)

    #     dfs(i+1,j,vis_count+1)
    #     dfs(i,j+1,vis_count+1)
    #     dfs(i,j-1,vis_count+1)
    #     dfs(i-1,j,vis_count+1)

    # check = False
    # for i in range(no_of_rows):
    #     for j in range(no_of_cols):
    #         if grid[i][j] == 2:
    #             check = True
    #             dfs(i,j,0)
    #             # print(i," ",j)
    #             break
    #     if check == True:
    #         break
    # # dfs(0,0,0)
    # return count[0]


    # BFS
    dq = deque()
    fresh_oranges = 0
    total_time = -1
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            if grid[i][j] == 2:
                dq.append((i,j))
            if grid[i][j] == 1:
                fresh_oranges += 1

    if fresh_oranges == 0:
        return 0

    while dq:
        n = len(dq)
        total_time += 1
        # fresh_oranges -= 1
        for _ in range(n):
            i,j = dq.popleft()

            # Shorter-Code
            for r,c in [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]:
                if r >= 0 and r < no_of_rows and c >= 0 and c < no_of_cols and grid[r][c] == 1:
                    dq.append((r,c))
                    fresh_oranges -= 1
                    grid[r][c] = 2

            # if i+1 >= 0 and i+1 < no_of_rows and j >= 0 and j < no_of_cols and grid[i+1][j] == 1:
            #     dq.append((i+1,j))
            #     fresh_oranges -= 1
            #     grid[i+1][j] = 2

            # if i >= 0 and i < no_of_rows and j+1 >= 0 and j+1 < no_of_cols and grid[i][j+1] == 1:
            #     dq.append((i,j+1))
            #     fresh_oranges -= 1
            #     grid[i][j+1] = 2

            # if i >= 0 and i < no_of_rows and j-1 >= 0 and j-1 < no_of_cols and grid[i][j-1] == 1:
            #     dq.append((i,j-1))
            #     fresh_oranges -= 1
            #     grid[i][j-1] = 2

            # if i-1 >= 0 and i-1 < no_of_rows and j >= 0 and j < no_of_cols and grid[i-1][j] == 1:
            #     dq.append((i-1,j))
            #     fresh_oranges -= 1
            #     grid[i-1][j] = 2



    if fresh_oranges == 0:
        return total_time
    else:
        return -1


grid1 = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[0,2]]
print(orangesRotting(grid1))
print(orangesRotting(grid2))