

def merge1(intervals):
    n = len(intervals)
    intervals.sort()
    merge_intervals = []

    i = 0
    while i < n:
        s_limit = intervals[i][0]
        e_limit = intervals[i][1]
        j = i + 1
        while j < n and intervals[j][0] <= e_limit:
            e_limit = max(e_limit,intervals[j][1])
            j += 1
        merge_intervals.append([s_limit,e_limit])
        i = j

    return merge_intervals



def merge2(intervals):
    n = len(intervals)
    intervals.sort()
    merge_intervals = []

    s_limit,e_limit = intervals[0][0],intervals[0][1]
    for i in range(1,n):
        item = intervals[i]
        if item[0] > e_limit:
            merge_intervals.append([s_limit,e_limit])
            s_limit = item[0]
            e_limit = item[1]
        else:
            e_limit = max(e_limit,item[1])
    merge_intervals.append([s_limit,e_limit])
    return merge_intervals











intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]

print(merge1(intervals1))
print(merge1(intervals2))
print()
print(merge2(intervals1))
print(merge2(intervals2))