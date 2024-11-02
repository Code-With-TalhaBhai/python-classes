

def maxArea(heights):
    max_area = float("-inf")
    i = 0
    j = len(heights) - 1

    while i < j:
        width = j - i
        height = min(heights[i],heights[j])
        max_area = max(max_area,width*height)

        if heights[i] <= heights[j]:
            i += 1
        elif heights[j] < heights[i]:
            j -= 1

    return max_area



height1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(height1))

height2 = [1,1]
print(maxArea(height2))
