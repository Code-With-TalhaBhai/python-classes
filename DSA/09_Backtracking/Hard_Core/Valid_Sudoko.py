
# Our task is to determine whether the board is valid according to the rules of Sudoku. We do not need to solve the Sudoku; we just need to validate the existing filled-in cells.



def valid_sudoko(board):
    from collections import defaultdict
    n = len(board)
    row_num = defaultdict(list)
    col_num = defaultdict(list)
    blocks = []

    def in_valid(row,col):
        item = board[row][col]
        if item in row_num[row] or item in col_num[col] or item in blocks[row//3][col//3]:
            return True
        return False

    for row in range(n):
        if len(blocks) == row//3:
            blocks.append([])
        for col in range(n):
            item = board[row][col]
            if len(blocks[row//3]) == col // 3:
                blocks[row//3].append([])
            
            if item != ".":
                if in_valid(row,col):
                    return False
                row_num[row].append(item)
                col_num[col].append(item)
                blocks[row//3][col//3].append(item)
    return True

    

board1 = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

board2 = [
["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]


print(valid_sudoko(board1))
print(valid_sudoko(board2))
# print(board1)
# print(board2)