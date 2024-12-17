

arr = [3,4,7,3,2,5,7,3,2,3,0]
# arr = [4,9,2,4,7,6]
# arr = [4,9,2,4,0,7,6]



def counting_sort(arr):
    max_num = max(arr)

    count_arr = [0] * (max_num+1)
    result_arr = [0] * len(arr)

    for item in arr:
        count_arr[item] += 1

    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]
    print(count_arr)

    for i in range(len(arr)):
        specified_idx = count_arr[arr[i]]-1
        result_arr[specified_idx] = arr[i]
        count_arr[arr[i]] -= 1

        # result_arr[count_arr[arr[i]]-1] = arr[i]
        # count_arr[arr[i]] -= 1

    return result_arr


print(counting_sort(arr))
