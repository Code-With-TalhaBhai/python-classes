



def minTimeToReach1(moveTime) -> int:
    import heapq
    m = len(moveTime)
    n = len(moveTime[0])
    min_heap = [(0,0,0)]
    visited = set()
    visited.add((0,0))

    while min_heap:
        t,x,y = heapq.heappop(min_heap)
        if x == m - 1 and y == n - 1:
            return t

        top = x - 1
        left = y - 1
        bottom = x + 1
        right = y + 1

        if top > -1 and (top,y) not in visited:
            maxi = max(t,moveTime[top][y]) + 1
            heapq.heappush(min_heap,(maxi,top,y))
            visited.add((top,y))
        if left > -1 and (x,left) not in visited:
            maxi = max(t,moveTime[x][left]) + 1
            heapq.heappush(min_heap,(maxi,x,left))
            visited.add((x,left))
        if bottom < m and (bottom,y) not in visited:
            maxi = max(t,moveTime[bottom][y]) + 1
            heapq.heappush(min_heap,(maxi,bottom,y))
            visited.add((bottom,y))
        if right < n and (x,right) not in visited:
            maxi = max(t,moveTime[x][right]) + 1
            heapq.heappush(min_heap,(maxi,x,right))
            visited.add((x,right))
    return -1



def minTimeToReach2(moveTime) -> int:
    import heapq
    m = len(moveTime)
    n = len(moveTime[0])
    min_heap = [(0,0,0)]
    min_time = [[float('inf')]*n for _ in range(m)]
    min_time[0][0] = 0
    directions = [(-1,0),(0,-1),(0,1),(1,0)]

    while min_heap:
        t,x,y = heapq.heappop(min_heap)
        if x == m - 1 and y == n - 1:
            return t
        
        if t > min_time[x][y]:
            continue

        
        for dx,dy in directions:
            nx = dx + x
            ny = dy + y

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                maxi = max(t,moveTime[nx][ny]) + 1
                if maxi < min_time[nx][ny]:
                    min_time[nx][ny] = maxi
                    heapq.heappush(min_heap,(maxi,nx,ny))
    return -1



moveTime1 = [[0,4],[4,4]]
moveTime2 = [[0,1],[1,2]]
moveTime3 = [[0,0,0],[0,0,0]]
moveTime4 = [[0,38,10],[58,29,83]]


print('With Visited Set')
print(minTimeToReach1(moveTime1))
print(minTimeToReach1(moveTime2))
print(minTimeToReach1(moveTime3))
print(minTimeToReach1(moveTime4))
print('Without Visited')
print(minTimeToReach2(moveTime1))
print(minTimeToReach2(moveTime2))
print(minTimeToReach2(moveTime3))
print(minTimeToReach2(moveTime4))