from binarytree import root
import collections


def top_view_binary_tree(root):
    if not root:
        return root
    q = collections.deque()
    q.append((root,0)) # tuple
    final = {}
    res = []

    while q:
        for i in range(len(q)):
            node = q.popleft()
            data = node[0].data
            col = node[1]
            if col not in final:
                # final[col] = [data]
                final[col] = data # if want to store in single list

            left = node[0].left
            right = node[0].right

            if left:
                q.append((left,col-1))
            if right:
                q.append((right,col+1))

    for k in sorted(final.keys()):
        res.append(final[k])

    return res




print(top_view_binary_tree(root))