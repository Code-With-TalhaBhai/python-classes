

def heapify(data,i,n):

    leftChild = (2 * i) + 1
    rightChild = (2 * i) + 2
    largest = i

    if leftChild < n and data[leftChild] > data[largest]:
        largest = leftChild
    if rightChild < n and data[rightChild] > data[largest]:
        largest = rightChild

    if i != largest:
        data[i],data[largest] = data[largest],data[i]
        heapify(data,largest,n)


def MaxHeap(data):
    
    n = len(data)
    for i in range(n//2,-1,-1):
        heapify(data,i,n)



def mergeHeaps():

    a = [6,5,4]
    b = [12,7,2]
    c = a + b
    
    MaxHeap(c)
    return c


print(mergeHeaps())