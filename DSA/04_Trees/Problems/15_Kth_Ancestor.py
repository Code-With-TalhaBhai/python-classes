from binarytree import root


def ancestor(root,node_data,k):
    if not root:
        return None

    if root.data == node_data:
        return root

    left = ancestor(root.left,node_data,k)
    right = ancestor(root.right,node_data,k)


    if left and not right:
        k[0] -= 1
        if k[0] <= 0:
            k[0] = 23456346
            return root
        return left
    

    if not left and right:
        k[0] -= 1
        if k[0] <= 0:
            k[0] = 75474574
            return root
        return right
    
    return None



def kth_ancestor(root,node_data,m):
    k = [m]
    node = ancestor(root,node_data,k)
    if node:
        return node.data
    else:
        return None
    

print(kth_ancestor(root,40,2))
print(kth_ancestor(root,40,3))
print(kth_ancestor(root,60,2))
print(kth_ancestor(root,60,1))