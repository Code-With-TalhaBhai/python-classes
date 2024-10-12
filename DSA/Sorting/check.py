



nums1 = [5,2,3,1,4,54,5474,4,98]
nums2 = [5,2,3,1,4,54,5474,4,98]


def merge_sort(arr):
    if len(arr) > 1:
        n = len(arr)//2
        left = arr[:n]
        right = arr[n:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print(arr)



def merge_sort2(arr,left,right):
    if left < right:
        mid = (left + right) // 2

        merge_sort2(arr,left,mid)
        merge_sort2(arr,mid+1,right)

        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]

        i = j = 0
        k = left
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def partition(arr,start,end):
    pivot = end
    i = start

    while i < end:
        if arr[i] >= arr[end]:
            pivot -= 1
        i += 1


        if end != pivot:
            arr[end],arr[pivot] = arr[pivot],arr[end]
            i = start
            j = end

            while i < pivot and j > pivot:
                if arr[i] > arr[pivot] and arr[j] < arr[pivot]:
                    arr[i],arr[j] = arr[j],arr[i]

                if arr[i] <= arr[pivot]:
                    i += 1

                if arr[j] > arr[pivot]:
                    j -= 1

        else:
            pivot -= 1

    return pivot



def quick_sort(arr,start,end):

    if start < end:  
        pivot = partition(arr,start,end)

        # quick_sort(arr,start,pivot)
        quick_sort(arr,start,pivot-1)
        quick_sort(arr,pivot+1,end)
    # if start >= end:
    #     return

    # pivot = partition(arr,start,end)
    # quick_sort(arr,start,pivot)
    # quick_sort(arr,pivot+1,end)




# Merge Sort
# merge_sort(nums1)
# print(nums1)
# merge_sort2(nums2,0,len(nums2)-1)
# print(nums2)


# Quick Sort
nums3 = [5,2,3,1,4,54,5474,4,98]
quick_sort(nums3,0,len(nums3)-1)
print(nums3)