# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

def prev_smaller(heights):
    same_heights = heights.copy()
    stack = [-1]
    for index,items in enumerate(same_heights):
        start = index
        while stack[-1] != -1 and same_heights[stack[-1]] >= items:
            stack.pop()           
        
        heights[index] = stack[-1]
        stack.append(index)



def next_smaller(heights):
    same_heights = heights.copy()
    stack = [-1]
    index = len(heights)
    
    for items in reversed(heights):
        index = index - 1
    
        while stack[-1] != -1 and same_heights[stack[-1]] >= items:
            stack.pop()
            
        heights[index] = stack[-1]
        stack.append(index)



histogram = [999,999,999,999]
prev_smaller(histogram)
print(histogram)

histogram = [999,999,999,999]
print(histogram)

next_smaller(histogram)
print(histogram)