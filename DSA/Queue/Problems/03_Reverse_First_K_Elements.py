from collections import deque


queue = deque([1,2,3,4,5])
k = 3
stack = []

for i in range(0,k):
    top = queue.popleft()
    stack.append(top)

# print(stack)
print(i)

while stack:
    top = stack.pop()
    # print(top)
    queue.append(top)


for j in range(i,len(queue)-1):
    top = queue.popleft()
    queue.append(top)

print(list(queue))
# print(len(queue))
