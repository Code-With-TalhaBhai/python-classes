import heapq



data1 = [44,32,34,33,43,22,50,46]
heapq.heapify(data1) # by-default it makes min-heap
print(data1)
heapq.heappop(data1)
print(data1)

heapq.heappush(data1,45)
heapq.heappush(data1,11)
print("Min Heap: ",data1)
# print(data1)


# Max-Heap is undocumented use your own implementation, just for testing
data3 = [46,32,34,33,43,22,50,44]
heapq._heapify_max(data3)
heapq._heappop_max(data3)
print("Max-Heap: ",data3)
