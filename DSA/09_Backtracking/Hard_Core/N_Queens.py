

def N_Queens1(n):
    res,single_pattern = [],[]


    def backtrack(row):
        if row == n:
            res.append(single_pattern.copy())
            return

        for col in range(n):
            queen_place = True
            queen_row = ["."]*n

            check_row = row
            pos_diagonal = col
            neg_diagonal = col
            while check_row > 0: # checking col attack
                check_row -= 1
                neg_diagonal -= 1
                pos_diagonal += 1

                if single_pattern[check_row][col] == "Q":
                    queen_place = False
                    break
                if neg_diagonal > -1 and single_pattern[check_row][neg_diagonal] == "Q":
                    queen_place = False
                    break
                if pos_diagonal < n and single_pattern[check_row][pos_diagonal] == "Q":
                    queen_place = False
                    break

            if queen_place:
                queen_row[col] = 'Q'
                single_pattern.append("".join(queen_row))
                backtrack(row+1)
                queen_row[col] = '.'
                single_pattern.pop()
                queen_place = False
    
    backtrack(0)
    return res


def N_Queens2(n):
    chess_board = [["."]*n for i in range(n)]
    # print(chess_board)
    res,single_pattern = [],[]


    def backtrack(row):
        if row == n:
        # if len(single_pattern) == n:
            res.append(single_pattern.copy())
            return

        for col in range(n):
            queen_place = True

            check_row = row
            pos_diagonal = col
            neg_diagonal = col
            while check_row > 0: # checking col attack
                check_row -= 1
                neg_diagonal -= 1
                pos_diagonal += 1

                if single_pattern[check_row][col] == "Q":
                    queen_place = False
                    break
                if neg_diagonal > -1 and single_pattern[check_row][neg_diagonal] == "Q":
                    queen_place = False
                    break
                if pos_diagonal < n and single_pattern[check_row][pos_diagonal] == "Q":
                    queen_place = False
                    break

            if queen_place:
                # queen_row[col] = 'Q'
                chess_board[row][col] = "Q"
                single_pattern.append("".join(chess_board[row]))
                backtrack(row+1)
                chess_board[row][col] = '.'
                single_pattern.pop()
                queen_place = False
    
    backtrack(0)
    return res


# Optimized Approach using HashMap(Dictionary)
def N_Queens3(n):
    chess_board = [["."]*n for i in range(n)]
    res,single_pattern = [],[]
    import collections
    hashmap_col = collections.defaultdict(bool)
    hashmap_neg_diag = collections.defaultdict(bool)
    hashmap_pos_diag = collections.defaultdict(bool)


    def backtrack(row):
        if row == n:
        # if len(single_pattern) == n:
            res.append(single_pattern.copy())
            return

        for col in range(n):
            queen_place = True
            
            #col and diagonal checking
            # if hashmap_col[col] == True or hashmap_pos_diag[col-row+n-1] == True or hashmap_neg_diag[row+col] == True:
            if hashmap_col[col] == True or hashmap_pos_diag[col-row] == True or hashmap_neg_diag[row+col] == True:
                queen_place = False

            if queen_place:
                chess_board[row][col] = "Q"
                hashmap_col[col] = True
                hashmap_neg_diag[row+col] = True
                hashmap_pos_diag[col-row] = True
                single_pattern.append("".join(chess_board[row]))
                backtrack(row+1)
                chess_board[row][col] = '.'
                hashmap_col[col] = False
                hashmap_neg_diag[row+col] = False
                hashmap_pos_diag[col-row] = False
                # hashmap_pos_diag[col-row+n-1] = False
                single_pattern.pop()  
                queen_place = False

    backtrack(0)
    return res



def N_Queens4(n):
    board = [["."]*n for i in range(n)]
    final = []

    # def under_attack(row,col):
    #     # checking for row
    #     for i in range(col-1,-1,-1):
    #         if board[row][i] == "Q":
    #             return True
            
    #     # check for col
    #     for j in range(row-1,-1,-1):
    #         if board[j][col] == "Q":
    #             return True

    #     # checking for main-diagonal
    #     i,j = row,col
    #     while i > -1 and j > -1:
    #         if board[i][j] == "Q":
    #             return True
    #         i -= 1
    #         j -= 1
            
    #     # # checking for secondary-diagonal
    #     i,j = row,col
    #     while i > -1 and j < n:
    #         if board[i][j] == "Q":
    #             return True
    #         i -= 1
    #         j += 1
    #     return False

    # Optimized
    def under_attack(row,col):
            check_row = row
            pos_diagonal = col
            neg_diagonal = col
            while check_row > 0: # checking col attack
                check_row -= 1
                neg_diagonal -= 1
                pos_diagonal += 1

                if board[check_row][col] == "Q":
                    return True
                if neg_diagonal > -1 and board[check_row][neg_diagonal] == "Q":
                    return True
                if pos_diagonal < n and board[check_row][pos_diagonal] == "Q":
                    return True

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

def N_Queens5(n):
    from collections import defaultdict
    board = [["."]*n for i in range(n)]
    final = []
    col_check = defaultdict(bool)
    main_diag_check = defaultdict(bool)
    sec_diag_check = defaultdict(bool)

    def under_attack(row,col):
        if col_check[col] or main_diag_check[row-col] or sec_diag_check[row+col]:   
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
                board[row][col] = "Q"
                col_check[col] = True
                main_diag_check[row-col] = True
                sec_diag_check[row+col] = True
                place_queen(row+1)
                col_check[col] = False
                main_diag_check[row-col] = False
                sec_diag_check[row+col] = False
                board[row][col] = "."


    place_queen(0)
    return final


n = 4
print(N_Queens1(n))
print(N_Queens2(n))
print(N_Queens3(n)) # Optimized with hashmap
print(N_Queens4(n)) # Optimized with Approach1
print(N_Queens5(n)) # Optimized with Approach3(hashmap)
