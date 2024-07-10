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


def countNodes(root):
    if not root:
        return 0
    
    left = countNodes(root.left)
    right = countNodes(root.right)

    return 1 + left + right




def is_CBT(root,index,totalNodes):
    if not root:
        return True        
    
    if index >= totalNodes:
        return False

    left = is_CBT(root.left,(2*index)+1,totalNodes)
    right = is_CBT(root.right,(2*index)+2,totalNodes)

    return left and right


# def isMaxHeap(root,left_limit,right_limit):
def isMaxHeap(root):
    if not root.left and not root.right:
        return True
    

    if not root.right:
        return (root.data >= root.left.data)
    
    if not (root.data >= root.left.data and root.data >= root.right.data):
        return False

    # left = isMaxHeap(root.left,left_limit,right_limit)
    # right = isMaxHeap(root.right,left_limit,right_limit)
    left = isMaxHeap(root.left)
    right = isMaxHeap(root.right)

    return left and right



root = BST()
insert(root,50)
insert(root,25)
insert(root,10)
insert(root,70)
insert(root,60)
insert(root,30)
insert(root,80)



# print("The total nodes of bst is: ",countNodes(root))
# print(is_CBT(root,0,countNodes(root)))
# print(isMaxHeap(root))


def isBST_Heap(root):
    if not root:
        return True
    
    n = countNodes(root)

    if is_CBT(root,0,n) and isMaxHeap(root):
        return True
    
    return False



print("The BST IS HEAP: ",isBST_Heap(root))

    

