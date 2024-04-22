

def next_smaller_element(v):
    stack = []
    stack.append(-1)
    top = stack[-1]
    index = len(v)
    for item in reversed(v):

        index = index - 1
        top = stack[-1]
        if top == -1:
            stack.append(item)


        if item > top:
            v[index] = top

        if item<top:
            stack.pop()
            v[index] = stack[-1]
            stack.append(item)



def next_nearest_smaller_element(v):
    stack = []
    stack.append(-1)
    top = stack[-1]
    index = len(v)

    for item in reversed(v):
        index = index - 1
        top = stack[-1]

        while(item<top):
            stack.pop()
            top = stack[-1]

        v[index] = top
        stack.append(item)



def next_nearest_greater_element(v):
    index = len(v)
    stack = []

    for item in reversed(v):
        index = index - 1
        # top = stack[-1]

        if stack and item > stack[-1]:
            stack.pop()
        
        if not stack:
            stack.append(item)
            v[index] = 0
        else:
            v[index] = stack[-1]
            stack.append(item)



def next_nearest_smaller_element_from_left(v):
    stack = [-1]
    index = 0
    for item in v:
        top = stack[-1]

        while item < top:
            stack.pop()
            top = stack[-1]

        v[index] = top
        stack.append(item)
        index = index + 1



def next_nearest_greater_element_from_left(v):
    stack = []
    index = 0

    for item in v:
        if stack and item > stack[-1]:
            stack.pop()
        
        if not stack:
            stack.append(item)
            v[index] = 0
        else:
            v[index] = stack[-1]
            stack.append(item)
        
        index = index + 1




v = [8,3,1,6,2,9,3]
print(v)
next_smaller_element(v)
print("Next Smaller Element")
print(v)

print()
print()

v = [5,3,1,9,6,5,3] # [3,1,-1,6,3,-1]
print(v)
print("Next Nearest Smaller Element")
next_nearest_smaller_element(v)
print(v)

print()
print()

v = [5,6,1,6,9,15,3]
print(v)
print("Next Nearest Greater Element")
next_nearest_greater_element(v)
print(v)

print()
print()

v = [8,3,1,6,2,9,3]
next_nearest_smaller_element_from_left(v)
print("Next Nearest Smaller Element From Left")
print(v)

print()
print()

v = [8,3,1,6,2,9,3]
next_nearest_greater_element_from_left(v)
print("Next Nearest Greater Element From Left")
print(v)
