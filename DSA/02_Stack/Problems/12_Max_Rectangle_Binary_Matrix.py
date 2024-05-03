
def largest_rectangle_histogram(rectangle):
    maxArea = -1
    stack = []
    for index,items in enumerate(rectangle):
        start = index
        while stack and stack[-1][1]>items:
            i,height = stack.pop()
            maxArea = max(maxArea,height*(index-i))
            start = i
        
        stack.append((start,items))

    while stack:
        i,h = stack.pop()
        maxArea = max(maxArea,h*(len(rectangle)-i))
    
    return maxArea

        



def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    rows = len(matrix)
    rectangle = [int(items) for items in matrix[0]]
    cols = len(rectangle)
    maxArea = largest_rectangle_histogram(rectangle)

    print('rectangle',rectangle)
    for row in range(1,rows): # enumerate
        for col in range(cols):
            if matrix[row][col] == str(0):
                rectangle[col] = 0
            else:
                rectangle[col] = rectangle[col] + int(matrix[row][col])

        print('rectangle',rectangle)
        totalArea = largest_rectangle_histogram(rectangle)
        if(totalArea>maxArea):
            maxArea = totalArea

    return maxArea
                
            
    



matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

print(maximalRectangle(matrix))


