from collections import deque

# Supports all four operations
# 1. Push_back
# 2. Push_front
# 3. Pop_front
# 4. Pop_back


queue = deque([435,643,634,634345,6,346])


queue.append(5)
queue.appendleft(4)
queue.appendleft(3)
queue.appendleft(5324)
queue.append(6)
queue.popleft()

queue.pop()

print(list(queue))