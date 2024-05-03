N = 3
S = 7

# x -> value to add
# m -> to add in which stack
stack = [0 for i in range(S)]
top = [-1 for i in range(N)]
next = [i+1 for i in range(S)]
next[S-1] = -1
freespot = 0


def push(x,m):
    # print(freespot)
    if freespot == -1:
        return False
    
    stack[freespot] = x
    next[freespot] = top[m-1]
    top[m-1] = freespot
    freespot = next[freespot]
    return True


def pop(m): 
    if top[m-1]==-1:
        return -1
    
    index = top[m-1]
    top[m-1] = next[index]
    next[index] = freespot
    freespot = index

    return stack[index]