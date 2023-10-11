
arr = [9,8,0,7,5,6,4,2,3,1];
print(arr)


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            # print(j)
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        # print()


bubble_sort(arr)
print(arr)