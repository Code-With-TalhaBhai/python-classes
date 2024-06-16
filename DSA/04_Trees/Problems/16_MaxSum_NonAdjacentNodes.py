from binarytree import root
from collections import deque


def maxSum_NonAdjacent1(root):
    if not root:
        return 0

    dq = deque()
    traverse = 0
    dq.append(root)
    # result = []
    upper = 0
    lower = 0

    while dq:

        for i in range(len(dq)):
            root = dq.popleft()
            left = root.left
            right = root.right

            if left:
                dq.append(left)
            if right:
                dq.append(right)

            if traverse % 2 == 0:
                upper += root.data
            elif traverse % 2 == 1:
                lower += root.data

        traverse += 1

    # print(upper,lower)
    return max(upper,lower)


def maxSum_NonAdjacent2(root):

    def maxSum_NonAdj(root):
        if not root:
            return (0,0)

        left = maxSum_NonAdj(root.left)
        right = maxSum_NonAdj(root.right)

        first = root.data + left[1] + right[1]
        second  = left[0] + right[0]

        return (first,second)
    
    first,second = maxSum_NonAdj(root)
    return max(first,second)

    



print(maxSum_NonAdjacent1(root))
print(maxSum_NonAdjacent2(root))