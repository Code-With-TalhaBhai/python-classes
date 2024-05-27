# A binary tree's maximum depth is the number of nodes,
# along the longest path from the root node down to the farthest leaf node.


from collections import deque


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        elif data > self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)


# Breadth-First-Search(BFS)-> using loop
def maxDepth1(root):
    dq = deque()
    if root:
        dq.append(root)
    level = 0

    while dq:
        lq = len(dq)
        for i in range(lq):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        level += 1
    return level


# Depth-First-Search(DFS) -> using recurrsion
def maxDepth2(root):
    if root == None:
        return 0
    
    left = maxDepth2(root.left)
    right = maxDepth2(root.right)

    height = max(left,right) + 1
    return height


from typing import List,Tuple
# Iterative Depth-First-Search
def maxDepth3(root):
    stack : List[Tuple[root,int]] = [(root,1)]
    maxi = 1

    while stack:
        node,depth = stack.pop()

        if node:
            maxi = max(maxi,depth)
            stack.append((node.left,depth+1))
            stack.append((node.right,depth+1))
    return maxi


root = Node(50)
root.insert(25)
root.insert(10)
root.insert(70)
root.insert(60)
root.insert(30)
root.insert(40)

print("The maximum depth of binary tree is: ",maxDepth1(root))
print("The maximum depth of binary tree is: ",maxDepth2(root))
print("The maximum depth of binary tree is: ",maxDepth3(root))