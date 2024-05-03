from queue import Queue

q = Queue()

# print(len(abc))

# for item in abc:
#     q.put(int(item))

q.put(46)
q.put(6)
q.put(47)
q.put(6)
q.put(8)

def print_q(q):
    while(q.empty() is not True):
        print(q.get(),end=" ")
    print()



# Using Recurrsion
# def queue_reversal():
#     while q.empty():
#         return
#     top = q.get()
#     queue_reversal()
#     # print(top)
#     q.put(top)

# queue_reversal()

# Using Stack
arr = []
while q.empty() is not True:
    arr.append(q.get())

print(arr)
while(arr):
    top = arr.pop()
    q.put(top)


print_q(q)