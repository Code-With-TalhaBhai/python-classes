

arr = [170,24,75,90,802,24,2,66]

def counting_sort(arr):
    max_num = max(arr)

    count_arr = [0] * (max_num+1)
    result_arr = [0] * len(arr)

    for item in arr:
        count_arr[item] += 1

    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(arr)):
        specified_idx = count_arr[arr[i]]-1
        result_arr[specified_idx] = arr[i]
        count_arr[arr[i]] -= 1
    return result_arr


def radix_sort(arr):
    max_num = max(arr)
    no_of_digits = 0
    while max_num > 0:
        max_num /= 10
        no_of_digits += 1


    for digit in range(no_of_digits):
        for i in range(len(arr)):
            item = str(arr[i])

            if len(item) < no_of_digits:
                



radix_sort(arr)