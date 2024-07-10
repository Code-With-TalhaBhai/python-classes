
data = [46,32,34,33,43,22,50,44]

def heapify(arr,i,n):
    
    leftChild = (2 * i) + 1
    rightChild = (2 * i) + 2
    largest = i

    # if n = len(n) - 1
    # if leftChild <= n and arr[largest] < arr[leftChild]:
    if leftChild < n and arr[largest] < arr[leftChild]:
        largest = leftChild
    if rightChild < n and arr[largest] < arr[rightChild]:
        largest = rightChild

    if i != largest:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,largest,n)


# heap sort
def kth_largest_element1(data,k):

    # heapify data
    n = len(data)
    for i in range(n//2,-1,-1):
        heapify(data,i,n)


    n -= 1
    for i in range(n,0,-1):
        data[0],data[i] = data[i],data[0]
        heapify(data,0,i)

    # print(data)
    return data[len(data)-k]





def kth_largest_element2(data,k):
    
    # print(data)
    data = [-data[i] for i in range(len(data))]
    # data = [-item for item in data]

    import heapq
    heapq.heapify(data)

    # print(data)

    for i in range(k-1):
        heapq.heappop(data)

    # print(data)
    return abs(heapq.heappop(data))




# With Sorting
k = 3
data1 = data.copy()
print('Kth largest element is: ',kth_largest_element1(data1,k))


# Without Sorting
k = 3
data2 = data.copy()
print('Kth largest element is: ',kth_largest_element2(data2,k))
