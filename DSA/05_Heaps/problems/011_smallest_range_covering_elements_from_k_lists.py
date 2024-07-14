import heapq

lists = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# [0-5] also a range covering atleast one element from every list
# [22-24] smallest range

heap = []
maxi = float("-inf")
for index,item in enumerate(lists):
    heapq.heappush(heap,(item[0],index,0))
    maxi = max(maxi,item[0])

ans = [heap[0][0],maxi]

while heap:
    val,row,col = heapq.heappop(heap)

    col += 1
    if col < len(lists[row]):
        num = lists[row][col]
        heapq.heappush(heap,(num,row,col))
        maxi = max(maxi,num)
        mini = heap[0][0]
        if ans[-1] - ans[0] > maxi - mini:
            ans[0],ans[-1] = mini,maxi
    else:
        break


print(ans)