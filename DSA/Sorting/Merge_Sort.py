
nums = [5,2,3,1,4,54,5474,4,98]



def merge_sort1(array):
    if len(array) > 1:
        m = len(array)//2  
        # Splitting      
        L = array[:m] # Call-by-value
        R = array[m:] # Call-by-value

        merge_sort1(L) # Pass-by-value 
        merge_sort1(R) # Pass-by-value

        # merging
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            # elif R[j] <= L[i]:
            else:
                array[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1



def merge2(arr,left_arr,right_arr):
    i = j = k = 0

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
    

def merge_sort2(array):
    if len(array) > 1:
        mid = len(array)//2
        left_arr = array[:mid]
        right_arr = array[mid:]

        merge_sort2(left_arr)
        merge_sort2(right_arr)

        merge2(array,left_arr,right_arr)



def merge3(arr,left,mid,right):
    
    arr1 = arr[left:mid+1]
    arr2 = arr[mid+1:right+1]

    l = m = 0
    k = left

    while l < len(arr1) and m < len(arr2):
        if arr1[l] < arr2[m]:
            arr[k] = arr1[l]
            l += 1
        else:
            arr[k] = arr2[m]
            m += 1
        k += 1

    while l < len(arr1):
        arr[k] = arr1[l]
        l += 1
        k += 1

    while m < len(arr2):
        arr[k] = arr2[m]
        m += 1
        k += 1


def merge_sort3(array,i,j):
    
    if i < j:
        mid = (i + j) // 2

        merge_sort3(array,i,mid)
        merge_sort3(array,mid+1,j)

        merge3(array,i,mid,j)

        



# merge_sort1(nums)
# print(nums)
# merge_sort2(nums)
# print(nums)
merge_sort3(nums,0,len(nums)-1)
print(nums)