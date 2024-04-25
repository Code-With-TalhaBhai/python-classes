
def prev_smaller(v):
    ans_v = [0 for _ in range(len(v))]
    stack = [-1]

    for index,item in enumerate(v):

        index_to_insert = index-1
        while item <= stack[-1]:
            stack.pop()   
            index_to_insert = index_to_insert - 1 
        
        ans_v[index] = index_to_insert
        stack.append(item)
    return ans_v


def next_smaller(v):
    ans_v = [0 for _ in range(len(v))]
    stack = [-1]
    index = len(v)

    for item in reversed(v):
        index_to_insert = index
        index = index - 1
        
        while item <= stack[-1]:
            stack.pop()
            index_to_insert = index_to_insert + 1
        
        ans_v[index] = index_to_insert
        stack.append(item)

    return ans_v


def largest_area_histogram(v):

    max = -1
    next_smaller_arr = next_smaller(v)
    prev_smaller_arr = prev_smaller(v)
    print(next_smaller_arr)
    print(prev_smaller_arr)
    for index,height in enumerate(v):
        width = next_smaller_arr[index] - prev_smaller_arr[index] - 1
        area = width * height
        if(area>max):
            max = area
    return max



def largest_area_histogram1(heights):
    maxArea = 0
    stack = []

    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index,height = stack.pop()
            maxArea = max(maxArea, height * (i-index))
            start = index
        stack.append((start,h))

    for i,h in stack:
        # print("i is: ",i,"h is",h)
        maxArea = max(maxArea, h*(len(heights)-i))
    return maxArea
    




# histogram = [2,1,5,6,2,3]
# histogram = [2,2,5,6,2,3]
# histogram = [1,1]
histogram = [999,999,999,999]



print(largest_area_histogram1(histogram))