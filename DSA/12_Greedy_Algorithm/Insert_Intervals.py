    # while i < n and interval[i][1] < newinterval[i][0]: #left



def insert(interval,newinterval):
    i = 0
    res = []
    n = len(interval)

    
    while i < n and interval[i][1] < newinterval[0] : #left
        res.append(interval[i])
        i += 1

    s_limit = newinterval[0]
    e_limit = newinterval[1]
    while i < n and e_limit >= interval[i][0]: # middle
        s_limit = min(s_limit,interval[i][0])
        e_limit = max(e_limit,interval[i][1])
        i += 1
    res.append([s_limit,e_limit])

    while i < n: # right
        res.append(interval[i])
        i += 1

    return res





intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]


print(insert(intervals1,newInterval1))
print(insert(intervals2,newInterval2))