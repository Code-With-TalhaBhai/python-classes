
nums = [5,2,3,1,4,54,5474,4,98]

def partition(arr,start,end):
  pivot = end
  for i in range(start,end):
    if arr[i] >= arr[end]:
      pivot -= 1

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
    return pivot - 1

  return pivot



def quick_sort1(arr,start,end):
  if start >= end:
    return

  pivot = partition(arr,start,end)
  quick_sort1(arr,start,pivot)
  quick_sort1(arr,pivot+1,end)


def quick_sort2(arr):
  if len(arr) <= 1:
      return arr
  else:
      pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
      left = [x for x in arr if x < pivot]  # Elements less than pivot
      middle = [x for x in arr if x == pivot]  # Elements equal to pivot
      right = [x for x in arr if x > pivot]  # Elements greater than pivot
      return quick_sort2(left) + middle + quick_sort2(right)  # Recursively sort


# quick_sort1(nums,0,len(nums)-1)
# print(nums)


sorted_arr = quick_sort2(nums)
print(sorted_arr)