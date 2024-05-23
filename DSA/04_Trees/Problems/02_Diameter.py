from binarytree import root


def height(root):
    if root == None:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    hei = max(left,right) + 1
    return hei


def diameter(root):
    if root == None:
        return 0
    
    left = diameter(root.left)
    right = diameter(root.right)
    left_right_height = height(root.left) + height(root.right) + 1
    
    dia = max(left,max(left_right_height,right))

    return dia


print(diameter(root))
