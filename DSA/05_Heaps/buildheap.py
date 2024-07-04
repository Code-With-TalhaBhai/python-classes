


def heapify1(arr,n,i):

    # index starting from zero
    leftChild = (2 * i) + 1
    rightChild = (2 * i) + 2
    largest = i

    if leftChild < n and arr[largest] < arr[leftChild]:
        largest = leftChild
    if rightChild < n and arr[largest] < arr[rightChild]:
        largest = rightChild

    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify1(arr,n,largest)

    

def heapify2(arr,n,i):

    leftChild = 2 * i
    rightChild = (2 * i) + 1

    largest = i

    if leftChild < n and arr[largest] < arr[leftChild]:
        largest = leftChild
    if rightChild < n and arr[largest] < arr[rightChild]:
        largest = rightChild

    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify2(arr,n,largest)





# Array to heap
arr : list[int|None] = [50,55,53,52,54]

# With zero-index
n = len(arr)
for i in range((n//2)-1,-1,-1):
    heapify1(arr,n,i);
for item in arr:
    print(item,end=" ")
print()


# With one-index
arr.insert(0,None)
for i in range(n//2,0,-1):
    heapify2(arr,n,i)

for i in range(1,len(arr)):
    print(arr[i],end=" ")
print()

    

