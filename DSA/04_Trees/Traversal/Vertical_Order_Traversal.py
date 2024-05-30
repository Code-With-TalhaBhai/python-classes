from binarytree import root
from collections import deque


# Using breath-first-search
def vertical_order_traversal(root):
    q = deque()
    q.append((root,0)) # tuple
    final = {}
    ans = []

    while q:
        for i in range(len(q)):
            node = q.popleft()
            data = node[0].data
            col = node[1]
            if col not in final:
                final[col] = [data]
            else:
                # final[col] = final[col] + [data]
                final[col].append(data)
            left = node[0].left
            right = node[0].right

            if left:
                q.append((left,node[1]-1))
            if right:
                q.append((right,node[1]+1))


    for k in sorted(final.keys()):
        ans.append(final[k])

    return ans





print(vertical_order_traversal(root))