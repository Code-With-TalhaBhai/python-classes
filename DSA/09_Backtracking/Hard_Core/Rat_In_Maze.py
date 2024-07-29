
maze1 = [
    [1, 0, 0, 0],
    [1, 1, 0, 1], 
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

maze2 = [
    [1, 0, 0, 0],
    [1, 1, 0, 1], 
    [1, 1, 0, 0],
    [1, 1, 1, 1]
]

maze3 = [
    [1,0],
    [1,0]
]

maze4 = [
    [0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1],
    [0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1],
    [0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1],
    [0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1]
]


def search_maze1(maze):
    maze_paths = []
    n = len(maze)

    if (maze[0][0] == 0):
        return [-1]

    visited_maze = []
    for i in range(n):
        visited_maze.append([0]*n)


    # DLRU -> chronologically
    def backtrack(x,y,path):
        if x == n-1 and y == n-1:
            maze_paths.append(path)
            return    

        visited_maze[x][y] = 1
        # DLRU -> chronologically
        if x < n-1 and maze[x+1][y] == 1 and visited_maze[x+1][y] == 0:
            path += "D"
            backtrack(x+1,y,path)
            # backtrack(x+1,y,path+"D") # can also be done by this way, so you dont' need to add or pop the string
            path = path[:-1]

        if y > 0 and maze[x][y-1] == 1 and visited_maze[x][y-1] == 0: 
            path += "L"
            backtrack(x,y-1,path)
            # backtrack(x,y-1,path+"L") # can also be done by this way, so you dont' need to add or pop the string
            path = path[:-1]

        if y < n-1 and maze[x][y+1] == 1 and visited_maze[x][y+1] == 0:
            path += "R"
            backtrack(x,y+1,path)
            # backtrack(x,y+1,path+"R") # can also be done by this way, so you dont' need to add or pop the string
            path = path[:-1]

        if x > 0 and maze[x-1][y] == 1 and visited_maze[x-1][y] == 0:
            path += "U"
            backtrack(x-1,y,path)
            # backtrack(x-1,y,path+"U") # can also be done by this way, so you dont' need to add or pop the string
            path = path[:-1]


        visited_maze[x][y] = 0    
        
    backtrack(0,0,"")
    return maze_paths if maze_paths else [-1]
        

def search_maze2(maze):
    maze_paths = []
    n = len(maze)

    if (maze[0][0] == 0):
        return [-1]

    def backtrack(x,y,path):
        if x == n-1 and y == n-1:
            maze_paths.append(path)
            return
        
        # if x < 0 or x == n or y < 0 or y == n:
        #     return
        
        # DLRU -> chronologically
        if x < n-1 and maze[x+1][y] == 1:
            maze[x][y] = 0
            backtrack(x+1,y,path+"D")
            maze[x][y] = 1

        if y > 0 and maze[x][y-1] == 1:
            maze[x][y] = 0
            backtrack(x,y-1,path+"L")
            maze[x][y] = 1

        if y < n-1 and maze[x][y+1] == 1:
            maze[x][y] = 0
            backtrack(x,y+1,path+"R")
            maze[x][y] = 1

        if x > 0 and maze[x-1][y] == 1:
            maze[x][y] = 0
            backtrack(x-1,y,path+"U")
            maze[x][y] = 1

    backtrack(0,0,"")
    return maze_paths if maze_paths else [-1]




# Extra Visited Array
print(search_maze1(maze1))
# print(search_maze1(maze2))
# print(search_maze1(maze3))
# print(search_maze1(maze4))


# Without Visited Array
print(search_maze2(maze1))
# print(search_maze2(maze4))
