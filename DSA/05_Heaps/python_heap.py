import heapq



data1 = [44,32,34,33,43,22,50,46]
heapq.heapify(data1) # by-default it makes min-heap
print(data1)
heapq.heappop(data1)
print(data1)

heapq.heappush(data1,45)
heapq.heappush(data1,11)
print("Min Heap: ",data1)
print(data1)
print()

data2 = [44,32,34,33,43,22,50,46]
data2 = [-num for num in data2]
heapq.heapify(data2) # by-default it makes min-heap
heapq.heappop(data2)
heapq.heappush(data2,-45)
heapq.heappush(data2,-11)
data2 = [-num for num in data2]
print("Max Heap: ",data2)
print()


# Max-Heap is undocumented use your own implementation, just for testing
data3 = [46,32,34,33,43,22,50,44]
heapq._heapify_max(data3)
heapq._heappop_max(data3)
print("Max-Heap: ",data3)
