import collections


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

def Level_Order_Traversal(root):
    dq = collections.deque()
    if root:
        dq.append(root)
    res = []

    while dq:
        level_nodes = []
        qlen = len(dq)

        for i in range(qlen):
            root = dq.popleft()     
            left = root.left
            right = root.right

            if left is not None:
                dq.append(left)
            if right is not None:
                dq.append(right)

            level_nodes.append(root.data)
        res.append(level_nodes)
    return res


root = Node(50)
root.insert(25)
root.insert(10)
root.insert(70)
root.insert(60)
root.insert(30)
root.insert(40)


# root = Node(80)
# root.left = Node(20)
# root.right = Node(40)
# root.left.left = Node(10)
# root.left.right = Node(10)


# print(Level_Order_Traversal(root))



def buildTree(preOrder,inOrder):
    if not preOrder or not inOrder:
        return None
    
    root = Node(preOrder[0])
    root_index = inOrder.index(root.data)
    # root_index = inOrder.index(root)

    root.left = buildTree(preOrder[1:root_index+1],inOrder[:root_index])
    root.right = buildTree(preOrder[root_index+1:],inOrder[root_index+1:])
    return root




