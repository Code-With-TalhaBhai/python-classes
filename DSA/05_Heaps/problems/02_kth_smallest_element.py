

def heapify(data,i,n):

    leftChild = (2 * i) + 1
    rightChild = (2 * i) + 2
    largest = i

    if leftChild < n and data[leftChild] > data[i]:
        largest = leftChild
    if rightChild < n and data[rightChild] > data[i]:
        largest = rightChild

    if i != largest:
        data[i],data[largest] = data[largest],data[i]
        heapify(data,largest,n)


def MaxHeap(data):
    
    n = len(data)
    for i in range(n//2,-1,-1):
        heapify(data,i,n)


def DeleteHeap(data):
    n = len(data)-1

    data[0],data[n] = data[n],data[0]
    data.pop()
    MaxHeap(data)


    



def kth_smallest_element1(data,k):
    data.sort()

    return data[k-1]


def kth_smallest_element2(data,k):
    
    max_data_heap = data[:k]
    MaxHeap(max_data_heap) #Maxi-Heap

    for i in range(k,len(data)):
        if max_data_heap[0] > data[i]:
            DeleteHeap(max_data_heap)
            max_data_heap.append(data[i])
            MaxHeap(max_data_heap)


    return max_data_heap[0]



k = 4
data = [46,32,34,33,43,22,50,44]
data1 = data.copy()
data2 = data.copy()

# With Sorting
print("Kth smallest element is: ",kth_smallest_element1(data1,k))
# Without Sorting
print("Kth smallest element is: ",kth_smallest_element2(data2,k))
