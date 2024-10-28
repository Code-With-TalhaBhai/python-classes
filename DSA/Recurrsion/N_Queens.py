

def n_queens(n):
    board = [["."]*n for i in range(n)]
    final = []

    def under_attack(row,col):
        # checking for row
        for i in range(col-1,-1,-1):
            if board[row][i] == "Q":
                return True
            
        # check for col
        for j in range(row-1,-1,-1):
            if board[j][col] == "Q":
                return True


        # checking for main-diagonal
        # main_diagonal = row - col
        i,j = row,col
        while i > -1 and j > -1:
            if board[i][j] == "Q":
                return True
            i -= 1
            j -= 1
            

        # # checking for secondary-diagonal
        # # secondary_diagonal = row + col
        i,j = row,col
        while i > -1 and j < n:
            if board[i][j] == "Q":
                return True
            i -= 1
            j += 1

        return False



    def place_queen(row):
        if row >= n:
            output = []
            for i in range(len(board)):
                output.append(''.join(board[i]))
            final.append(output)
            return

        for col in range(len(board)):
            if not under_attack(row,col):
                board[row][col] = "Q"
                place_queen(row+1)
                board[row][col] = "."


    place_queen(0)
    return final

print(n_queens(4))
# print(n_queens(3))
# print(n_queens(2))