from binarytree import root,Node

class linkedList():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data == None:
            self.data = data
        elif self.right == None:
            self.right = linkedList()
            self.right.data = data
        else:
            self.right.insert(data)


    

root_linkedlist = linkedList()


def traverse_linkedlist(head):
    if not head:
        print()
        return
    
    while head:
        print(head.data,end=" ")
        head = head.right

    # through recurrsion
    # traverse_linkedlist(head.right)




# Through Recurrsion(Time-Complexity(O->N),Space-Complexity(O->N)) and requies its own custom-tree
def flatten_tree_into_linkedlist1(root):
    if not root:
        return

    # using root_linkedlist its own tree, not recommended way
    root_linkedlist.insert(root.data)
    flatten_tree_into_linkedlist1(root.left)
    flatten_tree_into_linkedlist1(root.right)



# Through morris-traversal of preorder
def flatten_tree_into_linkedlist2(root):
    if not root:
        return
    
    curr = root

    while curr:
        if not curr.left:
            curr = curr.right
        else:
            predecessor = curr.left
            while predecessor.right is not None:
                predecessor = predecessor.right
            predecessor.right = curr.right

            # 1st
            # temp = curr
            # curr = curr.left
            # temp.right = curr
            # temp.left = None
            
            #2nd
            curr.right = curr.left
            curr.left = None
            curr = curr.right


    




# Through recurrsion with extra tree(space-complexity (O^n)) and time-complexity of (O^n)
# flatten_tree_into_linkedlist1(root)
# traverse_linkedlist(root_linkedlist)# just for check

# Through morris-traversal with (space-complexity (O^1)) and time-complexity of (O^n)
myroot = Node(50)
myroot.insert(40)
myroot.insert(30)
myroot.insert(45)
myroot.insert(60)
myroot.insert(55)
myroot.insert(70)
flatten_tree_into_linkedlist2(myroot)
traverse_linkedlist(myroot)# just for check

