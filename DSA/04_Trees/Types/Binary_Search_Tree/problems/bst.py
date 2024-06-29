class BST:
    def __init__(self,data=0):
        self.data : int | None = data
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



root = BST(50)
insert(root,25)
insert(root,10)
insert(root,70)
insert(root,60)
insert(root,30)
insert(root,40)