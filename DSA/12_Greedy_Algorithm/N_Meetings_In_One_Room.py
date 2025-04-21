


def meetings_in_one_room(start,end):
    start_end = [(start[i],end[i]) for i in range(len(start))]

    start_end.sort(key=lambda x: x[1])
    cnt = 1
    k = 0
    i = 1

    while i < len(start_end):
        if start_end[i][0] > start_end[k][1]:
            k = i
            cnt += 1
        i += 1

    return cnt



    # return start_end








start1 = [1, 3, 0, 5, 8, 5]
end1 =  [2, 4, 6, 7, 9, 9]

start2 = [10, 12, 20]
end2 = [20, 25, 30]


print(meetings_in_one_room(start1,end1))
print(meetings_in_one_room(start2,end2))