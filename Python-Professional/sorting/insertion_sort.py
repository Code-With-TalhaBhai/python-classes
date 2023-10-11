
arr = [9,8,0,7,5,6,4,2,3,1];
print(arr)


def insertion_sort(array):

    for i in range(1,len(array)):
        min = array[i]
        j = i-1
        while min < array[j] and j>=0:
            array[j+1] = array[j]
            j-=1
        array[j+1] = min

insertion_sort(arr)
print(arr)