

nums = [5,2,3,1,4,54,5474,4,98]


def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

        # print(arr)


selection_sort(nums)
print(nums)