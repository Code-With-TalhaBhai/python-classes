

n = 8
k = 3

next = [i+1 for i in range(n)]
next[n-1] = -1
front = [-1 for i in range(k)]
rear = [-1 for i in range(k)]

arr = [-21 for i in range(n)]


freespot = 0

def push(val,qn):
    global freespot
    if freespot == -1:
        print("No free space available. Queues Overflow")
        return 
    
    
    index = freespot 
    freespot = next[index]
    if front[qn-1] == -1:
        front[qn-1] = index
    next[rear[qn-1]] = index

    rear[qn-1] = index
    arr[index] = val



def pop(qn):
    global freespot

    if front[qn-1] == -1:
        print("Queues Underflow")
        return 
    
    index = front[qn-1]
    front[qn-1] = next[index]
    next[index] = freespot
    freespot = index
    arr[index] = -21


push(1,1)
push(2,1)
push(3,1)
push(5,2)
pop(1)
pop(1)
push(4,2)
# pop(2)
# pop(2)
# push(6,2)
# push(4,1)


print(arr)
    