from binarytree import root



def right_view_binary_tree(root):
    import collections
    if not root:
        return []
    q = collections.deque()
    q.append((root,0))
    final = {}
    res = []

    while q:
        for i in range(len(q)):
            node = q.popleft()
            data = node[0].data
            col = node[1]

            final[col] = data

            left = node[0].left
            right = node[0].right

            if left:
                q.append((left,col+1))
            if right:
                q.append((right,col+1))

    for k in final.keys():
        res.append(final[k])

    return res



print(right_view_binary_tree(root))