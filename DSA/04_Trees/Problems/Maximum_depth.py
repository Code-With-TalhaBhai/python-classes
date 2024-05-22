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


def maxDepth(root):
    dq = deque()
    if root:
        dq.append(root)
    res = []

    while dq:
        lq = len(dq)
        level = []
        for i in range(lq):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            level.append(node.data)
        res.append(level)
    return len(res)


root = Node(50)
root.insert(25)
root.insert(10)
root.insert(70)
root.insert(60)
root.insert(30)
root.insert(40)

print("The maximum depth of binary tree is: ",maxDepth(root))