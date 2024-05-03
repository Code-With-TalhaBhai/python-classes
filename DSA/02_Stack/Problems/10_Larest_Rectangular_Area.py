
def prev_smaller(v):
    ans_v = [0 for _ in range(len(v))]
    stack = [-1]

    for index,item in enumerate(v):

        while stack[-1] != -1 and item <= v[stack[-1]]:
            stack.pop()   
        
        ans_v[index] = stack[-1]
        stack.append(index)
    return ans_v


def next_smaller(v):
    ans_v = [0 for _ in range(len(v))]
    stack = [-1]
    index = len(v)

    for item in reversed(v):
        index = index - 1
        
        while stack[-1] != -1 and item <= v[stack[-1]]:
            stack.pop()
        
        ans_v[index] = stack[-1]
        stack.append(index)

    return ans_v


def largest_area_histogram1(v):

    max = -1
    prev_smaller_arr = prev_smaller(v)
    next_smaller_arr = next_smaller(v)
    # print(next_smaller_arr)
    # print(prev_smaller_arr)
    for _ in range(len(next_smaller_arr)):
        if next_smaller_arr[_] == -1:
            next_smaller_arr[_] = len(next_smaller_arr)

    for index,height in enumerate(v):
        width = next_smaller_arr[index] - prev_smaller_arr[index] - 1
        area = width * height
        if(area>max):
            max = area
    return max



def largest_area_histogram2(heights):
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
# histogram = [999,999,999,999]
histogram = [3, 1, 3, 2, 2]



print(largest_area_histogram1(histogram))
print(largest_area_histogram2(histogram)) # optimised