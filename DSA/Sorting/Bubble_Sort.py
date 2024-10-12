

nums = [5,2,3,1,4,54,5474,4,98]


def bubble_sort1(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
        # for j in range(n-i-1): # Optimized
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        # print(arr)
    # return arr[:]


def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1,0,-1):     
        # for j in range(n-1,i-0,-1): # Optimized
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
        print(arr)


bubble_sort1(nums)
print(nums)

# bubble_sort2(nums)
# print(nums)