from collections import defaultdict

def sudoko_solver(board):
    n = len(board)
    already_filled = defaultdict(bool)
    num_col = defaultdict(list)
    num_row = defaultdict(list)
    block = [] # multi-d Array

    for row in range(n):
        if len(block) <= row // 3:
            block.append([])
        for col in range(n):
            if len(block[row//3]) <= col//3:
                block[row//3].append([])
            item = board[row][col]
            if item != ".":
                already_filled[(row,col)] = True
                num_row[row].append(item)
                num_col[col].append(item)
                block[row//3][col//3].append(item)


    def valid(row,col,num):
        if num not in num_row[row] and num not in num_col[col] and num not in block[row//3][col//3]:
            return True
        return False


    def solve(row,col):
        # print(row," ",col)
        if row == n:
            # return 
            return True

        if col == n:
            # if solve(row+1,0):
            #     return True
            # return False
            return solve(row+1,0) # Optimization
        
        if already_filled[(row,col)]:
            # if solve(row,col+1):
            #     return True
            # return False
            return solve(row,col+1) # Opimization

        for i in range(1,n+1):
            # print(i)
            item = str(i)
            if valid(row,col,item):
                board[row][col] = item
                num_row[row].append(item)
                num_col[col].append(item)
                block[row//3][col//3].append(item)
                if solve(row,col+1):
                    return True
                num_row[row].pop()
                num_col[col].pop()
                block[row//3][col//3].pop()
                board[row][col] = "."
        return False

    solve(0,0)



board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

sudoko_solver(board)
# print(board)

for i in range(len(board)):
    print(board[i])