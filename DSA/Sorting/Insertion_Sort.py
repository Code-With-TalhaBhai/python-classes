

nums = [5,2,3,1,4,54,5474,4,98]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0  and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


insertion_sort(nums)
print(nums)