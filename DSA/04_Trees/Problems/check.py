from binarytree import buildTree,Level_Order_Traversal
from collections import deque,defaultdict


preorder = [1,2,4,8,5,10,3,7]
inorder = [8,4,2,10,5,1,3,7]

root = buildTree(preorder,inorder)

neighbour_dict = defaultdict(list)
dq = deque()
dq.append(root)

while dq:
    node = dq.popleft()


    left = node.left
    right = node.right

    if left:
        neighbour_dict[node.data].append(left.data)
        neighbour_dict[left.data].append(node.data)
        dq.append(left)
    if right:
        neighbour_dict[node.data].append(right.data)
        neighbour_dict[right.data].append(node.data)
        dq.append(right)

# print(neighbour_dict)
target = 10
nq = deque()
nq.append((target,0))
visited = set()
visited.add(target)

while nq:
    node,time = nq.popleft()
    for neighbour in neighbour_dict[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            nq.append((neighbour,time+1))

print(time)





    