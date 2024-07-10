

def heapify(arr,j,n):
    
    leftChild = (2 * j) + 1
    rightChild = (2 * j) + 2

    largest = j

    if leftChild < n and arr[largest] < arr[leftChild]:
        largest = leftChild
    if rightChild < n and arr[largest] < arr[rightChild]:
        largest = rightChild

    if j != largest:
        arr[j],arr[largest] = arr[largest],arr[j]
        heapify(arr,largest,n)


# Fake Heap-sort own solution
# def heap_sort(arr):
#     n = len(arr)
#     for i in range(len(arr)):
#         for j in range((n//2)-1,-1,-1):
#             heapify(arr,j,n)
#         n -= 1
#         arr[0],arr[n] = arr[n],arr[0]


# Real Heap-Sort
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,i,n) # Build Heap


    for i in range(n-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i) # min to max
        # heapify(arr,0,n) # max to min


arr : list[int] = [50,55,53,52,54]
# arr : list[int] = [5,1,1,2,0,0]
heap_sort(arr)


for items in arr:
    print(items,end=" ")
print()



