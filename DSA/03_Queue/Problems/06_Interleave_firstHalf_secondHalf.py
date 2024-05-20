from queue import Queue

# Using Queue
ans_Queue = Queue()
arr = [11,12,13,14,15,16,17,18,19,20]
# arr = [1,2,3,4]
half = int(len(arr)/2)


for i in range(half):
    ans_Queue.put(arr[0])
    arr.pop(0)


while(not ans_Queue.empty()):
    arr.append(ans_Queue.get())
    val = arr.pop(0)
    arr.append(val)

print('Using Queue',arr)



# Using Two Stacks
arr = [11,12,13,14,15,16,17,18,19,20]
half = int(len(arr)/2)
stack = []
newStack =  []
for i in range(half):
    stack.append(arr[0])
    arr.pop(0)


while(len(stack)>0):
    newStack.append(stack[-1])
    stack.pop()


while len(newStack)>0:
    arr.append(newStack[-1])
    newStack.pop()
    val = arr.pop(0)
    arr.append(val)

print('Using two stack ',arr)



# Using Single Stack
arr = [11,12,13,14,15,16,17,18,19,20]
half = int(len(arr)/2)

stack = []

for i in range(half):
    stack.append(arr[0])
    arr.pop(0)


while len(stack) > 0:
    val = stack.pop()
    arr.append(val)

for i in range(half):
    val = arr.pop()
    arr.insert(0,val)


for i in range(half):
    val = arr.pop(0)
    stack.append(val)


while len(stack) > 0:
    arr.append(stack[-1])
    stack.pop()
    val = arr.pop(0)
    arr.append(val)


print("Using Single Stack",arr)



