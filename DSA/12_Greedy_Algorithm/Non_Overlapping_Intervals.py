


def eraseOverlapIntervals(intervals) -> int:
    intervals.sort(key=lambda x:x[1])
    n = len(intervals)

    cnt = 1
    i,k = 1,0

    while i < n:
        if intervals[i][0] >= intervals[k][1]:
            k = i
            cnt += 1

        #2nd way -> for this cnt ==  0 and return cnt only
        # if intervals[k][1] > intervals[i][0]:
        #     cnt += 1
        # else:
        #     k = i
        i += 1 

    return n-cnt
    # return cnt
    

intervals1 = [[1,2],[2,3],[3,4],[1,3]]
intervals2 = [[1,2],[1,2],[1,2]]


print(eraseOverlapIntervals(intervals1))
print(eraseOverlapIntervals(intervals2))