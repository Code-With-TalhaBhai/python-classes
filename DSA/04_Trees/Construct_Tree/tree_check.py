
def check_preOrder(root):
    res = []

    if root:
        res.append(root.data)
        res = res + check_preOrder(root.left)
        res = res + check_preOrder(root.right)
    return res


def check_inOrder(root):
    res = []
    
    if root:
        res = check_inOrder(root.left)
        res.append(root.data)
        res = res + check_inOrder(root.right)
    return res


def check_postOrder(root):
    res = []

    if root:
        res = check_postOrder(root.left)
        res = res + check_postOrder(root.right)
        res.append(root.data)
    return res



    
