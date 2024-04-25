# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

def prev_smaller(heights):
    stack = []
    for index,items in enumerate(heights):
        
        while stack and stack[-1] > items:
            stack.pop()
        
        while stack and stack[-1] < items:
            items = stack[-1]
            
        
        stack.append(items)
        heights[index] = stack[-1]



def next_smaller(heights):
    stack = []
    index = len(heights)
    
    for items in reversed(heights):
        index = index - 1
        # print(index)
        
        while stack and stack[-1] > items:
            stack.pop()
        
        while stack and stack[-1] < items:
            items = stack[-1]
            
        stack.append(items)
        heights[index] = stack[-1]



histogram = [2,1,5,6,2,3]
prev_smaller(histogram)
print(histogram)

histogram = [2,1,5,6,2,3]
print(histogram)

next_smaller(histogram)
print(histogram)










# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

def prev_smaller(heights):
    stack = []
    for index,items in enumerate(heights):
        start = index
        while stack and heights[stack[-1]] > items:
            stack.pop()
        
        while stack and heights[stack[-1]] < items:
            start = stack[-1]
            
        
        stack.append(start)
        heights[index] = stack[-1]



def next_smaller(heights):
    stack = []
    index = len(heights)
    
    for items in reversed(heights):
        index = index - 1
        # print(index)
        
        while stack and stack[-1] > items:
            stack.pop()
        
        while stack and stack[-1] < items:
            items = stack[-1]
            
        stack.append(items)
        heights[index] = stack[-1]



histogram = [2,1,5,6,2,3] # [0,1,1,1,1,1]
prev_smaller(histogram)
print(histogram)

histogram = [2,1,5,6,2,3]
print(histogram)

next_smaller(histogram)
print(histogram)