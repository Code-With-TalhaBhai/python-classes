

# incomplete
def find_index(board,letter):

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == letter:
                return [row,col]
        
    return [-1,-1]


def check_exists(board,start_idx):
   ...

def word_search(board,word):
    get_index = find_index(board,word[0])
    if get_index == [-1,-1]:
        return False
    

    while (1):
        if check_exists(board,get_index) == [-1,-1]:
            return False
        else:
            get_index = find_index(board,word[0])
            coordinates = check_exists(board,get_index)






board = [
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]
]
word = "ABCCED"


print(word_search(board,word))