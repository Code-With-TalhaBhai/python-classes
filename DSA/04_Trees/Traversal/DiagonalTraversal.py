from binarytree import root
import collections


def Left_Diagonal_Traversal(root):
    if not root:
        return []
    q = collections.deque()
    q.append((root,0))
    final = {}
    res = []

    while q:
        for i in range(len(q)):
            node,col = q.popleft()

            if col not in final:
                final[col] = [node.data]
            else:
                final[col].append(node.data)

            left = node.left
            right = node.right

            if left:
                q.append((node.left,col-1))
            if right:
                q.append((node.right,col))


    for k in final.keys():
        res.append(final[k])
    # print(final)

    return res

def Right_Diagonal_Traversal(root):
    if not root:
        return []
    q = collections.deque()
    q.append((root,0))
    final = {}
    res = []

    while q:
        for i in range(len(q)):
            node,col = q.popleft()

            if col not in final:
                final[col] = [node.data]
            else:
                final[col].append(node.data)

            left = node.left
            right = node.right

            if left:
                q.append((node.left,col))
            if right:
                q.append((node.right,col+1))


    for k in final.keys():
        res.append(final[k])
    # print(final)

    return res




print("Left Diagonal Traversal: ",Left_Diagonal_Traversal(root))
print("Right Diagonal Traversal: ",Right_Diagonal_Traversal(root))

