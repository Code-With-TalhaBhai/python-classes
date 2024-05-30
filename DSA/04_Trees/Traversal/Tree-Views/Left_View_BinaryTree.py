from binarytree import root



def left_view_binary_tree(root):
    if not root:
        return []
    import collections
    q = collections.deque()
    final = {}
    res = []
    q.append((root,0)) # tuple

    while q:
        for i in range(len(q)):
            node = q.popleft()
            data = node[0].data
            col = node[1]

            if col not in final:
                # final[col] = [data]
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



print(left_view_binary_tree(root))