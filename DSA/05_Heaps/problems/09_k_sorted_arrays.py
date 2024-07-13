import heapq

arrays = [
    [45,90],
    [2,6,78,100,234],
    [1,5,9],
    [0]
]

# 0 1 2 5 6 9 45 78 90 100 234


sorted_heap = []
sorted_ans = []

for index,array in enumerate(arrays):
    if array:
        heapq.heappush(sorted_heap,(array[0],index,0))  #(arr_val,row,col)tuple


while sorted_heap:
    val,row,col = heapq.heappop(sorted_heap)
    sorted_ans.append(val)

    col += 1
    if col < len(arrays[row]):
        heapq.heappush(sorted_heap,(arrays[row][col],row,col))


print(sorted_ans)


