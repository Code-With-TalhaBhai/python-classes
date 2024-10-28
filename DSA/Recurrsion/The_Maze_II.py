

from itertools import count


def countPath(maze,src,dest):
    
    m = len(maze)
    n = len(maze[0])
    srcX,srcY = src
    destX,destY = dest
    count = [0]

    def find_path(i,j):
        down,right,left,up = i+1,j+1,j-1,i-1
        if i == destX and j == destY and (up == -1 or maze[up][j] == 1) and (left == -1 or maze[i][left] == 1) and (right == n or maze[i][right] == 1) and (down == m or maze[down][j] == 1) :
            return True
        
        count[0] += 1
        maze[i][j] = 1
        
        if down < m and maze[down][j] == 0:
            if find_path(down,j):
                return True
        if right < n and maze[i][right] == 0:
            if find_path(i,right):
                return True
        if left > -1 and maze[i][left] == 0:
            if find_path(i,left):
                return True
        if up > -1 and maze[up][j] == 0:
            if find_path(up,j):
                return True
            
        maze[i][j] = 0
        return False

    if find_path(srcX,srcY):
        return count[0]
    else:
        return False


# 0 - allowed(path)
# 1 - not allowed(obstacle)
maze1 = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]
]
start1 = [0,4]
destination1 = [4,4]


maze2 = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]
]
start2 = [0,4]
destination2 = [3,2]

maze3 = [
    [0,0,0,0,0],
    [1,1,0,0,1],
    [0,0,0,0,0],
    [0,1,0,0,1],
    [0,1,0,0,0]
]
start3 = [4,3]
destination3 = [0,1]


print(countPath(maze1,start1,destination1)) # True
print(countPath(maze2,start2,destination2)) # False
print(countPath(maze3,start3,destination3)) # False