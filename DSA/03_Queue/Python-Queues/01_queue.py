from queue import Queue


# put -> put an element into the queue if size is full wait for freeslot
# get -> remove an element and get value of deleted element

q = Queue(maxsize=4)

q.put(1)
q.put(2)
q.put(3)
# q.put(4)

top1 = q.get()
top2 = q.get()


print(q.empty())
print(q.full())
# print(q.qsize())
print(top1)
print(top2)