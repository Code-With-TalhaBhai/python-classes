
arr = [170,24,75,3,90,802,24,2,66]


def counting_sort(arr,exp):
    n = len(arr)

    count_arr = [0] * 10

    for item in arr:
        digit = (item // exp) % 10
        count_arr[digit] += 1

    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]

    output_arr = [0] * n


    for i in range(n-1,-1,-1):
        index = (arr[i] // exp) % 10
        output_arr[count_arr[index]-1] = arr[i]
        count_arr[index] -= 1


    for i in range(n):
        arr[i] = output_arr[i]




def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr,exp)
        exp *= 10
            

radix_sort(arr)
print(arr)