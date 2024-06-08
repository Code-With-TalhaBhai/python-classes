from binarytree import root

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
        return
    
    print(head.data,end=" ")
    traverse_linkedlist(head.right)




# Through Recurrsion(Time-Complexity(O->N),Space-Complexity(O->N))
def flatten_tree_into_linkedlist1(root):
    if not root:
        return

    root_linkedlist.insert(root.data)
    flatten_tree_into_linkedlist1(root.left)
    flatten_tree_into_linkedlist1(root.right)



# Through morris-traversal of preorder
def flatten_tree_into_linkedlist2(root):
    if not root:
        return
    
    curr = root
    while curr is not None:
        if curr.left is None:
            print(curr.data,end=" ")
            curr = curr.right
        else:
            print(curr.data,end=" ")
            temp = curr.left
            while temp.right is not None:
                temp = temp.right
            temp.right = curr.right
            temp1 = curr
            curr =  curr.left
            temp1.right = curr   




print("Flatten binary tree through recurrsion with extra tree(space-complexity (O^n)) and time-complexity of (O^n)")
flatten_tree_into_linkedlist1(root)
traverse_linkedlist(root_linkedlist)# just for check

print()
print("Flatten binary tree through morris-traversal with (space-complexity (O^1)) and time-complexity of (O^n)")
flatten_tree_into_linkedlist2(root)
print()
traverse_linkedlist(root)# just for check

