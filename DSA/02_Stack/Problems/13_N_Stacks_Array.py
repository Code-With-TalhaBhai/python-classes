N = 3
S = 7

# x -> value to add
# m -> to add in which stack
stack = [-1 for i in range(S)]
top = [-1 for i in range(N)]
next = [i+1 for i in range(S)]
next[S-1] = -1
freespot = 0


def push(x,m):
    global freespot
    # print(freespot)
    if freespot == -1:
        print("Stack Overflow")
        return False
    
    # stack[freespot] = x
    # next[freespot] = top[m-1]
    # top[m-1] = freespot
    # freespot = next[freespot]
    index = freespot
    top[m-1] = index
    freespot = next[index]
    next[index] = freespot
    stack[index] = x
    return True


def pop(m): 
    global freespot
    if top[m-1]==-1:
        return -1
    
    # index = top[m-1]
    # top[m-1] = next[index]
    # next[index] = freespot


    # freespot = index
    # stack[index] = -1
    # return stack[index]

    index = top[m-1]
    next[index] = freespot
    freespot = index
    stack[index] = -1





push(1,1)
push(2,1)
push(3,1)
# push(4,2)
pop(1)
# pop(1)
# push(6,2)
# push(7,3)


print('stack',stack)
print('next',next)
print('freespot',freespot)
