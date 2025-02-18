


def longest_increasing_path_matrix1(matrix):
    m = len(matrix)
    n = len(matrix[0])

    max_len = 0

    def find_length(i,j):
        
        left,left_idx = 1, j-1
        right,right_idx = 1, j+1
        top,top_idx = 1, i-1
        down,down_idx = 1, i+1
        

        # top
        if top_idx >= 0 and j >= 0 and j < n and matrix[top_idx][j] > matrix[i][j]:
            top = 1 + find_length(i-1,j)
        #left
        if left_idx >= 0 and i >= 0 and i < m and matrix[i][left_idx] > matrix[i][j]:
            left = 1 + find_length(i,j-1)
        # right 
        if right_idx < n and i >= 0 and i < m and matrix[i][right_idx] > matrix[i][j]:
            right = 1 + find_length(i,j+1)
        # down
        if down_idx < m and j >= 0 and j < n and matrix[down_idx][j] > matrix[i][j]:
            down = 1 + find_length(i+1,j)

        return max(left,right,top,down)


    for i in range(m):
        for j in range(n):
            max_len = max(max_len,find_length(i,j))
    return max_len



def longest_increasing_path_matrix2(matrix):
    m = len(matrix)
    n = len(matrix[0])

    max_len = 0
    memo = [[-1 for j in range(n)] for i in range(m)]


    def find_length(i,j):
        
        left,left_idx = 1, j-1
        right,right_idx = 1, j+1
        top,top_idx = 1, i-1
        down,down_idx = 1, i+1
        
        if memo[i][j] != -1:
            return memo[i][j]

        # top
        if top_idx >= 0 and j >= 0 and j < n and matrix[top_idx][j] > matrix[i][j]:
            top = 1 + find_length(i-1,j)
        #left
        if left_idx >= 0 and i >= 0 and i < m and matrix[i][left_idx] > matrix[i][j]:
            left = 1 + find_length(i,j-1)
        # right 
        if right_idx < n and i >= 0 and i < m and matrix[i][right_idx] > matrix[i][j]:
            right = 1 + find_length(i,j+1)
        # down
        if down_idx < m and j >= 0 and j < n and matrix[down_idx][j] > matrix[i][j]:
            down = 1 + find_length(i+1,j)

        memo[i][j] =  max(left,right,top,down)
        return memo[i][j]

    for i in range(m):
        for j in range(n):
            max_len = max(max_len,find_length(i,j))
    return max_len

    

def longest_increasing_path_matrix3(matrix):
    m = len(matrix)
    n = len(matrix[0])
    max_len = 0
    memo = {}

    def dfs(i,j,prev_val):
        if i < 0 or i == m or j < 0 or j == n or prev_val >= matrix[i][j]:
            return 0

        if (i,j) in memo:
            return memo[(i,j)] 

        curr_val = matrix[i][j]
        memo[(i,j)] = max(1+dfs(i+1,j,curr_val),1+dfs(i-1,j,curr_val),1+dfs(i,j+1,curr_val),1+dfs(i,j-1,curr_val))
        return memo[(i,j)]

    for i in range(m):
        for j in range(n):
            max_len = max(max_len,dfs(i,j,-1))

    return max_len




matrix1 = [[9,9,4],[6,6,8],[2,1,1]]
matrix2 = [[3,4,5],[3,2,6],[2,2,1]]
matrix3 = [[1]]

print('With Recurrsion')
print(longest_increasing_path_matrix1(matrix1))
print(longest_increasing_path_matrix1(matrix2))
print(longest_increasing_path_matrix1(matrix3))
print('With Memoization')
print(longest_increasing_path_matrix2(matrix1))
print(longest_increasing_path_matrix2(matrix2))
print(longest_increasing_path_matrix2(matrix3))
print('With DFS')
print(longest_increasing_path_matrix3(matrix1))
print(longest_increasing_path_matrix3(matrix2))
print(longest_increasing_path_matrix3(matrix3))