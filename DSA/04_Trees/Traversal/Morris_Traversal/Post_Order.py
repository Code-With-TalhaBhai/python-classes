from binarytree import root


# Not completed  yet
def morris_post_traversal(root):

    curr = root
    while curr:
        if curr.left is None:
            print(curr.data)
            curr = curr.right
        else:
            precedence = curr.left
            while precedence.right is not None:
                precedence = precedence.right
            
        





morris_post_traversal(root)