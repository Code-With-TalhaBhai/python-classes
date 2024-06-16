import collections

class BST:
    def __init__(self):
        self.data : int | None = None
        self.left : None | BST = None
        self.right : BST | None = None

# Insertion
def insert(root,data):
    if root.data is None:
        root.data = data

    elif root.data > data:
        if root.left == None:
            root.left = BST()
            root.left.data = data
        else:
            insert(root.left,data)
    elif root.data < data:
        if root.right == None:
            root.right = BST()
            root.right.data = data
        else:
            insert(root.right,data)


# Traverse
def level_order_traversal(root):
    res = []
    dq = collections.deque()
    dq.append(root)

    while dq:
        level = []

        for i in range(len(dq)):
            node = dq.popleft()
            level.append(node.data)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        res.append(level)
    print(res)


def search(root,val,path):
    if not root:
        return []
    
    path.append(root.data)

    if root.data == val:
        return path

    if val < root.data:
        return search(root.left,val,path)
    else:
        return search(root.right,val,path)


# As the node at the most left is minimum in BST     
def findMin(root):
    if not root.left:
        return root
    return findMin(root.left)

# And Node in right is maximum in BST
def findMax(root):
    if not root.right:
        return root
    
    return findMax(root.right)


# Delete Node from BST -> Recurrsion
def delete(root,val):
    if not root:
        return None
    
    # Leaf-Node
    if root.data == val:
        if not root.left and not root.right:
            return None
        
        # One child/subtree with right node is None
        if root.left is not None and root.right is None:
            return root.left
        
        # One child/subtree with left node is None
        elif root.left is None and root.right is not None:
            return root.right

        elif root.left is not None and root.right is not None:
            # by inorder predecessor
            temp = findMax(root.left) 
            root.data = temp.data
            root.left = delete(root.left,temp.data)
            return root

            # By InOrder Successor
            # temp = findMin(root.right)
            # root.data = temp.data
            # root.right = delete(root.right,temp.data)
            # return root        
    else:
        if val < root.data:
            root.left = delete(root.left,val)
        elif val > root.data:
            root.right = delete(root.right,val)

    return root



def inOrder(root):
    if not root:
        return 
    
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)
    


root = BST()
insert(root,50)
insert(root,25)
insert(root,10)
insert(root,70)
insert(root,60)
insert(root,30)
insert(root,40)


level_order_traversal(root)
print(search(root,30,[])) # searching
print("The minimum value in Tree is: ",findMin(root).data)
print("The maximum value in Tree is: ",findMax(root).data)


# Deletion
# 1. Deleting the leaf Node
# 2. Deleting the Node which have left child/subtree
# 3. Deleting the Node which have right child/subtree
# 4. Deleting the Node which have both left/right child/subtree
# delete(root,60)
# print("Level Order Traversal after deletion 60")
# level_order_traversal(root)

# Delete Leaf-Node
# delete1 = delete(root,40)
# print("Level Order Traversal after deletion 40")
# level_order_traversal(delete1)

# # Delete Node with one child
# delete2 = delete(root,70)
# print("Level Order Traversal after deletion 70")
# level_order_traversal(delete2)

# Delete Node with both children
delete3 = delete(root,25)
print("Level Order Traversal after deletion 70")
level_order_traversal(delete3)
