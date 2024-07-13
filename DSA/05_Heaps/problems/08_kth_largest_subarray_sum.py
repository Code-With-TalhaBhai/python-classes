
import heapq

def heapify(arr,i,n):

    leftChild = (i*2)+1
    rightChild = (i*2)+2

    largest = i

    if leftChild < n and arr[largest] < arr[leftChild]:
        largest = leftChild 
    if rightChild < n and arr[largest] < arr[rightChild]:
        largest = rightChild 

    if i != largest:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,largest,n) 


def heap_sort(arr):
    
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,i,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)


def kth_largest_subarray_sum1(arr,k):

    sub_arr_sum = []
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
        sub_arr_sum.append(sum)

    heap_sort(sub_arr_sum)
    print(sub_arr_sum)
    return sub_arr_sum[n-k]    


def kth_largest_subarray_sum2(arr,k):
    
    subarr_minheap = []
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]

        if len(subarr_minheap) < k:
            heapq.heappush(subarr_minheap,sum)
        else:
            if subarr_minheap[0] < sum:
                heapq.heappop(subarr_minheap)
                heapq.heappush(subarr_minheap,sum)

    # print(subarr_minheap)
    return subarr_minheap[0]
        





arr = [1,2,3,4,5]
k = 3
# Not Space optimised -> sorting additional heap space required
print("The kth largest subarray sum is: ",kth_largest_subarray_sum1(arr,k))
# With Space Optimization
print("The kth largest subarray sum is: ",kth_largest_subarray_sum2(arr,k))


