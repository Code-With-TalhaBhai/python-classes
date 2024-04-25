# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

def prev_smaller(heights):
    same_heights = heights.copy()
    # stack = [-1]
    stack = []
    for index,items in enumerate(same_heights):
        start = index
        while stack and same_heights[stack[-1]] > items:
            stack.pop()
        
        if stack and same_heights[stack[-1]] <= items:
            start = stack[-1]
            
        
        stack.append(start)
        heights[index] = stack[-1]
        # return same_heights
        # print(heights[stack[-1]])
        # print(stack)



def next_smaller(heights):
    same_heights = heights.copy()
    stack = []
    index = len(heights)
    
    for items in reversed(heights):
        index = index - 1
        start = index
        # print(index)
        
        while stack and same_heights[stack[-1]] >= items:
            stack.pop()
        
        if stack and same_heights[stack[-1]] <= items:
            start = stack[-1]
            
        stack.append(start)
        heights[index] = stack[-1]



histogram = [2,1,5,6,2,3] # [0,1,1,1,1,1]
# histogram = [999,999,999,999]
prev_smaller(histogram)
print(histogram)

histogram = [2,1,5,6,2,3] # [0,1,1,1,1,1]
print(histogram)

next_smaller(histogram) # [1,1,4,4,4,5]
print(histogram)