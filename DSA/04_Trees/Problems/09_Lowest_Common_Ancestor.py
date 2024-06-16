from binarytree import root



def lower_common_ancestor(n1,n2,root):
    if not root:
        return None
    
    if root.data == n1 or root.data == n2:
        return root
    
    left = lower_common_ancestor(n1,n2,root.left)
    right = lower_common_ancestor(n1,n2,root.right)

    if left and right:
        return root
    elif not left and right:
        return right
    elif left and not right:
        return left
    else:
        return None




print(lower_common_ancestor(10,30,root).data)
print(lower_common_ancestor(25,70,root).data)
print(lower_common_ancestor(30,40,root).data)