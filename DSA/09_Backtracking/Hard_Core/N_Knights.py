

def n_knights(n):
    board = [["."]*n for i in range(n)]
    final = []


    def under_attack(row,col):
        
        single_neg_row = row-1
        double_neg_row = row-2

        single_neg_col = col-1
        double_neg_col = col-2
        single_pos_col = col+1
        double_pos_col = col+2


        if (single_neg_row > -1 and ((double_neg_col > -1 and board[single_neg_row][double_neg_col] == "K") or (double_pos_col < n and board[single_neg_row][double_pos_col]=="K"))):
            return True
        
        if (double_neg_row > -1 and ((single_neg_col > -1 and board[double_neg_row][single_neg_row] == "K") or (single_pos_col < n and board[double_neg_row][single_pos_col] == "K"))):
            return True


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
                board[row][col] = "K"
                place_queen(row+1)
                board[row][col] = "."


    place_queen(0)
    return final



print(n_knights(4))