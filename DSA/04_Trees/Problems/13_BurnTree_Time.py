from difflib import ndiff
from binarytree import buildTree
import collections


preorder = [1,2,4,8,5,10,3,7]
inorder = [8,4,2,10,5,1,3,7]

root = buildTree(preorder,inorder)


def MinTime_BurnTree1(root,target):
    neighbour_dict = collections.defaultdict(list)
    dq = collections.deque()
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
            neighbour_dict[right.data].append(node.data)
            neighbour_dict[node.data].append(right.data)
            dq.append(right)
   
   
    nq = collections.deque()
    nq.append((target,0))
    visited = set()
    visited.add(target)
    
    while nq:
        node,time = nq.popleft()

        for neighbour in neighbour_dict[node]:
            if neighbour not in visited:
                nq.append((neighbour,time+1))
                visited.add(neighbour)

    return time



def find_neighbour(root,n_dict):
    if not root:
        return 
    
    if root.left:
        n_dict[root.data].append(root.left.data)
        n_dict[root.left.data].append(root.data)
    if root.right:
        n_dict[root.data].append(root.right.data)
        n_dict[root.right.data].append(root.data)

    find_neighbour(root.left,n_dict)
    find_neighbour(root.right,n_dict)

def find_time(target,neighbour_dict):
    nq = collections.deque()
    nq.append((target,0))
    visited = set()
    visited.add(target)
    
    while nq:
        node,time = nq.popleft()

        for neighbour in neighbour_dict[node]:
            if neighbour not in visited:
                nq.append((neighbour,time+1))
                visited.add(neighbour)

    return time


def MinTime_BurnTree2(root,target):
    neighbour_dict = collections.defaultdict(list)
    find_neighbour(root,neighbour_dict)
    return find_time(target,neighbour_dict)

   


print("The minimum time to burn tree is: ",MinTime_BurnTree1(root,10))
print("The minimum time to burn tree is: ",MinTime_BurnTree2(root,10))