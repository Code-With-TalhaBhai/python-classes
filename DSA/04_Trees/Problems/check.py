from binarytree import buildTree,Level_Order_Traversal
from collections import deque,defaultdict


preorder = [1,2,4,8,5,10,3,7]
inorder = [8,4,2,10,5,1,3,7]

root = buildTree(preorder,inorder)

neighbour_dict = defaultdict(list)



def find_neighbour(root):
    if not root:
        return
    
    if root.left:
        neighbour_dict[root.data].append(root.left.data)
        neighbour_dict[root.left.data].append(root.data)
    if root.right:
        neighbour_dict[root.data].append(root.right.data)
        neighbour_dict[root.right.data].append(root.data)

    find_neighbour(root.left)
    find_neighbour(root.right)


find_neighbour(root)
# print(neighbour_dict)

target = 10
visited = set()
visited.add(target)






# print(time_to_burn())
