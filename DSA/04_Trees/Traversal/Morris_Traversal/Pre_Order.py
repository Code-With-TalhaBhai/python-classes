from binarytree import root


def morris_preorder_traversal(root):
    curr = root

    while curr is not None:
        if curr.left is None:
            print(curr.data)
            curr = curr.right
        else:
            print(curr.data)
            precedence = curr.left
            while precedence.right is not None:
                precedence = precedence.right
            precedence.right = curr.right
            curr = curr.left            



morris_preorder_traversal(root)