from binarytree import root


def totalSum(root):
    if not root:
        return 0
    
    left = totalSum(root.left)
    right = totalSum(root.right)

    return root.data + left + right
    




print("The total sum of whole tree is: ",totalSum(root))