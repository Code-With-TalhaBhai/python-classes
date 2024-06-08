


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
    import collections
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



# def construct_tree(order):
#     if order:
#         for i in range(len(order)):
#             if i == 0:
#                 root = Node(order[0])
#             else:
#                 root.insert(order[i])
#     return root


# # order = [1,2,3,4,5,6,7]
# order = [3,9,20,15,7]
# root = construct_tree(order)



# print(Level_Order_Traversal(root))