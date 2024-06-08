from binarytree import root


def morris_inorder_traversal(root):
    curr = root

    while curr is not None:
        if curr.left is None:
            print(curr.data)
            curr = curr.right
        else:
            precedence = curr.left
            while precedence.right is not None:
                precedence = precedence.right
            precedence.right = curr

            temp = curr
            curr = curr.left
            temp.left = None



morris_inorder_traversal(root)