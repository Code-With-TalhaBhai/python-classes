# Best Case Time-Complexity: O(n + k)-> The best case happens when every bucket gets equal number of elements.
# Worst Case Time-Complexity: O(n^2) The worst case happens when one bucket gets all the elements.




# For floating-point numbers
# arr = [0.78,0.17,0.39,0.26,0.72,0.99,0.21,0.12,0.23,0.68] # range[0,1)
arr = [78.9,17.8,0.39,2.6,0.72,99.8,21.3,0.12,2.3,68.3] # range (0,float("inf"))


def insertion_sort(bucket):
    n = len(bucket)
    if n <= 1:
        return

    j = 1
    while j < n:
        key = bucket[j]
        k = j-1
        while k >= 0 and bucket[k] > key:
            bucket[k+1] = bucket[k]
            k -= 1
        bucket[k+1] = key
        j += 1



def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    max_value = max(arr)
    min_value = min(arr)

    for i in range(n):
        # If range is between 0(inclusive) and 1(exclusive) range[0,1)
        # bucket_index = int(arr[i] * n) 
        # buckets[bucket_index].append(arr[i])

        # If numbers are greater than 1. Then, first we make it with normal distribution
        normalized_value = (arr[i] - min_value) / (max_value - min_value) # making between 0,1 distribution
        bucket_index = int(normalized_value * (n - 1))
        buckets[bucket_index].append(arr[i])


    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    i = 0
    for i in range(n):
        for item in buckets[i]:
            arr[index] = item
            index += 1

        




bucket_sort(arr)
print(arr)