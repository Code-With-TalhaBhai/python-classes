
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



root = BST()
insert(root,50)
insert(root,25)
insert(root,10)
insert(root,70)
insert(root,60)
insert(root,30)
insert(root,80)


def inorder(root,arr):
    if not root:
        return None
    
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)


def postorder_check(root,arr):
    if not root:
        return None
    
    postorder_check(root.left,arr)
    postorder_check(root.right,arr)
    arr.append(root.data)



def postorder(root,arr,index_arr):
    if not root:
        return None
    

    postorder(root.left,arr,index_arr)
    postorder(root.right,arr,index_arr)
    root.data = arr[index_arr[0]]
    index_arr[0] += 1


def BST_To_MaxHeap(root):
    arr = []
    inorder(root,arr) # As, inorder of BST is sorted
    index_arr = [0]
    postorder(root,arr,index_arr) 


BST_To_MaxHeap(root)


def check():
    arr = []
    postorder_check(root,arr)
    print(arr)


check()
