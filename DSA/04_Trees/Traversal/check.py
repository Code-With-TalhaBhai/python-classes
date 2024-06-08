from binarytree import root


def preOrder(root):
    if not root:
        return
    
    print(root.data, end=" ")

    preOrder(root.left)
    preOrder(root.right)



def inOrder(root):
    if not root:
        return 
    
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)


def postOrder(root):
    if not root:
        return
    
    postOrder(root.left)
    postOrder(root.right)

    print(root.data,end=" ")




print("Pre-Order")
preOrder(root)
print()
print("In-Order")
inOrder(root)
print()
print("Post-Order")
postOrder(root)
