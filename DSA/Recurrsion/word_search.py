

def word_search(board,word):
    start_char = word[0]
    starting_points = []
    m = len(board)
    n = len(board[0])
    visited = set()

    def search(coordinates,char_idx):
        if len(word) == char_idx:
            return True

        i,j = coordinates
        visited.add(coordinates)
        down,right,left,up = i+1,j+1,j-1,i-1
        new_char_idx = char_idx + 1
        if (down < m) and board[down][j] == word[char_idx] and (down,j) not in visited: #down
            if search((down,j),new_char_idx):
                return True
            # visited.remove((down,j))
        if (right < n) and board[i][right] == word[char_idx] and (i,right) not in visited : #right
            if search((i,right),new_char_idx):
                return True
            # visited.remove((i,right))
        if (left > -1) and board[i][left] == word[char_idx] and (i,left) not in visited: # left
            if search((i,left),new_char_idx):
                return True
            # visited.remove((i,left))
        if (up > -1 and board[up][j] == word[char_idx]) and (up,j) not in visited: #up
            if search((up,j),new_char_idx):
                return True
            # visited.remove((up,j))

        visited.remove((i,j))
        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == start_char:
                starting_points.append((i,j))

    for i in range(len(starting_points)):
        if search(starting_points[i],1):
            return True
        # visited.clear()
        
    return False
    



board1 = [
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]
]
word1 = "ABCCED"

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"

board4 = [["C","A","A"],
["A","A","A"],
["B","C","D"]]
word4 = "AAB"

board5 = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
word5 = "ABCESEEEFS"

print(word_search(board1,word1))
print(word_search(board2,word2))
print(word_search(board3,word3))
print(word_search(board4,word4))
print(word_search(board5,word5))